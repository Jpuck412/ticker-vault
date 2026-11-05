# Webull Reconnected Premarket Follow-up — 2026-11-05 04:11–04:12 EST

**Research only — no order placed.** This is a new, later Webull observation. It does not overwrite the earlier 03:20 EST unverified placeholder:
[2026-11-05 03:20 EST overnight attempt](https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-05_0320_EST_overnight_ignition_unverified.md).

## Source, timestamp and session integrity

- Connected Webull ranking, extended/overnight snapshots, minute bars, quotes/depth, ticks and news calls succeeded after reconnection.
- Ranking/snapshot collection: approximately **04:11 EST**; final quote/depth/tick samples: approximately **04:12 EST** (Thursday, Nov 5; EST = UTC−05:00).
- Ranked list is Webull US-stock **PRE_MARKET gainers** at retrieval. Rankings are not a historical scan before 04:00. This does **not** establish first ignition time.
- Percentages and prices from separate ranking/snapshot fields can differ as quotes move. Session volume fields may be cumulative or extended-hours aggregate; use minute-bar volume for interval evidence and do not relabel totals as PRE-only.
- Four of the five current ranked names (AEHL, ZNB, PLCE, ARQ) also appeared in the Nov 4 historical after-hours carry-forward list. That overlap is a watchlist persistence observation, not proof of fresh catalyst or continued trade quality.
- Dedup key: `2026-11-05|PRE|04:11_EST|<symbol>`. The 03:20 record stays immutable.

## Five leading Webull PRE_MARKET gainers

| Rank | Symbol | Webull rank price / gain | Session data visible in snapshot | Current quote / spread | Research notes |
|---:|---|---:|---|---|---|
| 1 | **ZNB** | $1.3787 / +121.66% | Snapshot extended-hours last $1.3683, +119.98%; OVN last $1.10, high $1.10, low $0.9146, volume 1,815,093. Extended-hours volume field 2,559,771; precise PRE-only scope UNKNOWN. | At ~04:11:27: $1.38 bid / $1.39 ask; $0.01 (~0.72%) spread. Depth showed 850 at best bid vs 4,094 at best ask; stacked asks 3,303 at $1.40. | 5.00M total / 5.00M outstanding shares shown by snapshot. Recent prints included repeated buyer-tagged trades at $1.39, but also sell/neutral prints; buyer control not established. No verified fresh catalyst found in returned news; targeted SEC dilution check NOT completed. |
| 2 | **JDZG** | $0.4621 / +52.65% | Extended last $0.4574, +51.66%; OVN last $0.3625, high $0.3625, low $0.302, volume 150,240. Extended-hours volume field 2,071,303; precise PRE-only scope UNKNOWN. | At ~04:11:25: $0.451 bid / $0.4591 ask; $0.0081 (~1.78%) spread. Depth 610 at best bid vs 100 at best ask; 27,594 shares offered at $0.4657. | 5.43M total / 5.13M outstanding shares shown. M1 PRE volumes: 09:08 UTC 183,261; 09:09 156,512; 09:10 259,189; 09:11 29,422. 09:10 range $0.4379–$0.4762; 09:11 close $0.4591. Recent prints were mixed, with many neutral/seller-classified prints. News returned older negative earnings/mover stories (Nov 2–3), not a verified fresh Nov 5 catalyst. |
| 3 | **AEHL** | $9.42 / +50.24% | Snapshot extended last $9.53, +51.99%; OVN last $9.66, high $11.38, low $9.26, volume 153,005. Extended-hours volume field 83,589; precise PRE-only scope UNKNOWN. | At ~04:11:05: $9.38 bid / $9.57 ask; $0.19 (~2.0%) spread. | Price is outside preferred low-price focus. Historical Webull news referenced an October ATM agreement allowing up to $100M in securities; current capacity/use not checked in SEC filings. |
| 4 | **PLCE** | $0.3431 / +42.37% | Snapshot extended last $0.3375, +40.04%; OVN last $0.3336, high $0.3911, low $0.3245, volume 3,528,588. Extended-hours volume field 1,412,183; precise PRE-only scope UNKNOWN. | Quote/depth drifted during the check. At ~04:11:48: $0.3278 bid / $0.3294 ask; $0.0016 (~0.49%) spread. Depth 1,055 at best bid vs 2,302 at best ask; 5,000 bid at $0.3236. | M1 PRE: 09:07 UTC volume 292,051; 09:08 94,918; 09:09 27,748; 09:10 20,395; 09:11 1,015. Price faded from $0.3648 high at 09:04 to $0.3375 at 09:11 and then latest ticks near $0.328. Prior PRE low $0.3218; support not confirmed. Webull news included Nov 2 Bloomberg report on a possible liquidation option in bankruptcy. Severe business/financing risk; current SEC status not checked. |
| 5 | **ARQ** | $2.3212 / +25.88% | Snapshot extended last $2.3209, +25.45%; OVN last $2.54, high $2.69, low $2.15, volume 250,312. Extended-hours volume field 448,059; precise PRE-only scope UNKNOWN. | At ~04:11:01: $2.31 bid / $2.33 ask; $0.02 (~0.86%) spread. | Above preferred sub-$2 range. Webull news returned no symbol-specific items. No fresh catalyst, tape-control or SEC dilution clearance established. |

