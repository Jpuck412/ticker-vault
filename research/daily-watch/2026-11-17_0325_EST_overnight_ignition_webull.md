# Overnight Ignition Vault — 2026-11-17 03:25 EST

Research only. Connected Webull stock snapshots queried during 03:25–03:27 EST. **OVN is the overnight session, NOT PRE_MARKET**. PRE_MARKET leaderboard endpoint returned prior regular-session-style ranking data (GMM +371% with Monday volume), so it was **rejected as a Tuesday premarket ranking**. No market-wide overnight leaderboard is available from this connector. Top five below are selected from a limited symbol universe, not a claim of the market-wide top five. Ranked by research relevance, not entry priority. All price changes are Webull OVN versus Monday 16:00 close, not change since first trade.

## Five selected positive research candidates
| Symbol | OVN last $ | OVN % | OVN shares | OVN bid/ask $ | L1 spread/mid | Last trade ET | Quote ET |
|---|---:|---:|---:|---|---:|---|---|
| CSAI | 2.26 | 73.85% | 1,542,147 | 2.25/2.26 | 0.44% | 11/17, 03:25:43 | 11/17, 03:25:48 |
| SPAI | 3.31 | 34.01% | 437,406 | 3.3/3.31 | 0.30% | 11/17, 03:25:48 | 11/17, 03:25:49 |
| GLAS | 1.67 | 29.46% | 182,374 | 1.66/1.67 | 0.60% | 11/17, 03:25:35 | 11/17, 03:25:35 |
| AYTU | 2.62 | 43.96% | 33,944 | 2.6/2.62 | 0.77% | 11/17, 03:25:25 | 11/17, 03:25:43 |
| AKAN | 2.59 | 17.19% | 914,573 | 2.57/2.59 | 0.78% | 11/17, 03:24:44 | 11/17, 03:25:38 |

## Exceptions and controls
| Symbol | OVN last $ | OVN % | OVN shares | OVN bid/ask $ | L1 spread/mid | Last trade ET | Quote ET |
|---|---:|---:|---:|---|---|---|---|
| GP | 1.59 | 12.77% | 114,272 | 1.59/1.63 | 2.48% | 11/17, 03:24:37 | 11/17, 03:25:40 |
| GIPR | 0.254 | -2.23% | 233,399 | 0.2517/0.2545 | 1.11% | 11/17, 03:24:50 | 11/17, 03:25:16 |
| GMM | 1.61 | -19.90% | 956,274 | 1.61/1.62 | 0.62% | 11/17, 03:25:25 | 11/17, 03:25:45 |
| CYAB | 0.1176 | -14.04% | 2,106,741 | 0.1169/0.1176 | 0.60% | 11/17, 03:25:42 | 11/17, 03:25:42 |
| CLRO | 4.43 | -7.32% | 15,426 | 4.42/4.52 | 2.24% | 11/17, 03:25:26 | 11/17, 03:25:31 |

Snapshot fields from Webull get_stock_snapshot(overnight_required=true), observed near 03:25 ET. Quote freshness is determined by the individual quote timestamp, not assumed. Prices and quotes may be asynchronous. All quote spreads are indicative; a single quote cannot prove tightening or executable depth. First ignition before 04:00 is NOT established by one observation; the observation itself is before 04:00.

## Catalyst provenance and dilution
- **CSAI**: original issuer Q3 release 2026-11-16 17:30 ET (prior dated after-hours record); Nov 16 10-Q in Webull SEC filing feed (exact EDGAR acceptance time UNKNOWN). Secondary Benzinga 2026-11-17 00:56:30 ET cites going-concern doubt, $2.2M cash and negative operating cash flow; treat as financing/dilution risk, not proof of active ATM. Source https://www.sec.gov/Archives/edgar/data/0001709628/000168316826008864/cloud_i10q-093026.htm
- **AYTU**: original acquisition release Nov 16 16:02 ET; $2.70 cash offer contingent on closing/tender conditions. Overnight $2.62 is not a free 8-cent spread. Original SEC acceptance UNKNOWN. https://www.globenewswire.com/news-release/2026/11/16/3404140/0/en/rosemont-pharmaceuticals-to-acquire-aytu-biopharma-to-accelerate-us-expansion.html
- **GLAS**: original Q3 release Nov 16 16:05 ET. SEC acceptance and dilution status UNKNOWN. https://www.globenewswire.com/news-release/2026/11/16/3404116/0/en/glass-house-brands-reports-third-quarter-2026-financial-results.html
- **SPAI**: Nov 16 10-Q listed by Webull; acceptance time UNKNOWN. Nov 10 government contract is historical, not fresh ignition. https://www.sec.gov/Archives/edgar/data/0002011208/000149315226052406/form10-q.htm
- **AKAN**: no verified fresh original catalyst; most recent listed Webull 6-K Sep 30, not proof of clean dilution. https://www.sec.gov/Archives/edgar/data/0001888014/000121390026105355/ea0306489-6k_akanda.htm
- GP, GIPR, GMM, CYAB, CLRO: original fresh catalyst and SEC acceptance timestamps UNKNOWN in this run. Historical runner carryovers are not newly proven ignitions.

## Historical comparison and deduplication
Retrieved Nov 16 18:26 EST after-hours record at https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-16_1826_EST_afterhours_catalyst_vault_webull.md. CSAI, AYTU, GLAS, GP, GIPR, SPAI and GMM carry over; do not label their first ignition new. The Puck Elite repository code search for 'ignition' returned no results; methodology comparison beyond evidence-first rules UNKNOWN. Duplicate check for this exact 2026-11-17 03:25 file returned 404, so create-only is appropriate. Dedup key = (2026-11-17, symbol, 03:25 snapshot window); no earlier observation overwritten.

## Evidence / permission
- Price speed: UNKNOWN (no synchronized sequential trades examined).
- Interval volume acceleration: UNKNOWN (cumulative OVN volume only).
- Buyer-controlled tape: UNKNOWN.
- Support and support defense: UNKNOWN.
- Spread stability/tightening: UNKNOWN (one L1 observation).
- Defined risk: UNKNOWN.
- First catalyst-responsive trade, first ignition time, latency: UNKNOWN.
- Verified news-with-no-move: NONE ESTABLISHED. AKAN and other movers have NO VERIFIED FRESH NEWS, not proof no news exists. GMM and CYAB are downside controls, not proven false ignitions.

**NO TRADE APPROVED. NO PROOF = NO TRADE.**
