# Runner Outcome Comparison — 2026-10-30 — 2026-10-30 07:05:47 EDT

**Run started:** Friday 2026-10-30 07:04:03 EDT; **comparison compiled:** 2026-10-30 07:05:47 EDT (UTC 2026-10-30T11:05:47.378Z).  
**Source hierarchy:** connected GitHub early snapshot → connected Webull attempted (authorization failed) → timestamped Stock Analysis individual PRE quotes → Stock Analysis Oct 30 PRE screener (independent, unsynchronized) → Market Chameleon delayed 06:39 PRE report → original issuer PR/SEC links from preserved early research.  
**Market sessions:** Oct 29 16:00–20:00 EDT = AFTER HOURS (AH); Oct 29 20:00–Oct 30 04:00 EDT = OVERNIGHT (OVN); Oct 30 04:00–09:30 EDT = PREMARKET (PRE). No new OVN trades verified. **NO TRADE VERIFIED.**

## Immutable early baseline and deduplication

- **Original early research file, retained unchanged:** https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-30_032040_ET_overnight_ignition.md
- **Original blob SHA:** `a881791dbc499451facb3e39e45d2a97e07652d1`.
- **Original observation time:** **2026-10-30 03:20:40 EDT**. It did **NOT** contain live overnight quotes: its five symbols were **Oct 29 ~19:55–19:59 ET AH carry-forwards**. Their prices must not be described as Oct 30 03:20 observations.
- **This follow-up observation:** **2026-10-30 ~07:04–07:05 EDT**. Individual PRE last-trade timestamps differ; see below.
- Dedup keys: `date|session|symbol|source-last-trade-time`. The `03:20:40|OVN_ATTEMPT` key denotes a **missing-data research attempt**, not an executed trade. Historical AH baselines and PRE quotes are stored as different sessions and never merged into one time series.
- Other nearby archive: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-29_1830_ET_afterhours_catalyst_vault.md and https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-29_065915_ET_premarket_followup.md .
- Prior second-repo baseline (not a new Oct 30 observation): https://github.com/Jpuck412/puck-elite-price-action-v2/blob/main/research/runner-comparisons/2026-10-12_0535_ET_webull_premarket.md .

## Recheck of the SAME five original candidates

**Change formula:** `(Oct 30 PRE last trade / Oct 29 AH carry-forward last trade - 1)*100`. This is **AH→PRE**, not 03:20 OVN→07:05 PRE. Percent versus Oct 29 regular close is a different denominator. Prices are **last-trade observations, not executable bids**.

| Symbol | Oct 29 AH price (time ET) | Oct 30 PRE last (last-trade time ET) | AH→PRE change | PRE % vs Oct 29 16:00 close | Reported PRE volume, source/time | Quote age at ~07:05 ET | Outcome relative to AH |
|---|---:|---:|---:|---:|---|---|---|
| **SLGB** | $0.4227 (19:59) | **$0.3493 (07:03)** | **−17.36%** | **+70.56%** | **26,612,762** shares; Stock Analysis Oct 30 screener, retrieved ~07:05; screener price **$0.36** is **not synchronized** with 07:03 last trade | ~2 min | **Partial AH fade**; still large PRE gap. Not a verified false *overnight* ignition. |
| **NRXP** | $3.361 (19:59) | **$2.940 (06:50)** | **−12.53%** | **+10.53%** | **1,542,192** shares; Stock Analysis Oct 30 screener ~07:05 | ~15 min | **AH fade**; upcoming issuer regulatory news unconfirmed at capture. |
| **WKHS** | $3.090 (19:59) | **$3.130 (06:57)** | **+1.29%** | **+22.75%** | **694,236** shares; Stock Analysis Oct 30 screener ~07:05; screener price $3.10 differs from individual 06:57 last | ~8 min | **AH price retention / modest continuation**; not verified buyer control. |
| **FNGR** | $0.1650 (19:59) | **$0.1017 (06:47)** | **−38.36%** | **−28.73%** | **~24.0M** shares; Market Chameleon 06:39 delayed PRE report; no synchronized PRE volume with 06:47 last | ~18 min | **Severe AH→PRE reversal / negative control**. No confirmed 03:20 ignition. |
| **BURU** | $0.4250 (19:55) | **$0.5700 (07:04)** | **+34.12%** | **+53.35%** | **79,111,012** shares; Stock Analysis Oct 30 screener ~07:05; screener price $0.56 not synchronized with 07:04 last | ~1 min | **Strongest AH→PRE price continuation** of original five, but no verified tape or entry permission. |