**Removed from the prior carry-forward five:** JLHL was not in the current top-30 PRE_MARKET gainers returned. Snapshot near 04:12: extended last $7.8277 (+10.25% vs snapshot close); OVN last $7.53, high $9.52, low $7.25, volume 174,306; current $7.84 bid / $8.20 ask (~4.55% spread). No further tape or fresh catalyst verification.

## Intraday evidence and interpretation

### ZNB — WAIT / research watch only
- Current L1 spread was relatively tight, and recent buyer-tagged prints occurred at the ask. However, displayed sell liquidity above the quote was substantially larger than best bid liquidity, the market had already made a very large move, and no completed support/reclaim confirmation or fresh catalyst was verified.
- Visible 1-minute support from a current-time chart was not established. Do not infer support from the overnight low alone.
- **Upgrade evidence required:** fresh synchronized 1-minute volume expansion, repeated ask lifts with buyer control, a defined reclaim/hold level and a quote that remains tight. Failed hold of the current base means invalidation; exact base remains UNKNOWN.

### JDZG — NO / skip for this snapshot
- A large 09:10 UTC minute volume burst was followed by a sharp decline in interval volume. The current spread was wider than ZNB's and displayed a sizable ask at $0.4657. The sample tape was mixed/mostly neutral, not clear buyer control.
- Recent Webull news was stale relative to this check and negative in tone. A fresh catalyst and dilution check are absent.
- **Invalidation:** failure to hold the 09:10 low of $0.4379. This is a chart reference only, not a validated support level or recommendation.

### PLCE — NO / momentum deteriorating
- Price retraced from the 09:04 UTC high of $0.3648 to about $0.328 during the final quote/tick sample. Latest ticks included repeated prints at $0.3281–$0.3294, with sell/neutral prints after the earlier buying burst. The quoted bid/ask was tight, but price and volume behavior did not show a clean renewed ignition.
- The Nov 2 liquidation-option report is material negative context. A low spread cannot offset weakening price action or issuer distress.
- **Invalidation/watch line:** prior PRE low $0.3218; it is a historical low, not confirmed support. No entry without a new reclaim, speed/volume expansion and buyer control.

### AEHL / ARQ — not entry-cleared
- Ranking gain alone is insufficient. AEHL had a ~2% spread and known historical ATM overhang; ARQ is above the user's preferred price band and lacks tick/volume-acceleration verification.
- A new catalyst, tape control, support and dilution clearance were not established for either.

## Puck permission result

**No candidate passes the entry test at this observation. No trade is approved.** Rank data and short tick samples show activity, but a completed one-candle confirmation, durable speed/volume acceleration, buyer control, defended support, defined risk and current dilution clearance are not all established. No order actions were taken.

## Research takeaways to retain

1. Record first available Webull check at **04:11 EST**, after the 04:00 premarket opening; do not label it pre-4AM ignition.
2. Four carry-forward after-hours names remained among the current PRE leaders, but PLCE's live price weakened sharply and prior persistence did not guarantee continuation.
3. ZNB showed large overnight volume and a tight spread but a visible ask wall; separate the strong percentage gain from order-book quality.
4. JDZG's concentrated minute-volume burst and immediate fade are a useful failed/unstable ignition sample.
5. Keep overnight, premarket, and extended-hours aggregate volumes in distinct fields. Current Webull snapshot volume scope is not always explicit.
6. No candidate was granted a YES; preserve UNKNOWN fields as unknown rather than filling them from candles or stale news.
