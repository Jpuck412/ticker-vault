# Ticker Vault

Historical/live market-microstructure intelligence engine focused on **Speed, Spread, Volume** and immediate price response.

## Core research contract
- Never infer tape speed or spread from candles.
- Historical features use only information available at that timestamp.
- Catalyst timestamp/type is context, not an entry trigger.
- Runner cohorts include failed ignitions/controls to avoid winner-only bias.
- Pattern claims require out-of-sample validation and sample counts.

## Pipeline
1. ingest trades + NBBO quotes
2. normalize each symbol against its own time-local baseline
3. detect ignition events
4. attach catalyst timestamps/types where verified
5. generate Big-3 fingerprints
6. measure forward MFE/MAE, continuation and failure
7. discover recurring sequences
8. validate walk-forward on unseen dates
9. calculate highest-information check windows
10. compare live states with validated historical cohorts

## Environment
Copy .env.example to .env.local. No API keys belong in Git.
