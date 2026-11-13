# Runner Outcome Comparison — 2026-11-13 ~06:56 EST

## Provenance
Original immutable observation: [03:26 overnight snapshot](https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-13_0326_EST_overnight_ignition_webull.md). Follow-up: connected Webull US_STOCK extended-hours snapshots and PRE_MARKET top-20 leaderboard collected ~06:56 ET. Each follow-up trade and quote has its own ET timestamp below. Original overnight prices and shares are reproduced exactly, not rewritten. Dedup key: date/symbol/follow-up ~06:56 ET. No trades executed.

## Same-symbol comparison
Price delta = (follow-up PRE extended-hour last / original OVN last -1). These are asynchronous indicative observations, not returns. OVN volume difference is same session field but may have a session boundary or feed update; not a rate of volume acceleration. PRE* is separate session total and MUST NOT be subtracted from OVN. Quote spread uses follow-up bid/ask midpoint.

|Symbol|03:26 OVN price|~06:56 PRE last|Price delta|03:26 OVN shares|Follow-up OVN shares|Follow-up PRE* shares|PRE bid/ask|Spread|PRE trade / quote ET|
|---|---:|---:|---:|---:|---:|---:|---|---:|---|
|SHFS|0.0311|0.0306|-1.61%|44,314,389 OVN|48,002,490 OVN (3,688,101 change)|198,634,360 PRE*|0.0298/0.0315|5.55%|06:56:49 / 06:56:40|
|MRLN|1.36|1.3787|1.37%|977,121 OVN|1,055,884 OVN (78,763 change)|2,979,825 PRE*|1.3700/1.3800|0.73%|06:56:48 / 06:56:48|
|SNAL|3.2|2.7300|-14.69%|444,387 OVN|492,890 OVN (48,503 change)|764,373 PRE*|2.6800/2.7500|2.58%|06:56:49 / 06:54:51|
|PARA|0.1306|0.10|-23.43%|11,151,733 OVN|11,654,595 OVN (502,862 change)|16,192,488 PRE*|0.10/0.105|4.88%|06:56:43 / 06:56:36|
|VTSI|3.48|3.40|-2.30%|55,646 OVN|58,431 OVN (2,785 change)|43,598 PRE*|3.32/3.40|2.38%|06:56:44 / 06:56:44|
|SLSN|1.25|1.2000|-4.00%|29,629 OVN|32,275 OVN (2,646 change)|111,902 PRE*|1.1700/1.2000|2.53%|06:56:12 / 06:56:12|
|CRMN|0.9877|0.9401|-4.82%|174,858 OVN|189,128 OVN (14,270 change)|8,771,423 PRE*|0.93/0.96|3.17%|06:56:49 / 06:56:48|
|OGEN|0.2457|0.2143|-12.78%|1,174,344 OVN|1,204,136 OVN (29,792 change)|408,735 PRE*|0.2030/0.2225|9.17%|06:56:48 / 06:56:28|
|PLCE|0.3978|0.3685|-7.37%|743,152 OVN|870,003 OVN (126,851 change)|633,965 PRE*|0.354/0.3753|5.84%|06:56:47 / 06:54:44|
|ADXN|4.91|4.70|-4.28%|11,245 OVN|12,242 OVN (997 change)|46,911 PRE*|4.60/4.70|2.15%|06:56:47 / 06:56:47|
|CENN|0.1695|0.1531|-9.68%|1,064,914 OVN|1,131,904 OVN (66,990 change)|954,091 PRE*|0.1531/0.16|4.41%|06:56:26 / 06:56:05|
|POAS|2.78|2.6503|-4.67%|138,427 OVN|144,658 OVN (6,231 change)|72,220 PRE*|2.6200/2.9000|10.14%|06:56:48 / 06:56:38|
|ICMB|1.02|1.0697|4.87%|28,630 OVN|32,074 OVN (3,444 change)|34,458 PRE*|0.95/1.07|11.88%|06:55:24 / 06:49:56|

