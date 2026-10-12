# Early-detection validation protocol — v1 (2026-10-12)

**Mission:** detect actionable pressure BEFORE a ticker becomes an obvious top gainer. Detection is NOT entry permission.

## Primary signal
Trades/sec acceleration, shares/sec acceleration, NBBO spread stability/compression, aggressor-buy share, defended support, and a defined invalidation level. Quote/trade feeds must be time-aligned. Missing, delayed or stale data is UNKNOWN, never zero or YES. Candles cannot establish trade speed, spread or buyer aggression.

## State machine
DISCOVERED → WAKING → IGNITION_UNVERIFIED → CONFIRMING → ELIGIBLE_REVIEW → RUNNING/FAILING. Hard failure or support break => REVOKED. No auto execution.

## Measurements
- At every decision time t, compute speed = trade prints/30s, volume = shares/30s, each normalized to trailing 90s baseline ending 60s before t. Compare recent 30s against previous 30s for acceleration.
- NBBO spread % = (ask-bid)/mid; compare median prior 30s. Record top-of-book depth and quote age.
- Buyer share = aggressor-buy volume / known-aggressor volume; if side unknown, mark unverified.
- Support is the last confirmed defended price zone based on prior data; a crude trailing-low proxy is research-only, not production support.
- Preserve feed, venue coverage, latency, corporate action adjustments, symbol mappings and point-in-time float.

## Evaluation (non-negotiable)
- Universe includes *every eligible symbol at each decision timestamp*, failed ignitions, controls, delisted names, and non-runners. No cherry-picking winners.
- Define pre-registered target: first +10% forward move within 30 minutes, with <=5% adverse excursion before target; separately test +5%/15m, +20%/60m and support-break rates. Targets are research hypotheses, not claims.
- Measure earliest alert time vs first appearance on a contemporaneously captured gainers board, median lead time, precision/recall, false alerts per hour, detection-to-confirmation latency, MFE/MAE, spread/slippage and conditional expected value.
- Purged chronological walk-forward folds, train/validation/test by *day*, embargo around overlapping horizons; separate symbols and market regimes. No future PR, filings, float revisions or hindsight labels in features.
- Compare against baselines: % gainer rank, volume spike alone, speed alone, speed+volume, Big Three, Big Three+buyers+support+catalyst.
- Stratify by 04:00-06:30, 06:30-07:00, 07:00-09:30, 09:30-09:40, 09:40-11:00 ET; also by news→ignition lag and float/price cohorts. Do not assume a 'best time' without confidence intervals.
- Optimize for quality: minimize false entries, drawdown and false alerts subject to acceptable lead time; not maximum alert count.
- Simulate limit orders with recorded NBBO/depth, latency, nonfills, partial fills, spread and fees. Never assume mid-price execution.
- Live shadow deployment first; freeze every alert and future outcome immutably. Promote only after statistically credible out-of-sample results.

## Data procurement
1. Historical *tick trades and quotes* with premarket coverage, exchange timestamps and aggressor-side classification or documented reconstruction. OHLCV alone is insufficient.
2. Gainers leaderboard historical snapshots, not a reconstructed hindsight leaderboard.
3. PR and news *first-seen* timestamps, source IDs; EDGAR submission acceptance times and dilution risk; point-in-time corporate actions/float.
4. Separate offline chat-history notes from independently verified market-data observations.

SEC official submissions API: https://www.sec.gov/search-filings/edgar-application-programming-interfaces ; respect SEC access limits. Nasdaq defines premarket 04:00–09:30 ET: https://listingcenter.nasdaq.com/rulebook/nasdaq/rules/Nasdaq%20Equity%201

## Immediate implementation status
A local standalone Python standard-library research prototype was created and passed five unit tests on 2026-10-12. It demonstrates point-in-time rolling calculations and fail-closed logic. It is NOT connected to a live feed, and its simple trailing-low support proxy is NOT a validated entry signal. Full tick data, real-time feed, replay corpus and walk-forward study remain outstanding.
