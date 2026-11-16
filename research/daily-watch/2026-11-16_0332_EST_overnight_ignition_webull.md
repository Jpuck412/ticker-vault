# Overnight Ignition Vault — 2026-11-16 ~03:32 EST

## Provenance and timing
Connected Webull US_STOCK snapshot with overnight_required=true, collected approximately 03:32 ET Monday November 16 2026. Actual OVN trade/quote epoch timestamps are included in provider response; snapshot observations asynchronous. Webull PRE_MARKET gainers endpoint also queried but returned a leaderboard whose prices/volume appear tied to Friday November 13 regular session, so **not accepted as a fresh Monday premarket leaderboard**. OVN and PRE are different sessions. First ignition time UNKNOWN; no candle inference. Dedup key date/symbol/~03:32 ET/OVN. Prior 2026-11-13 03:26 record consulted; no previous observations changed.

## Five primary candidates (research relevance, not proof of first ignition)
|Symbol|OVN price|OVN change vs Friday close|OVN shares|OVN bid / ask|L1 spread midpoint|OVN last/quote ET|Assessment|
|---|---:|---:|---:|---|---:|---|---|
|POLA|$0.4739|+75.06%|4,005,030|$0.4724 / $0.4722|UNKNOWN crossed quote|~03:32/~03:32|Largest positive response in checked universe; crossed quote invalid; equity facility history; NO TRADE|
|CLRO|$4.35|+29.08%|320,243|$4.35 / $4.39|0.92%|~03:32/~03:32|Continues Friday after-hours observation; original catalyst UNKNOWN; NO TRADE|
|VTSI|$4.39|+3.54%|10,052|$4.38 / $4.40|0.46%|~03:32/~03:32|Prior earnings-driven mover, low Monday OVN volume; NO TRADE|
|MRLN|$1.11|-1.77%|107,768|$1.10 / $1.11|0.90%|~03:31/~03:32|Previously strong; overnight deterioration control; NO TRADE|
|SLSN|$1.45|-4.61%|22,912|$1.44 / $1.45|0.69%|~03:32/~03:32|Prior runner now negative OVN; NO TRADE|

Note: top five is a balanced candidate/control research selection from checked symbols, **not a verified complete market-wide top-five overnight ranking**. Webull does not provide a dedicated OVN market-wide ranking in this call. Monday OVN quote freshness approximately contemporaneous for primary five; trade and quote timestamps rounded.

## Exceptions and downside controls
|Symbol|OVN price|OVN change|OVN volume|L1 spread|Finding|
|---|---:|---:|---:|---:|---|
|SHFS|$0.0275|-9.24%|22,197,451|0.73%|Heavy volume negative overnight; dilution/corporate action history|
|ZBAO|$0.2307|-17.43%|551,421|2.74%|Friday gainer faded|
|ONFO|$0.6166|-20.39%|257,809|2.04%|Friday gainer faded|
|FCUV|$5.32|-24.86%|239,584|0.38%|Friday leader faded|
|OGEN|$0.1860|-7.46%|393,848|1.44%|Negative control|
|PARA|$0.1024|-1.54%|585,509|1.36%|Corporate-action-adjusted history; risk unknown|
|AIMD|$1.10|-10.57%|140,029|1.83%|Friday after-hours candidate faded|
|SNAL|$2.67|-2.20%|6,106|3.73%|Low overnight volume|
|STAK|$1.52|-1.30%|25,490|1.31%|Negative control|
|SHIM|$3.13|-3.69%|1,004|0.64%|Stale last trade; bid/ask 1 share each|
|MITQ|$0.5657|0%|24|11.74%|Illiquid; stale last trade|
|BBCI|$1.19|0%|211|1.68%|Illiquid; stale last trade|

Spreads calculated as (ask-bid)/midpoint for positive uncrossed quotes; do not interpret as executable liquidity. Quotes are point-in-time only. Exact per-symbol first ignition, interval speed, volume acceleration, spread trend, buyer-initiated tape, defended support and defined risk all UNKNOWN.

## Catalyst / SEC / dilution
- POLA: Friday Nov 13 Benzinga secondary roundup published 2026-11-13 16:05:45 ET, https://news-static.webullfintech.com/us/news-html/20261113/15918487480615936.html . Not original issuer catalyst. Earlier Nov 13 after-hours vault flagged Roth equity facility / financing risk. Original SEC acceptance and primary PR time UNKNOWN.
- VTSI: Webull Friday Nov 13 secondary news at 09:52:55 ET noted Roth Buy reiteration, and separate Friday earnings coverage; Nov 12 10-Q in earlier vault. Original issuer PR/SEC acceptance time for current overnight move UNKNOWN.
- CLRO: retrieved stock-news feed did not establish a fresh Monday original catalyst; historical roundup Nov 6 only in visible results. MRLN and SLSN: Webull stock-news returned empty arrays; this is not proof no catalyst exists.
- Monday Nov 16 original issuer PR timestamps, SEC 8-K/424B/S-3/ATM/equity-line acceptance timestamps and fresh dilution status NOT VERIFIED. First responsive executed trades UNKNOWN. News-without-move category NOT ESTABLISHED; move-without-verified-fresh-news includes POLA/CLRO. No false ignition claimed from price snapshots.

## Cross-repository comparison
- Jpuck412/ticker-vault/research/daily-watch/2026-11-13_0326_EST_overnight_ignition_webull.md: MRLN, SLSN, VTSI and SHFS recurring; Monday snapshot is new date and session, not a duplicate. Earlier after-hours Nov 13 POLA/CLRO also reported. No repository-wide duplicate enumeration available.
- Jpuck412/puck-elite-price-action-v2/README.md: evidence-first, missing data stays missing, historical pattern match is not prediction; methodology applied here.

## Permission
All symbols **NO TRADE APPROVED**. Speed ↑ UNKNOWN; interval volume ↑ UNKNOWN; spread stability UNKNOWN; buyer control UNKNOWN; defended support UNKNOWN; risk definition UNKNOWN. A single quote and cumulative OVN volume do not establish tape strength. NO PROOF = NO TRADE.

## Sources
Connected Webull PRE_MARKET leaderboard (potentially stale Friday data), Webull US_STOCK overnight snapshot collected ~03:32 ET 2026-11-16, Webull stock news POLA/CLRO/VTSI/MRLN/SLSN, GitHub prior dated ticker-vault research and puck-elite-price-action-v2 README.