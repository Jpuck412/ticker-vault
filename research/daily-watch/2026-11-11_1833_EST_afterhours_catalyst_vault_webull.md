# After-Hours Catalyst Vault — 2026-11-11 18:33 EST

## Provenance
Webull AFTER_MARKET leaderboard (gainers and losers), separately queried Webull extended-hour stock snapshots and independent L1 quotes, retrieved approximately 18:33 ET Nov 11, 2026. Prices and ranking percentages are asynchronous; below use snapshot AH prices/changes and AH-only volumes. Webull timestamps are epoch milliseconds and should be converted to America/New_York for detailed auditing. No tick-by-tick time-and-sales or intraminute acceleration was available. First ignition must not be inferred from high/low candles.

Dedup key: 2026-11-11 / ticker / 18:33 ET / AFTER_MARKET catalyst vault. No matching Nov 11 afterhours file was returned by repository search. Earlier Nov 10 18:34 record was retrieved and preserved.

## Five primary candidates
|Ticker|AH snapshot last|AH change from 16:00 close|AH-only volume|L1 bid/ask|Midpoint spread|Displayed best ask|Original post-16:00 catalyst|First responsive print|Verdict|
|---|---:|---:|---:|---|---:|---:|---|---|---|
|PLCE|$0.8600|+333.25%|34,906,276|$0.8600/$0.8668|0.79%|2|UNKNOWN; Nov 8 Chapter 11 and Nov 9 8-K are historical|UNKNOWN|NO TRADE — bankruptcy, ask liquidity|
|ICMB|$1.2102|+95.79%|1,351,487|$1.20/$1.22|1.65%|33|UNKNOWN|UNKNOWN|NO TRADE|
|ADXN|$5.6500|+95.50%|2,936,286|$5.60/$5.75|2.64%|30|UNKNOWN; historical ATM financing reported Aug 2026|UNKNOWN|NO TRADE|
|POAS|$1.5400|+70.98%|3,407,250|$1.50/$1.59|5.83%|22|UNKNOWN|UNKNOWN|NO TRADE|
|CENN|$0.1776|+21.39%|15,052,539|$0.1770/$0.1827|3.17%|5,000|UNKNOWN; historical 424B5 dated Oct 13|UNKNOWN|NO TRADE|

**Additional meaningful positive:** NCT $0.8600 +19.44%, AH-only 5,469,994, bid/ask $0.86/$0.89 (3.43%), best bid only 2 shares; Nov 10 reverse-split/6-K report, proposed effective Nov 16 (secondary source; original acceptance time UNKNOWN). No trade.

**Negative controls:** RKDA $0.1792, -24.64%, AH-only 2,159,977, bid/ask $0.1651/$0.1810 (~9.19%); XAIR $2.0200, -23.19%, AH-only 49,176, bid/ask $2.01/$2.40 (~17.69%). First negative response timing UNKNOWN. WHLR also -19.89% in leaderboard, but AH-only volume and L1 not checked; historical user exclusion, not a candidate.

## Catalyst / risk distinction
Webull same-day news keyword searches for PLCE, ICMB, ADXN, POAS, CENN, NCT returned empty. These are **moves without verified fresh post-16:00 issuer news**, NOT proof of no news. No independently verified news-without-move candidate identified. PLCE's Chapter 11 petitions Nov 8 and Nov 9 8-K are confirmed historical bankruptcy developments, not proof of tonight's trigger. PLCE filing reported approximately $394m debt-instrument obligations. CENN 424B5 dated Oct 13, 2026 merits dilution review. ADXN historical ATM financing merits dilution review. NCT reverse split creates share-adjustment risk. Original SEC EDGAR acceptance timestamps, 8-K/6-K/424B/S-3/ATM/equity-line issuance after 16:00, FDA/clinical, earnings, merger timestamps: UNKNOWN where not directly verified. Catalyst-to-first-meaningful-executed-response latency UNKNOWN for every ticker.

## Original sources and audit
- Webull connected AFTER_MARKET ranking, snapshot and L1 quotes, retrieved Nov 11 ~18:33 ET.
- Webull same-day news searches, Nov 11 2026, no matching articles for six symbols.
- PLCE bankruptcy Reuters Nov 9: https://www.reuters.com/legal/litigation/clothing-retailer-childrens-place-files-bankruptcy-seek-sale-2026-11-09/
- PLCE 8-K index (Nov 9 08:00 listed by secondary aggregator): https://www.stocktitan.net/sec-filings/PLCE/8-k.html
- CENN filing history: https://www.aries.com/us/en/stocks/CENN/filings
- NCT reverse split/6-K secondary reporting: https://www.stocktitan.net/overview/NCT/
- Direct EDGAR original filing/acceptance verification remains outstanding: https://www.sec.gov/edgar/search/
- Prior preserved record: research/daily-watch/2026-11-10_1834_EST_afterhours_catalyst_vault_webull.md

## Puck permission and unknowns
Price speed ↑ UNKNOWN; interval volume acceleration UNKNOWN; buyer-controlled executed tape UNKNOWN; spread trend UNKNOWN (single quote); defended support UNKNOWN; defined risk UNKNOWN. Quote freshness must be assessed against retrieval; quote timestamps available as raw epoch ms in Webull response, but cross-feed synchronization not guaranteed. All five plus controls **NO TRADE**. No proof = no trade.
