# Runner Outcome Comparison — Friday 2026-10-23, 07:02:23 ET

**Status:** Research only — **NO TRADE VERIFIED**. **Original observation:** 03:20:21 ET, Webull `OVN` session (before 04:00). **Follow-up:** 07:02:23 ET, Webull `PRE` session. Eastern Daylight Time (UTC−04:00). The original archive was fetched from connected GitHub and is **unchanged**:
https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-23_032021_ET_overnight_ignition.md

**Sources:** connected Webull US_STOCK snapshot (including `extend_hour_*` PRE and `ovn_*` OVN), Webull PRE gainers ranking, PRE M1 bars (non-delayed, 06:40–06:59 ET volume windows), 200 sampled PRE trades per original candidate plus XXII; original issuer PRs and SEC sources linked below. **Session discipline:** the 03:20 OVN shares and 07:02 PRE shares are different cumulative session counters and must **not** be subtracted from one another. Final OVN volumes are shown separately for 03:20→04:00 same-session deltas. Prices may be compared across sessions.

## Immutable original-five outcome: 03:20:21 OVN → 07:02:23 PRE

|Symbol|03:20 OVN price|07:02 PRE price|Price change vs early|03:20 OVN shares|Final OVN shares (04:00 reset)|Additional OVN shares after 03:20|07:02 PRE shares (separate session)|PRE bid/ask|Instant PRE spread|PRE quote ET / age at 07:02:23|PRE last trade age|06:50–06:59 / 06:40–06:49 M1 shares (ratio)|Outcome|
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---:|---|---|
|LUCD|$0.4525|$0.4483|**−0.93%**|2,766,981|3,256,605|+489,624|9,860,067|$0.4400 / $0.4766|**7.99%**|07:02:22.497 / 1s|<1s|839,947 / 1,235,425 = **0.68×**|Price near early; wide spread, volume slowing|
|GPUS|$0.1453|$0.1469|**+1.10%**|13,637,252|14,636,785|+999,533|27,399,627|$0.1460 / $0.1502|**2.84%**|07:02:23.226 / <1s|<1s|654,559 / 1,419,739 = **0.46×**|Modest price continuation; volume slowing|
|CJMB|$0.5805|$0.5642|**−2.81%**|1,274,939|1,322,682|+47,743|4,267,090|$0.5609 / $0.5783|**3.05%**|07:00:07.651 / **136s stale**|<1s|28,130 / 57,907 = **0.49×**|Fade; quote unreliable|
|STAK|$1.7700|$1.9690|**+11.24%**|172,425|178,600|+6,175|789,677|$1.9600 / $1.9800|**1.02%**|07:02:23.178 / <1s|<1s|48,474 / 38,089 = **1.27×**|Strongest original-five price continuation|
|SDEV|$1.1600|$1.1100|**−4.31%**|852,254|899,323|+47,069|521,024|$1.1000 / $1.1200|**1.80%**|07:02:23.019 / <1s|~1s|13,745 / 5,356 = **2.57×**|Fade despite modest absolute volume acceleration|

**Spread formula:** `200 × (ask−bid)/(ask+bid)`. Instantaneous L1 only; NOT evidence spread is stable. Quotes are asynchronous. M1 comparison uses **completed** clock minutes 06:50–06:59 ET versus 06:40–06:49 ET; missing minute bars count as zero. The in-progress 07:02 bar is excluded. These are **historical volume measurements, not verified real-time tape speed or buyer control**.

**Data-quality caution:** Webull's `ovn_price` values returned after the 04:00 transition sometimes differ from the last 03:20 OVN snapshot and are NOT used as substitutes for the original observation. Final OVN cumulative volumes were retrieved separately and can be compared with original same-session OVN volumes, but no conclusion about trade direction follows.

## New meaningful premarket leader (not in original five)

|Symbol|First snapshot in this record|PRE price|PRE change vs Oct 22 16:00 close|PRE shares|PRE bid/ask|Spread|Quote ET / age|06:50–06:59 / 06:40–06:49 volume|Origin status|
|---|---|---:|---:|---:|---|---:|---|---|---|
|**XXII**|**07:02:23 ET PRE**|**$0.4482**|**+107.79%** vs $0.2157|**35,447,161**|$0.4345 / $0.4700|**7.85%**|07:01:56.572 / **27s**|974,987 / 1,280,414 = **0.76×**|New PRE leader; not in 03:20 selected list; exact first ignition UNKNOWN|

XXII had a Webull reported final OVN volume of **1,025,505**, but **no XXII 03:20 original price was captured**; its early-to-current price return is **UNKNOWN** and must not be invented. In a separate historical scan restricted to today's 04:00–07:02 PRE M1 bars, the **first returned qualifying bar** (close >=10% above Oct 22 close and >=25,000 shares over trailing five clock minutes) was **04:01 ET** (close $0.2426; trailing five-minute shares 111,175). This is a **retrospective threshold**, NOT verified first ignition or first responsive tick. Prior-day issuer PR was **Oct 22 10:35 AM ET**, reporting preliminary unaudited Q3 revenue +66% to $4.8m and positive gross profit. Source: https://www.stocktitan.net/news/XXII/22nd-century-group-preliminarily-reports-third-quarter-financial-r164qpmae650.html ; Oct 22 8-K indexed under accession 0001493152-26-048034 (exact acceptance timestamp needs SEC primary-index verification). **News-to-first-responsive-trade latency UNKNOWN.** Reported wide spread and quote staleness make it a negative execution-quality control, not an approved trade.

