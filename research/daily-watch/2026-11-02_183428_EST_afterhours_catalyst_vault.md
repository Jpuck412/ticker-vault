# After-Hours Catalyst Vault — Monday, 2026-11-02 — 18:34:28 EST

**Research window:** 2026-11-02 16:00–20:00 EST (UTC−05:00); **interim capture** at approximately 18:34 EST, NOT the 20:00 session close. **Top five = research-selected US-listed small-cap candidates/controls, NOT a verified Webull marketwide leaderboard.** All figures USD. **No trade permission / no orders.**

## Source integrity and collection method

1. Connected Webull `get_gainers_losers(AFTER_MARKET)` gainers and losers and `get_most_active` were each invoked. **All three failed:** `User input required but current turn is running in a non-interactive mode.` No Webull after-hours leaderboard, Webull bid/ask, or Webull tick tape obtained.
2. **Fallback connected Alpaca delayed-SIP** `get_stock_snapshot` and `get_stock_latest_quote` for QNRX/CERS/HCTI/ACH/AMIX/INO/CLRO/CALC/JDZG/BLZE succeeded. All quoted trades and bid/ask levels have their own UTC timestamps, converted below to EST (subtract five hours). Latest usable delayed prints were around **18:15–18:20 EST**, except noted stale names. This is a **delayed snapshot, not an executable order-book observation**.
3. Alpaca `get_stock_bars` (1-minute and 5-minute historical intervals) and `get_stock_trades` requests for after-hours intervals **failed** with `api_error` / `internal_error`. Therefore **after-hours-only cumulative volume, speed, volume acceleration, aggressive buyer/seller prints, first responsive trade and verified defended support are UNKNOWN**. Snapshot `daily_bar.volume` is **regular/daily volume and MUST NOT be misrepresented as AH-only**. Snapshot `minute_bar.volume` is a single isolated minute, not cumulative AH participation.
4. A public **Benzinga sector movers article stamped 16:05 EST** is an early *article-level* observation, not an exact executed trade timestamp. Its CERS +13.48%/$2.68 and INO −4.2%/$1.82 are separate, unsynchronized observations from the delayed Alpaca snapshots. https://www.benzinga.com/trading-ideas/movers/26/11/62797158/12-health-care-stocks-moving-monday-s-after-market-session
5. **Warning on public screener staleness:** Stock Analysis `/markets/afterhours/gainers/` displayed the **identical Friday Oct 30 INO $2.05 / +240.31%, CLRO $4.60 / +34.85%, CALC $1.82 / +24.61%** rows while labeling its page Nov 2. These are Friday carry-forward values in the existing GitHub vault, so the screen was **REJECTED as a November 2 leaderboard**. https://stockanalysis.com/markets/afterhours/gainers/
6. GitHub existing `research/daily-watch/` checked. Existing Monday `2026-11-02_034651_EST_overnight_ignition.md` and `2026-11-02_0703_EST_premarket_followup.md` remain unchanged; Oct 30 after-hours `2026-10-30_182740_ET_afterhours_catalyst_vault.md` is a separate historical baseline. Also inspected `Jpuck412/puck-elite-price-action-v2/research/runner-comparisons/` (historical Oct 12 reference only). This record uses a new path, preserving all earlier observations.
7. Dedupe key `2026-11-02|AFTER_MARKET|actual_vendor_trade_timestamp_EST|symbol`; early 16:05 article observation is keyed separately as `2026-11-02|16:05_EST|BENZINGA_ARTICLE|symbol`, not merged into later Alpaca last trades.

## Top five research-selected small caps — delayed-SIP source, not Webull

`Regular close` is Alpaca's Nov 2 `daily_bar.close`; AH change = (timestamped last trade / regular close − 1) × 100. The L1 spread uses the **separate quote timestamp**, which may differ from the trade time. Quote values are delayed and **NOT executable at 18:34**.