## Leaderboard changes
Current Webull PRE_MARKET top 5: ZBAO +112.38%, RAIN +65.65%, MRLN +43.09%, SHFS +33.78%, SLSN +32.01%. These leaderboard percentage changes are relative to regular-session reference, NOT since 03:26. Of original five primary names, MRLN and SHFS remain top five, VTSI #7, SNAL #11, PARA absent from retrieved top 20. SLSN was an early exception and is now #5. New meaningful leaders ZBAO ($0.4354, PRE volume 25720007, spread 3.30%) and RAIN ($0.7865, PRE volume 11070780, spread 1.88%) did NOT feature in the early 03:26 primary/control list. ZBAO OVN 0.2171 / 7176 shares; RAIN OVN 1.00 / 3994535 shares; neither establishes first ignition timing. RAIN's premarket last is well below its OVN last, indicating strong intra-session reversal relative to this separate snapshot.

Continuation by price comparison: MRLN modestly higher; SHFS slightly lower; SNAL, PARA and VTSI lower. Ranking disappearance is not a proven failed ignition. False ignition verdict UNKNOWN absent synchronized ticks and a defined first-ignition criterion. OGEN, PLCE, ADXN and other negative controls retained above.

## News and catalyst evidence
Previously archived SHFS dilution/reverse-split concerns, MRLN Nov 12 10-Q, VTSI Nov 12 10-Q, PLCE bankruptcy and ICMB merger context remain historical; no original issuer PR publication/SEC acceptance timestamps or first responsive prints verified in this check. Fresh Webull keyword news results (untrusted secondary news, not original issuer timestamp):

```text
ZBAO: {"text":"{\"keyword\":\"ZBAO\",\"data\":[]}"}
RAIN: {"text":"{\"keyword\":\"RAIN\",\"data\":[]}"}
MRLN: {"text":"{\"keyword\":\"MRLN\",\"data\":[{\"news_id\":\"15914783272453120\",\"title\":\"Merlin (MRLN) Stock Jumps Over 54% After Hours: What's Going On?\",\"summary\":\"Merlin Inc. shares jumped 54.50% to $1.49 following third-quarter results where EPS of $0.37 beat estimates by 227.6% and revenue of $3.46 million exceeded expectations by 58.3%. GAAP net income was $73.8 million, including a $103.6 million non-cash gain from warrant liability changes. The aerospace and defense company held $161.6 million in cash with no debt. Merlin expects 2027 operating expenses to fall \\\"meaningfully\\\" below 2026 levels, with plans to fund operations into 2029 without capital raises.\",\"source\":\"Benzinga\",\"url\":\"https://news-static.webullfintech.com/us/news-html/20261113/15914783272453120.html\",\"publish_time\":\"2026-11-13T05:23:06.000+0000\",\"sentiment\":\"POSITIVE\",\"related_symbols\":[\"EMDM4\",\"ESU4\",\"ESZ4\"]}]}"}
SHFS: {"text":"{\"keyword\":\"SHFS\",\"data\":[]}"}
```

First-seen catalyst timestamp, response latency and fresh dilution verification: UNKNOWN unless independently verified in primary filing. News absence in feed is not proof of no news.

## Permission gate and limitations
Speed acceleration UNKNOWN; interval volume acceleration UNKNOWN; tape buyer control UNKNOWN; defended support UNKNOWN; spread trend UNKNOWN (single fresh L1 observation); executable risk UNKNOWN. L1 spread alone does not establish fills. All symbols NO TRADE APPROVED. No inference of ignition from candle highs/lows. Quote freshness is explicit via timestamps; trade timestamps can differ. Source: Webull connected PRE_MARKET ranking, extended-hour snapshot and L1 fields; original GitHub archive linked above. Prior methodology: Jpuck412/puck-elite-price-action-v2. NO PROOF = NO TRADE.