Other premarket-ranking exceptions at the follow-up: **AARD $4.94 (+25.06% vs close, PRE 565,492 shares, 0.40% spread, above preferred $3.99 ceiling)**; **SAIQ $6.7795 (+28.40%, PRE 559,248 shares, 0.15% spread, above ceiling)**. These are not promoted to the original-five set.

## Other early controls

|Symbol|03:20 OVN|07:02 PRE|Price change|PRE shares|PRE spread / quote freshness|Interpretation|
|---|---:|---:|---:|---:|---|---|
|RBNE|$0.2110|$0.2034|**−3.60%**|6,263,731|0.99%; quote ~4s old|Mild fade, 06:50–06:59 M1 volume 0.67× preceding 10m; financing risk persists|
|SHFS|$0.3522|$0.2981|**−15.36%**|7,359,781|5.99%; quote ~32s old|Clear price failure of earlier recovery; M1 volume 0.41×; spread poor|

**Disappearances:** none of the original five disappeared from returned Webull quotes. **Leaderboard displacement:** XXII became the top observed PRE percentage gainer; original five were not all still among top percentage leaders. A quote remaining available is not proof of continued leadership.

## Catalyst timestamps, corrections, and dilution

- **LUCD — original Oct 22 16:20 ET issuer PR**: Medicare reimbursement for EsoGuard plus $15m Series C convertible preferred financing, conversion price $0.3519/common share. First qualifying historical Oct 22 ATH bar **16:22 ET**, two minutes after PR. First responsive trade and causation **UNKNOWN**. Source: https://www.prnewswire.com/news-releases/lucid-diagnostics-begins-receiving-medicare-reimbursement-for-esoguard-and-closes-15-million-financing-302917430.html . Preferred conversion/resale risk persists.
- **GPUS — IMPORTANT corrected fresh news:** **Oct 22 16:15 ET issuer PR** announced **suspension** of the common-stock ATM after approximately **127.2m shares** sold for **$50.6m** gross; the earlier 03:20 record discussed the ATM but had not verified this suspension. Source: https://www.prnewswire.com/news-releases/hyperscale-data-announces-suspension-of-its-at-the-market-offering-302917415.html . **New Oct 23 06:00 ET issuer PR** reaffirmed 2027 revenue guidance of $300m–$350m and adjusted EBITDA $60m–$80m; first responsive trade after 06:00 and causation **UNKNOWN**. Source: https://www.prnewswire.com/news-releases/hyperscale-data-reaffirms-2027-guidance-of-300-million-to-350-million-in-revenue-and-60-million-to-80-million-in-adjusted-ebitda-302917679.html . Suspension does not undo past dilution or prohibit future financing.
- **CJMB — fresh Oct 22/23 issuer PR acceptance UNKNOWN**. Historical ATM/resale exposure noted in early file. New price weakness is observable; news attribution not.
- **STAK — Oct 21 16:20 ET issuer earnings PR**, prior-day 20-F/6-K; exact filing acceptance and current first responsive tick **UNKNOWN**. Source: https://www.prnewswire.com/news-releases/stak-inc-announces-financial-results-for-fiscal-year-2026-302915863.html . No verified fresh Oct 23 catalyst for the current price rise.
- **SDEV — prior Oct 6 S-3/A** covers up to 212,876,259 shares for resale/underlying prefunded warrants, subject to restrictions. Current actual sales **UNKNOWN**. Source: https://www.sec.gov/Archives/edgar/data/1389545/000143774926032232/sdev20261004_s3a.htm . Fresh Oct 23 catalyst UNKNOWN.
- **XXII — Oct 22 10:35 ET preliminary earnings PR** (prior regular session), **not verified new 04:00 catalyst**. First meaningful qualifying bar at 04:01 does not prove the original trade was after 04:00; no causal inference. The issuer stated 3,416,441 common shares outstanding and no warrants outstanding as of Oct 22, per its preliminary release; verify current fully diluted capitalization independently.

## Support, tape, and permission

Webull provided PRE tick samples for the five original candidates and XXII (up to 200 latest trades each); many prints were coded `N`, with some `B`/`S`. The sample is incomplete and aggressor semantics are not independently validated. Therefore **sustained buyer control: UNKNOWN**, **continuous tape speed acceleration: UNKNOWN**, **defended support: UNKNOWN** for all. The M1 bar-volume ratios are directly observed but not tick-speed or buyer-control proofs. L1 bid/ask is instantaneous, not stable-spread evidence. Defined stop distance and acceptable risk per candidate **UNKNOWN**.

**PUCK PERMISSION for LUCD, GPUS, CJMB, STAK, SDEV, XXII and all exceptions: NO TRADE VERIFIED.** Require speed ↑, volume ↑, spread stable/↓, verified buyer control, defended support, defined risk, evidence > prediction. No order was submitted.

## Deduplication, provenance and archive

- Original immutable GitHub source: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-10-23_032021_ET_overnight_ignition.md
- Follow-up unique keys: `2026-10-23/PRE/07:02:23 ET/<SYMBOL>`. The 03:20:21 `OVN` keys remain unchanged.
- New create-only target: `Jpuck412/ticker-vault/research/daily-watch/2026-10-23_070223_ET_premarket_followup.md`. Checked for existing file before creation: **404 / absent**.
- Webull current snapshot observed ~07:02:23 ET; Webull PRE gainers ranking and M1/tick samples; original issuer PRs above.
- This is research from the observed universe, not a certified marketwide exhaustive top-ten. Data may change rapidly after capture.
