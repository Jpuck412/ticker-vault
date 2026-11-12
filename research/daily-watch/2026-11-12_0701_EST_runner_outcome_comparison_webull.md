# Runner Outcome Comparison — 2026-11-12 ~07:01 EST

## Audit and methodology
Original snapshot: [03:19 EST overnight vault](2026-11-12_0319_EST_overnight_ignition_webull.md), read directly from GitHub (not modified). Follow-up: connected Webull US_STOCK get_stock_snapshot with extend_hour_required=true, overnight_required=true, plus PRE_MARKET top-20 gainers, queried ~07:01 EST. **Early prices are OVN last, later prices are extend_hour_last_price (PRE session); price changes are indicative, not executable returns.** Current quote bid/ask is separate and may be asynchronous. Webull's extend_hour_volume is NOT a premarket-only counter in these responses and cannot be subtracted from early ovn_volume. Overnight counters in the current response refer to the OVN session and may have changed after 03:19 but are not directly comparable with PRE volumes. Dedup key: 2026-11-12 / symbol / ~07:01 EST / runner outcome comparison. No original records overwritten.

## All nine original symbols
|Symbol|03:19 OVN last $|~07:01 PRE last $|Indicative price change|03:19 OVN volume|~07:01 extended volume (scope ambiguous)|~07:01 L1 spread|PRE top 20|
|---|---:|---:|---:|---:|---:|---:|---|
|PLCE|0.7638|0.9788|28.15%|4,476,908 OVN|33,813,310 extended (NOT comparable)|4.08%|Top 20|
|POAS|2.26|2.24|-0.88%|925,552 OVN|5,060,046 extended (NOT comparable)|0.45%|Top 20|
|ADXN|5.86|5.0122|-14.47%|267,508 OVN|1,545,249 extended (NOT comparable)|0.80%|Top 20|
|CENN|0.2114|0.2182|3.22%|8,175,984 OVN|61,368,203 extended (NOT comparable)|3.70%|Top 20|
|ICMB|0.8451|0.8515|0.76%|447,332 OVN|2,621,901 extended (NOT comparable)|1.17%|Top 20|
|NCT|0.7983|0.7799|-2.30%|141,717 OVN|202,780 extended (NOT comparable)|4.25%|Outside top 20|
|PEPG|5.68|5.5991|-1.42%|23,836 OVN|199,328 extended (NOT comparable)|2.53%|Outside top 20|
|MI|0.4938|0.41|-16.97%|98,347 OVN|333,052 extended (NOT comparable)|2.95%|Outside top 20|
|SMX|10.72|9.65|-9.98%|61,179 OVN|63,056 extended (NOT comparable)|0.82%|Outside top 20|

**Freshness:** follow-up snapshot's quote timestamps clustered around epoch 1794484861–1794484905 ms (~07:01 ET), with extended last trades around same retrieval; original OVN trade/quote times are recorded in the 03:19 file. Last-trade timestamps are not synchronized to L1 quotes. Quote size at best levels can be extremely thin (e.g., PLCE bid size 5 shares, CENN bid size 100 shares, MI ask size 1991 shares); spread alone is insufficient for execution. Current quotes are a single observation, so spread stability/tightening UNKNOWN.

## Current PRE_MARKET leaderboard versus original list
Top five in Webull PRE_MARKET ranking: PLCE +393.50%, POAS +148.70%, CRMN +101.75%, ADXN +73.43%, CENN +47.57% (ranking feed; asynchronous to snapshot). ICMB also remains top 20 at +37.76%. **Four of the original top five (PLCE, POAS, ADXN, CENN) remain top five; ICMB remains top 20.** NCT, PEPG, MI, SMX are absent from retrieved top 20. Disappearance from ranking does NOT prove failed ignition. CRMN is newly meaningful: Webull extended last ~$2.3297, quoted $2.30/$2.35 (~2.15%), extended volume 6,057,701 (not PRE-only); OVN price/volume unavailable in response. Its ~07:01 gain is a ranking change, not verified first ignition. DPU (+34.59% ranking, extended last ~$2.1386, 6.56M extended volume) and DBGI (+30.53% ranking, ~$0.1910, 40.997M extended volume) are secondary controls; neither has verified first-ignition time.

## Outcome and caveats
- Apparent continuation vs early OVN price: PLCE +28.15%, CENN +3.22%, ICMB +0.76%. PLCE Chapter 11 remains a major structural equity risk.
- Apparent deterioration: ADXN -14.47%, POAS -0.88%, NCT -2.30%, PEPG -1.42%, MI -16.97%, SMX -9.98%. POAS still ranks second by PRE gain despite a slightly lower price than early OVN last; do NOT label false ignition from this.
- No **verified** false ignitions: first responsive tick, velocity/volume intervals, and defended support were not established. Ranking disappearance and later price decline are observational proxies only.
- Early OVN volume and follow-up extended-hour volume have different session scopes: **volume change UNKNOWN**. Cumulative OVN volume at later snapshot is not a measured PRE acceleration rate.
- Support UNKNOWN; high/low ranges are not proof of defended levels. Buyer-controlled tape UNKNOWN; price speed UNKNOWN; interval volume acceleration UNKNOWN; defined executable risk UNKNOWN.
- News: historical [Nov 11 after-hours record](2026-11-11_1833_EST_afterhours_catalyst_vault_webull.md) flags PLCE Nov 8 Chapter 11/Nov 9 8-K; ICMB merger with BCIC reported in secondary article at Nov 12 01:32:21 EST; PLCE secondary article at Nov 12 00:41:47 EST. Original issuer release times, original SEC acceptance timestamps, and first response times remain UNKNOWN. Other original catalysts UNKNOWN. Sources: https://news-static.webullfintech.com/us/news-html/20261112/15909392279913472.html and https://news-static.webullfintech.com/us/news-html/20261112/15909191739950080.html .

## Execution verdict
ALL SYMBOLS **NO TRADE APPROVED**. Speed ↑ UNKNOWN; interval volume ↑ UNKNOWN; spread trend UNKNOWN; buyer control UNKNOWN; defended support UNKNOWN; defined risk UNKNOWN. No proof = no trade.
