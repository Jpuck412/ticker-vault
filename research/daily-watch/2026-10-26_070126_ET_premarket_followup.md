# Runner Outcome Comparison — Monday 2026-10-26 — 07:01:26 ET

**Observation pair:** original `2026-10-26 03:30:05.333 ET` (Webull `OVN` session) versus follow-up `2026-10-26 ~07:01:26 ET` (Webull `PRE` session). Eastern time is EDT (UTC−04). **Original snapshot was retrieved from GitHub and remains unchanged.** This is a new follow-up file, not a revision. Deduplication key: `2026-10-26/PRE/07:01:26_ET/<SYMBOL>`.

**Sources:** connected Webull `get_stock_snapshot` (PRE and OVN), `get_gainers_losers(rank_type=PRE_MARKET)`, `get_stock_bars(M1,trading_sessions=PRE)`, `get_stock_tick` for SPRC and TGL, `get_stock_news` for TGL, YMAT, RENT, SPRC; GitHub original snapshot [03:30:05 ET](https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-26_033005_ET_overnight_ignition.md). **Prices are single-point observations, not entry prices.** Webull's `extend_hour_last_price` and `extend_hour_volume` are treated as the PRE observation here; `ovn_volume` is a separate session counter. Webull's PRE ranking is discovery, not proof of trade eligibility.

## Original five: immutable OVN baseline versus PRE follow-up

| Symbol | 03:30 OVN price | 07:01 PRE price | Change since 03:30 | 03:30 OVN shares | 07:01 PRE shares | 07:01 bid / ask | Instant spread | Quote age at ~07:01:26 | Outcome |
|---|---:|---:|---:|---:|---:|---|---:|---|---|
| SPRC | $1.7800 | $1.5400 | **−13.48%** | 541,936 | 4,570,047 | $1.5400 / $1.5500 | 0.65% | ~6 sec | **Failed continuation / price fade** |
| RENT | $3.1700 | $3.1813 | **+0.36%** | 744,816 | 2,802,237 | $3.1800 / $3.1900 | 0.31% | <1 sec | **Near-flat continuation**, not a fresh breakout |
| MYND | $0.3020 | $0.2609 | **−13.61%** | 343,376 | 305,556 | $0.2600 / $0.2832 | 8.54% | ~3 sec | **Failed continuation / wide spread** |
| AUID | $0.3729 | $0.3205 | **−14.05%** | 2,226,353 | 710,999 | $0.3052 / $0.3294 | 7.63% | **~21 minutes STALE** | **Failed continuation; quote not execution-grade** |
| INLF | $0.2023 | $0.1870 | **−7.56%** | 354,751 | 114,573 | $0.1806 / $0.2025 | 11.43% | **~7 min 36 sec STALE** | **Failed continuation; quote not execution-grade** |

**Volume comparison warning:** OVN and PRE volume fields count different sessions. Do **not** subtract them or claim a single-session acceleration. They are preserved side by side for participation comparison. None of the five disappeared from Webull's returned quotes; **absence from the leading PRE percentage ranking is not disappearance from trading**. Four of five were below their early prices; RENT was +0.36%.

## Measurable recent PRE volume — completed M1 bars

Comparison windows: **06:40–06:49 ET** versus **06:50–06:59 ET**, summing returned completed M1 bars and treating missing minutes as no returned activity *within the sample*. These are bar-volume ratios, **not tick-speed or buyer-control proof**.

| Symbol | 06:40–06:49 shares | 06:50–06:59 shares | Recent/prior | Reading |
|---|---:|---:|---:|---|
| SPRC | 157,289 | 55,367 | 0.35× | Declining recent participation |
| RENT | 100,976 | 57,300 | 0.57× | Declining recent participation |
| MYND | 9,765 | 16,347 | 1.67× | Rising from low base despite price fade |
| AUID | 1,138 | 5,321 | 4.68× | Tiny absolute sample; stale L1 quote |
| INLF | UNKNOWN | UNKNOWN | UNKNOWN | Insufficient returned bars in both windows |
| TGL | 748,012 | 1,356,831 | **1.81×** | Substantial recent PRE volume acceleration |
| YMAT | 4,218 | 5,675 | 1.35× | Low absolute recent participation |

