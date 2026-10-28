# Overnight Ignition Vault — Wednesday 2026-10-28 — 03:16:30 ET

**Result: PARTIAL / NO VERIFIED CURRENT OVERNIGHT MARKET DATA.** The five names below are a **Tuesday October 27 20:00 ET AFTER-HOURS (ATH) carry-forward activity set**, **NOT** the top five October 28 overnight (OVN) gainers. No current OVN ranking or quote is certified. This distinction is essential for evaluating whether ignition began before 04:00 ET. No order placed.

## Session boundaries and evidence provenance

- **ATH:** Tue 2026-10-27 16:00–20:00 ET. **OVN:** Tue 2026-10-27 20:00–Wed 2026-10-28 04:00 ET. **PRE:** begins Wed 2026-10-28 04:00 ET and **has not begun** at 03:16:30 ET.
- **Attempted connected Webull:** `get_gainers_losers(PRE_MARKET)`, `get_gainers_losers(AFTER_MARKET)`, and `get_stock_snapshot(overnight_required=true)` all returned **"User input required but current turn is running in a non-interactive mode."** Thus **NO** current Webull OVN price, volume, bid/ask, tick, trade or quote timestamp was obtained. PRE ranking would not itself prove OVN ignition.
- **Attempted secondary broker feed:** connected Alpaca `get_stock_snapshot(feed=overnight)` returned `INVALID_ARGUMENT ... api_error`. Not evidence of zero trading.
- **Public live-source search:** No trustworthy per-symbol **2026-10-28 ~03:16 ET OVN** ranking or synchronized tick/quote was found. Public premarket boards still displayed the **Oct 27** session and were rejected as Oct 28 OVN evidence.
- **Usable previous-session baseline:** MarketChameleon report expressly **"As of 27-Oct-2026, 8:00 PM ET"**, marked delayed 15 minutes, and identifies the five highest-volume names below. **Its 8 PM price, change, and share counts are ATH, NOT OVN.** Source: https://marketchameleon.com/reports/afterhourstrading .
- **GitHub comparison:** inspected `Jpuck412/ticker-vault/research/daily-watch/` (no existing Oct 28 file at this check), original Oct 27 18:32 ATH vault, Oct 27 03:23 OVN placeholder, and `Jpuck412/puck-elite-price-action-v2/README.md`. The methodology requires live-provider evidence and unknown-data integrity. No prior observations altered.

## Five selected high-participation ATH carry-forward candidates — NOT a verified OVN top five

**Price and % columns below: October 27 20:00 ET AFTER-HOURS ONLY, compared with October 27 16:00 regular close.** Reported share counts are ATH from MarketChameleon; quote-age/underlying execution timestamps beyond the report's 20:00 summary are not independently available. **All October 28 03:16 ET OVN fields are UNKNOWN.**

| Symbol | Oct 27 ATH 20:00 price | ATH % | Reported ATH volume | Oct 28 OVN price | OVN % | OVN volume | OVN bid/ask/spread | Quote freshness | First actual OVN ignition | Verdict |
|---|---:|---:|---:|---|---|---|---|---|---|---|
| **SNTI** | $0.20 | +7.1% | 30.1M | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | NO TRADE VERIFIED |
| **WFF** | $0.06 | −6.2% | 21.5M | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | NO TRADE VERIFIED; weak-move control |
| **SHFS** | $0.10 | −13.2% | 18.7M | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | NO TRADE VERIFIED; failed-momentum control |
| **GPUS** | $0.23 | +9.6% | 17.4M | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | NO TRADE VERIFIED |
| **NEXR** | $0.51 | −6.5% | 14.6M | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | NO TRADE VERIFIED; weak-move control |

**Selection method:** the five most active symbols named by a dated public ATH report, all priced below $1; this is **not** a comprehensive NASDAQ/NYSE/NYSE American eligibility or OVN-rank certification. WFF and SHFS deliberately retained as negative controls. Trade eligibility and exchange instrument status **UNKNOWN**.

## Exceptional after-hours names — NOT OVN observations

| Symbol | Oct 27 ATH 20:00 | Class | Research caution |
|---|---|---|---|
| **BRAI** | $5.16 / +56.0% | Exceptional price momentum; outside preferred sub-$4 band | Prior issuer AI/CX announcement **Oct 26 09:00 ET**, not fresh OVN; first responsive trade UNKNOWN. |
| **BOOM** | $6.28 / +17.4% | Verified Oct 27 earnings response chronology, above preferred price band | Original issuer earnings PR **Oct 27 16:05 ET**; first trade after news UNKNOWN. |
| **ULBI** | $15.56 / +144.7% | Merger-arbitrage control, not ordinary small-cap momentum ignition | Original cash acquisition PR **Oct 27 16:15 ET**, $16 proposed cash consideration; first response UNKNOWN. |
| **SCKT** | Prior Oct 27 17:58 $0.3769 / −27.01% | Historical fresh negative-news control | Delisting/OTCID plan original issuer PR Oct 27 16:55 ET; not a verified Oct 28 OVN observation. |

MarketChameleon ATH report: https://marketchameleon.com/reports/afterhourstrading . Original ULBI release: https://www.globenewswire.com/news-release/2026/10/27/3389645/18622/en/enersys-to-acquire-ultralife-corporation-in-a-320-million-all-cash-transaction.html . Other original PR URLs and timestamps in Oct 27 18:32 vault below.

## Newly located SNTI filing — IMPORTANT correction to prior catalyst classification

