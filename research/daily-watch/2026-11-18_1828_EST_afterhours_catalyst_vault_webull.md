# After-Hours Catalyst Vault — 2026-11-18 ~18:28 EST

**Research only.** Capture window starts 16:00 EST. Connected Webull AFTER_MARKET gainers/losers, extended-hours stock snapshots and Level-1 quotes collected ~18:28 EST. Ranking % is relative to regular close, NOT first ignition. Webull volume ranking field is regular-session volume; below use **extend_hour_volume** only. Snapshots and quotes not perfectly synchronized. All times America/New_York. Do not infer first responsive trade from OHLC candles.

## Five selected AH leaders (ranking order; not trade-qualified)

|Symbol|AH last $|AH change vs close|AH-only volume|Bid $|Ask $|L1 spread / midpoint|Evidence / caveat|
|---|---:|---:|---:|---:|---:|---:|---|
|INHD|3.7394|+62.58%|2,886,757|3.73|3.75|0.53%|Best bid only 10 shares; fresh issuer catalyst UNKNOWN|
|SPRC|0.3535|+30.88%|424,042|0.3400|0.3594|5.55%|Historical warrant inducement and Nov 9 F-3; financing risk|
|JYD|0.9999|+18.36%|107|0.7874|1.0800|31.34%|Quote stale vs snapshot; illiquid ranking control|
|XCH|3.9300|+17.66%|163|3.14|3.89|21.34%|Quote stale, negligible participation|
|INLF|0.2692|+18.43%|2,524,190|0.269|0.270|0.37%|**Earlier 08:00 ET issuer PR, not a new AH catalyst**|

Note: INLF ranking was +17.42% at initial leaderboard pull and +18.43% in subsequent live snapshot; two distinct observations, not synchronized. JYD and XCH remain in top ranked candidates solely as **illiquidity controls**, not meaningful tradable runners. INLF included as high-participation exceptional candidate instead of lower-liquidity TREO (+15.04%, 851 AH shares; 1.89/2.67 bid/ask, 34.21% spread). Rank order and candidate selection are deliberately separate.

## Downside / failure controls

|Symbol|AH last $|AH %|AH-only volume|Bid / ask|Spread/mid|Interpretation|
|---|---:|---:|---:|---|---:|---|
|FCHL|0.3514|-37.82%|2,125,008|0.3455 / 0.3700|6.85%|Sharp downside; first sell impulse UNKNOWN|
|MRM|0.2002|-24.17%|UNKNOWN|0.184 / 0.2269|20.88%|Very wide spread|
|INVZ|0.1200|-17.07%|51,525|0.1189 / 0.1500|23.14%|Illiquid downside quote|

## Original catalyst / SEC chronology and dilution

- **INLF:** issuer original GlobeNewswire press release **2026-11-18 08:00 EST**, six-axis robotics products and purchase/sales agreements with 10 partners, expected aggregate value >$10m. This predates 16:00 and is NOT a verified after-hours first ignition. https://www.globenewswire.com/news-release/2026/11/18/3405585/0/en/inlif-inlf-advances-commercialization-of-its-next-generation-six-axis-industrial-robots-securing-more-than-us-10-million-in-partner-purchase-and-sales-agreements.html
- **INLF dilution precedent:** October 19 pricing and October 20 closing of $3.75m registered direct offering; June 30 1-for-200 share combination announcement. Current shelf/ATM/equity line status UNKNOWN. https://marketchameleon.com/Overview/INLF/PressReleases/
- **SPRC:** prior Oct 26 warrant exercise inducement reported by Webull/Benzinga at **16:15:24 UTC = 12:15:24 EDT**, not a fresh Nov 18 AH catalyst. Nov 9 F-3 and Nov 16 6-K listed in filing index; original SEC acceptance timestamps and current effective dilution capacity UNKNOWN. https://www.aries.com/us/en/stocks/SPRC/filings
- **INHD, JYD, XCH, FCHL, MRM, INVZ:** original post-16:00 issuer PR/8-K/6-K/424B/S-3/F-3/ATM/equity-line, merger, split, FDA, clinical or earnings catalysts NOT VERIFIED. Absence of verified source does not prove absence of news. Exact SEC acceptance timestamps UNKNOWN.
- **News with no move:** no verified instance in checked universe. **Moves with no verified fresh post-16:00 news:** INHD, SPRC, JYD, XCH, FCHL and other controls; INLF has a verified **morning** catalyst only.

## Response timing and permission

First meaningful price/volume response for **all symbols UNKNOWN**. Catalyst-to-response latency UNKNOWN. Tick-by-tick response sequence not established. Speed acceleration UNKNOWN; incremental volume acceleration UNKNOWN; buyer control UNKNOWN; defended support UNKNOWN; spread trend UNKNOWN; executable defined risk UNKNOWN. Quoted spreads are single L1 samples, not evidence of stable executable liquidity. No false-ignition claim based on candles.

## Comparison with existing vault

Compared with 2026-11-17 18:29 EST after-hours record (AZI, CRIS, ABTS, BMGL, AKAN, downside SHFS/IRIX/BAER) at https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-17_1829_EST_afterhours_catalyst_vault_webull.md . Tonight's primary selection differs from yesterday's five; this does not prove yesterday's leaders disappeared from the full market without a matched recheck. Existing records unchanged.

## Provenance and gaps

Webull get_gainers_losers AFTER_MARKET DESC/ASC, get_stock_snapshot extend_hour_required=true, get_stock_quotes depth=1, get_stock_news (INHD, SPRC, INLF, JYD, TREO); public GlobeNewswire issuer PR and filing indices. Individual Webull quote timestamps stored as Unix milliseconds: INHD 1795044520957; SPRC 1795044522076; JYD 1795043921766; XCH snapshot quote 1795043650304; INLF 1795044517553; FCHL 1795044516877; MRM 1795044231059; INVZ 1795044105653. Trade timestamps and full tape unavailable for causality. SEC original acceptance times UNKNOWN; no clean-float assertion. **NO TRADE APPROVED — NO PROOF = NO TRADE.**