**Support:** Nearby sampled M1 ranges are not proof of a defended level. **Defended support UNKNOWN for all**. **Sustained buyer control UNKNOWN**; sampled PRE ticks for SPRC/TGL were returned but do not establish continuous aggressor control. **Continuous tape-speed acceleration UNKNOWN**. **Spread stability UNKNOWN** (one L1 snapshot per comparison, and TGL's displayed spread changed substantially between successive observations). **Defined executable risk UNKNOWN**.

## Newly meaningful PRE candidates

| Symbol | 07:01 PRE price | Gain vs Friday 16:00 close | PRE volume | OVN volume (separate) | Bid / ask | Spread | Quote age | First qualifying PRE M1 bar* |
|---|---:|---:|---:|---:|---|---:|---|---|
| **TGL** | $0.3193 | **+44.15%** | **31,855,414** | 88,389 | $0.3030 / $0.3300 | **8.53%** | ~7 sec | **04:00 ET** (first PRE minute) |
| **YMAT** | $2.3000 | **+12.20%** | 1,627,654 | 17,899 | $2.2800 / $2.3100 | 1.31% | ~51 sec | **04:35 ET** |

*Research threshold: one-minute close >=10% above the previous regular-session close, plus >=25,000 shares over the preceding five clock minutes. **First qualifying minute is NOT first ignition or first responsive tick.** For TGL, 04:00 was already active (160,326 shares), so the actual start could precede PRE. Its early OVN volume was small but nonzero, and no tick-based first ignition is verified. YMAT also traded at 04:00 but first met the combined threshold at 04:35.

**TGL is the dominant newly emerging PRE volume/percentage candidate** in the observed Webull ranking, but its L1 spread was 8.53% at the archived observation. An earlier Webull quote within the same retrieval sequence showed ~$0.3200/$0.3223 (about 0.72%); this is **spread instability**, not an approved tight spread. **NO TRADE**. YMAT is a secondary new PRE participation case, not a verified buyer-controlled runner.

## First-seen news and dilution chronology (ET)

- **RENT:** SEC Form 4 purchase filings accepted **Fri Oct 23 approximately 16:07–16:11 ET**, purchases at $3.55; Webull/Benzinga follow-up **Fri 16:28:42 ET**. Friday archived ATH first qualifying bar **16:14 ET**, after SEC acceptance but **causality and first responsive trade UNKNOWN**. September 424B3 rights offering up to 4,225,352 shares: financing/share-supply risk. Sources: [issuer SEC filings](https://investors.renttherunway.com/financial-information/sec-filings), [Webull news](https://news-static.webullfintech.com/us/news-html/20261023/15799433364384768.html).
- **SPRC:** Last specific clinical item returned **Thu Oct 22 09:08:02 ET** (SCI-110/Phase IIb progress); Oct 23 6-K acceptance time UNKNOWN; earlier convertible note exchange/F-3 resale risk. No verified new Monday issuer catalyst. Source: [Webull clinical report](https://news-static.webullfintech.com/us/news-html/20261022/15792040960863232.html).
- **MYND:** Identified prior leadership news **Thu Oct 8 07:47:40 ET**, not fresh Monday; no verified new issuer catalyst. SEC/NYSE American compliance/share-structure risk from original archive. Source: [Oct 8 6-K](https://www.sec.gov/Archives/edgar/data/0001708441/000170844126000106/executivetransition6-kcover.htm).
- **AUID:** Prior financing PR **Mon Oct 5 16:15 ET**; $1.35m convertible debentures/warrants, not evidence of sales Monday. No verified new issuer catalyst. Source: [SEC exhibit](https://www.sec.gov/Archives/edgar/data/1534154/000121390026108219/ea030800701ex99-1.htm).
- **INLF:** Oct 19 **09:15 ET** $3.75m registered-direct financing pricing and Oct 20 **15:30 ET** closing announcement; warrants/dilution exposure. No verified new Monday catalyst. Source: [Oct 21 6-K](https://www.sec.gov/Archives/edgar/data/0001991592/000121390026111362/ea0309124-6k_inlif.htm).
- **TGL:** Webull/Benzinga first identified specific news **Fri Oct 23 17:21:39 ET**: subsidiary Tadaa Technologies' Oct 21 software-development agreement involving an AI agricultural traceability platform and RM8m fees; **this is a secondary news timestamp, not independently confirmed original issuer publication**. Earlier Oct 15 board-member ~$1.2m subscription financing. No verified Monday PR. Exact first news-to-price latency UNKNOWN. Source: [Webull news](https://news-static.webullfintech.com/us/news-html/20261023/15799641769454592.html).
- **YMAT:** Webull/Benzinga H1 results **Fri Oct 23 16:38:49 ET**, negative EPS report; previously disclosed equity facility/debt-to-equity conversion, potential dilution. No verified Monday new PR. News-to-first trade latency UNKNOWN. Source: [Webull H1 report](https://news-static.webullfintech.com/us/news-html/20261023/15799472689357824.html).

**News with no move versus moves with no verified new news:** TGL's current major PRE move has **no verified fresh Monday issuer announcement**; this is not proof that no news exists. MYND/AUID/INLF faded with no fresh Monday catalyst verified. No independently confirmed Monday issuer-news-with-zero-response control was established.

## Additional controls / risk exceptions

- **GPUS:** PRE ~$0.1676, PRE shares ~1.79m; overnight ~2.82m. Not a major PRE percentage leader; historical ATM risk.
- **SHFS:** PRE ~$0.1120, PRE shares ~3.19m; overnight ~7.68m. Weak price and financing/compliance risk.
- **STKH:** PRE ~$0.4339 with ~5.83m PRE shares, but wide $0.4100/$0.4500 quote; early OVN quote was crossed. Unreliable execution conditions.
- **XXII:** Earlier Webull status **CO (liquidate-only)**; do not classify as buy-eligible without updated instrument-status verification.

## Research classification and permission

**Continuation:** RENT essentially flat (+0.36%) after 03:30; **not confirmed momentum continuation**. **False/failed early ignitions:** SPRC, MYND, AUID, INLF each below their original prices. **New premarket leader:** TGL (+44.15% versus prior close, ~31.86m PRE shares), but large/unstable spread; YMAT is secondary. **Disappearance:** NONE from available quote lookup; original names absent from the PRE top-percentage shortlist are still quoted.

**PUCK PERMISSION — NO TRADE VERIFIED for every ticker.** Increasing continuous speed UNKNOWN; increasing volume is measured only for certain bar windows; stable/tight spread not established; buyer control UNKNOWN; defended support UNKNOWN; executable stop/invalidation risk UNKNOWN. No orders or trade instructions created. **Evidence > prediction. No proof = no trade.**

### Provenance and deduplication

Original immutable file: [2026-10-26_033005_ET_overnight_ignition.md](https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-26_033005_ET_overnight_ignition.md). This comparison uses distinct `2026-10-26/PRE/07:01:26_ET/<SYMBOL>` keys; repository directory was checked before creation and no same-day PRE follow-up existed. Times/volumes/quotes reflect connected Webull responses collected approximately **07:00–07:01:26 ET**; exact local call receipt may differ by seconds. No historical file overwritten.
