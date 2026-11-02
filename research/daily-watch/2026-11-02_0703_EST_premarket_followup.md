# Runner Outcome Comparison — Monday 2026-11-02 — ~07:03 EST

**Follow-up observation:** Monday 2026-11-02, latest vendor PRE trade prints at **07:03:00–07:03:01 EST** (12:03 UTC), with one stale PRE print at 05:53:24 EST (FEBO) and one at 07:00:04 EST (CALC). **Early archive:** Monday **03:46:51 EST**. **Early snapshot was a research-only attempt with NO live November 2 overnight quotes**; its prices were **Friday October 30 AFTER_MARKET carry-forwards**, not Monday 03:46 trades. **No trade verified; no orders placed.**

**Sources:** Connected GitHub original archive (read, preserved), connected Webull attempted (interactive authorization blocked), connected TipRanks two consecutive stock-quote responses, connected Alpaca delayed-SIP L1 quotes for independent spread observations (quotes at 06:48 / 06:36 / 04:58 EST, **not live at 07:03**). Alpaca IEX snapshots were checked but only showed Friday October 30 last trades and quotes, therefore discarded as Monday evidence. Alpaca OVERNIGHT feed returned an API error. Alpha Vantage bulk quotes returned **explicitly artificial sample data**, which was rejected completely. TipRanks marketwide percent-gainer and unusual-volume endpoints returned mostly larger-cap/general lists without timestamped small-cap quotes, so **no verified marketwide small-cap PRE leaderboard** was established.

## Baseline integrity and five matched tickers

**Original early observation time:** 2026-11-02 03:46:51 EST, `research/daily-watch/2026-11-02_034651_EST_overnight_ignition.md`.
**Original price timestamp:** Friday 2026-10-30 after-hours last prints, approximately 19:35–19:59 **EDT**, not Monday overnight. **Monday 03:46 OVN prices, volumes, spreads: UNKNOWN for all.**
**Follow-up price:** Monday 2026-11-02 PRE, latest TipRanks `pre_post_market` print. Percent delta = (Monday PRE last / Friday AH last - 1) × 100. This is **Friday AH → Monday PRE**, NOT `03:46 → 07:03`.
**Volume:** vendor `pre_post_market.volume` cumulative fields from two observations roughly 07:02:33–07:02:43 and 07:03:00–07:03:01 EST. The exact session coverage (PRE-only vs combined extended hours) is **not documented** by this connector; label **reported extended-hours volume**, not verified overnight volume or a matched 03:46 delta. Change between two consecutive vendor readings is an observed cumulative-volume increment **only**, not evidence of volume acceleration, tape speed, or buyer aggression.

| Symbol | Friday AH baseline | Monday PRE last, trade ET | Fri AH→Mon PRE | Vendor reported ext-hours vol (earlier → later) | Increment between readings | Delayed-SIP L1 bid / ask, quote ET | L1 spread (absolute; % midpoint) | Current support / tape / risk |
|---|---:|---|---:|---|---:|---|---|---|
| **INO** | $2.0500 (Fri ~19:59 EDT) | **$2.0400**, Mon **07:03:01 EST** | **−0.49%** | 19,001,328 → 19,007,420 | **+6,092** | $2.05 / $2.06 at **06:48:21 EST** | $0.0100 (**0.49%**) | **UNKNOWN / UNKNOWN / UNKNOWN** |
| **CLRO** | $4.5990 (Fri ~19:59 EDT) | **$5.5900**, Mon **07:03:01 EST** | **+21.55%** | 5,779,340 → 5,781,746 | **+2,406** | $5.83 / $5.84 at **06:48:21 EST** | $0.0100 (**0.17%**) | **UNKNOWN / UNKNOWN / UNKNOWN** |
| **CALC** | $1.8190 (Fri ~19:52 EDT) | **$1.6800**, Mon **07:00:04 EST** | **−7.64%** | 24,272 → 24,272 | **0** | $1.63 / $1.73 at **06:36:19 EST** | $0.1000 (**5.95%**) | **UNKNOWN / UNKNOWN / UNKNOWN** |
| **SLGB** | $0.3600 (Fri ~19:59 EDT) | **$0.3228**, Mon **07:03:00 EST** | **−10.33%** | 16,193,459 → 16,194,463 | **+1,004** | $0.3156 / $0.3157 at **06:48:17 EST** | $0.0001 (**0.03%**) | **UNKNOWN / UNKNOWN / UNKNOWN** |
| **FEBO** | $0.7600 (Fri ~19:35 EDT) | **$0.6304**, Mon **05:53:24 EST** (STALE) | **−17.05%** | 216 → 216 | **0** | $0.6304 / $0.7800 at **04:58:28 EST** (VERY STALE) | $0.1496 (**21.21%**) | **UNKNOWN / UNKNOWN / UNKNOWN** |

