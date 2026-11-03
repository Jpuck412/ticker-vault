# Runner Outcome Comparison — 2026-11-03 ~07:05 EST

## Original immutable baseline
Original archive: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-03_0321_EST_overnight_ignition.md
Original research capture: 03:21 EST, Nov 3. **Its prices are actually Nov 2 20:00 EST after-hours close vendor observations**, NOT executed Nov 3 03:21 overnight trades. Thus the differences below are **Nov 2 AH reference -> Nov 3 delayed premarket trade**, NOT 03:21->07:05 returns.

## Source, time, integrity
- Webull stock snapshot and PRE_MARKET ranking attempted; both blocked: "User input required but current turn is running in a non-interactive mode."
- Alpaca connected get_stock_snapshot / get_stock_latest_quote, feed **delayed_sip**, retrieved near 07:05 EST; source exchange timestamps below. Quotes and trades are delayed ~15 minutes or older. https://alpaca.markets/
- GitHub original file fetched directly; separate search of Jpuck412/puck-elite-price-action-v2 for 2026-11-03 returned no matches.
- Dedupe: 2026-11-03|~07:05_EST|PRE_FOLLOWUP_DELAYED_SIP|symbol. Original record untouched.

## Same five and meaningful exceptions
| Symbol | Nov 2 AH baseline | Nov 3 PRE last trade | Historical baseline-to-follow-up change | Delayed bid / ask | Delayed spread | Last trade time EST | Change in comparable session volume |
|---|---:|---:|---:|---|---:|---|---|
| PARA | $2.45 | $1.92 | -21.63% | $1.92 / $1.93 | $0.0100 | 06:50:05 EST | UNKNOWN |
| BLZE | $10.46 | $9.92 | -5.16% | $9.9 / $10.06 | $0.1600 | 06:48:59 EST | UNKNOWN |
| AEHG | $2.66 | $2.56 | -3.76% | $2.56 / $2.58 | $0.0200 | 06:33:08 EST | UNKNOWN |
| GPRO | $1.1 | $1.0199 | -7.28% | $1.01 / $1.02 | $0.0100 | 06:49:28 EST | UNKNOWN |
| BRAI | $2.96 | $2.74 | -7.43% | $2.72 / $2.76 | $0.0400 | 06:49:21 EST | UNKNOWN |
| MERC | $0.29 | $0.251 | -13.45% | $0.251 / $0.2511 | $0.0001 | 06:50:09 EST | UNKNOWN |
| CCTG | $0.42 | $0.2754 | -34.43% | $0.2754 / $0.2785 | $0.0031 | 06:49:30 EST | UNKNOWN |

**Quote timestamps:** PARA 06:50:09, BLZE 06:49:28, AEHG 06:48:59, GPRO 06:50:07, BRAI 06:50:06, MERC 06:50:09, CCTG 06:50:01 EST. AEHG's last trade is 06:33, considerably staler than quote. The listed trade times are NOT snapshot collection times.

**Volume:** Original vendor Nov 2 AH volume: PARA 8.26M, BLZE 6.45M, AEHG 5.03M, GPRO 9.24M, BRAI 3.75M. Alpaca Nov 3 premarket session cumulative volume was NOT provided. Its Nov 2 daily bars (e.g., PARA 8,587,548; BLZE 6,702,729) represent different session conventions and are not comparable to AH-only volume. Latest minute-bar volumes: PARA 4,856 (06:49), BLZE 611 (06:48), AEHG 744 (06:33), GPRO 8,879 (06:49), BRAI 305 (06:49), MERC 334,947 (06:49), CCTG 2,720 (06:49). Minute bars are isolated samples, NOT volume acceleration or comparable session delta.

## Outcome classification
- **Historical AH-to-PRE fade:** PARA, BLZE, AEHG, GPRO, BRAI all below historical AH reference. BLZE remains above Nov 2 regular close ($7.40), despite pullback from $10.46 AH reference.
- **Exceptional fades:** MERC and CCTG also below secondary-vendor Nov 2 AH references; these baselines are less robust, use as controls.
- **Continuation:** no original-five ticker continued above Nov 2 AH baseline in these delayed readings. This does NOT prove failed overnight ignition.
- **Disappearance:** none confirmed. All seven returned delayed trades; no marketwide current leader ranking was accessible, so leaderboard disappearance UNKNOWN.
- **False ignition:** cannot certify; original record had NO tick-verified pre-04:00 ignition.
- **Current marketwide leaders/new meaningful runner:** UNKNOWN due Webull access and lack of authenticated broad premarket screener.

## News, dilution, support and risk
Original archive: BLZE Nov 2 earnings event with original issuer release timestamp UNKNOWN; PARA, AEHG, GPRO, BRAI, MERC, CCTG first-seen issuer news and SEC acceptance timestamps UNKNOWN. No new issuer PR/SEC primary document independently retrieved during this comparison. Do not infer causality or dilution cleanliness. First meaningful trade response to any catalyst UNKNOWN.
- Defended intraday support UNKNOWN (isolated minute bars are not confirmation).
- Delayed quoted spreads are point-in-time only; **spread stability UNKNOWN**. No executable contemporaneous spread.
- Price speed ↑ UNKNOWN; volume acceleration ↑ UNKNOWN; buyer-controlled tape UNKNOWN; defined risk UNKNOWN.
- **NO TRADE VERIFIED. No orders placed.**

## Sources
- GitHub original 03:21 research record linked above.
- Connected Alpaca delayed SIP stock snapshot and quote returned on Nov 3 ~07:05 EST; trade/quote timestamps explicitly above.
- Webull live endpoints failed requiring interactive authorization.
