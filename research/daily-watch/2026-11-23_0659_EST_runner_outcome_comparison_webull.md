# Runner Outcome Comparison — 2026-11-23 ~06:59 EST

Research only. Original snapshot ~03:16–03:17 EST preserved unchanged at https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-23_0316_EST_overnight_ignition_webull.md . Follow-up connected Webull US_STOCK snapshot at ~06:59 EST. Individual source times below are Unix milliseconds UTC. PRE is a different session from OVN; **do not add their volumes**. Prices are observations, not executable returns.

## SAME original tickers (including original controls)
|Symbol|03:16 OVN price|~06:59 PRE price|Price change from first|03:16 OVN shares|Additional OVN shares by follow-up|Current PRE shares (separate)|PRE bid/ask|PRE spread midpoint|PRE trade UTC ms|PRE quote UTC ms|
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
|WETO|0.8577|0.6663|-22.32%|6,129,373|536,830|21,474,734|0.66/0.6672|1.08%|1795435164256|1795435163334|
|MRM|0.4928|0.3805|-22.79%|5,555,443|510,639|12,930,868|0.365/0.3822|4.60%|1795435162544|1795435161347|
|MEDS|1.72|2.2901|33.15%|1,046,572|92,043|7,832,456|2.29/2.3|0.44%|1795435163480|1795435163433|
|DWTX|1.22|1.2302|0.84%|179,670|9,944|199,409|1.17/1.29|9.76%|1795435154712|1795435099903|
|NXAT|0.4608|0.4442|-3.60%|322,968|15,813|259,352|0.4435/0.4577|3.15%|1795435118001|1795435160219|
|VWAV|0.159|0.1408|-11.45%|1,939,257|17,307|979,171|0.138/0.145|4.95%|1795435156884|1795435035405|
|RAYA|0.6021|0.5701|-5.31%|101,494|10,999|59,401|0.5672/0.5983|5.34%|1795434711020|1795434714307|
|GOVX|1.52|1.4700|-3.29%|25,830|461|30,760|1.32/1.57|17.30%|1795434915305|1795434599913|
|NAK|0.4622|0.4501|-2.62%|2,444|600|19,356|0.45/0.4885|8.20%|1795434176564|1795434617378|
|IQST|0.7159|0.6900|-3.62%|410|0|1,243|0.6624/0.69|4.08%|1795431539830|1795431540057|

Additional OVN shares computed from current OVN cumulative volume minus original OVN cumulative volume. PRE volume is a separate counter. PRE bid/ask is a single L1 snapshot and does not prove spread stability. Quote freshness is determined from source quote timestamps versus ~06:59 EST; IQST is stale. OVN last prices can change after original snapshot, so original values are immutable reference.

## Newly prominent PRE candidates
Webull PRE_MARKET ranking and snapshot cross-check: RBNE, IVVD, HUHU and MSS, plus previously tracked WETO/MEDS/MRM. Ranking may contain thin-print distortions; verify against current PRE session fields.
|Symbol|PRE price|PRE shares|PRE bid/ask|PRE trade UTC ms|Classification|
|---|---:|---:|---|---:|---|
|MSS|1.33|885,415|1.33/1.34|1795435164191|No archived 03:16 baseline; ignition UNKNOWN|
|RBNE|0.052|90,412,726|0.0516/0.0525|1795435164338|No archived 03:16 baseline; ignition UNKNOWN|
|HUHU|0.1700|27,031,582|0.1677/0.1700|1795435163411|No archived 03:16 baseline; ignition UNKNOWN|
|IVVD|0.5565|7,838,871|0.5500/0.5620|1795434959548|No archived 03:16 baseline; ignition UNKNOWN|

RBNE has exceptionally high PRE share count but a very low price; its first ignition, SEC capital structure and actionable liquidity are UNKNOWN. HUHU has high PRE volume but only 10,358 OVN shares in returned snapshot; it was not a verified pre-04:00 ignition. IVVD and MSS have no original baseline.

## Interpretation
- MEDS shows price continuation from original 03:16 observation; WETO and MRM show substantial retracement from first observation, despite large PRE volume.
- DWTX modestly positive; NXAT lower. Other original controls tracked without cherry-picking.
- A ticker's absence from a partial top-30 leaderboard is **not** proof of disappearance from trading; leaderboard omission alone cannot prove a false ignition.
- Interval speed, volume acceleration, buyer-controlled tick tape, defended support, support break and defined entry/stop risk: UNKNOWN. A pair of cumulative session volumes cannot demonstrate instantaneous volume acceleration.
- Known older MEDS secondary coverage: https://news-static.webullfintech.com/us/news-html/20261120/15954332937339904.html ; original issuer timestamp and first responsive trade UNKNOWN. WETO financing exposure and MEDS dilution flagged in prior archives, not cleared today. Fresh first-seen primary PR/SEC catalyst timestamps for these PRE moves UNKNOWN.
- Sources: connected Webull real-time US_STOCK snapshot with extend_hour_required=true and overnight_required=true; connected Webull PRE_MARKET ranking; original GitHub file above.
- Dedup key: 2026-11-23 + symbol + original source snapshot (~03:16 EST) + follow-up source snapshot (~06:59 EST). New file; original unchanged.

## Permission
Speed ↑ UNKNOWN; volume ↑ acceleration UNKNOWN; spread stable/tightening UNKNOWN; buyers control tape UNKNOWN; defended support UNKNOWN; risk defined UNKNOWN. **NO TRADE APPROVED — NO PROOF = NO TRADE.**