**Critical volume distinction:** Oct 29 **AH-only** volumes in early file were SLGB **37.1M**, FNGR **22.5M**, BURU **101.5M**; NRXP and WKHS AH-only volumes **UNKNOWN**. Oct 30 **PRE** volumes above are different session totals. Therefore **volume change since 03:20 and acceleration are UNKNOWN for all five**. Comparing 37.1M AH to 26.6M PRE would be a false volume-delta calculation. Different sources and delayed report clocks prohibit reliable interval acceleration inference.

**All bid/ask spreads, order-book depth, executed-tick speed, buyer aggression, defended support and stop/entry risk: UNKNOWN.** Public last-trade prices and candles cannot certify these.

## Current PRE leaders versus early list; new exceptions

- **SLGB**: Stock Analysis Oct 30 PRE **#1 by percent** on first page: screener $0.36, **+77.54%**, PRE volume **26,612,762**. Individual stock page 07:03 last is $0.3493, +70.56%. The two are **not synchronized**; use source-specific prices, not interchangeable figures.
- **BURU**: PRE **#2 by percent**: screener $0.56, **+49.80%**, **79,111,012** PRE shares. Individual 07:04 last $0.57, +53.35%. Also **#1 most active PRE** in Market Chameleon 06:39 report at ~75.9M (delayed).
- **WKHS**: PRE screener **#4**: $3.10, **+21.57%**, **694,236** PRE shares. Individual 06:57 last $3.13. Still on leaderboard.
- **NRXP**: PRE screener **#12**: $2.94, **+10.53%**, **1,542,192** PRE shares. Still positive against close, but AH price faded.
- **FNGR**: **Not on first page of positive PRE gainers** because its last quote is negative; **not delisted or missing from trading**. Market Chameleon 06:39 ranked FNGR among most active PRE at **~24.0M** shares and **~−29%**. This is a **gainer-leaderboard disappearance**, not an instrument disappearance.
- **NEW — HUBC / Nasdaq:** Oct 30 **06:41 ET** individual PRE last **$0.1521**, **+12.67%** vs Oct 29 close; PRE screener at ~07:05 **$0.15 / +13.19% / 65,069,062 shares**. Market Chameleon 06:39 ranked it **#2 most active PRE** at **64.4M**. Fresh Oct 30 original issuer catalyst **NOT VERIFIED**; last listed press news is older, prior September reverse split and listing compliance issues. **No trade verified.**
- **NEW — NCPL / Nasdaq:** Oct 30 **06:46 ET** individual PRE last **$2.020**, **+13.48%**; PRE screener **875,254 shares**. Repeat multi-day ticker from Oct 28–29 research, historical equity line/warrant risk, **no new Oct 30 original issuer catalyst verified**. **No trade verified.**
- **No confirmed market disappearance** among the five: all have a dated Oct 30 PRE price. **No actual early-overnight ignition can be labeled true or false** because the 03:20 record had no OVN tape.

## Catalyst chronology / first responsive trade

| Symbol | First verified original issuer news time ET | Catalyst status at follow-up | First meaningful executed price/volume response | Dilution / capital risk |
|---|---|---|---|---|
| **SLGB** | Oct 29 **16:15** | Nasdaq 180-day bid-price compliance extension; possible reverse split **not executed** | **UNKNOWN** | Future reverse split possible; no fresh issuance proven |
| **NRXP** | Oct 29 **16:01** | Scheduled Oct 30 **08:30** conference call and promised *before-open* regulatory news. At ~07:05 issuer press-release index still listed Oct 29 as newest; Oct 30 milestone contents **NOT VERIFIED** | **UNKNOWN** | New filing/ATM/dilution status **UNKNOWN** |
| **WKHS** | Oct 29 **16:01** | Signed **$10M reference-unit** modular AI agreement; contemplated 150-unit LOI **non-binding**; secondary-indexed 8-K ~16:16 (not primary acceptance verified) | **UNKNOWN** | New issuance from announcement **not proven** |
| **FNGR** | Oct 29 **16:30** | Non-binding BlueFlare term sheet; proposed other parties ~**80% fully diluted** ownership if completed, **not** an executed issuance | **UNKNOWN** | **High potential ownership dilution** if consummated |
| **BURU** | Oct 29 **daytime**, exact primary time **UNKNOWN** | NYSE American compliance news; no new original Oct 30 PR verified | **UNKNOWN** | Oct 23 424B3 up to **20M resale shares**; prior split |
| **HUBC** | Fresh Oct 30 PR **UNKNOWN** | Volume/price move without verified new catalyst | **UNKNOWN** | Prior September reverse split; fresh financing **UNKNOWN** |
| **NCPL** | Fresh Oct 30 PR **UNKNOWN** | Repeat mover without verified new catalyst | **UNKNOWN** | Historical equity line/warrants |

