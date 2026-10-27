# Runner Outcome Comparison — Tuesday 2026-10-27 — check initiated 07:04:15 ET

**Status: PARTIAL — connected Webull authorization blocked.** The early 03:23:42 ET record exists but contains **no verified Oct 27 overnight prices or volumes**. Consequently **no actual 03:23-to-07:04 price/volume change can be calculated**. The table below compares separately timestamped *public premarket quotes* against **Oct 26 ~18:31 ET after-hours indicative prices** as a historical proxy, NOT against the unobserved 03:23 overnight market. Never promote a proxy to a verified early-ignition result.

**Session boundaries (ET):** Oct 26 AFTER_HOURS (ATH) 16:00–20:00; Oct 26/27 OVERNIGHT (OVN) 20:00–04:00; Oct 27 PREMARKET (PRE) 04:00–09:30. **Current comparison check initiated 2026-10-27 07:04:15 EDT (UTC−04:00).** Public pages expose *different per-symbol quote times*; they are not simultaneous 07:04 ticks.

## Provider audit

- GitHub connected read succeeded for the exact early file `research/daily-watch/2026-10-27_032342_ET_overnight_ignition.md` and Oct 26 ATH baseline.
- Connected Webull `get_gainers_losers(PRE_MARKET)` and `get_stock_snapshot(SNTI,MKDW,BRAI,VNTG,TGL; extended+overnight)` explicitly attempted and both returned **"User input required but current turn is running in a non-interactive mode."** Therefore no Webull quotes, bid/ask, tick prints, 1m bars, or Webull session volume were obtained.
- Public Stock Analysis stock detail pages explicitly label quote time, date, and PRE price; public PRE gainers table lists volumes but has **no per-row timestamp**. Its values differ slightly from individually timestamped stock pages and must not be merged as synchronous ticks.
- **Data not available is UNKNOWN, never zero.** Do not calculate OVN-to-PRE volume deltas from separate counters or regular-session volume.

## Exact same five names as the 03:23 early record

**Early Oct 27 03:23 OVN quote: UNKNOWN for ALL FIVE.** Original research was a carry-forward shortlist, not a measured early-morning price observation.

| Symbol | Oct 26 ~18:31 ATH indicative price (historical) | Oct 27 PRE price / actual source time ET | Approx. % vs historical ATH price* | Actual % from 03:23 OVN | PRE % vs Oct 26 16:00 close (stock detail) | PRE volume | PRE bid/ask / spread | Buyer control, defended support |
|---|---:|---|---:|---|---:|---|---|---|
| **SNTI** | ~$0.27 | **$0.2066 @ 06:47** | **−23.48%** | **UNKNOWN** | +17.99% | **30,137,016** in untimed public screener; not synced to 06:47 | **UNKNOWN** | **UNKNOWN** |
| **MKDW** | ~$0.56 | **$0.4208 @ 06:42** | **−24.86%** | **UNKNOWN** | +0.79% | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** |
| **BRAI** | ~$2.79 | **$3.1200 @ 07:02** | **+11.83%** | **UNKNOWN** | +47.17% | **3,464,410** in untimed public screener; not synced to 07:02 | **UNKNOWN** | **UNKNOWN** |
| **VNTG** | ~$0.52 | **$0.4626 @ 05:23** (**stale**) | **−11.04%** | **UNKNOWN** | +0.52% | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** |
| **TGL** | ~$0.27 | **$0.2270 @ 06:48** | **−15.93%** | **UNKNOWN** | −6.47% | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** |

*The historical ATH reference prices are **rounded screener readings with unknown exact trade timestamps**, and were not taken at 03:23. Approximate returns above are **only directional proxy comparisons**: (PRE detail quote / rounded historical ATH quote − 1) × 100. They are NOT actual overnight-to-current returns or evidence of executable profit. No synchronized baseline volume exists; **volume change for every ticker is UNKNOWN**.

Individual quote sources:
- SNTI https://stockanalysis.com/stocks/snti/ (06:47 ET PRE)
- MKDW https://stockanalysis.com/stocks/mkdw/ (06:42 ET PRE)
- BRAI https://stockanalysis.com/stocks/brai/ (07:02 ET PRE)
- VNTG https://stockanalysis.com/stocks/vntg/ (05:23 ET PRE; stale)
- TGL https://stockanalysis.com/stocks/tgl/ (06:48 ET PRE)
- Public premarket ranking and **untimed** volume: https://stockanalysis.com/markets/premarket/gainers/

**Status classification (provisional, historical proxy only):** BRAI retained strength above its prior ATH indicative price; SNTI/MKDW/VNTG/TGL were below their prior ATH indicative prices. This is **not** proof of successful/failed first overnight ignition because the first overnight response was never observed. BRAI and SNTI appeared on the public PRE top-20 page; MKDW, VNTG, TGL were absent from the **visible first 20 only**, which is not delisting, disappearance from trading, or proof of zero volume.

## Newly meaningful PRE exceptions, not in the early five

