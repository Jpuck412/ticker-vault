# Overnight Ignition Vault — 2026-11-06 03:24 EST

## Data integrity
Connected Webull PRE_MARKET leaderboard retrieved around 03:24 EST (before 04:00 ET). Webull AFTER_MARKET leaderboard separately retrieved as prior-session context. **PRE_MARKET is a vendor ranking label, not proof of premarket exchange trades before 04:00.** Overnight-required L1 quotes requested; quote timestamps are epoch milliseconds converted to EST. Ranking price and L1 quotes are materially inconsistent for several tickers; no synchronized last-trade timestamp supplied. Ranking volume may include previous session(s); session boundary UNKNOWN. Therefore no first ignition, speed, volume acceleration, tape, or defended support can be verified. No trade authorized.

## Top five Webull ranked US small-cap momentum candidates (03:24 ET observation)
|Symbol|Rank price|Rank % move|Reported volume (session UNKNOWN)|Overnight L1 bid/ask|Spread / midpoint|L1 timestamp EST|Data integrity|Verdict|
|---|---:|---:|---:|---|---|---|---|---|
|AEHL|$12.68|+102.23%|26,622,565|$10.85/$10.81|CROSSED; INVALID|03:24:04|Bid above ask; rank vs quote discrepancy; historical ATM risk|NO TRADE|
|LABT|$0.3851|+101.20%|753,749,663|$0.4921/$0.4905|CROSSED; INVALID|03:24:05|Rank vs quote discrepancy; reverse-split/authorized-share risk|NO TRADE|
|ZNB|$1.19|+91.32%|87,091,436|$1.02/$1.03|$0.01 / 0.98%|03:23:55|Rank price $1.19 not synchronized to L1|NO TRADE|
|FLYE|$2.63|+54.70%|27,752,335|$2.00/$2.01|$0.01 / 0.50%|03:23:54|Rank price $2.63 not synchronized to L1|NO TRADE|
|AMTX|$1.70|+36.00%|16,591,322|$1.73/$1.74|$0.01 / 0.58%|03:22:04|L1 >2 min old at observation; ranking unsynchronized|NO TRADE|

Additional meaningful exceptions (ranked, not verified overnight ignition):
- ELPW $3.41 +35.86%, reported volume 63,879,868; L1 $1.16/$1.19, spread $0.03 / 2.55%, quote 03:22:31 EST. Huge rank/quote discrepancy. NO TRADE.
- ARQ $2.4903 +34.61%, reported volume 11,346,612; L1 $2.26/$2.30, spread $0.04 / 1.75%, quote 03:20:44 EST (stale). NO TRADE.
- Other prior AFTER_MARKET leaderboard context: CIIT $2.47 +59.35%, SHFS $0.0387 +45.49%, RCT $0.0416 +38.67%, JDZG $0.5032 +27.46%, COYA $3.535 +25.80%. These are NOT verified current overnight leaders; session boundaries and quote freshness UNKNOWN.

## Historical comparison
- 2026-11-05 18:33 EST AFTER_MARKET vault: AEHL was a -23.74% downside control at $13.23; today's rank shows +102.23% at $12.68, but changes are measured against differing reference baselines and must not be interpreted as an overnight +102% return. Historical AEHL $100m ATM announced Oct 1, 2026; dilution status NOT CLEARED.
- Prior 2026-11-05 07:05 EST outcome vault: ZNB $1.4483, ELPW $4.09, ARQ $2.32; today's ranking values differ but do not represent same-session first observations.
- Existing Jpuck412/puck-elite-price-action-v2 scanner guidance: Top Gainers → Speed → Spread → Volume → Entry → Exit; no invented tape, support, catalyst or float.
- Deduplication key: 2026-11-06 / each symbol / 03:24 EST. This file is a NEW observation; earlier dated files unchanged.

## Catalyst / SEC checks
- LABT SEC June 17, 2026 8-K documents 1-for-10 reverse split effective June 19 16:01 ET: https://www.sec.gov/Archives/edgar/data/2079272/000121390026069512/ea0294845-8k_lakewood.htm
- LABT September 28, 2026 17:49 ET 8-K acceptance (secondary tracker) describes approval of increase in authorized common stock to 100m and further reverse-split authority: https://www.stocktitan.net/sec-filings/LABT/8-k-lakewood-amedex-biotherapeutics-inc-reports-material-event-2bf16e9b9387.html . Authorization is not proof of actual issuance.
- AEHL historical financing/ATM and October 2026 filing references in 2026-11-05 after-hours vault. Current shares sold UNKNOWN.
- Fresh original November 5 after-close issuer PR timestamps, November 6 SEC acceptance timestamps, first meaningful overnight trade timestamps and exact news-to-response latency: UNKNOWN for ALL candidates. No fresh catalyst verified in this scan. No-news-found is not proof of no news.

## Permission / missing fields
For every symbol: executed price-speed sequence UNKNOWN; volume acceleration UNKNOWN; aggressive buyer tape UNKNOWN; defended support UNKNOWN; defined executable risk UNKNOWN; verified pre-04:00 first ignition UNKNOWN. Bid/ask L1 alone does not prove stability. Crossed quotes AEHL/LABT must be rejected. **NO PROOF = NO TRADE.**

Sources: connected Webull PRE_MARKET and AFTER_MARKET rankings (~03:24 EST); connected Webull overnight-required L1 quotes (individual timestamps above); GitHub prior record https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-05_1833_EST_afterhours_catalyst_vault_webull.md ; https://github.com/Jpuck412/puck-elite-price-action-v2/blob/main/skills/puck-momentum/scanner.md ; SEC and secondary links above.
