# Runner Outcome Comparison — 2026-11-16 ~07:00 EST

## Provenance
Original immutable early snapshot: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-16_0332_EST_overnight_ignition_webull.md (~03:32 EST). Follow-up connected Webull US_STOCK snapshot with extend_hour_required=true and overnight_required=true, plus PRE_MARKET gainers leaderboard, approximately 07:00 EST November 16, 2026. Price comparisons are **overnight last versus premarket last**, indicative and non-executable. Snapshot prices, quote times and session volume are asynchronous. Do not add overnight and premarket volumes. Fresh follow-up premarket quote timestamp near 07:00 EST; original file contains rounded original times. No tick tape retrieved.

## Same-symbol comparisons
|Symbol|03:32 OVN price|~07:00 PRE price|Price delta|OVN volume original → follow-up (same-session field)|PRE volume (separate field)|Current L1 spread|
|---|---:|---:|---:|---|---:|---:|
|POLA|0.4739|0.3649|-23.00%|4,005,030 → 4,129,060 (+124,030; overnight only)|12,731,028 (premarket separate)|2.33%|
|CLRO|4.35|5.0663|16.47%|320,243 → 326,690 (+6,447; overnight only)|3,429,635 (premarket separate)|0.79%|
|VTSI|4.39|4.33|-1.37%|10,052 → 10,594 (+542; overnight only)|28,691 (premarket separate)|2.33%|
|MRLN|1.11|1.13|1.80%|107,768 → 111,610 (+3,842; overnight only)|208,853 (premarket separate)|6.22%|
|SLSN|1.45|1.53|5.52%|22,912 → 24,585 (+1,673; overnight only)|55,293 (premarket separate)|5.71%|
|SHFS|0.0275|0.024|-12.73%|22,197,451 → 22,815,054 (+617,603; overnight only)|18,861,094 (premarket separate)|15.32%|
|ZBAO|0.2307|0.1996|-13.48%|551,421 → 555,894 (+4,473; overnight only)|663,335 (premarket separate)|4.93%|
|ONFO|0.6166|0.5845|-5.21%|257,809 → 266,899 (+9,090; overnight only)|152,205 (premarket separate)|5.13%|
|FCUV|5.32|4.9292|-7.35%|239,584 → 260,378 (+20,794; overnight only)|202,877 (premarket separate)|3.70%|
|AIMD|1.1|1.4385|30.77%|140,029 → 141,139 (+1,110; overnight only)|9,244,669 (premarket separate)|1.40%|

Remaining original controls: OGEN, PARA, SNAL, STAK, SHIM, MITQ, BBCI were not re-quoted in this follow-up; current price, volume, spread and outcome **UNKNOWN**. This is a partial recheck, not full original-universe coverage.

## New leaders from fresh PRE_MARKET leaderboard and snapshots
- AKAN $2.0497, +50.71% vs prior close, PRE volume 8,289,359, bid 2.04 ask 2.05 (~0.49%); not on early archived list. Overnight price $1.90 and OVN volume 1,641,392; first ignition UNKNOWN.
- GP $1.7202, +48.29%, PRE volume 9,842,455, bid 1.72 ask 1.73 (~0.58%); OVN $1.15 / 12,150 shares; first ignition UNKNOWN.
- LGHL $1.98, +37.50%, PRE volume 2,329,673, bid 1.98 ask 1.99 (~0.50%); overnight only 7 shares; first ignition UNKNOWN.
- GIPR $0.2755, +24.32%, PRE volume 11,610,421, bid .2665 ask .2844 (~6.50%); OVN $0.3644 and 4,187,029 shares; apparent deterioration relative to overnight, first ignition UNKNOWN.
- SBMT $9.88, +58.84%, PRE volume **10 shares only**, bid $5.54 ask $9.22 (~49.86%); reject as illiquid leaderboard artifact.
- Existing CLRO $5.0663 (+50.34% premarket) and POLA $0.3649 (+34.80% premarket) remain on leaderboard. These percentages use prior regular close, **not** the 03:32 prices.

## Outcomes
- Original top five: CLRO +16.47%, VTSI -1.37%, POLA -23.00%, MRLN +1.80%, SLSN +5.52% between snapshots. CLRO continues strongly; POLA has major deterioration despite still being a premarket gainer. These are NOT verified ignition/failure labels.
- Original candidate disappearance from leaderboard: VTSI, MRLN, SLSN absent from retrieved top 20, not proof of inactivity. POLA and CLRO retained.
- Overnight cumulative changes shown for the 10 rechecked symbols are **not acceleration**. Some PRE totals are below OVN totals due to session reset, not negative traded volume.
- Verified support, buyer-initiated trades, interval speed, volume acceleration, spread stability and first responsive trade all **UNKNOWN**. One L1 quote does not prove buyer control or defended support.

## News and risk
Original 03:32 record references POLA's Nov 13 16:05:45 ET secondary roundup and historical equity facility; no fresh primary-source issuer or SEC acceptance timestamp established by this comparison. CLRO original catalyst UNKNOWN. First-seen original news times for all other symbols UNKNOWN. No original PR/SEC verification conducted at follow-up; dilution status UNKNOWN except historical flagged POLA facility / SHFS risks. No inference from candles.

## Permission and verdict
ALL symbols **NO TRADE APPROVED**: speed UNKNOWN, volume acceleration UNKNOWN, spread trend UNKNOWN, buyer control UNKNOWN, defended support UNKNOWN, defined executable risk UNKNOWN. Evidence > prediction. Original snapshot preserved. Dedup identity: 2026-11-16 / symbol / ~07:00 EST / PRE follow-up; distinct from ~03:32 EST / OVN.

## Sources
Connected Webull get_stock_snapshot US_STOCK (10 original symbols + 5 newcomers) and get_gainers_losers PRE_MARKET queried November 16 ~07:00 EST; linked GitHub original file above.