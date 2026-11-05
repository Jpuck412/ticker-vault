# Runner Outcome Comparison — 2026-11-05 07:05 EST

## Provenance
- Original: [03:20 EST early snapshot](2026-11-05_0320_EST_overnight_ignition_unverified.md), **historical November 4 after-hours carry-forward only**; no verified Nov 5 pre-4AM trades.
- Follow-up: Webull connected PRE_MARKET top-20 ranking and L1 stock quotes, retrieved at approximately 07:05 EST Nov 5. Quote timestamps are epoch milliseconds converted to ET. Ranking response did not include per-row quote timestamps; ranking freshness UNKNOWN.
- Comparison below is historical Nov 4 AH vendor price to Nov 5 Webull PRE_MARKET ranking price; **not** price change since a genuine 03:20 overnight trade.
- No original records modified. Dedup key: 2026-11-05 + ticker + 07:05 EST.

## Original five — later observation
| Symbol | Nov 4 AH vendor price | Nov 5 Webull PRE_MARKET price | Difference vs historical price | Reported ranking volume (session scope UNKNOWN) | Bid / ask at quote timestamp ET | Spread / % of midpoint | Outcome |
|---|---:|---:|---:|---:|---|---|---|
| AEHL | $10.63 | $10.71 (+71.46% vs preclose) | +$0.08 (+0.75%) | 768,137 | $10.70 / $10.89 at 07:05:04.007 | $0.19 / 1.76% | CONTINUATION in ranking, not verified speed |
| ZNB | $0.98 | $1.4483 (+133.12%) | +$0.4683 (+47.79%) | 12,652,872 | $1.44 / $1.45 at 07:05:04.665 | $0.01 / 0.69% | STRONGEST PRICE CONTINUATION vs AH historical |
| PLCE | $0.36 | $0.2984 (+23.82%) | -$0.0616 (-17.11%) | 6,650,432 | $0.2974 / $0.308 at 07:05:03.235 | $0.0106 / 3.50% | RETRACEMENT, still ranked |
| JLHL | $9.15 | NOT in returned top-20; last trade UNKNOWN | UNKNOWN | UNKNOWN | $7.44 / $7.57 at 07:04:57.655 | $0.13 / 1.73% | DISAPPEARED FROM TOP-20; bid/ask not last trade |
| ARQ | $2.20 | $2.32 (+26.49%) | +$0.12 (+5.45%) | 1,296,052 | $2.32 / $2.33 at 07:05:04.956 | $0.01 / 0.43% | CONTINUATION in ranking |

All percentages in parentheses after current prices are Webull PRE_MARKET change ratios relative to its supplied prior close, not changes since 03:20. Webull volume is a single snapshot; acceleration and change since 03:20 UNKNOWN. Quote sizes are displayed book depth, not executed trade volume. The 03:20 report had no current-session price, volume or spread, so true same-session changes UNKNOWN.

## New meaningful top-20 candidates
| Symbol | Webull PRE_MARKET price | Change vs prior close | Ranking reported volume | L1 bid / ask (timestamp ET) | Spread | Classification |
|---|---:|---:|---:|---|---|---|
| ELPW | $4.09 | +63.35% | 6,358,588 | $4.11 / $4.15 (07:05:08.038) | $0.04 (0.97% midpoint) | NEW leader; last-ranking price and later quote differ |
| JDZG | $0.435 | +44.13% | 14,640,820 | $0.432 / $0.46 (07:05:06.579) | $0.028 (6.28% midpoint) | NEW leader; wide spread |
Additional large-price names excluded from low-priced focus; TBI $12.91 +31.20% but only 37,169 reported volume, excluded from primary small-cap shortlist. No verified first ignition time for any ticker.

## Catalyst / dilution checks
- Fresh original PR/SEC timestamp and first responsive trade for AEHL, ZNB, PLCE, JLHL, ARQ, ELPW, JDZG: UNKNOWN. Historical Nov 4 AH watchlist lists JLHL 04:20 news listing but issuer time unverified, ARQ earnings categorization with original time UNKNOWN.
- ZNB: March 10 2026 issuer announcement of convertible notes and warrants under F-3 (historical dilution overhang, **not** a Nov 5 catalyst): https://www.nasdaq.com/press-release/zeta-network-group-nasdaq-znb-announces-pricing-6-million-registered-direct-offering
- ELPW: issuer IR archive records Oct 28 $25.5M agreement, earlier offerings and share consolidation; historical dilution/reverse-split risk, **not** proven Nov 5 catalyst: https://ir.elongpower.com/info . Historical Nov 2 report of lock-up expiration Nov 3: https://www.marketscreener.com/quote/stock/ELONG-POWER-HOLDING-LIMIT-154102801/news/ . Direct SEC acceptance times not checked.
- No original fresh Nov 5 catalyst has been independently matched to first responsive tick. Moves without verified fresh news: all listed above. News without move: not established.

## Integrity / permission
- Webull PRE_MARKET ranking at ~07:05 EST is NOT overnight execution tape; no pre-04:00 ignition proven.
- Bid/ask quote times are fresh ~07:05, but ranking last-price timestamps are UNKNOWN; do not equate ranking last price to simultaneous executable price.
- No sequential tick or trade prints, no time-series volume, no aggressive buyer classification, no defended support test, no defined invalidation risk. All UNKNOWN.
- No confirmed false ignition: PLCE historical-to-current retracement and JLHL absence from top 20 are *research flags*, not proven failed pre-04:00 ignitions.
- Verdict ALL: NO TRADE. No orders placed. NO PROOF = NO TRADE.