The Oct 27 ~18:32 archive classified SNTI as **"move / no verified fresh 16:00+ PR"**. Subsequent research located **two** material filings relevant to that qualification:
- **2026-10-26 16:17 ET, 8-K, accession 0001140361-26-040772**: merger completion (underlying closing Oct 21) and contractual contingent value rights, not a new clinical milestone. Secondary filing timestamp and direct EDGAR index: https://www.gosleesignals.com/filing/2147889 ; https://www.sec.gov/Archives/edgar/data/1854270/000114036126040772/0001140361-26-040772-index.htm .
- **2026-10-27 16:38 ET, 8-K, accession 0001628280-26-067624**: board resignation and **Oct 30 CVR record date** following the completed Oct 21 merger. **Timestamp reported by third-party EDGAR index, not independently confirmed from the original SEC acceptance index** (SEC index direct read failed). https://www.gosleesignals.com/filing/2158881 ; https://www.sec.gov/Archives/edgar/data/1854270/000162828026067624/0001628280-26-067624-index.htm .
- Therefore, **SNTI had a relevant fresh post-16:00 SEC filing that the Oct 27 archive did not identify**. This new file corrects the research record **without overwriting** the earlier observation. **The filing's causal link to any specific price/volume response remains UNKNOWN.** Oct 27 20:00 ATH price $0.20 (+7.1%) cannot establish first response to the 16:38 filing.
- **Dilution/structure:** Sept 24 prospectus/resale registration of up to 25,555,024 shares issuable on convertible-note exchange, prior reverse-split authorization 1:20–1:50, merger/CVR restructuring. These are risks, **not proof of Oct 28 share issuance**. https://www.stocktitan.net/sec-filings/SNTI/ ; https://www.stocktitan.net/sec-filings/SNTI/8-k.html .

## Other catalyst and dilution checks (historical only)

- **GPUS:** Oct 22 16:15 ET announcement reported suspension of its then-existing ATM program; prior large share issuance and financing exposure warrant review. Exact Oct 28 new financing or issuer PR **UNKNOWN**. Oct 27 ATH +9.6% alone does not verify catalyst attribution.
- **NEXR:** Original Oct 27 **08:17 ET** issuer announcement concerning a KeepZone AI sale for $1M in buyer securities plus contingent earn-out; **not fresh 20:00+ OVN news**. https://www.globenewswire.com/news-release/2026/10/27/3388976/0/en/nexera-technologies-signs-definitive-agreement-to-sell-keepzone-ai-to-a-global-aerospace-and-defense-company-for-up-to-6-million.html . Actual new issuance by NEXR **UNKNOWN**.
- **WFF, SHFS:** no original post-20:00 issuer catalyst established; this means **UNVERIFIED**, not no news. Current SEC 8-K/424B/S-3/ATM/equity-line acceptance, float changes, reverse splits and dilution **UNKNOWN**.
- **BRAI:** original Oct 26 09:00 ET AI expansion issuer PR in prior archive; Oct 27 ATH 20:00 +56.0% does not establish a new overnight news trigger.
- **BOOM:** original Oct 27 16:05 ET issuer earnings PR (Q3 revenue $172.8M, net income $9.7M), verified prior session. First responsive tick and new overnight financing **UNKNOWN**.

## Classification and evidence integrity

- **Verified fresh news, price response chronology:** SNTI Oct 27 16:38 secondary-indexed 8-K + Oct 27 20:00 ATH net positive; BOOM Oct 27 16:05 earnings + ATH positive; ULBI Oct 27 16:15 merger + ATH positive. **Causality and first meaningful price-volume response UNKNOWN for all**.
- **Move with no verified fresh overnight news:** none can be established for the Oct 28 OVN session without a current OVN quote. Historical ATH GPUS/NEXR/BRAI may have moved without a *verified new post-20:00* issuer catalyst; absence of verification is not proof of absence.
- **News with no OVN move:** cannot classify; OVN response data **UNKNOWN**.
- **Negative controls:** WFF, SHFS, NEXR at 20:00 ATH; their negative changes despite activity are **not** proof of failed OVN ignition. ULBI merger-arbitrage exceptional control.
- **Missing for every Oct 28 candidate:** synchronized 03:16 ET price, OVN % vs close, OVN session volume, bid/ask and spread, quote freshness, tick-by-tick trade times, tape speed, volume acceleration, buyer aggression, defended support, defined executable risk, exact news-to-first-response latency. Do not infer early ignition from candles or report zero in place of UNKNOWN.
- **PUCK PERMISSION:** speed ↑ UNKNOWN; volume ↑ UNKNOWN; spread ↔/↓ UNKNOWN; buyers control UNKNOWN; support UNKNOWN; risk UNKNOWN. **NO TRADE VERIFIED for every symbol.**

## Deduplication and immutable prior records

- **Current check key:** `2026-10-28/OVN/03:16:30_ET/<SYMBOL>` for SNTI, WFF, SHFS, GPUS, NEXR; values are **unverified current-OVN placeholders**. Distinct historical baseline key `2026-10-27/ATH/20:00_ET/<SYMBOL>`. Do not promote ATH observations to OVN observations or conflate ATH and PRE counters.
- Prior Oct 27 18:32 ATH: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-27_1832_ET_afterhours_catalyst_vault.md
- Prior Oct 27 03:23 OVN placeholder: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-27_032342_ET_overnight_ignition.md
- Prior Oct 27 07:04 PRE follow-up: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-27_070415_ET_premarket_followup.md
- Methodology: https://github.com/Jpuck412/puck-elite-price-action-v2/blob/main/README.md
- No overwrite or mutation of previous observations. Recheck **same five** plus exceptions in a **new** 04:00+ PRE / 07:00 follow-up file if accessible. **No proof = no trade.**
