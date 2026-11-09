# Overnight Ignition Vault — 2026-11-09 03:21 ET

## Provenance and limitations
Webull PRE_MARKET ranking queried at approximately 03:21 ET Monday Nov 9, **before the 04:00 ET premarket opening**. These are overnight/extended-hours ranking observations, NOT verified first ignition. Webull's PRE_MARKET label does not establish session-specific first-trade time. Ranking prices and depth quotes are materially asynchronous; ranking volume has UNKNOWN session coverage. No historical tick sequence, trade prints, or intraday volume buckets were returned. Thus first ignition, speed, volume acceleration, buyer control, support, and risk remain UNKNOWN; NO TRADE for every symbol. Dedup key 2026-11-09 / symbol / 03:21 ET ranking capture. No earlier Nov 9 file was present in inspected daily-watch directory.

## Ranked top five plus meaningful controls
| Symbol | Ranking price | Ranking % gain | Reported volume (session UNKNOWN) | L1 bid / ask | L1 spread % midpoint | Quote ET Nov 9 | Data assessment |
|---|---:|---:|---:|---|---:|---|---|
| VIVK | $0.8143 | +120.08% | 252,169,744 | $0.442 / $0.45 | 1.79% | 03:21:28 | Ranking price outside L1 spread; UNSYNCHRONIZED |
| CDT | $1.47 | +73.76% | 27,133,043 | $1.11 / $1.12 | 0.90% | 03:21:38 | Ranking price outside L1 spread; UNSYNCHRONIZED |
| RCT | $0.0508 | +69.33% | 676,429,642 | $0.0412 / $0.0413 | 0.24% | 03:21:28 | Ranking price outside L1 spread; UNSYNCHRONIZED |
| CIIT | $2.48 | +60.00% | 41,800,081 | $2.14 / $2.15 | 0.47% | 03:21:17 | Ranking price outside L1 spread; UNSYNCHRONIZED |
| DBGI | $0.6651 | +41.51% | 91,752,424 | $0.3022 / $0.3049 | 0.89% | 03:21:36 | Ranking price outside L1 spread; UNSYNCHRONIZED |
| SHFS | $0.0362 | +36.09% | 670,096,924 | $0.0299 / $0.03 | 0.33% | 03:21:37 | Ranking price outside L1 spread; UNSYNCHRONIZED |
| VSA | $2 | +29.87% | 29,801,335 | $2.04 / $2.07 | 1.46% | 03:21:37 | Ranking price outside L1 spread; UNSYNCHRONIZED |

Top five: VIVK, CDT, RCT, CIIT, DBGI. Exceptions/controls: SHFS (sub-dollar high reported volume) and VSA (next ranked small cap). Quote times derived from Webull epoch-millisecond quote_time converted to America/New_York. No verified quote freshness relative to exact ranking fetch time; quotes are approximately contemporaneous at 03:21 ET, not a synchronized NBBO. L1 displayed size is not tape or buyer control. Very large reported volumes may be cumulative from prior sessions.

## Catalysts and dilution
- CDT: Webull news search returned Benzinga item 'Corvus Capital Proposes To Acquire CDT Equity At $2 Per Share', timestamp 2026-11-06 14:24:34 UTC (09:24:34 ET), https://news-static.webullfintech.com/us/news-html/20261106/15877274426893312.html . Secondary-source report only; original issuer publication, proposal terms and SEC acceptance time UNKNOWN. Historical catalyst, NOT verified Monday ignition.
- RCT: Benzinga recap timestamp 2026-11-06 07:07:16 UTC (02:07:16 ET), concerning Argentina distributor integration, https://news-static.webullfintech.com/us/news-html/20261106/15875556044203008.html . Original issuer publication and first responsive trade UNKNOWN.
- CIIT: Benzinga recap timestamp 2026-11-06 05:33:03 UTC (00:33:03 ET), https://news-static.webullfintech.com/us/news-html/20261106/15875186421242880.html . Original catalyst UNKNOWN.
- VIVK, DBGI: Webull news search for Nov 6–9 returned no matching items; this is NOT evidence that no news exists.
- Current SEC 8-K, S-3, 424B, ATM/equity-line acceptance timestamps, split-adjustment status and live dilution risk: UNKNOWN / not verified in this run.

## Prior research / comparison
Reviewed ticker-vault research/daily-watch directory: existing Nov 5/6 after-hours and overnight records, no Nov 9 record at read time. CDT, RCT, CIIT, DBGI recur from Nov 5/6 watchlists; recurring symbols are not new independent ignitions. Reviewed puck-elite-price-action-v2 README: evidence-first architecture, no-trade when required inputs missing. Prior files untouched. Source: Webull connected PRE_MARKET gainers and per-symbol overnight_required L1 depth; GitHub connected directory and README.

## Permission verdict
Speed ↑ UNKNOWN; volume ↑ UNKNOWN; spread measured once but trend UNKNOWN; buyer control UNKNOWN; defended support UNKNOWN; defined executable risk UNKNOWN. All NO TRADE. Next comparison should capture the SAME symbols at 07:00 ET and preserve this snapshot. Do not infer first ignition from candle ranges or leaderboard position.