**Quote freshness / market depth:** Delayed-SIP quotes above are not executable 07:03 bid/ask observations. INO, CLRO, SLGB quotes ~15 min old at follow-up; CALC ~27 min; FEBO ~125 min. The narrow SLGB quote is **not** proof of a stable spread; the CLRO 06:48 quote and 07:03 last price are asynchronous. No synchronized order book or verified bid/ask spread **at trade time** was obtained. All support, stop distance and entry-risk calculations remain UNKNOWN.

## Continuation, reversals, and disappearance assessment

- **CLRO — strongest historical-baseline continuation:** $4.599 Friday AH → $5.59 Monday PRE (**+21.55%**). Reported extended-hours cumulative volume rose 2,406 between vendor snapshots. This is **price continuation across sessions**, **NOT a verified pre-04:00 ignition**, and no buyer-controlled tape, volume acceleration or support has been proven. No fresh Nov 2 issuer catalyst verified.
- **INO — near-retention, fresh analyst-news exception:** $2.05 Friday AH → $2.04 Monday PRE (**−0.49%**), with 6,092 incremental vendor-reported shares between two follow-up snapshots. **H.C. Wainwright upgraded INO to Buy from Neutral**, secondary headline with stated **06:15:32 EST** publication time on Nov 2; no original analyst note independently retrieved. This is a **new Monday news event**, separate from Friday's FDA approval. No first response tick is known. Issuer FDA approval PR was **Friday Oct 30 18:01 EDT**; Reuters had already reported INO up >200% at **16:44 EDT**; original FDA public posting time and first responsive trade remain UNKNOWN. Issuer-scheduled **08:00 EST Monday call is still future at this follow-up**. Historical July common/warrant financing risk remains; new issuance Monday UNKNOWN.
- **SLGB — partial fade:** Friday AH $0.36 → Monday PRE $0.3228 (**−10.33%**). Historical Oct 29 **16:15 EDT** Nasdaq compliance-extension news, not new Monday issuer news. 1,004 incremental reported extended-hours shares across vendor snapshots; no first-ignition or failed-ignition proof. Reverse split mentioned as a future possibility in original notice, **not confirmed executed**.
- **CALC — fade and wide delayed quote:** Friday AH $1.819 → Monday PRE $1.68 (**−7.64%**), no observed vendor-volume increment across two snapshots. Historical **up to $25M ATM** under SEC S-3 / 424B5; Monday ATM sales UNKNOWN. 06:36 delayed-SIP quote was $0.10 wide (~5.95% of midpoint), but cannot be treated as 07:03 execution spread.
- **FEBO — stale, thin-participation control:** Friday AH $0.76 → Monday **05:53** PRE last $0.6304 (**−17.05%**), with vendor-reported ext-hours volume only 216 and no change across observations. Quote at 04:58 EST $0.6304/$0.78 (~21.21% midpoint). **Not confirmed to have disappeared**; a stale last trade is not proof trading ceased. No fresh issuer catalyst verified.

**No certified false ignition**: the 03:46 archive contained no Monday overnight executed trades. **No confirmed disappearance**: all five have a Monday PRE-labeled price, although FEBO is stale. **No certified early-ignition continuation**: no synchronized early tape. **Newly meaningful runner:** none added as verified small-cap leader; marketwide Webull ranking inaccessible and available alternate marketwide mover lists lack adequate small-cap, session and timestamp qualification. INO's analyst upgrade is a new **catalyst exception** on an existing tracked symbol, not a new symbol.

## Catalyst chronology / dilution notes

| Symbol | First verifiable news / filing timestamp | Fresh Nov 2 issuer news | First meaningful executed price-volume response | Historical dilution risk |
|---|---|---|---|---|
| INO | Reuters Fri Oct 30 **16:44 EDT** already reports >200% AH; issuer approval PR **18:01 EDT**; Monday Nov 2 **06:15:32 EST** secondary analyst-upgrade headline | New Monday issuer PR **UNKNOWN**; 08:00 EST call scheduled | **UNKNOWN** | July common/warrant financing; fresh draw/issuance **UNKNOWN** |
| CLRO | Friday after-hours original catalyst **UNKNOWN**; historical merger proposal | **UNKNOWN** | **UNKNOWN** | Proposed merger consideration **12.5M shares** and prospective $10–15M financing; completion **UNKNOWN** |
| CALC | Historical Sept 30 SEC 8-K / 424B5 ATM | **UNKNOWN** | **UNKNOWN** | Up to $25M ATM; actual Monday sales **UNKNOWN** |
| SLGB | Oct 29 **16:15 EDT** Nasdaq extension PR | **UNKNOWN** | **UNKNOWN** | Possible future reverse split; completion **UNKNOWN** |
| FEBO | Fresh Friday/Monday issuer catalyst **UNKNOWN** | **UNKNOWN** | **UNKNOWN** | New issuance **UNKNOWN** |

