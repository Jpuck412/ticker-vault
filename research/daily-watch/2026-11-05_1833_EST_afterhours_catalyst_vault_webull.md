# After-Hours Catalyst Vault — 2026-11-05 18:33 EST

## Scope and provenance
- US-listed AFTER_MARKET movers retrieved from connected Webull at ~18:33–18:34 EST Nov 5, 2026. Ranked by Webull AFTER_MARKET change ratio; separately retrieved decliners. Quote timestamps below are from Webull L1 depth; leaderboard snapshot timestamp not supplied.
- IMPORTANT: Webull ranking 'volume' is reported without a clearly specified session boundary. **Do not call it after-hours-only volume or infer acceleration.**
- Prior vault consulted: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-04_1830_EST_afterhours_catalyst_vault.md . Prior AEHL appears again, now as a decliner. Do not conflate sessions.
- Ranking price and L1 bid/ask are not guaranteed to be synchronized; crossed or out-of-market last prices are NOT execution evidence.

## Five selected small-cap gainers (research candidates, not trades)
|Symbol|Webull AH last|AH change|Webull reported volume (session definition UNKNOWN)|L1 bid/ask|Spread / midpoint|Quote time EST|First fresh issuer catalyst after 16:00 EST|First responsive trade|Verdict|
|---|---:|---:|---:|---|---|---|---|---|---|
|CDT|$0.0901|+113.00%|79,472,752|$0.0824/$0.0975|$0.0151 / 16.79%|18:33:47|UNKNOWN|UNKNOWN|NO TRADE; exceptionally wide spread|
|CIIT|$2.45|+58.71%|5,511,942|$2.47/$2.49|$0.02 / 0.81%|18:33:48|UNKNOWN|UNKNOWN|NO TRADE; leaderboard last below current bid; synchronization UNKNOWN|
|DVLT|$0.0837|+41.39%|163,792,199|$0.081/$0.088|$0.007 / 8.28%|18:33:34|UNKNOWN|UNKNOWN|NO TRADE; wide spread|
|UONEK|$4.24|+19.77%|3,185|$3.50/$4.28|$0.78 / 20.05%|16:58:47 **STALE**|UNKNOWN|UNKNOWN|NO TRADE; thin reported volume and stale/wide quote|
|DBGI|$0.54|+14.89%|180,316|$0.57/$0.59|$0.02 / 3.45%|18:32:46|UNKNOWN|UNKNOWN|NO TRADE; ranking last below quoted bid, time mismatch|

Selection prioritizes sub-$5 small caps, not just largest percentages. Larger-cap FROG, ETON, LASR, NET were excluded from primary five; FROG ranked +21.79% at $90.88 with 5,232,923 reported volume, but not small-cap.

## Exceptional negative controls / failed continuation
|Symbol|Webull AH last|AH change|Reported volume (session UNKNOWN)|L1 bid/ask|Spread / midpoint|L1 time EST|Catalyst and first trade|Verdict|
|---|---:|---:|---:|---|---|---|---|---|
|AEHL|$13.23|-23.74%|26,319,251|$13.00/$13.23|$0.23 / 1.75%|18:33:48|Fresh Nov 5 catalyst UNKNOWN; historic Oct 1 $100m ATM announcement and Oct 22 424B5 reported; direct SEC acceptance time UNKNOWN. First sell trade UNKNOWN.|NO TRADE; high dilution-risk priority; previous Nov 4 gainer now Nov 5 decliner, not proof of first ignition failure|
|BDMD|$0.1243|-21.08%|377,052,359|$0.122/$0.128|$0.006 / 4.80%|18:32:22|UNKNOWN|NO TRADE; extremely high reported volume but no acceleration evidence|
|EVGN|$0.2557|-22.42%|7,507,541|NOT RETRIEVED|UNKNOWN|UNKNOWN|UNKNOWN|NO TRADE; decline control|

## Catalyst research and SEC risk
- Fresh original issuer PR publication times **UNKNOWN** for CDT, CIIT, DVLT, UONEK, DBGI, AEHL, BDMD. Web search did not substantiate a Nov 5 post-16:00 issuer catalyst for the primary five. These are **moves with no verified same-session news**, not proof that no news exists.
- AEHL prior Oct 1, 2026 16:08 ET announcement: $100m ATM program: https://finviz.com/news/398009/antelope-enterprise-holdings-limited-announces-100-million-at-the-market-equity-offering-program . Historical Oct 22 424B5 and Nov 2 6-K are listed by secondary filings tracker https://br.advfn.com/bolsa-de-valores/nasdaq/AEHL/noticias ; exact EDGAR acceptance timestamps and whether shares sold remain UNKNOWN. Historical 1-for-16 reverse split effective Aug 7, 2026 also reported https://www.stocktitan.net/news/AEHL/ . These are **not** Nov 5 ignition catalysts.
- Nov 5 after-close earnings event scheduled for CNDT according to issuer's Oct 27 release https://conduent.gcs-web.com/news-releases/news-release-details/conduent-report-third-quarter-2026-financial-results-november-5 ; actual Nov 5 earnings publication timestamp and market response NOT VERIFIED, so do not label a news-with-no-move control.
- SEC 8-K, 424B, S-3, ATM, equity-line, merger, FDA/clinical, reverse-split scans for all five primary candidates were **not completed at direct EDGAR accession level**. Dilution risk UNKNOWN (not cleared).
- **News with no move:** NONE VERIFIED. **Moves without verified fresh news:** five selected gainers and negative controls. Do not infer news causality.

## Ignition integrity and Puck Permission
- Exact first meaningful post-16:00 executed trade, volume-response timestamp, trade prints, speed acceleration, volume acceleration, buyer aggression, defended support: **UNKNOWN** for all.
- Bid/ask measured for seven symbols; quoted spreads alone cannot establish a stable or tightening trend.
- Price sequence/candle-based origin inference prohibited. No entries authorized. **NO PROOF = NO TRADE**.
