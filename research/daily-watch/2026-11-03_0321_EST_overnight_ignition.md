# Overnight Ignition Vault — 2026-11-03 03:21 EST

**Capture time:** 2026-11-03 03:21 EST (UTC-05). **Session:** overnight (20:00–04:00 EST), not regular premarket (04:00–09:30 EST). **Result:** no verified overnight quotes or pre-04:00 ignition. The following five are **2026-11-02 AFTER_MARKET carry-forward research candidates only**, NOT current November 3 overnight leaders. No trade approved.

## Collection / integrity
- Connected Webull `get_gainers_losers(PRE_MARKET)` and `get_gainers_losers(AFTER_MARKET)` attempted; both rejected: **User input required but current turn is running in a non-interactive mode**. Current overnight leaderboard, bid/ask, trades, spread, and quote freshness UNKNOWN.
- Connected GitHub: read `research/daily-watch/2026-11-02_183428_EST_afterhours_catalyst_vault.md`; searched for 2026-11-03 existing files (none found by search); compared `Jpuck412/puck-elite-price-action-v2` scanner and evidence rules. No previous snapshot overwritten.
- Historical after-hours reference: https://stocksetups.com/movers/after-hours (Nov 2 **20:00 EST** close; site-reported after-hours figures). Independent alternative with divergent session-volume conventions: https://www.chartmill.com/stock/markets/usa/movers/after-hours-gainers ; do not combine vendor volumes.
- Dedupe key: `2026-11-03|03:21_EST|CARRY_FORWARD_2026-11-02_AFTER_MARKET|symbol`. The source quote observation time is **Nov 2 20:00 EST session close**, not a Nov 3 executed-trade timestamp.

## Five historical candidates, NOT overnight top five
| Symbol | Prior session / source time | Price | Change vs Nov 2 regular close | Reported AH volume | Nov 3 overnight price / % / volume | Bid / ask / spread / quote freshness | First ignition before 04:00 |
|---|---|---:|---:|---:|---|---|---|
| PARA | Nov 2 AH close 20:00 EST, StockSetups | $2.45 | +46.27% | 8.26M (vendor-reported) | UNKNOWN | UNKNOWN | UNKNOWN |
| BLZE | Nov 2 AH close 20:00 EST, StockSetups | $10.46 | +40.52% | 6.45M (vendor-reported) | UNKNOWN | UNKNOWN | UNKNOWN |
| AEHG | Nov 2 AH close 20:00 EST, StockSetups | $2.66 | +28.81% | 5.03M (vendor-reported) | UNKNOWN | UNKNOWN | UNKNOWN |
| GPRO | Nov 2 AH close 20:00 EST, StockSetups | $1.10 | +16.18% | 9.24M (vendor-reported) | UNKNOWN | UNKNOWN | UNKNOWN |
| BRAI | Nov 2 AH close 20:00 EST, StockSetups | $2.96 | +16.08% | 3.75M (vendor-reported) | UNKNOWN | UNKNOWN | UNKNOWN |

**Caveat:** StockSetups and ChartMill show materially different after-hours volume figures for some symbols; source definitions/coverage not reconciled. The reported figures above are NOT November 3 overnight volume, nor verified Webull volume. Percent changes are historical after-hours gains, NOT overnight gains.

## Exceptions and controls
- **MERC:** StockAnalysis Nov 2 AH page reports approximately $0.29 / +132.86%, while other after-hours vendors differ; source volume and actionable liquidity unverified. Flag as extraordinary **unverified-volume** exception, not ranked overnight ignition. https://stockanalysis.com/markets/afterhours/gainers/
- **CCTG:** StockAnalysis Nov 2 AH page reports ~$0.42 / +44.10%; no Nov 3 overnight trade confirmation. https://stockanalysis.com/markets/afterhours/gainers/
- **CERS:** Nov 2 18:20 EST prior archive $2.25 / -4.66% after Phase 3 news; StockSetups Nov 2 AH close $2.29 / -1.51%, 3.98M vendor-reported AH volume. Negative clinical-news response control, not a confirmed failed overnight ignition.
- **CLRO:** Nov 2 prior archive 18:19:53 EST $5.75 / +1.77%, but StockSetups Nov 2 AH close $5.48 / -4.20%. This is a historical **inter-observation reversal**, not a tick-verified trajectory; historical merger/financing overhang. Nov 3 overnight UNKNOWN.
- **INO / CALC / ACH:** Prior Nov 2 archive contains observations and historical FDA/ATM/receivables context; no Nov 3 overnight prices verified. Not promoted as new ignition.

## Catalysts, filings and dilution
- **BLZE:** Nov 2 earnings-event context and reported AH repricing; prior Nov 2 18:34 archive explicitly did NOT verify original results release timestamp. Original Nov 2 PR / SEC 8-K acceptance, first responsive trade UNKNOWN here. Earlier Oct 12 announcement scheduled Nov 2 earnings; schedule is not proof of response.
- **PARA / AEHG / GPRO / BRAI / MERC / CCTG:** Original Nov 2 issuer PR timestamp, SEC 8-K/424B/S-3/ATM/equity-line checks, reverse splits, dilution status and first responsive trade **UNKNOWN** in this run; no claim of clean dilution status or news causation.
- **CERS:** Prior archive Reuters Nov 2 16:26 EST clinical report; original issuer publication and first response UNKNOWN. A prior 16:05 article-level price observation predates Reuters, so causality cannot be assigned.
- **CLRO:** Historical merger consideration shares and planned financing noted in Nov 2 archive, not evidence of a new issuance.
- **INO / CALC:** Historical warrant and ATM risks from prior records; no new overnight draw verified.
- **News with no move:** NOT CERTIFIED. **Moves with no verified news:** carry-forward PARA, AEHG, GPRO, BRAI, MERC, CCTG (unverified catalyst, NOT proof of no news).

## Puck permission
Speed ↑ UNKNOWN; volume acceleration ↑ UNKNOWN; spread stable/tightening UNKNOWN; buyer-controlled tick tape UNKNOWN; defended support UNKNOWN; risk/invalidation UNKNOWN. No inference from candles or percentage gainers. **NO PROOF = NO TRADE.** No orders placed.

**Follow-up requirement:** At a future authenticated live-data check, recheck SAME symbols and preserve this snapshot; compare only synchronized session-aware observations, mark disappearance only with evidence, and keep historical AH and actual overnight measurements separate.
