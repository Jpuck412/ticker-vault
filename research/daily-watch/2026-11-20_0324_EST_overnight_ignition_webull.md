# Overnight Ignition Vault — 2026-11-20 ~03:24 EST

Research-only, Webull US_STOCK overnight snapshots, captured during the 03:23–03:25 EST window on Friday November 20, 2026. Source: connected Webull get_stock_snapshot with overnight_required=true. Snapshot times are approximate; individual source timestamps below are authoritative. OVN percent changes are against Nov 19 regular-session closing price, NOT first ignition or first-observation return. No claim of market-wide exhaustive ranking. Webull PRE_MARKET ranking returned values inconsistent with current overnight snapshot (e.g. VIVS $0.1947 while OVN $0.3472), so the ranking is considered prior-session/stale and NOT used for selection. PRE session is not yet active at 03:24 EST.

## Five selected meaningful overnight candidates

|Symbol|OVN last USD|OVN change vs RTH close|OVN cumulative shares|OVN bid / ask|Spread / mid|Last OVN trade ET (MM/DD HH:mm:ss)|OVN quote ET (MM/DD HH:mm:ss)|
|---|---:|---:|---:|---|---:|---|---|
|MEDS|1.15|58.03%|1180312|1.14 / 1.15|0.87%|11/20, 03:24:20|11/20, 03:24:24|
|VIVS|0.3493|19.83%|6904109|0.3488 / 0.3495|0.20%|11/20, 03:24:27|11/20, 03:24:28|
|RAYA|0.7361|49.92%|1572171|0.7308 / 0.736|0.71%|11/20, 03:24:26|11/20, 03:24:26|
|CHSN|0.1059|7.40%|9211672|0.1058 / 0.1059|0.09%|11/20, 03:24:28|11/20, 03:24:28|
|GMM|1.86|-3.13%|302508|1.85 / 1.86|0.54%|11/20, 03:24:24|11/20, 03:24:24|

Selection balances overnight gain, participation, quote quality and control examples. MEDS/VIVS/RAYA are major continuation candidates from Nov 19 AH; CHSN has unusually large overnight volume but weak absolute price and past runner/failure history; GMM has meaningful participation but negative OVN change. None is a verified first ignition. CHSN's low-priced 9.18M-share activity is a special control, not automatically a buy candidate.

## Additional meaningful exceptions and controls

|Symbol|OVN last USD|OVN change vs RTH close|OVN cumulative shares|OVN bid / ask|Spread / mid|Last OVN trade ET|OVN quote ET|
|---|---:|---:|---:|---|---:|---|---|
|CIGL|0.205|17.68%|15578|0.205 / 0.23|11.49%|11/20, 03:23:24|11/20, 03:23:24|
|INLF|0.2562|-8.83%|278193|0.2563 / 0.26|1.43%|11/20, 03:19:07|11/20, 03:23:45|
|LGHL|0.9589|11.63%|61207|0.9589 / 0.9589|0.00%|11/20, 03:23:40|11/20, 03:24:21|
|INHD|2.71|-3.90%|55093|2.70 / 2.71|0.37%|11/20, 03:24:15|11/20, 03:24:15|
|SPRC|0.3018|0.60%|230185|0.302 / 0.3019|UNKNOWN (crossed/invalid)|11/20, 03:24:05|11/20, 03:23:23|
|AKAN|3.36|-2.04%|77501|3.36 / 3.37|0.30%|11/20, 03:24:18|11/20, 03:24:18|
|FGI|5.85|11.22%|5131|5.69 / 5.85|2.77%|11/20, 03:20:40|11/20, 03:20:40|

SPRC has a crossed L1 quote in source data (bid > ask): spread INVALID, do not calculate negative spread or claim tight liquidity. LGHL and CIGL have wide spreads. INLF and AKAN negative OVN responses provide deterioration controls. FGI only 5,131 overnight shares. One snapshot cannot prove speed, volume acceleration, spread trend, buyer control, support or first ignition.

## Catalyst / SEC / dilution source discipline

- VIVS original issuer release **2026-11-19 08:05 EST**: seven-figure pharma testing agreement, updated guidance expectations; **prior morning news, NOT fresh overnight catalyst**. Original https://www.globenewswire.com/news-release/2026/11/19/3406540/37000/en/vivosim-labs-signs-seven-figure-agreement-with-a-top-10-global-pharmaceutical-company-expects-to-exceed-its-500-revenue-growth-guidance-for-fiscal-2027.html . First price/volume response after original publication UNKNOWN.
- MEDS/RAYA/CIGL/FGI: no verified fresh issuer release or SEC filing acceptance time in available check. This is NOT evidence no news exists.
- INHD previous original SEC 8-K accepted **2026-11-18 ~16:10 EST**, redomiciliation merger, not cash acquisition: https://www.sec.gov/Archives/edgar/data/1961847/000149315226053065/form8-k.htm . This is prior news, not newly verified Nov 20 catalyst.
- INLF original Nov 18 08:00 EST robotics announcement: https://www.globenewswire.com/news-release/2026/11/18/3405585/0/en/inlif-inlf-advances-commercialization-of-its-next-generation-six-axis-industrial-robots-securing-more-than-us-10-million-in-partner-purchase-and-sales-agreements.html . Historical financing/reverse-split risk; current dilution availability UNKNOWN.
- SPRC historical F-3/warrant risk noted in earlier vault, current effective financing capacity UNKNOWN.
- For all other symbols, original PR publication/SEC acceptance timestamps, current S-3/F-3/424B/ATM/equity line, float changes, and dilution clearance UNKNOWN. No false assurance of SEC clearance. Fresh 2026-11-20 first-seen catalyst timing UNKNOWN; first responsive trade UNKNOWN. No news-without-move case established. Observed moves without VERIFIED fresh overnight primary news do not mean news is absent.

## Prior archive comparison and dedup

Reviewed 2026-11-19 ~18:30 AH record: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-19_1830_EST_afterhours_catalyst_vault_webull.md and Nov 19 03:23 OVN archive: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-19_0323_EST_overnight_ignition_webull.md . MEDS/VIVS/RAYA/CIGL/FGI recur from Nov 19 AH; GMM/INLF/INHD/SPRC/AKAN recur from prior vaults. Distinguish repeated observations from new first ignitions. Puck Elite V2 README https://github.com/Jpuck412/puck-elite-price-action-v2/blob/main/README.md requires pressure, support, risk and source evidence. Unique observation key **2026-11-20 + symbol + ~03:24 EST + OVN**; no prior observations overwritten.

## PUCK permission / explicit unknowns

Price-speed increase UNKNOWN; interval volume acceleration UNKNOWN; buyer-controlled tape UNKNOWN; defended support UNKNOWN; spread stability UNKNOWN; original first ignition UNKNOWN; risk-defined invalidation UNKNOWN. Single L1 quote and cumulative session volume are NOT tape. PRE session data for today UNKNOWN / not yet started at capture. **NO TRADE APPROVED. NO PROOF = NO TRADE.**
