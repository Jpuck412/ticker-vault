# Runner Outcome Comparison — Thursday 2026-10-29 — 06:59:15 ET

**Original research:** [03:20:48 ET overnight ignition file](https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-29_032048_ET_overnight_ignition.md), read directly from GitHub. **Follow-up:** approximately 06:57–06:59:15 EDT (UTC−04:00). **Sessions:** historical Oct 28 **ATH** 16:00–20:00 ET, attempted Oct 29 **OVN** 20:00–04:00 ET, and current Oct 29 **PRE** 04:00–09:30 ET. **Do not conflate them.**

## Data availability, source integrity and critical limitation

- **Webull connector attempted:** `get_gainers_losers(PRE_MARKET)`, `get_most_active(VOLUME)`, and `get_stock_snapshot(overnight_required=true)`; all returned `User input required but current turn is running in a non-interactive mode.` Thus **no current Webull quotes, order book, spread, ticks or marketwide ranking**. Do not describe this as a Webull-confirmed scan.
- **Fallback:** Connected TipRanks `get_stock_quotes` returned a `pre_post_market` block and per-symbol `last_trade_date` timestamps. Two successive provider observations were made at approximately 06:58 and 06:59 ET. The block is marked **PRE** by the provider (`is_premarket=true`); the quoted `volume` below is its extended-hours block volume, **treated as reported PRE-associated volume but independently audited session boundaries UNKNOWN**. Never merge with Oct 28 regular-session or ATH volume.
- TipRanks `get_market_movers(category=2)` returned symbol names only and was predominantly outside the low-priced small-cap universe; **no verified comprehensive current small-cap PRE leaderboard**.
- Alpha Vantage realtime bulk quotes/bid-ask/top movers attempts returned **rate-limit / premium-entitlement errors**. Consequently **bid, ask, spread, NBBO freshness, actual buyer/seller aggression and support remain UNKNOWN**.
- The 03:20:48 original file contained **zero verified Oct 29 overnight prices or volumes**. Its five names were Oct 28 ATH **carry-forward research candidates**, NOT a true 03:20 overnight top five. Therefore the change column below compares Oct 28 historical ATH prices to current PRE prices, **not OVN-to-PRE returns**.
- Provider quotes are asynchronous; quote last-trade timestamps are distinct from tool retrieval times. No historical tick stream was retrieved. No inference of first ignition from candles.

## SAME five carry-forward names — historical ATH vs 06:59 PRE

The original historical prices are reproduced exactly as preserved in the 03:20 file; no earlier record was modified. `Δ ATH→PRE` = (current PRE / Oct 28 historical ATH price − 1) × 100; historical ATH observations are asynchronous/rounded, so changes are approximate.

| Symbol | Oct 28 historical ATH price (original 03:20 file) | Oct 29 PRE price | Approx Δ ATH→PRE | PRE % vs Oct 28 16:00 close (TipRanks) | Reported PRE-block volume | Latest trade time EDT | Approx quote age at 06:59:15 | PRE bid/ask/spread | Verdict |
|---|---:|---:|---:|---:|---:|---|---|---|---|
| **NCPL** | $1.5800 | **$1.5600** | **−1.27%** | **+41.82%** | **1,620,151** | **06:59:15** | ~0 sec | **UNKNOWN** | Price held close to prior ATH reference; **not verified OVN continuation / NO TRADE** |
| **JDZG** | $1.8500 | **$1.4700** | **−20.54%** | **−2.00%** | **436,667** | **06:58:04** | ~71 sec | **UNKNOWN** | Major historical ATH-to-PRE fade; **not a proven false OVN ignition / NO TRADE** |
| **ELOG** | $1.0200 | **$0.8630** | **−15.39%** | **0.00%** | **5** | **04:00:22** | **~2h 59m STALE** | **UNKNOWN** | Very stale, effectively no current confirmation; **NO TRADE** |
| **FTCI** | $1.5000 | **$1.3682** | **−8.79%** | **+2.87%** | **1,862** | **06:42:02** | **~17m 13s STALE** | **UNKNOWN** | Thin and stale; **NO TRADE** |
| **LABT** | $0.2700 | **$0.2443** | **−9.52%** | **−14.28%** | **1,144,091** | **06:58:57** | ~18 sec | **UNKNOWN** | Heavy activity with negative price response; **NO TRADE** |

