# Runner Outcome Comparison — 2026-11-17 ~07:01 EST

Original snapshot: [03:25 EST overnight](https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-17_0325_EST_overnight_ignition_webull.md). Follow-up: connected Webull PRE session snapshot, queried ~07:01 ET, November 17, 2026. Original preserved. Sources: Webull get_stock_snapshot with extend_hour_required=true and overnight_required=true; get_gainers_losers PRE_MARKET. PRE leaderboard may have stale/inconsistent session fields; individual live snapshot used for prices. Quote timestamps and trades in returned snapshot are not perfectly synchronized. Price delta compares 03:25 OVN with ~07:01 PRE, not an executable return. OVN volume delta compares cumulative OVN session field at two observations; PRE volume is separate and NOT subtracted from OVN.

|Symbol|03:25 OVN $|~07:01 PRE $|Price delta|03:25 OVN vol|07:01 OVN vol|OVN vol delta|07:01 PRE vol|PRE bid/ask|Spread/mid|
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
|CSAI|2.26|1.29|-42.92%|1,542,147|1,682,529|140,382|3,743,789|1.28/1.29|0.78%|
|SPAI|3.31|2.93|-11.48%|437,406|553,625|116,219|671,625|2.91/2.94|1.03%|
|GLAS|1.67|1.47|-11.98%|182,374|211,746|29,372|291,363|1.42/1.5|5.48%|
|AYTU|2.62|2.64|0.76%|33,944|36,518|2,574|168,463|2.63/2.64|0.38%|
|AKAN|2.59|2.89|11.58%|914,573|962,245|47,672|2,160,569|2.88/2.9|0.69%|
|GP|1.59|2.15|35.22%|114,272|122,487|8,215|9,034,348|2.15/2.16|0.46%|
|GIPR|0.254|0.2467|-2.87%|233,399|239,424|6,025|286,997|0.2289/0.2744|18.08%|
|GMM|1.61|1.64|1.86%|956,274|984,098|27,824|750,633|1.54/1.65|6.90%|
|CYAB|0.1176|0.1018|-13.44%|2,106,741|2,223,197|116,456|2,622,977|0.1/0.102|1.98%|
|CLRO|4.43|4.5797|3.38%|15,426|16,029|603|36,569|4.4/4.58|4.01%|
|SMTK|UNKNOWN|0.2101|UNKNOWN|UNKNOWN|4,376|UNKNOWN|517,223|0.21/0.2136|1.70%|
|BMGL|UNKNOWN|0.3855|UNKNOWN|UNKNOWN|515,364|UNKNOWN|16,592,827|0.3805/0.42|9.87%|
|BURU|UNKNOWN|0.2365|UNKNOWN|UNKNOWN|22,986|UNKNOWN|13,236,962|0.235/0.2586|9.56%|

## Interpretation
- Original five: CSAI fell 42.92%, SPAI fell 11.48%, GLAS fell 11.98%, AYTU rose 0.76%, AKAN rose 11.58% from their 03:25 OVN observations. This is observed deterioration/continuation, NOT verified false ignition.
- GP advanced 35.22% from its early observation and is a meaningful emerging premarket leader; BMGL, BURU and SMTK appeared on the PRE leaderboard but lacked 03:25 baseline, so first-seen timing UNKNOWN.
- The leaderboard returned GP, AYTU, SMTK, AKAN, BMGL, BURU, SPAI and GLAS, with some highly suspect tiny-volume entries (SENEB 2 shares, AKO B 1 share). CSAI and CYAB disappeared from retrieved top 20. Do not equate rank disappearance with stopped trading.
- CSAI: original issuer earnings release 2026-11-16 17:30 ET; AYTU acquisition release 16:02 ET; GLAS earnings 16:05 ET. Original response trade timestamps UNKNOWN. Other original issuer first-seen news timestamps UNKNOWN. Dilution and financing risks from early archive remain applicable; no fresh SEC verification performed here.
- Current PRE quote timestamps are near ~07:01 ET in Webull response (Unix milliseconds), but precise wall-clock capture timestamp is approximate; OVN quote fields near 04:00 ET are stale for 07:01 PRE and MUST NOT be used for current spread.
- Current spreads are point-in-time indicative only. No verified intraday defended support, synchronized trade speed, interval volume acceleration, buyer-control tape, or executable stop/risk. No verified first ignition or failure time. Cumulative volume deltas are not acceleration. Source session labels can be inconsistent; PRE volume vs OVN volume is not a same-session comparison.

**Verdict: NO TRADE APPROVED. NO PROOF = NO TRADE.**