| Rank | Symbol / venue | Nov 2 regular close | AH last / trade time EST | Change vs regular close | Delayed L1 bid / ask; quote time EST | L1 spread / approx % midpoint | AH-only volume | Catalyst and classification |
|---|---|---:|---|---:|---|---|---|---|
| 1 | **BLZE / Nasdaq** | $7.4000 | **$10.0500**, 18:20:00 | **+35.81%** | $9.96 / $10.06; 18:20:00 | **$0.10 / 1.00%** | **UNKNOWN** | **Strong price repricing with scheduled earnings, but fresh actual earnings PR NOT VERIFIED**. Oct 12 16:16 EDT issuer announcement scheduled Q3 results for Nov 2 after close and 17:00 EST call. First AH response UNKNOWN; don't attribute move to an unverified release. |
| 2 | **CERS / Nasdaq** | $2.3600 | **$2.2500**, 18:20:13 | **−4.66%** | $2.25 / $2.28; 18:20:13 | **$0.03 / 1.32%** | **UNKNOWN** | **Fresh Phase 3 RedeS trial positive endpoint; negative/failed-move control.** Reuters article **16:26 EST** confirmed non-inferiority but FDA has NOT approved the experimental RBC system. Separate Benzinga 16:05 article showed $2.68/+13.48%, followed by 18:20 last $2.25, a **−16.04% change between non-synchronous vendor observations**, not a proven tick-by-tick selloff. Original issuer release exact time and first responsive trade UNKNOWN. Q3 earnings also scheduled for Nov 2; actual results release not independently verified in this capture. |
| 3 | **CLRO / Nasdaq** | $5.6500 | **$5.7500**, 18:19:53 | **+1.77%** | $5.75 / $5.76; 18:19:49 | **$0.01 / 0.17%** | **UNKNOWN** | **Carry-forward momentum / move without verified fresh Nov 2 AH news.** Earlier Oct 30 vault showed $5.25 at 18:17 EDT; Monday 07:03 PRE archive $5.59. Historical merger proposal includes 12.5M consideration shares and planned $10–15M financing; no Nov 2 closing/issuance confirmed. |
| 4 | **ACH / NYSE** | $0.2635 | **$0.2740**, 18:20:11 | **+3.98%** | $0.2740 / $0.2743; 18:20:13 | **$0.0003 / 0.11%** | **UNKNOWN** | **Same-day but premarket news, NOT new 16:00+ catalyst:** original Business Wire **06:45 EST** announced extension of $150M receivables program to Oct 2029, amount unchanged; SEC 8-K **06:50 EST** acceptance per secondary filing index. Oct 30 **16:45 EDT** NYSE listing-standard notice creates separate compliance risk. AH first response UNKNOWN. |
| 5 | **INO / Nasdaq** | $1.8900 | **$1.9104**, 18:19:57 | **+1.08%** | $1.91 / $1.92; 18:20:10 | **$0.01 / 0.52%** | **UNKNOWN** | **Friday Oct 30 FDA approval carry-forward, not a fresh Monday AH FDA event.** Original FDA public posting time UNKNOWN; Friday Reuters **16:44 EDT** already reported >200% AH; issuer Friday PR **18:01 EDT**. Monday 06:15:32 EST secondary analyst upgrade and 08:00 EST company call were earlier events. July $20M common-stock/warrant financing including 42.1M warrant-underlying shares: historical dilution risk, not proof of new Monday issuance. |

**Quote freshness:** At 18:34:28 EST, the five latest trades/quotes are approximately 14–15 minutes old (consistent with delayed-SIP). These L1 spreads are measured at the individual quote times, **not proven stable or tightening**. No real-time market depth was obtained.

## Additional exceptions and negative controls

| Symbol | AH last / time EST | Regular close | AH net change | L1 bid/ask; quote time | Control / catalyst status |
|---|---|---:|---:|---|---|
| **HCTI / Nasdaq** | $5.1900 at 18:19:41 | $4.9800 | **+4.22%** | $4.95 / $5.20 at 18:15:25 (**$0.25, ~4.93% midpoint**) | Move with **no verified fresh Nov 2 issuer PR**; historical Feb 2026 1-for-60 reverse split; liquidity/spread caution. AH volume UNKNOWN. |
| **JDZG / Nasdaq** | $0.4957 at 18:19:13 | $0.5264 | **−5.83%** | $0.4702 / $0.4957 at 18:19:56 (**$0.0255, ~5.28% midpoint**) | Negative control; no fresh AH catalyst verified; repeated historical fades in Oct 28–30 vault. AH volume UNKNOWN. |
| **CALC / Nasdaq** | $1.4103 at 18:15:03 | $1.4000 | **+0.74%** | $1.41 / $1.56 at 18:20:08 (**$0.15, ~10.10% midpoint**) | Friday AH runner but weak Monday after-hours move; historical **up to $25M ATM** under S-3/424B5, no Nov 2 draw confirmed. AH volume UNKNOWN. |
| **QNRX / Nasdaq** | $4.0079 at **16:56:55** (stale) | $4.0200 | **−0.30%** | $4.00 / $4.20 at **16:48:05** (stale, **$0.20 ~4.88% midpoint**) | **False early apparent gain / stale-print control:** Benzinga 16:05 article said $4.67/+16.2%, but the later available delayed last trade was $4.0079. Exact 16:05 trade time, first response and subsequent path UNKNOWN. Oct 29 company announcement scheduled Nov 5 earnings, **not a new Nov 2 AH catalyst**. |

## News/SEC chronology — original timestamp vs first meaningful response

