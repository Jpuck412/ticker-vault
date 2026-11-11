# Overnight Ignition Vault — 2026-11-11 ~03:17 EST

## Provenance / session integrity
Connected Webull PRE_MARKET gainers leaderboard and separate overnight_required=true stock snapshots/L1 quotes retrieved around 03:17 ET (08:17 UTC), **before 04:00 ET**. At this clock time the session is OVERNIGHT, not regular 04:00–09:30 premarket, despite Webull leaderboard label PRE_MARKET. Ranking prices, percentage gains and ranking volume are NOT synchronized with overnight trades. Leaderboard volume is NOT verified overnight volume; use explicit ovn_volume instead. Snapshot timestamp is approximate; exact per-symbol overnight trade and quote times are listed below. No tick stream, interval volume, first ignition, tape buyer aggression or support confirmation. NEVER infer these from candles. Deduplication key 2026-11-11 / symbol / ~03:17 EST. New file only, no overwrite.

## Top five selected from US-listed small-cap momentum leaderboard, with actual overnight data
The ranking gain is the provider leaderboard percentage, **NOT** overnight return. The separate OVN % is from snapshot ovn_change_ratio; different baselines. Quote spread is (ask-bid)/midpoint, one point only.

|Symbol|Leaderboard price / gain|Leaderboard reported volume (session UNKNOWN)|OVN last price / OVN %|OVN volume|OVN bid/ask / spread|OVN last trade ET|OVN quote ET|Quality|
|---|---|---:|---|---:|---|---|---|---|
|PEPG|$5.49 / +129.71%|106,515,887|$5.15 / +11.71%|255,345|$5.15/$5.20 / 0.97%|03:16:25|03:17:08|leaderboard and OVN price asynchronous|
|SMX|$17.9995 / +92.51%|30,650,059|$20.19 / +4.88%|238,229|$20.10/$20.20 / 0.50%|03:17:19|03:17:18|extreme historical corporate action/float risk; ask size limited|
|MI|$0.39385 / +59.91%|411,696,893|$0.4858 / +19.51%|1,592,522|$0.4858/$0.4862 / 0.082%|03:17:07|03:17:14|leaderboard far below overnight; 10 shares at best ask|
|MNDO|$1.25 / +43.68%|12,216,845|$1.25 / -0.79%|2,987|$1.24/$1.27 / 2.39%|03:13:38|03:13:38|stale quote ~3.5 min; best ask only 1 share|
|BYAH|$2.95 / +35.31%|3,205,389|$1.79 / -8.21%|3,186|$1.69/$1.77 / 4.62%|03:11:16|03:14:47|stale, poor spread, tiny depth; ranking mismatch|

## Meaningful exceptions and negative controls
|Symbol|Leaderboard price / gain|Leaderboard volume (session UNKNOWN)|OVN price / OVN %|OVN volume|Bid/ask / spread|OVN last trade ET|Quote ET|Reason|
|---|---|---:|---|---:|---|---|---|---|
|PXLW|$6.71 / +28.67%|17,886,868|$7.10 / -2.61%|13,135|$7.09/$7.11 / 0.28%|03:16:01|03:17:17|leaderboard positive, overnight negative; ask 83 shares, bid 3|
|TTEC|$1.69 / +21.15%|22,277,854|$2.27 / -5.42%|34,826|$2.27/$2.28 / 0.44%|03:16:04|03:17:10|overnight negative; bid 5 shares|
|CISS|$2.03 / +16.00%|10,529,219|$1.98 / -2.94%|8,828|$1.98/$2.02 / 2.00%|03:08:57|03:15:23|stale last trade; recurring prior research|

Leaderboard also contained large-cap/non-target symbols and extremely illiquid outliers (e.g. BRBI 432 reported shares); excluded from top five. The five are research candidates, NOT validated first ignitions. A high leaderboard % can reflect yesterday's activity, not current overnight momentum.

## Catalyst / dilution evidence
Webull searches for PEPG, SMX, MI, MNDO (2026-11-10 through 2026-11-11) returned zero matching articles. This is **not evidence that no news exists**. Original issuer PR timestamps, SEC 8-K/424B/S-3/ATM/equity-line acceptance timestamps, reverse splits, financing status, and catalyst-to-first-meaningful-price/volume-response latency are **UNKNOWN** for all eight in this capture. SMX exhibits exceptionally small snapshot outstanding share count (285,794) and extremely high split-adjusted historical 52-week high, a corporate-action/float integrity warning, not independently verified current dilution. MI likewise shows extreme historical 52-week high, requiring split-adjustment review. No first-seen news timestamp can be assigned without primary-source confirmation.

## GitHub comparison
Read 2026-11-10_0324_EST_overnight_ignition_webull.md in Jpuck412/ticker-vault: prior primary OMH/CKX/EDSA/JDZG/MF, exceptions NWGL/NTCL. None of those appear in today's retrieved first 25 leaderboard results; ranking disappearance across days is NOT proven failure. CISS recurs from 2026-11-10 after-hours research; today's overnight snapshot is separate, not a duplicate. Read Jpuck412/puck-elite-price-action-v2/README.md: evidence-first architecture, no prediction from historical pattern matches. No identical 2026-11-11 / symbol / ~03:17 observation was found in the compared dated Nov 10 record; repository-wide exhaustive duplicate scan NOT performed.

## Permission verdict
All eight: **NO TRADE APPROVED**. Speed increasing UNKNOWN; volume acceleration UNKNOWN (only single cumulative OVN volume); spread trend UNKNOWN; buyer-controlled executed tape UNKNOWN; defended support UNKNOWN; defined executable risk UNKNOWN; original catalyst time UNKNOWN. Single-point spread and bid/ask size do not prove execution. First ignition before 4 AM remains UNKNOWN, even though snapshot captured before 4 AM. Source: connected Webull PRE_MARKET leaderboard, Webull overnight-required stock snapshot and depth L1, connected Webull news search, GitHub prior research and V2 README.
