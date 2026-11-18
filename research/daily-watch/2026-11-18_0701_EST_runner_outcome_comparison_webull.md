# Runner Outcome Comparison — 2026-11-18 ~07:01 EST

**Research only; no trade approved.** Original source: [03:23 EST archived overnight snapshot](https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-18_0323_EST_overnight_ignition_webull.md). Original file preserved. Follow-up connected Webull get_stock_snapshot (US_STOCK, overnight_required=true, extend_hour_required=true), get_stock_quotes L1, and get_gainers_losers(PRE_MARKET), collected around 07:01 EST Nov 18. Prices are last reported PRE extended-hour prices, not executable bids. Original overnight values retained. **OVN cumulative volume is not comparable directly with PRE session volume; delta is same OVN field only.**

|Symbol|03:23 OVN price|~07:01 PRE price|Change from early|OVN volume 03:23 → last OVN|OVN volume Δ|PRE volume (separate)|PRE L1 bid/ask|Spread/mid|Outcome|
|---|---:|---:|---:|---:|---:|---:|---|---:|---|
|ABTS|$0.4817|$0.3114|-35.35%|2,895,635 → 3,106,204|+210,569|11,412,846|0.31/0.3386|8.82%|Lower follow-up|
|AZI|$1.23|$0.93|-24.39%|1,957,997 → 2,113,169|+155,172|4,840,508|0.88/0.93|5.52%|Lower follow-up|
|GP|$3.22|$2.9532|-8.29%|287,193 → 427,694|+140,501|1,713,532|2.97/3.03|2.00%|Lower; leaderboard present|
|CRIS|$0.5922|$0.51|-13.88%|1,131,715 → 1,225,169|+93,454|2,666,549|0.49/0.53|7.84%|Lower follow-up|
|AKAN|$2.35|$2.5105|6.83%|329,319 → 359,870|+30,551|559,165|2.51/2.55|1.58%|Higher follow-up|
|BMGL|$0.3659|$0.3225|-11.86%|402,680 → 432,717|+30,037|841,151|0.2988/0.332|10.53%|Lower follow-up|
|FRTT|$0.6301|$0.6598|4.71%|278,663 → 298,674|+20,011|512,493|0.6447/0.6897|6.74%|Higher follow-up|
|SLS|$17.18|$18.38|6.98%|62,608 → 70,332|+7,724|110,513|18.12/18.45|1.80%|Higher follow-up|
|PAVS|$2.41|$2.24|-7.05%|3,506 → 5,700|+2,194|26,288|2.21/2.33|5.29%|Lower follow-up|


## New premarket leaders and ranking limitations

Webull PRE_MARKET ranking returned SVRE +122.21% at $0.9098, GMM +51.06% at $2.095, AZI +27.38% at $0.93, AKAN +22.92% at $2.5185, GP +12.66% at $2.9518 (plus very low-volume names). Fresh per-symbol snapshot confirms SVRE ~$0.9097, PRE volume 16,206,754 and L1 0.9095/0.915 (spread ~0.60%); GMM ~$2.0779, PRE volume 4,264,193 and L1 2.06/2.07 (~0.48%). Both were **not in the early nine-symbol archive**, so first-observation change and first ignition are UNKNOWN. Ranking feed and snapshot have minor collection-time differences; some ranking fields may be stale, so fresh per-symbol data takes precedence. GP remains a listed leader but below its 03:23 price. AZI and AKAN appear on leaderboard. ABTS and CRIS not in returned top 20: **leaderboard disappearance**, not proof trading stopped. SVRE and GMM are newly meaningful relative to selected early universe, not proof they were absent market-wide before 04:00.

## Classification and caveats

- **Sharp deterioration:** ABTS, AZI, CRIS, BMGL. ABTS PRE $0.3114 vs $0.4817 early; AZI $0.93 vs $1.23. These are adverse early-to-follow-up outcomes, **not verified false ignition** because first response and tape sequence are missing.
- **Relative continuation:** AKAN +6.83%, FRTT +4.71%, SLS +6.98%; latter two are negative-control names with higher PRE price, not automatically momentum confirmations. GP lower than early, still premarket leader.
- **Execution caution:** ABTS ~8.82% L1 spread; CRIS ~7.84%; BMGL ~10.53% with just 1 share at best ask; FRTT ~6.75% with 1 share at best ask; PAVS ~5.29% with 1 share best bid and 2 best ask. L1 depth is not sustained liquidity.
- **Catalysts:** Early archive found no verified original fresh issuer PR or SEC acceptance times for primary candidates. First-seen original catalyst time, first meaningful responsive tick, catalyst-to-response delay, dilution review and any fresh follow-up news are UNKNOWN; no primary source timing claim is made.
- **Evidence:** Tick-by-tick speed, volume acceleration, buyer control, defended support, and executable defined risk UNKNOWN. Snapshot quotes near ~07:01 EST, but individual quote timestamps and trades are not synchronized; see Webull source fields. PRE volumes are session totals and cannot prove acceleration. No false ignition or support break asserted without tape.

**PUCK PERMISSION: NO TRADE APPROVED — NO PROOF = NO TRADE.**
