# Runner Outcome Comparison — 2026-11-09 ~07:00 ET

## Source and timestamps
Original: [03:21 ET GitHub snapshot](https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-09_0321_EST_overnight_ignition_webull.md), unmodified. Follow-up: connected Webull US_STOCK snapshot with extend_hour_required=true and overnight_required=true, PRE_MARKET top-20 ranking and new leader L1 quotes, approximately 07:00–07:01 ET November 9, 2026. Quote epoch timestamps in API output were near 07:00 ET; individual quotes are asynchronous. Original leaderboard prices were NOT synchronized with 03:21 L1. Price change below is **ranking price vs follow-up extended-hours last price**, not verified trade-to-trade return. Original reported volumes have UNKNOWN session coverage; follow-up extend_hour_volume is PRE session; no volume-change inference is valid. No trade ticks, prints, support tests or volume time series obtained.

## Original seven followed up
| Symbol | 03:21 ranking price | ~07:00 PRE last | Indicative change | 03:21 reported volume | ~07:00 PRE volume | Volume change | ~07:00 bid/ask (mid spread) | Rank status |
|---|---:|---:|---:|---:|---:|---|---|---|
| VIVK | $0.8143 | $0.4251 | -47.80% | 252,169,744 (UNKNOWN session) | 252,652 (PRE) | NOT COMPARABLE | $0.419/$0.45 (7.13%) | Absent from retrieved top 20 |
| CDT | $1.47 | $1.121 | -23.74% | 27,133,043 (UNKNOWN session) | 61,560 (PRE) | NOT COMPARABLE | $1.12/$1.14 (1.77%) | Absent from retrieved top 20 |
| RCT | $0.0508 | $0.0339 | -33.27% | 676,429,642 (UNKNOWN session) | 4,838,440 (PRE) | NOT COMPARABLE | $0.0333/$0.0349 (4.69%) | Absent from retrieved top 20 |
| CIIT | $2.48 | $2.1 | -15.32% | 41,800,081 (UNKNOWN session) | 52,724 (PRE) | NOT COMPARABLE | $2.01/$2.1 (4.38%) | Absent from retrieved top 20 |
| DBGI | $0.6651 | $0.2288 | -65.60% | 91,752,424 (UNKNOWN session) | 6,756,324 (PRE) | NOT COMPARABLE | $0.2254/$0.2288 (1.50%) | Absent from retrieved top 20 |
| SHFS | $0.0362 | $0.0245 | -32.32% | 670,096,924 (UNKNOWN session) | 15,884,474 (PRE) | NOT COMPARABLE | $0.0244/$0.0267 (9.00%) | Absent from retrieved top 20 |
| VSA | $2 | $2.2 | 10.00% | 29,801,335 (UNKNOWN session) | 70,269 (PRE) | NOT COMPARABLE | $2.17/$2.27 (4.50%) | Absent from retrieved top 20 |

The original ranking-price/quote mismatch was material for all seven, therefore these percentage differences **must not be interpreted as realized returns or definitive false ignitions**. Original 03:21 bid/ask quotes are in linked snapshot. Present L1 quote timestamps vary; VIVK and RCT quotes are older than some last trades. No defensible spread trend can be inferred from asynchronous session quotes.

## New PRE_MARKET top leaders at ~07:00 ET
| Symbol | Follow-up PRE last | PRE reported volume | L1 bid/ask | L1 midpoint spread | Classification |
|---|---:|---:|---|---:|---|
| OMH | $15.3818 | 928,562 | $15.32/$15.5 | 1.17% | NEW vs 03:21 shortlist |
| NWGL | $4.3098 | 2,328,014 | $4.29/$4.38 | 2.08% | NEW vs 03:21 shortlist |
| JDZG | $0.3544 | 15,234,706 | $0.3515/$0.3624 | 3.05% | NEW vs 03:21 shortlist |
| NTCL | $0.3477 | 24,244,495 | $0.32/$0.3739 | 15.54% | NEW vs 03:21 shortlist |
| INLF | $0.306 | 16,614,842 | $0.305/$0.3353 | 9.46% | NEW vs 03:21 shortlist |

Ranked Webull PRE_MARKET top five included OMH, NWGL, JDZG, NTCL, CKX; CKX excluded from the small-price research shortlist ($14.9885 ranking; 130,375 reported ranking volume) and INLF added as meaningful sub-dollar exception. These current prices/quotes were retrieved separately from rankings and are not fully synchronized. Ranking gain percentages: OMH +108.42%, NWGL +70.12%, JDZG +68.60%, NTCL +52.66%, INLF +34.65%. Reported ranking volumes may differ from snapshot PRE volumes.

## Outcome classification and catalysts
- Original five VIVK, CDT, RCT, CIIT, DBGI, plus SHFS and VSA: **all absent from retrieved current top 20**; ranking disappearance verified, not necessarily failed trades. Indicative price changes negative for first six, positive for VSA. **False ignition: UNPROVEN** because original prices were asynchronous with L1.
- New leaders OMH/NWGL/JDZG/NTCL/INLF: no 03:21 baseline; first ignition timing UNKNOWN. They cannot be labeled newly ignited at 07:00.
- First-seen news: original 03:21 record cites historical CDT November 6 09:24:34 ET secondary report, RCT November 6 02:07:16 ET recap, CIIT November 6 00:33:03 ET recap. These are NOT verified original issuer release timestamps or Monday ignition. Fresh first-seen PR/SEC acceptance times for all current leaders UNKNOWN; dilution/ATM/424B/S-3 status UNKNOWN.
- Support defended UNKNOWN; speed UNKNOWN; volume acceleration UNKNOWN; aggressive buyer control UNKNOWN; spread direction UNKNOWN; defined risk UNKNOWN. NO TRADE APPROVED for any symbol.

## Data integrity
Dedup key 2026-11-09 / symbol / ~07:00 ET follow-up. Keep original 03:21 file intact. Prices are not synchronized, and original reported volume and current PRE volume are different definitions. Do not subtract them to claim volume change. Candlestick highs/lows do not prove defended support. Webull snapshots and PRE_MARKET ranking are connected data sources; no historical tick feed used.
