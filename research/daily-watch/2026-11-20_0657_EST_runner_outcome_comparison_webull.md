# Runner Outcome Comparison — 2026-11-20 06:57 EST

**Research only. NO TRADE APPROVED.** Original observation: 2026-11-20 ~03:24 EST, connected Webull OVN session, archived at https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-20_0324_EST_overnight_ignition_webull.md . Follow-up: 2026-11-20 ~06:57 EST, connected Webull PRE_MARKET snapshots, L1 quote observations and PRE_MARKET ranking. Original file not modified. Distinct session volumes: overnight cumulative (ovn_volume) and premarket cumulative (extend_hour_volume). PRE prices are compared to early OVN observations, not claimed executable returns. Source: connected Webull get_stock_snapshot, get_gainers_losers and get_stock_quotes.

## Original top five outcomes
|Symbol|03:24 OVN price|06:57 PRE price|Change from early|03:24 OVN shares|Later OVN shares|OVN delta shares|06:57 PRE shares|PRE bid / ask|PRE spread/mid|Outcome|
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
|MEDS|1.1500|1.0502|-8.68%|1,180,312|1,359,121|+178,809|4,283,019|1.05 / 1.06|0.95%|Deterioration|
|VIVS|0.3493|0.3103|-11.17%|6,904,109|7,297,826|+393,717|15,389,630|0.3091 / 0.3230|4.40%|Deterioration, widened spread|
|RAYA|0.7361|0.7366|+0.07%|1,572,171|1,714,490|+142,319|13,074,232|0.7339 / 0.7500|2.17%|Approximately flat, strong PRE participation|
|CHSN|0.1059|0.0966|-8.78%|9,211,672|9,642,351|+430,679|21,730,673|0.0966 / 0.1047|8.05%|Deterioration despite high PRE volume|
|GMM|1.8600|1.6800|-9.68%|302,508|335,332|+32,824|363,400|1.68 / 1.70|1.18%|Deterioration|

## Original exceptions and controls rechecked
|Symbol|03:24 OVN|06:57 PRE|Price delta|Early OVN shares|Later OVN shares|PRE shares|PRE spread/mid|
|---|---:|---:|---:|---:|---:|---:|---:|
|CIGL|0.2050|0.1791|-12.63%|15,578|17,124|1,420,959|10.78%|
|INLF|0.2562|0.2489|-2.85%|278,193|305,826|115,587|2.39%|
|LGHL|0.9589|0.7800|-18.66%|61,207|61,699|35,269|21.77%|
|INHD|2.7100|2.4244|-10.54%|55,093|57,683|119,800|8.91%|
|SPRC|0.3018|0.2560|-15.18%|230,185|237,136|245,832|5.29%|
|AKAN|3.3600|4.6287|+37.76%|77,501|79,441|1,776,245|0.43%|
|FGI|5.8500|5.1800|-11.45%|5,131|5,219|5,113|10.45%|

AKAN is the standout positive reversal since 03:24; however displayed best bid was only 2 shares at one 06:57 quote. RAYA approximately flat despite large PRE volume. PRE volume is a distinct session, **not** an increment to OVN volume; overnight cumulative increases do **not** prove acceleration. No actual first ignition time or buyer-controlled tape verified.

## New PRE leaderboard candidates absent from early top five
|Symbol|~06:57 PRE price|PRE change vs prior close|PRE shares|PRE L1 bid/ask|Spread/mid|Early baseline|
|---|---:|---:|---:|---|---:|---|
|NXAT|0.3873|approximately +73%|14,595,174|0.3700 / 0.3983|7.37%|UNKNOWN; not in early tracked list|
|LABT|0.2679|approximately +26%|3,030,231|0.2639 / 0.2679|1.50%|UNKNOWN|
|NIVF|0.0413|+18.0%|68,595,351|0.0399 / 0.0420|5.13%|UNKNOWN|

NXAT's PRE percentage comes from contemporaneous leaderboard (~+73.36%) and can fluctuate; latest trade around 06:57 shows 0.3873. These are later prominent names, **not** proven post-04:00 ignitions. NXAT OVN last 0.249 with 55,822 OVN shares, but no 03:24 observation, so no early-to-current return is computed. LABT OVN last 0.2161, 2,355 OVN shares. NIVF OVN last 0.0412, 11,068,102 OVN shares. PRE ranking includes thin-volume outliers (e.g. REBN 5 shares), excluded from meaningful selection.

## Timing, news and permission
- Original VIVS primary issuer news published **Nov 19 08:05 EST**, seven-figure pharma agreement; https://www.globenewswire.com/news-release/2026/11/19/3406540/37000/en/vivosim-labs-signs-seven-figure-agreement-with-a-top-10-global-pharmaceutical-company-expects-to-exceed-its-500-revenue-growth-guidance-for-fiscal-2027.html . First responsive trade **UNKNOWN**.
- INHD earlier SEC 8-K Nov 18 ~16:10 EST: https://www.sec.gov/Archives/edgar/data/1961847/000149315226053065/form8-k.htm . First responsive trade **UNKNOWN**.
- INLF original Nov 18 08:00 EST robotics announcement https://www.globenewswire.com/news-release/2026/11/18/3405585/0/en/inlif-inlf-advances-commercialization-of-its-next-generation-six-axis-industrial-robots-securing-more-than-us-10-million-in-partner-purchase-and-sales-agreements.html . First responsive trade **UNKNOWN**.
- Other original first-seen news, fresh SEC financing/dilution clearance, catalyst-response latency: **UNKNOWN**. No new original PR/SEC acceptance-time verification in this follow-up.
- Exact individual quote timestamps available from connected Webull; follow-up snapshots were taken around **06:57:19–06:57:35 EST**. Some L1 quotes were older than last trades, notably LGHL (quote ~06:53:50), FGI (~06:54:03), SPRC (~06:54:16), INLF (~06:50:59), INHD (~06:56:33), VIVS (~06:56:36). Do not treat as synchronized execution quotes.
- Original leaderboard disappearances: MEDS and RAYA remain among PRE top three, while VIVS, CHSN and GMM absent from retrieved top-30 PRE gainers (absence from ranking only, **not** disappearance from trading). AKAN newly prominent at +34.95% versus regular close, while NXAT leads PRE ranking. The comparison's +37.76% AKAN is **relative to 03:24 OVN price**.
- Observed declines do not prove false ignition; false ignition **UNVERIFIED** without tick sequence. Defended support, price-speed trend, interval volume acceleration, buyer control, current spread stability, risk invalidation **UNKNOWN**. A single L1 quote does not prove executable liquidity.
- Dedup key **2026-11-20 + symbol + 06:57 EST + PRE**. Compared against original 03:24 file and Nov 19 AH archive; no original records overwritten.

**PUCK PERMISSION: NO TRADE APPROVED. NO PROOF = NO TRADE.**
