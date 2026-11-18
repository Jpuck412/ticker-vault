# Overnight Ignition Vault — 2026-11-18 03:23 EST

**Research only.** Connected Webull US_STOCK get_stock_snapshot with overnight_required=true and extend_hour_required=true; PRE_MARKET ranking was also requested but returned apparently previous-session leaders, **not** a reliable live overnight ranking. Selected candidates are ranked for research by observed overnight gain/participation and liquidity, not a certified market-wide top five. Snapshot around 03:23 ET, Wednesday 2026-11-18. All quoted times ET on 2026-11-18 unless otherwise noted. Quote and trade timestamps differ. OVN percentage changes are Webull overnight session fields, not from first ignition. No premarket observations yet: premarket begins at 04:00 ET.

## Top five selected (first five rows), exceptions and negative controls

|Symbol|OVN price USD|Webull OVN %|OVN cumulative volume|OVN bid|OVN ask|L1 spread/mid|Last OVN trade ET|OVN quote ET|First ignition time|Verdict|
|---|---:|---:|---:|---:|---:|---:|---|---|---|---|
|ABTS|0.4817|51.19%|2,895,635|0.4808|0.4818|0.21%|03:23:00|03:23:04|UNKNOWN|NO TRADE|
|AZI|1.23|68.47%|1,957,997|1.23|1.24|0.81%|03:22:51|03:23:03|UNKNOWN|NO TRADE|
|GP|3.22|22.90%|287,193|3.21|3.22|0.31%|03:23:05|03:23:05|UNKNOWN|NO TRADE|
|CRIS|0.5922|9.30%|1,131,715|0.5922|0.6006|1.41%|03:23:05|03:23:05|UNKNOWN|NO TRADE|
|AKAN|2.35|14.63%|329,319|2.35|2.37|0.85%|03:23:05|03:23:05|UNKNOWN|NO TRADE|
|BMGL|0.3659|12.76%|402,680|0.365|0.3659|0.25%|03:21:35|03:23:00|UNKNOWN|NO TRADE|
|FRTT|0.6301|-6.71%|278,663|0.63|0.6301|0.02%|03:22:59|03:23:00|UNKNOWN|NO TRADE|
|SLS|17.18|-10.29%|62,608|17.19|17.3|0.64%|03:22:54|03:22:53|UNKNOWN|NO TRADE|
|PAVS|2.41|-9.40%|3,506|2.4|2.41|0.42%|03:22:15|03:22:34|UNKNOWN|NO TRADE|

Top five: ABTS, AZI, GP, CRIS, AKAN. BMGL is a positive exception; FRTT, SLS and PAVS are negative/low-participation controls. SLS is not a preferred small-cap price-band candidate; retained as a high-profile deterioration control. Quote freshness must be judged against actual acquisition time; timestamp is not a continuous liquidity guarantee. No spread tightening inference from one quote. Webull PRE_MARKET leaderboard displayed previous-session values and was excluded as current premarket evidence.

## Historical / methodology comparison

- 2026-11-17 18:29 ET after-hours archive: AZI, CRIS, ABTS, BMGL, AKAN already appeared, so these are **continuations of observed activity**, not newly verified first ignitions. Prior after-hours prices: AZI $1.08, CRIS $0.7573, ABTS $0.4458, BMGL $0.4035, AKAN $2.44. Their overnight prices are not comparable to AH percentages because session baselines differ. GP appeared in 2026-11-17 07:01 follow-up and earlier research.
- Prior archive: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-17_1829_EST_afterhours_catalyst_vault_webull.md
- Puck Elite Price Action V2 README inspected: evidence-first market scan, catalyst, structure, risk, and historical fingerprint; pattern matching is not proof of prediction. https://github.com/Jpuck412/puck-elite-price-action-v2/blob/main/README.md
- Deduplication key: 2026-11-18 + symbol + this 03:23 ET observation; unique filename; no existing records changed.

## Catalyst, dilution, data integrity

Webull search_news on 2026-11-17 through 2026-11-18 returned no matching items for AZI, CRIS, ABTS, AKAN, BMGL. GP keyword returned unrelated PAGP news, excluded. No verified original issuer PR timestamp, SEC 8-K/424B/S-3 acceptance timestamp, ATM/equity line status, reverse split, merger, FDA, earnings or other primary catalyst timestamp established for these selected candidates. These remain **moves without verified fresh news**, not proof of no news. Dilution risk and float verification UNKNOWN. First meaningful responsive trade and catalyst-to-response latency UNKNOWN. No synchronized tick-by-tick tape, successive volume samples or tested support: speed UNKNOWN; volume acceleration UNKNOWN; buyer control UNKNOWN; defended support UNKNOWN; executable risk UNKNOWN. Single L1 spread measured only at quote time. **NO TRADE APPROVED — NO PROOF = NO TRADE.**

## Source provenance

Connected Webull: get_gainers_losers(PRE_MARKET), get_stock_snapshot(US_STOCK, overnight_required=true), search_news (2026-11-17 to 2026-11-18). GitHub fetch_file on ticker-vault prior archive and puck-elite-price-action-v2 README. The market-wide OVN leaderboard is unavailable; selected universe consists of carryover names and premarket ranking context, not an exhaustive overnight discovery feed.