| Symbol | Public PRE quote and source time ET | PRE % vs Oct 26 16:00 close | Untimed public PRE screener volume | Spread | News / status | First actual PRE response |
|---|---|---:|---:|---|---|---|
| **XXII** | **$0.1189 @ 06:55** | **+34.50%** | **111,787,805** | **UNKNOWN** | Original issuer release **Oct 26 07:37 ET** on Pinnacle Pure product expansion; separate Oct 22 10:35 ET preliminary Q3 release. Historical prior vault reported **liquidate-only**, but **current order eligibility UNKNOWN**; verify before any trade. | **UNKNOWN** |
| **TDIC** | **$1.7600 @ 06:54** | **+17.33%** | **3,457,511** | **UNKNOWN** | Fresh Oct 27 issuer catalyst **NOT VERIFIED**; current SEC/dilution status **UNKNOWN**. | **UNKNOWN** |

Sources: https://stockanalysis.com/stocks/xxii/ ; https://stockanalysis.com/stocks/tdic/ ; https://stockanalysis.com/markets/premarket/gainers/ ; original issuer release https://www.globenewswire.com/news-release/2026/10/26/3388008/0/en/22nd-century-expands-the-pinnacle-pure-portfolio-to-6-sku-s-with-addition-of-100-s-and-menthol-varieties.html

**Caution:** Public PRE screener may update after its individual detail pages; its share-volume figures have no per-symbol clock time and cannot be certified as 07:04 ET readings. XXII has extreme prior capital-structure/price dislocation; the current instrument permission and bid/ask remain unverified.

## Catalyst chronology, dilution, first-seen timing

- **BRAI:** Original issuer announcement **Oct 26 09:00 ET** (Force AI / RADIUS CX expansion), before Oct 26 regular and after-hours sessions. Oct 26 ATH indicative ~$2.79, Oct 27 07:02 PRE $3.12. The first responsive trade, causation, and PRE volume acceleration are **UNKNOWN**. https://www.globenewswire.com/news-release/2026/10/26/3388145/0/en/braiin-targets-usd-56-9-billion-cx-software-market-with-agentic-ai-expansion-and-major-upgrade-to-radius-cx-platform.html
- **SNTI:** Earlier merger approval, convertible-note share issuance and authorization for 1:20–1:50 reverse split; exact current dilution status **UNKNOWN**. No fresh Oct 27 issuer catalyst or first responsive trade verified.
- **MKDW:** Earlier up-to-$100m ATM and 30m-share acquisition issuance; **actual current sales UNKNOWN**. No fresh Oct 27 issuer catalyst or first responsive trade verified.
- **VNTG:** No fresh Oct 27 issuer catalyst verified; financing status **UNKNOWN**.
- **TGL:** Prior Oct 23 AI agriculture agreement/8-K and earlier financing arrangements; original SEC acceptance timestamp and current new sales **UNKNOWN**.
- **XXII:** Original issuer announcement **Oct 26 07:37 ET** (product expansion) preceded PRE activity by many hours; first actual price/volume response and causal relationship **UNKNOWN**. Prior Oct 22 earnings news is historical.
- **TDIC:** Current fresh PR/SEC catalyst, first response and dilution status **UNKNOWN**.

**News-first vs move-first:** The existence of a prior press release is not evidence it caused today's move. None of these has tick-level evidence sufficient to compute news-to-first-responsive-trade latency.

## Ranking and falsification findings

1. **BRAI** is the strongest apparent continuation *against the historical ATH proxy* (+11.83%), and its timestamped public PRE quote was +47.17% vs Oct 26 regular close at 07:02. **Actual early-OVN-to-PRE return UNKNOWN.**
2. **SNTI, MKDW, VNTG, TGL** are below rounded prior ATH prices; treat as **provisional faded ATH candidates**, not verified failed OVN ignitions.
3. **XXII and TDIC** emerged in public PRE gainers, but neither was part of the five historical carry-forwards. Exact first appearance, spread and executable risk **UNKNOWN**.
4. **No stock is proven to have disappeared from trading.** Absence from the visible top-20 PRE page is a ranking observation only.
5. **Actual volume acceleration, continuous tick speed, tape buyer aggression, support defense, spread stability, float-adjusted risk and executable entry/exit are UNKNOWN for all.** Do not infer from a single price quote or bar.

## Deduplication, immutable references, and permission

Dedup key for this follow-up: `2026-10-27/PRE/07:04:15_ET/<SYMBOL>`; each symbol's **source trade timestamp** is additionally preserved above. This is a research comparison record, not a synchronized tape snapshot. No original observation is overwritten.

- Early Oct 27 03:23:42 OVN **UNVERIFIED** carry-forward: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-27_032342_ET_overnight_ignition.md
- Oct 26 ~18:31 ATH baseline: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-26_1831_ET_afterhours_catalyst_vault.md
- Methodology: https://github.com/Jpuck412/puck-elite-price-action-v2/blob/main/README.md

**PUCK PERMISSION: NO TRADE VERIFIED — ALL.** Required conditions (speed ↑, volume ↑, spread ↔/↓, buyers controlling tape, defended support, defined executable risk) were not jointly verified for any candidate. **No orders placed.** Webull needs interactive authorization before a true synchronized early-versus-current comparison can be produced.