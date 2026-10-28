# Runner Outcome Comparison — Wednesday 2026-10-28 — scheduled ~07:00 ET

**Status: PARTIAL. GitHub early snapshot retrieved; connected Webull blocked by non-interactive authorization.** Public per-symbol premarket quotes obtained for 3/5 original carry-forward tickers; the 03:16:30 ET snapshot had **no verified 2026-10-28 overnight prices**. Therefore **NO legitimate 03:16→07:00 OVN-to-PRE return, first-ignition outcome, volume acceleration or marketwide current-leader ranking** can be calculated. No orders placed.

## Sources and immutable observation boundaries

- **Original early record, Wed 2026-10-28 03:16:30 ET:** https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-28_031630_ET_overnight_ignition.md . It preserved **Tuesday 2026-10-27 20:00 ET AFTER-HOURS (ATH)** volume leaders SNTI/WFF/SHFS/GPUS/NEXR; no live Oct 28 OVN quote. Its 03:16 fields are UNKNOWN and **must not be represented as price observations**.
- **Historical ATH baseline:** MarketChameleon https://marketchameleon.com/reports/afterhourstrading , explicitly dated **2026-10-27 20:00 ET** (reported delayed); prices rounded to cents. Baseline volumes are **Oct 27 ATH reported values**, not 03:16 Oct 28 OVN volumes.
- **Follow-up:** Wed 2026-10-28 approximately 07:00 ET. Public.com premarket stock pages are asynchronous; their **individual site-reported last-update clock times** are given below. Public labels them “EST” although Oct 28 is EDT; treat them as **Eastern wall-clock labels with unverified offset**, not independently validated synchronized timestamps. Price precision is **only cents**.
- **Connected Webull:** get_gainers_losers(PRE_MARKET), get_stock_snapshot(overnight_required=true), get_stock_tick(PRE) all rejected with `User input required but current turn is running in a non-interactive mode.` No connected Webull quotes, ticks, bid/ask or current leaderboard. Alpha Vantage bulk endpoint returned **explicitly artificial sample data** (rejected); Financial Datasets returned **$0 credits** (no data). Public marketwide premarket pages either still displayed Oct 27 or lacked a reliable small-cap ranked board. Do not fabricate rankings.
- **Previous catalyst vault:** https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-27_1832_ET_afterhours_catalyst_vault.md ; **methodology:** https://github.com/Jpuck412/puck-elite-price-action-v2/blob/main/README.md . Original research remains unchanged.

## SAME five: Oct 27 20:00 ATH carry-forward vs Oct 28 PRE

**NOT a comparison to 03:16 OVN prices** (those do not exist). ATH→PRE changes are **rough cross-session changes computed from rounded two-decimal prices**, NOT actual first-ignition outcomes. % formula (PRE / prior ATH − 1)×100; volume counters are not compared across sessions.

| Symbol | Oct 27 20:00 ATH price / ATH % vs Oct 27 close / reported ATH vol | Oct 28 PRE quote (source timestamp) | Approx ATH→PRE change | Oct 28 PRE volume | Spread | Defended support | Classification / limitations |
|---|---|---|---:|---|---|---|---|
| **SNTI** | $0.20 / +7.1% / 30.1M | **$0.19 @ 06:30 Eastern site-label**; +1.23% vs Oct 27 regular close | **~−5.0%** | UNKNOWN session-attributed; vendor unclassified “Volume” 2.28M (not directly comparable) | UNKNOWN | UNKNOWN | Modest ATH-to-PRE fade, **NOT verified false OVN ignition**. |
| **WFF** | $0.06 / −6.2% / 21.5M | **UNKNOWN**; public page still shows Oct 27 09:30 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | No valid Oct 28 quote; **NOT proof of disappearance**. |
| **SHFS** | $0.10 / −13.2% / 18.7M | **UNKNOWN**; public page still shows Oct 27 09:30 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Weak Oct 27 ATH control; no verified Oct 28 outcome. |
| **GPUS** | $0.23 / +9.6% / 17.4M | **$0.23 @ 07:00 Eastern site-label**; +9.60% vs Oct 27 regular close | **~0.0%** | UNKNOWN session-attributed; vendor unclassified “Volume” 3.19M | UNKNOWN | UNKNOWN | Rough ATH-to-PRE price retention; **not verified buyer-controlled continuation**. |
| **NEXR** | $0.51 / −6.5% / 14.6M | **$0.42 @ 06:00 Eastern site-label**; −22.24% vs Oct 27 regular close | **~−17.65%** | UNKNOWN session-attributed; vendor unclassified “Volume” 1.34M | UNKNOWN | UNKNOWN | **Strong additional fade** from ATH baseline; first OVN ignition not established. |

**Primary public follow-up pages:**
- SNTI https://public.com/stocks/snti/pre-market (Oct 28 06:30 displayed $0.19).
- WFF https://public.com/stocks/wff/pre-market (last dated Oct 27; reject as current).
- SHFS https://public.com/stocks/shfs/pre-market (last dated Oct 27; reject as current).
- GPUS https://public.com/stocks/gpus/pre-market (Oct 28 07:00 displayed $0.23).
- NEXR https://public.com/stocks/nexr/pre-market (Oct 28 06:00 displayed $0.42).
- Vendor page “Volume” does not establish PRE-only volume, and may refresh at different times than the price. **ATH-to-PRE volume change UNKNOWN** for every symbol. Source pages are dynamic and can subsequently show newer times/prices.

## Meaningful additional candidates and controls (not new verified marketwide leaders)

