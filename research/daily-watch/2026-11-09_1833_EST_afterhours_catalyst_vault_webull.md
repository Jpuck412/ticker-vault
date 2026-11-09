# After-Hours Catalyst Vault — 2026-11-09 18:33 EST

## Method / provenance
Webull connected AFTER_MARKET gainers/losers, extended-hours snapshots and single Level-1 quotes fetched around 18:33 EST on Monday November 9 2026. Ranking prices and percent gains are leaderboard observations; snapshot last prices, extended-hour volume and quote times are separate fields and not necessarily synchronized. All prices USD. Webull search_news queried for TANH CODX CISS SKYE WFF with Nov 9 date filter; returned empty arrays. This is NOT proof that no news exists. Earlier archive read: research/daily-watch/2026-11-06_1831_EST_afterhours_catalyst_vault_webull.md (preserved). First meaningful response and first trade after catalyst cannot be determined without time-and-sales/tick data.

## Top five meaningful candidates
| Symbol | Ranking AH price / gain | Snapshot AH last | AH volume (snapshot) | Bid / ask (L1) | Approx spread / midpoint | Fresh issuer catalyst >=16:00 ET | First meaningful response | Verdict |
|---|---|---|---:|---|---:|---|---|---|
| TANH | $33.52 / +74.25% | $33.52 | 485,106 | 33.52 / 33.78 | 0.77% | UNKNOWN | UNKNOWN | NO TRADE: highly volatile, tiny ask size 1 |
| CODX | $0.4724 / +47.81% | $0.4778 | 1,560,721 | 0.4700 / 0.4787 | 1.83% | UNKNOWN | UNKNOWN | NO TRADE: buyer control/speed unverified; historic shelf risk |
| CISS | $2.53 / +44.57% | $2.4699 | 1,032,191 | 2.40 / 2.60 (separate L1 query) | 8.00% | UNKNOWN | UNKNOWN | NO TRADE: wide and quote discrepancy |
| SKYE | $0.9389 / +36.07% | $0.9389 | 5,521 | 0.9389 / 0.9900 (separate L1) | 5.30% | UNKNOWN | UNKNOWN | NO TRADE: thin AH volume and stale quote |
| WFF | $1.3399 / +23.18% | $1.34 | 2,173,808 | 1.33 / 1.35 | 1.49% | UNKNOWN | UNKNOWN | NO TRADE: no validated speed/buyer control |

Volume is Webull extend_hour_volume, not the leaderboard's daily 'volume'. Snapshot last and quote may not match. No spread TREND can be deduced from one quote.

## Additional exceptions / negative controls
- MVST: leaderboard $0.30 / -51.42%, reported day volume 8,868,819; L1 $0.290/$0.305 = 5.04% spread. Catalyst UNKNOWN; first sell response UNKNOWN. NO TRADE.
- TGE: leaderboard $0.2901 / -19.42%, reported day volume 30,074,785; extended-hours snapshot volume 290,688; L1 $0.290/$0.3255 = 11.54% spread. Was +61.18% on Nov 6 after-hours, but this is a DIFFERENT session and cannot establish a failed first ignition. NO TRADE.
- BRBI: +29.82% leaderboard but only 276 reported shares in ranking; excluded from top five for extremely thin participation.
- SFWL: +22.59% leaderboard, 1,162 reported shares; excluded for thin participation.
- CODX financing: historical May 12 2026 S-3 and July 27 2026 424B5 shelf/prospectus described by secondary filing tracker (https://filingfirehose.com/sec/CODX). Direct EDGAR verification and current ATM sales UNKNOWN. The historical filings are NOT fresh Nov 9 catalysts.

## Catalyst / timing investigation
Webull Nov 9 keyword news results for five primary symbols were empty. Broader web search did not independently verify a fresh post-16:00 issuer release for these names. No November 9 original SEC acceptance timestamp verified. Earnings/FDA/clinical/merger/reverse split/ATM/equity-line status for the current session: UNKNOWN unless specifically noted as historical. First-seen catalyst publication timestamp UNKNOWN for all primary names; first meaningful price/volume response UNKNOWN; news-to-move latency UNKNOWN.
- **Moves with no verified fresh news:** TANH, CODX, CISS, SKYE, WFF (not claims of news absence).
- **News with no verified move:** NONE ESTABLISHED.
- **Weak/negative move controls:** MVST, TGE.
- SEC source for follow-up: https://www.sec.gov/edgar/search/
- Historical CODX filings secondary tracker: https://filingfirehose.com/sec/CODX

## Evidence / permission gate
Price speed trend UNKNOWN; volume acceleration UNKNOWN; aggressive buyer tape UNKNOWN; defended support UNKNOWN; spread trend UNKNOWN; defined executable risk UNKNOWN; initial ignition timestamp UNKNOWN. Single Level-1 spreads are observed but do not establish stable executable liquidity. Ranking-vs-snapshot differences must not be treated as sequential trades. No inference from candles. NO PROOF = NO TRADE. No orders placed.