- **CERS — 2026-11-02 16:26 EST (Reuters):** Phase 3 RedeS primary endpoint met; RBC system remains investigational and not FDA approved. Reuters publication is independently timestamped; original issuer distribution and SEC acceptance timestamps **UNKNOWN**. The 16:05 Benzinga price is *earlier* than Reuters, so do **not** infer Reuters caused the earlier move. First response **UNKNOWN**. https://www.reuters.com/business/healthcare-pharmaceuticals/cerus-blood-safety-system-meets-main-goal-late-stage-trial-2026-11-02/
- **BLZE — 2026-10-12 16:16 EDT:** original Business Wire earnings-*schedule* announcement for Nov 2 after close, with 17:00 EST conference call. **Actual Nov 2 results PR original timestamp, SEC acceptance and first responsive trade UNKNOWN** despite the large net price gain. https://ir.backblaze.com/news/news-details/2026/Backblaze-to-Announce-Third-Quarter-2026-Results-on-November-2-2026/default.aspx
- **ACH — 2026-11-02 06:45 EST:** original Business Wire extension of $150M receivables sale program to 2029; **06:50 EST** 8-K SEC acceptance *as indexed by StockTitan, not directly validated against EDGAR header*. This is **premarket news**. https://www.stocktitan.net/news/ACH/accendra-health-announces-extension-of-150-million-receivables-sale-mg5proaaq7gt.html ; https://www.stocktitan.net/sec-filings/ACH/8-k-accendra-health-inc-va-reports-material-event-03c9e80bec3b.html
- **INO — 2026-10-30 FDA approval**, Friday Reuters 16:44 EDT and Friday issuer PR 18:01 EDT; Monday 06:15:32 EST analyst upgrade was reported in previous 07:03 vault. **No verified new Monday after-hours FDA approval**. Historical July 2026 warrant/equity issuance risk. https://www.stocktitan.net/sec-filings/INO/8-k.html
- **CLRO — historical merger/financing overhang** from Friday Oct 30 vault. New Nov 2 8-K/424B/S-3/ATM/merger closing **NOT VERIFIED**.
- **HCTI — historical reverse split**, original Feb 6 2026 10:19 EST issuer PR (1-for-60 effective Feb 10); not a fresh Nov 2 event. https://www.prnewswire.com/news-releases/healthcare-triangle-inc-announces-1-for-60-reverse-stock-split-as-part-of-nasdaq-compliance-plan-302681409.html
- **CALC — historical ATM overhang** from Sept 30 2026 S-3/424B5 (up to $25M). New Nov 2 sales **UNKNOWN**.
- **News without a move:** No defensible *fresh after-16:00 issuer news with confirmed zero response* could be certified; missing tick/volume data prevents that conclusion. ACH is **old-news / mild AH move** control, not news-with-no-move proof.
- **Moves without verified fresh news:** **BLZE** (earnings event scheduled but actual release unverified), **CLRO**, **HCTI**, and **JDZG** (negative); classification means *not verified in targeted search*, not proof no announcement exists.
- **New SEC filing coverage:** targeted SEC/secondary index checks, **NOT exhaustive all-market EDGAR search**. No fresh post-16:00 424B/S-3/ATM/equity-line draw, reverse split, merger close or offering is asserted for these candidates without an original document and acceptance header.

## Prior vault comparison

- `2026-10-30_182740_ET_afterhours_catalyst_vault.md`: **INO, CLRO, CALC** repeated; they must be tagged **multi-session**, not new ignition. Earlier Oct 30 INO FDA news and CLRO merger risk remain the reference.
- `2026-11-02_034651_EST_overnight_ignition.md`: **INO, CLRO, SLGB, CALC, FEBO** were historical Friday AH carry-forwards with **no verified Monday 03:46 OVN tape**.
- `2026-11-02_0703_EST_premarket_followup.md`: **CLRO +21.55%** Friday AH→Monday PRE; **INO −0.49%**, **CALC −7.64%**, **SLGB −10.33%**, **FEBO −17.05%**. Those historical-baseline comparisons are not today's after-hours changes. Today's BLZE/CERS/ACH observations are new research candidates, while CLRO/INO/CALC are repeats.
- `Jpuck412/puck-elite-price-action-v2/research/runner-comparisons/2026-10-12_0535_ET_webull_premarket.md`: historical framework only; no Nov 2 quote.
- This file is append-only with independent observation keys and does not alter earlier records.

## Puck permission / limitations

- **Speed increasing:** UNKNOWN (no continuous trades).
- **After-hours volume and volume acceleration:** UNKNOWN (no session-matched intervals).
- **Spread stable/tightening:** UNKNOWN (one delayed L1 per symbol; *absolute spread measured*, stability unverified).
- **Buyer-controlled tape:** UNKNOWN.
- **Defended support / confirmation candle:** UNKNOWN; no inference from OHLC.
- **Risk distance / stop and executable liquidity:** UNKNOWN.
- **News-to-first-meaningful-price+volume-response latency:** UNKNOWN for all; a published news timestamp and later net price difference do not establish ignition.
- **Trade permission:** **NO** for all. **No proof = no trade.** No orders placed.

**Archive source summary:** connected GitHub previous vaults; connected Webull auth failure; connected Alpaca delayed-SIP timestamped trades and quotes; Benzinga 16:05 EST sector mover article; Reuters 16:26 EST CERS trial report; issuer and secondary SEC filing pages linked above. All observations are as-of this 18:34 interim capture.