| Symbol | Oct 27 20:00 ATH historical | Oct 28 PRE public quote | Rough ATH→PRE | Evidence status |
|---|---|---|---|---|
| **BRAI** | $5.16 / +56.0% | **$4.64 @ 05:30 Eastern site-label**; +40.18% vs Oct 27 regular close | **~−10.08%** | Exceptional carry-forward retracement; above preferred $4 ceiling; NOT newly discovered marketwide leader. Vendor page displays “Volume” 2.09M, session attribution UNKNOWN; spread/tape/support UNKNOWN. https://public.com/stocks/brai/pre-market |
| **BOOM** | $6.28 / +17.4% | **$6.33 @ 07:00 Eastern site-label**; +18.32% vs Oct 27 regular close | **~+0.80%** | Modest carry-forward price retention after verified earnings PR; outside preferred sub-$4 band. Vendor “Volume” 85.54K, session attribution UNKNOWN; spread/tape/support UNKNOWN. https://public.com/stocks/boom/pre-market |
| **ULBI** | $15.56 / +144.7% | **UNKNOWN**; public page lacks a dated Oct 28 quote | UNKNOWN | $16 cash merger consideration; merger-arbitrage exception, NOT ordinary sub-$4 ignition. https://public.com/stocks/ulbi/pre-market |

**New meaningful 07:00 PRE runner absent from early five:** **NOT VERIFIED.** Available generic premarket screens lacked a reliable timestamped 2026-10-28 small-cap leader list. No “new leader” is claimed.

## First-seen catalyst chronology (not causal attribution)

- **SNTI:** Oct 27 **~16:38 ET Form 8-K**, accession `0001628280-26-067624`, CVR record date Oct 30 and board changes; acceptance time from **secondary EDGAR index only**, direct SEC confirmation UNKNOWN. Original early vault correction: https://www.sec.gov/Archives/edgar/data/1854270/000162828026067624/0001628280-26-067624-index.htm . Historical convertible/resale registration and reverse-split authorization; no fresh issuance proven. First responsive trade **UNKNOWN**.
- **GPUS:** Historical issuer Oct 22 **16:15 ET** ATM suspension announcement; prior dilution/financing exposure. No verified Oct 28 fresh original PR or response time; **UNKNOWN**.
- **NEXR:** Original issuer Oct 27 **08:17 ET** KeepZone AI sale agreement, not new overnight: https://www.globenewswire.com/news-release/2026/10/27/3388976/0/en/nexera-technologies-signs-definitive-agreement-to-sell-keepzone-ai-to-a-global-aerospace-and-defense-company-for-up-to-6-million.html . First response **UNKNOWN**.
- **WFF / SHFS:** Fresh issuer catalyst timestamp **UNKNOWN**; no confirmed original 2026-10-28 release.
- **BRAI:** Original Oct 26 **09:00 ET** AI-platform expansion PR (prior day); first response **UNKNOWN**.
- **BOOM:** Original Oct 27 **16:05 ET** Q3 earnings PR; first responsive tick **UNKNOWN**. Source and financials in Oct 27 ATH vault.
- **ULBI:** Original Oct 27 **16:15 ET** $16/share cash merger PR; first response **UNKNOWN**. https://www.globenewswire.com/news-release/2026/10/27/3389645/18622/en/enersys-to-acquire-ultralife-corporation-in-a-320-million-all-cash-transaction.html

## Outcome classification and missing fields

- **No verified early-OVN ignition or false ignition**: no 03:16 OVN price/tape existed; cross-session ATH→PRE fades cannot substitute.
- **Observed cross-session price fade:** NEXR ~−17.65%, SNTI ~−5%, BRAI ~−10.08% (exception); only against rounded **Oct 27 20:00 ATH**, NOT against an Oct 28 early OVN snapshot.
- **Rough cross-session price retention:** GPUS ~0%; BOOM ~+0.80% (exception); **not proof of buyer control or continuation from a verified early ignition**.
- **Disappearance:** none can be established; WFF and SHFS lack dated current quotes, not evidence they stopped trading or left a leaderboard.
- **Current 07:00 premarket leaders vs early five:** cannot make a valid marketwide comparison without a synchronized current ranking.
- **For all:** actual first pre-04:00 ignition, continuous tick speed, buyer aggression, relative volume acceleration, bid/ask spread and stability, confirmed support, precise first-news-to-price-response latency, defined executable stop/risk and exchange buy eligibility **UNKNOWN**. Even when a single vendor displays a volume figure, its session attribution and timestamp remain **UNKNOWN**.
- **PUCK PERMISSION:** speed ↑ UNKNOWN; volume ↑ UNKNOWN; spread ↔/↓ UNKNOWN; buyer control UNKNOWN; support UNKNOWN; risk UNKNOWN. **NO TRADE VERIFIED. No orders placed.**

## Deduplication / write integrity

- Source early snapshot key: `2026-10-28/OVN/03:16:30_ET/SNTI|WFF|SHFS|GPUS|NEXR` with **all current prices UNKNOWN**.
- Historical carry-forward baseline keys: `2026-10-27/ATH/20:00_ET/<SYMBOL>`.
- New observation keys: `2026-10-28/PRE/<vendor-reported-clock-time>/<SYMBOL>` (with source precision, independent quote times, and unknown UTC offset), including BRAI/BOOM exceptions. Do not deduplicate different sessions/times as if identical.
- **New record only:** `research/daily-watch/2026-10-28_070040_ET_premarket_followup.md`; earlier files not overwritten.
