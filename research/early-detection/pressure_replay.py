"""PUCK point-in-time pressure detector. Research only; input is timestamped trade+NBBO JSONL."""
import json,sys,math,statistics
from datetime import datetime,timedelta
from collections import defaultdict,deque

def parse(r):
 try:
  t=datetime.fromisoformat(r["ts"].replace("Z","+00:00"))
  p,s,b,a=[float(r[k]) for k in ("price","size","bid","ask")]
  if t.tzinfo is None or not all(map(math.isfinite,(p,s,b,a))) or min(p,s,b,a)<=0 or b>a:return None
  return dict(t=t,p=p,s=s,b=b,a=a,side=r.get("side"),symbol=str(r["symbol"]).upper())
 except (KeyError,ValueError,TypeError):return None

def features(h,t):
 recent=[x for x in h if t-timedelta(seconds=30)<x["t"]<=t]
 prior=[x for x in h if t-timedelta(seconds=60)<x["t"]<=t-timedelta(seconds=30)]
 base=[x for x in h if t-timedelta(seconds=150)<x["t"]<=t-timedelta(seconds=60)]
 if len(recent)<3 or len(prior)<3 or len(base)<6:return None
 def v(xs):return sum(x["s"] for x in xs)
 def spread(x):return (x["a"]-x["b"])/((x["a"]+x["b"])/2)
 side_known=all(x["side"] in ("B","S") for x in recent)
 buyer=sum(x["s"] for x in recent if x["side"]=="B")/v(recent) if side_known else None
 f=dict(speed_ratio=(len(recent)/30)/(len(base)/90),
 speed_accel=len(recent)/len(prior),
 volume_ratio=(v(recent)/30)/(v(base)/90),
 volume_accel=v(recent)/v(prior),
 spread=spread(recent[-1]),spread_change=spread(recent[-1])/statistics.median(map(spread,prior)) if statistics.median(map(spread,prior))>0 else None,
 buyer_ratio=buyer,price=recent[-1]["p"],support_proxy=min(x["p"] for x in prior))
 return f

def state(f):
 if f is None:return "INSUFFICIENT_DATA"
 if f["price"]<f["support_proxy"]:return "REVOKED"
 if f["spread"]>.02:return "BLOCKED_SPREAD"
 if f["spread_change"] is None:return "INSUFFICIENT_DATA"
 if not (f["speed_ratio"]>=2 and f["speed_accel"]>=1.3 and f["volume_ratio"]>=2 and f["volume_accel"]>=1.3 and f["spread_change"]<=1.1):return "WATCH"
 if f["buyer_ratio"] is None:return "IGNITION_UNVERIFIED_TAPE"
 if f["buyer_ratio"]<.6:return "WAIT_BUYERS"
 return "WAIT_SUPPORT_CONFIRMATION_AND_RISK_REVIEW"

def replay(rows):
 h=defaultdict(deque)
 parsed=sorted((x for r in rows if (x:=parse(r)) is not None),key=lambda x:(x["t"],x["symbol"]))
 for x in parsed:
  q=h[x["symbol"]];q.append(x)
  while q and x["t"]-q[0]["t"]>timedelta(seconds=151):q.popleft()
  f=features(q,x["t"])
  if f is not None:yield dict(symbol=x["symbol"],ts=x["t"].isoformat(),**f,state=state(f))

if __name__=="__main__":
 with open(sys.argv[1],encoding="utf8") as fp:
  for result in replay(json.loads(line) for line in fp if line.strip()):print(json.dumps(result))