News headlines with no observed price response and moves with no verified fresh issuer news cannot be **causally classified** without synchronized trades. INO Monday analyst upgrade is verified as a **secondary-source timestamped headline**, not as the origin of its Friday FDA repricing.

## Data-source and integrity audit

1. **Original immutable early GitHub snapshot**: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-02_034651_EST_overnight_ignition.md
2. **Prior Friday AH origin record**: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-30_182740_ET_afterhours_catalyst_vault.md
3. **Connected Webull PRE_MARKET gainers and symbol snapshots:** both failed `User input required but current turn is running in a non-interactive mode.` No Webull PRE market leader list, depth, tick data or volume. This is an **authorization barrier**, not a zero-volume result.
4. **Connected TipRanks stock quotes** for `INO,CLRO,CALC,SLGB,FEBO`: first snapshot ~07:02:33–07:02:43 EST (some earlier), second snapshot ~07:03:00–07:03:01 EST; field `pre_post_market` for last trade and cumulative volume. **TipRanks is not Webull**. No verified 03:46 prices.
5. **Connected Alpaca `delayed_sip` latest quotes**: bid/ask quote timestamps explicitly shown in table. **IEX feed returned only Friday October 30 records** and was rejected for Monday comparison. `overnight` feed errored. Delayed SIP quotes must not be combined with 07:03 prints to imply synchronized executable spreads.
6. **Alpha Vantage bulk endpoint** returned premium-access message and **explicit artificial demonstration quotes**, rejected.
7. **TipRanks headline**: https://www.tipranks.com/news/the-fly/inovio-upgraded-to-buy-from-neutral-at-h-c-wainwright-thefly-news (Nov 2 06:15:32 EST per connected TipRanks news). Original INO PR: https://www.prnewswire.com/news-releases/inovio-announces-fda-accelerated-approval-of-voceryq-an-immunotherapy-to-reduce-the-frequency-of-surgery-in-adults-with-recurrent-respiratory-papillomatosis-rrp-302925406.html . Original SEC CALC ATM 8-K: https://www.sec.gov/Archives/edgar/data/1534133/000119312526409049/d39303d8k.htm and 424B5: https://www.sec.gov/Archives/edgar/data/1534133/000119312526409041/d145394d424b5.htm .
8. **Historical elite scanner baseline:** https://github.com/Jpuck412/puck-elite-price-action-v2/blob/main/research/runner-comparisons/2026-10-12_0535_ET_webull_premarket.md ; historical only, not a November 2 observation.
9. **Dedup keys:** original `2026-11-02|03:46:51_EST|OVERNIGHT_ATTEMPT|symbol`; follow-up `2026-11-02|07:03_EST|PRE_TIPRANKS|symbol` (FEBO/CALC retain actual last-trade time), delayed quotes `2026-11-02|quote_timestamp_EST|DELAYED_SIP|symbol`; Friday AH baselines `2026-10-30|AFTER_MARKET|last_trade_EDT|symbol`. Each observation remains separate. Original files were **not overwritten**.

## Puck permission verdict — NO TRADE VERIFIED

- Speed ↑: **UNKNOWN** (two non-synchronized last prints cannot verify tape speed).
- Volume ↑: **increment observed for three symbols** but **acceleration UNKNOWN**, session coverage UNKNOWN.
- Spread ↔ / ↓: **UNKNOWN** (one delayed quote per symbol; no stable/tightening sequence).
- Buyer-controlled executed tape: **UNKNOWN**.
- Defended support: **UNKNOWN**.
- Defined executable risk / stop: **UNKNOWN**.
- Evidence > prediction: **NOT SATISFIED**; one-candle confirmation **NOT VERIFIED**.

**All five: NO TRADE VERIFIED. No orders placed.** This is a source-qualified historical-baseline follow-up, **not** a certified early-overnight runner-success study. **No proof = no trade.**