**Original ATH volumes:** NCPL/JDZG/ELOG/FTCI **UNKNOWN**; LABT **21.2M reported Oct 28 ATH shares** at the 20:00 report. Comparing 21.2M ATH with 1.144M current PRE does **not** measure acceleration, because sessions and observation windows differ. **True volume change since 03:20 OVN = UNKNOWN for all five.**

### Additional *within-follow-up* provider observations (NOT OVN baseline)

The first TipRanks pull around 06:58 and second around 06:59 reported:
- **NCPL:** $1.55 / 1,617,634 shares (last trade **06:57:56**) → $1.56 / 1,620,151 shares (**06:59:15**): **+2,517** reported PRE-block shares and +$0.01 price between provider observations.
- **JDZG:** $1.50 / 433,588 (**06:57:09**) → $1.47 / 436,667 (**06:58:04**): **+3,079** reported shares, −$0.03 price.
- **ELOG:** $0.863 / 5 (**04:00:22**) → unchanged: **no fresh quote**; do not infer zero actual trading.
- **FTCI:** $1.3682 / 1,862 (**06:42:02**) → unchanged: **no fresh quote**.
- **LABT:** $0.2479 / 1,137,691 (**06:57:54**) → $0.2443 / 1,144,091 (**06:58:57**): **+6,400** reported shares, −$0.0036 price.

These are **two asynchronous cumulative-volume observations**, not tick data or evidence of volume **acceleration** (which requires multiple comparable intervals). Do not infer buyer control or support from them.

## Additional meaningful PRE names / controls

| Symbol | Source context | PRE quote | PRE % vs Oct 28 close | PRE-block volume | Latest trade EDT | Historical ATH reference | Approx Δ ATH→PRE | Classification |
|---|---|---:|---:|---:|---:|---|---:|---|
| **KDK** | Freshly rechecked Oct 28 ATH vault candidate, **not** in 03:20 five | **$1.4450** | **+10.31%** | **4,678,290** | **06:58:43** | Oct 28 ~18:29 **$1.58** | **−8.54%** | **Meaningful PRE participation**, not verified new ignition or buyer-controlled tape; NO TRADE |
| **NEXR** | Oct 28 historical negative control, **not** in 03:20 five | **$0.3339** | **−29.56%** | **197,794** | **06:58:16** | Oct 28 closing ATH **~$0.34** | **−1.79%** | Negative-price control, NO TRADE |

Within the two follow-up provider reads: **KDK** PRE block volume **4,672,755 → 4,678,290** (+5,535), price **$1.46 → $1.445** (−$0.015); **NEXR** volume **197,794 → 197,794** with price **$0.3283 → $0.3339**. NEXR's unchanged volume alongside a changed trade time demonstrates why the provider cannot be treated as a synchronized tick feed. **No volume acceleration or buyer-control claim.**

**Comparison to marketwide leaders:** Webull rankings were inaccessible. TipRanks mover names and public `premarketprice.com/premarket-gainers/2026-10-29` were dominated by larger-cap stocks, and did not establish a small-cap universe-wide rank. Among **only these seven sampled symbols**, NCPL had the strongest observed PRE percentage change vs prior regular close (+41.82%), while KDK had the largest reported PRE-block volume (~4.68M). These are **sample-specific**, not marketwide top-rank claims. Neither is trade-approved.

## First-seen catalyst chronology / dilution checks

- **NCPL:** Prior secondary-indexed **2026-07-09 ~16:30 ET** 8-K about a **$15M equity purchase line** and warrants; primary SEC acceptance time **UNKNOWN**. No new Oct 29 issuer announcement verified by targeted public search; no proof one does not exist. First price-volume response to original financing **UNKNOWN**. Historical dilution risk elevated.
- **JDZG:** Prior 6-K documents **10-for-1 consolidation effective 2026-06-01** and authorized-share structure; fresh Oct 29 catalyst **UNKNOWN**. Prior Oct 28 RTH −75.41% and ATH rebound cannot be reconstructed as a verified ignition. First responsive trade **UNKNOWN**.
- **ELOG:** Historical **2026-08-28 ~16:30 ET** secondary-indexed preferred-stock/convertibility filing; primary SEC acceptance **UNKNOWN**. No fresh issuer news verified; first price-volume response **UNKNOWN**.
- **FTCI:** Historical **2026-08-05 ~06:39 ET** secondary-indexed 8-K describing up to **$20M equity-purchase facility**; primary SEC acceptance and actual new share issuance **UNKNOWN**. Fresh news **UNKNOWN**.
- **LABT:** Original **2026-10-21 ~08:02 ET** antimicrobial/clinical PR and **2026-09-21 08:02 ET** shareholder letter mentioning historic **$7.5M private placement**. SEC issuer listing shows Sep 29 8-K and Sep 18 S-1; no independently verified Oct 29 acceptance. New catalyst and first responsive trade **UNKNOWN**.
- **KDK:** **Two original Oct 28 issuer announcements** verified from the company's investor-relations site: **09:00 ET** DTL Transport agreement to deploy **75 driverless trucks**, and **16:00 ET** Stoneridge technology collaboration. These are **two different catalysts**; do not assign all subsequent price action to the 09:00 release. Neither has verified first trade/volume-response latency. Historical SEC prospectus/financing risk warrants separate review; **new Oct 29 issuance UNKNOWN**.
- **NEXR:** Prior Oct 27 **08:17 ET** transaction announcement identified in earlier vault, not verified new Oct 29 news. First responsive trade **UNKNOWN**.

