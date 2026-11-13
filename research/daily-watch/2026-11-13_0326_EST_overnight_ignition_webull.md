# Overnight Ignition Vault — 2026-11-13 ~03:26 EST

## Scope and provenance
Connected Webull PRE_MARKET gainers ranking and independent US_STOCK overnight_required=true stock snapshots collected ~03:26 ET Friday Nov 13 2026. **PRE_MARKET leaderboard is a different calculation period and must not be interpreted as today's overnight ignition**. The leaderboard showed PLCE, POAS, PARA, ICMB, ADXN etc., many reflecting prior regular/premarket strength. Selected names below are ranked by observed **OVN** percentage, activity, and relevance, not proof of initial ignition. All are US_STOCK, LISTED in Webull; exchange-specific eligibility should be revalidated before execution. Quote/trade times below converted from Unix milliseconds to ET; snapshots asynchronous. Single point spread = (ask-bid)/midpoint. No earlier observations overwritten. Dedup key 2026-11-13 / symbol / ~03:26 ET / OVN.

## Five primary overnight research candidates
|Symbol|OVN last|OVN % vs prior regular close|OVN shares|OVN bid / ask|Spread|Best bid/ask shares|Last trade ET|Quote ET|Verdict|
|---|---:|---:|---:|---|---:|---|---|---|---|
|SHFS|$0.0311|+38.22%|44,314,389|$0.0310 / $0.0311|0.32%|7978 / 372|~03:26:45|~03:26:51|NO TRADE; dilution/corporate action risk|
|MRLN|$1.36|+41.02%|977,121|$1.36 / $1.37|0.73%|1107 / 1|~03:26:52|~03:26:52|NO TRADE; one share best ask|
|SNAL|$3.20|+40.35%|444,387|$3.19 / $3.20|0.31%|82 / 118|~03:26:51|~03:26:51|NO TRADE; thin depth|
|PARA|$0.1306|+29.69%|11,151,733|$0.1305 / $0.1323|1.37%|17021 / 100|~03:26:48|~03:26:51|NO TRADE; extreme corporate-action-adjusted historical price range; dilution status UNKNOWN|
|VTSI|$3.48|+32.82%|55,646|$3.47 / $3.48|0.29%|618 / 25|~03:26:40|~03:26:40|NO TRADE; low OVN volume, thin ask|

Order is research significance, not strict percentage rank.

## Exceptions and negative controls
|Symbol|OVN last|OVN change|OVN shares|L1 bid / ask|Spread|Assessment|
|---|---:|---:|---:|---|---:|---|
|SLSN|$1.25|+37.51%|29,629|$1.25 / $1.33|6.20%|Wide spread, poor execution; Nov 12 10-Q historical context|
|CRMN|$0.9877|+18.32%|174,858|$0.9877 / $0.9869|UNKNOWN (crossed)|Invalid market; NO TRADE|
|OGEN|$0.2457|-29.82%|1,174,344|$0.2459 / $0.2486|1.09%|Negative control; last below bid due asynchronous trade/quote|
|PLCE|$0.3978|-10.41%|743,152|$0.4000 / $0.4095|2.35%|Bankruptcy risk; negative control|
|ADXN|$4.91|-7.18%|11,245|$4.90 / $4.96|1.22%|Prior momentum faded; financing history|
|CENN|$0.1695|-6.87%|1,064,914|$0.1695 / $0.1697|0.12%|Prior runner negative OVN; prospectus history|
|POAS|$2.78|-7.64%|138,427|$2.78 / $2.79|0.36%|Prior runner negative OVN|
|ICMB|$1.02|-3.77%|28,630|$1.01 / $1.02|0.99%|Merger headline from earlier session; current fresh catalyst UNKNOWN|

## Catalyst chronology and dilution
- SHFS: previous Nov 12 after-hours vault documents reverse-split and convertible-share repricing concerns; fresh Nov 13 primary-source PR/SEC acceptance time UNKNOWN. Webull stock-news feed returned older news, not a verified fresh issuer catalyst.
- MRLN: Nov 12 10-Q https://www.sec.gov/Archives/edgar/data/0002028707/000162828026073397/mrln-20260930.htm ; original SEC acceptance time UNKNOWN; fresh overnight response time UNKNOWN. Webull stock-news returned no entries.
- VTSI: Nov 12 10-Q https://www.sec.gov/Archives/edgar/data/0001085243/000143774926036549/vtsi20260930_10q.htm ; original acceptance time UNKNOWN. Webull stock-news returned no entries.
- SLSN: Nov 12 10-Q https://www.sec.gov/Archives/edgar/data/0000883107/000199937126025220/slsn-10q_093026.htm ; original acceptance UNKNOWN.
- SNAL: latest retrieved Webull news Oct 29; no verified fresh issuer catalyst. PARA: retrieved Nov 12 secondary roundup at https://news-static.webullfintech.com/us/news-html/20261112/15911881505162240.html published 12:05:39 EST, not a first catalyst or overnight ignition proof.
- No fresh original PR or SEC acceptance time independently confirmed in this pass. News with no move: NONE VERIFIED. Moves without verified fresh news: primary five. First responsive executed price/volume time: UNKNOWN for all. Historical high/low bars do not establish first ignition.
- Dilution/financing risk: SHFS significant historical flag; PARA, SNAL, MRLN, VTSI current financing status UNKNOWN pending issuer SEC review.

## Comparison and methodology
Compared GitHub ticker-vault Nov 12 03:19 overnight and Nov 12 18:33 after-hours archives. SHFS/MRLN/SNAL/VTSI already observed yesterday AH; recurrence does not prove first ignition. PLCE/POAS/ADXN/CENN/ICMB from Nov 12 early snapshot now show negative OVN changes, not conclusively failed ignition. GitHub puck-elite-price-action-v2 README describes evidence-first methodology and explicitly cautions that historical candle pattern matching is not predictive. Repository-wide duplicate enumeration not established; create-only dated path prevents overwrite.

## Permission and unknowns
**All names NO TRADE APPROVED.** Verified speed acceleration UNKNOWN; interval volume acceleration UNKNOWN (one cumulative OVN volume point); buyer-initiated tape UNKNOWN; spread trend UNKNOWN (one quote); defended support UNKNOWN; defined executable risk UNKNOWN; first ignition time before 04:00 UNKNOWN. Current L1 spread alone is not proof of execution quality. No candle inference. NO PROOF = NO TRADE.

## Source records
Webull PRE_MARKET ranking, Webull US_STOCK overnight snapshot around 03:26 ET Nov 13; Webull stock news for SHFS, MRLN, SNAL, PARA, SLSN, VTSI. GitHub research/daily-watch/2026-11-12_0319_EST_overnight_ignition_webull.md and 2026-11-12_1833_EST_afterhours_catalyst_vault_webull.md; Jpuck412/puck-elite-price-action-v2/README.md.
