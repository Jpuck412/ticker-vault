# After-Hours Catalyst Vault — 2026-11-17 ~18:28–18:29 EST

Research only. Sources: connected Webull get_gainers_losers AFTER_MARKET (both directions), get_stock_snapshot (extend_hour_required=true), get_stock_quotes L1, search_news (2026-11-17); public web/SEC research. Snapshot and quote timestamps are not perfectly synchronized. **Reported volume below is the Webull extend_hour_volume field, not regular-session volume.** Changes are Webull AH versus regular close, not change from first response. All symbols listed US exchanges in Webull. No proof of first ignition from candles.

## Five selected meaningful AH movers

|Symbol|AH last $|AH %|AH volume|Bid|Ask|Spread/mid %|Quote time ET|Original catalyst time|First meaningful trade/volume response|Status|
|---|---:|---:|---:|---:|---:|---:|---|---|---|---|
|AZI|1.08|47.92|5,218,557|1.07|1.08|0.93%|11/17, 18:28:37|UNKNOWN|UNKNOWN|Move with no verified fresh issuer catalyst|
|CRIS|0.7573|39.77|3,612,901|0.751|0.7569|0.78%|11/17, 18:28:41|UNKNOWN|UNKNOWN|Move with no verified fresh issuer catalyst|
|ABTS|0.4458|39.92|14,505,185|0.4275|0.4578|6.85%|11/17, 18:28:25|UNKNOWN|UNKNOWN|Move with no verified fresh issuer catalyst|
|BMGL|0.4035|24.35|650,686|0.3666|0.4389|17.95%|11/17, 18:27:48|UNKNOWN|UNKNOWN|Move with no verified fresh issuer catalyst|
|AKAN|2.44|19.02|2,290,653|2.41|2.44|1.24%|11/17, 18:28:40|UNKNOWN|UNKNOWN|Move with no verified fresh issuer catalyst|

## Exceptional/negative controls

|Symbol|AH last $|AH %|AH volume|Bid|Ask|Spread/mid %|Quote time ET|Interpretation|
|---|---:|---:|---:|---:|---:|---:|---|
|GTBP|3.8502|21.08|183|3.02|4.23|33.38%|11/17, 18:26:01|Only 183 AH shares; stale/wide quote|
|SHFS|0.0114|-22.97|65,527,956|0.0112|0.012|6.90%|11/17, 18:28:35|Recurring high-volume downside|
|IRIX|0.51|-27.10|56,918|0.5099|0.52|1.96%|11/17, 18:24:28|Downside control|
|BAER|0.1654|-12.95|325,868|0.1508|0.1789|17.05%|11/17, 18:26:02|Downside control|

## Provenance, news, filings and financing

- Webull symbol news searches for AZI, CRIS, ABTS, BMGL and GTBP on Nov 17 returned zero articles. This is **not** proof no news exists. Original issuer PR, SEC 8-K/424B/S-3/ATM/equity line, reverse split, merger, FDA/clinical, earnings and dilution events were searched in public sources but no **fresh post-16:00 ET primary catalyst with verified timestamp** was established for these five. All original publication/SEC acceptance times UNKNOWN.
- No news-without-move case verified; five primary cases classified **move without verified fresh news**. First meaningful responsive trade, first volume expansion, news-to-response latency, intraperiod tape and defended support UNKNOWN. Do not infer first ignition from OHLC candles or cumulative volume.
- GTBP is a low-volume exception (183 shares) with bid 3.02 / ask 4.23; treat ranking as unreliable execution signal. BMGL bid 0.3666 / ask 0.4389 is extremely wide. SHFS repeated from earlier November archives and shows significant downside after-hours.
- Dilution/financing review for all current symbols is INCOMPLETE; active ATM, S-3, 424B, equity line, convertible terms and split-adjusted float UNKNOWN unless separately documented. No unsupported clean-float claim.
- Separate market context, **not a new AH ignition**: SLS had significant Nov 17 daytime movement associated with reported phase-3 AML vaccine survival results (Reuters https://www.reuters.com/business/healthcare-pharmaceuticals/sellas-cancer-vaccine-extends-survival-blood-cancer-trial-2026-11-17/). Webull AH leaderboard showed SLS -12.04%, but original issuer release timestamp and first response UNKNOWN. Do not label this a post-16:00 catalyst.

## Historical comparison

Earlier Nov 17 overnight (03:25) and runner follow-up (07:01) records were located in ticker-vault/research/daily-watch/. AKAN is a recurring observed candidate, not first-time ignition; BMGL appeared in the morning follow-up exceptions. SHFS previously appeared in Nov 13 overnight and later records. Preserve those records; no overwrite. Reference: https://github.com/Jpuck412/ticker-vault/blob/main/research/daily-watch/2026-11-17_0701_EST_runner_outcome_comparison_webull.md

## Permission and limitations

Speed increasing UNKNOWN; volume acceleration UNKNOWN; spread values are single L1 observations (not stability); buyer-controlled tape UNKNOWN; defended support UNKNOWN; defined risk UNKNOWN. **NO TRADE APPROVED.** Source freshness: quote times above, observed around 18:28–18:29 ET; tick history and original PR/SEC acceptance timestamps unavailable or unverified. These are selected research candidates from the Webull leaderboard, not necessarily the best executable trades.