**Original-source links:** KDK 09:00: https://investors.kodiak.ai/news-releases/news-release-details/kodiak-ai-and-dtl-transport-reach-historic-agreement-deploy-75 ; KDK 16:00: https://investors.kodiak.ai/news-releases/news-release-details/stoneridge-and-kodiak-ai-announce-collaboration-advance ; LABT filing list https://lakewoodamedex.investorroom.com/sec-filings ; LABT original letter https://www.prnewswire.com/news-releases/lakewood-amedex-biotherapeutics-ceo-issues-letter-to-shareholders-highlighting-transformational-progress-and-outlook-for-nu-3-302884099.html . Historical SEC/PR context and caveats are in the original 03:20 vault.

## Outcome classification — strict evidence boundaries

- **Historical ATH→PRE fades:** JDZG (−20.54%), ELOG (−15.39% but quote stale), LABT (−9.52%), FTCI (−8.79% but stale), KDK (−8.54%); **NCPL** retained near prior ATH (−1.27%). **These are not measured OVN-to-PRE outcomes.**
- **Confirmed false pre-04:00 ignitions:** **NONE CAN BE CLASSIFIED**, because no verified pre-04:00 tick/price/volume baseline exists.
- **Confirmed OVN continuations:** **NONE CAN BE CLASSIFIED** for the same reason.
- **Disappeared from today's PRE market:** **NONE VERIFIED**. All five have TipRanks PRE blocks, but ELOG and FTCI are stale; absence of a recent quote is **not** a delisting or confirmed disappearance.
- **News with no observed response:** **UNKNOWN** without synchronized tape; **moves without verified fresh news** are possible but cannot be certified as news-free.
- **PRE spread, support/retests, aggressor-side buyer control, executable stop/invalidation, order eligibility:** **UNKNOWN for every symbol**.

## PUCK permission / risk verdict

| Requirement | Evidence |
|---|---|
| Speed rising from tick data | **UNKNOWN** |
| Volume accelerating across matched intervals | **UNKNOWN** (only two cumulative PRE observations) |
| Spread stable/narrowing | **UNKNOWN** (no live bid/ask) |
| Buyers controlling tape | **UNKNOWN** |
| Defended support | **UNKNOWN** |
| Defined executable risk / eligibility | **UNKNOWN** |
| Proof of first pre-04:00 ignition | **UNKNOWN** |

**ALL SEVEN: NO TRADE VERIFIED. NO ORDERS PLACED.** A large PRE percentage change is not a trade entry. If support breaks after a future verified entry, exit; none was approved here.

## Repository audit / immutable records

- Original Oct 29 03:20:48 file (left untouched): https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-29_032048_ET_overnight_ignition.md
- Oct 28 ~18:29 ATH record (left untouched): https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-28_1829_ET_afterhours_catalyst_vault.md
- `Jpuck412/puck-elite-price-action-v2` README checked: https://github.com/Jpuck412/puck-elite-price-action-v2/blob/main/README.md ; reinforces evidence-first and missing-data discipline.
- Dedup keys: original `2026-10-29/OVN/03:20:48_ET/<SYMBOL>/NO_VERIFIED_QUOTE`; current `2026-10-29/PRE/06:59:15_ET/<SYMBOL>/TipRanks`. Historical Oct 28 ATH entries remain distinct by date/session/source. This is a **new file**, not an overwrite.

**Bottom line:** The usable comparison is **Oct 28 ATH carry-forward vs Oct 29 06:59 PRE** with verified, timestamped *fallback-provider* quotes and clear quote staleness. There is **no verified early-overnight-to-PRE comparison** because Webull authorization blocked overnight data. **No proof = no trade.**