**Original issuer / SEC links retained for provenance:**
- SLGB Oct 29 16:15 issuer: https://www.globenewswire.com/news-release/2026/10/29/3391856/0/en/smart-logistics-global-limited-receives-additional-180-day-nasdaq-compliance-period.html
- NRXP Oct 29 16:01 issuer: https://ir.nrxpharma.com/news-releases/news-release-details/nrx-pharmaceuticals-nasdaq-nrxp-host-conference-call-october-30 ; current press index https://ir.nrxpharma.com/press-releases
- WKHS Oct 29 16:01 issuer: https://www.globenewswire.com/news-release/2026/10/29/3391805/0/en/workhorse-enters-modular-ai-infrastructure-market-through-foundational-terrapod-partnership-with-uk-based-rhaelm.html ; primary 8-K body https://www.sec.gov/Archives/edgar/data/1425287/000162828026068250/wkhs-20261028.htm
- FNGR Oct 29 16:30 issuer: https://ir.fingermotion.com/newsroom/press-releases/detail/228/fingermotion-signs-term-sheet-for-business-combination-with-blueflare-group-holdings-to-form-a-north-american-power-first-digital-infrastructure-company
- BURU Oct 29 compliance: https://www.businesswire.com/news/home/20261029630353/en/NUBURU-Regains-Compliance-with-NYSE-American-Continued-Listing-Standards/

## Quote and leaderboard sources (actual scope, not interchangeable)

- Stock Analysis **individual** PRE last trades with source-labelled quote timestamps: https://stockanalysis.com/stocks/slgb/ ; https://stockanalysis.com/stocks/nrxp/ ; https://stockanalysis.com/stocks/wkhs/ ; https://stockanalysis.com/stocks/fngr/ ; https://stockanalysis.com/stocks/buru/ ; https://stockanalysis.com/stocks/hubc/ ; https://stockanalysis.com/stocks/ncpl/
- Stock Analysis **Oct 30 PRE gainers** page (cumulative PRE volume, source-specific and **not quote-synchronized** to individual pages), accessed ~07:05: https://stockanalysis.com/markets/premarket/gainers/
- Market Chameleon **Oct 30 06:39 ET** report (page header 06:40; **15-minute delayed**): https://marketchameleon.com/Reports/PremarketTrading . BURU 75.9M, HUBC 64.4M, SLGB 26.4M, FNGR 24.0M PRE shares. Not an exact 07:05 snapshot.
- Webull connected PRE gainers, most-active, five-symbol extended-hours/overnight snapshot, SLGB/FNGR depth quotes, BURU PRE/OVN tick history were **attempted**. Each rejected with `User input required but current turn is running in a non-interactive mode.` No connected Webull data was obtained.

## Classification / no-trade verdicts

- **Relative AH→PRE continuation:** **BURU +34.12%**, **WKHS +1.29%**. Both lack executable verification.
- **Relative AH→PRE fading:** **FNGR −38.36%** (severe), **SLGB −17.36%**, **NRXP −12.53%**. This is NOT a confirmed failure of pre-04:00 ignition.
- **Leaderboard disappearance:** FNGR no longer on positive PRE gainers, but still actively traded by public PRE volume. **Instrument disappearance: NONE VERIFIED**.
- **Early OVN first-seen price, first responsive news-to-tape latency, change in volume since 03:20, spread, support, speed, buyer control, and defined risk: ALL UNKNOWN.**
- **PUCK PERMISSION:** For every original and additional symbol, speed ↑ **UNKNOWN**; volume acceleration ↑ **UNKNOWN**; spread stable/tight **UNKNOWN**; buyer-controlled tape **UNKNOWN**; support defended **UNKNOWN**; risk **UNDEFINED**. **NO TRADE VERIFIED. NO ORDER PLACED.** Historical percentage retention is not an entry signal.

**Methodological conclusion:** The early 03:20 file successfully preserved **AH research candidates**, not overnight measurements. The current PRE follow-up gives valid *cross-session historical price retention* and *current PRE cumulative participation* without falsely inventing overnight ignition, quote freshness, volume acceleration or buyers.
