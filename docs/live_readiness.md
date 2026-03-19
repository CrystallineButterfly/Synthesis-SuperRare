# Live readiness

- **Project:** Autonomous Brush Trader
- **Track:** SuperRare
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:20+00:00`

## Trust boundaries

- **SuperRare** — `rest_json` — Mint art-series media and auction metadata.
- **Uniswap** — `rest_json` — Quote swaps and bounded liquidity moves.
- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **Venice** — `rest_json` — Run private reasoning over sensitive inputs.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **Bankr Gateway** — `rest_json` — Route inference through cost-aware model selection.

## Offline-ready partner paths

- **ERC-8004 Receipts** — prepared_contract_call
- **ENS** — prepared_contract_call

## Live-only partner blockers

- **SuperRare**: SUPERRARE_API_KEY, SUPERRARE_MINT_URL — https://superrare.com/
- **Uniswap**: UNISWAP_API_KEY, UNISWAP_QUOTE_URL — https://developers.uniswap.org/
- **Venice**: VENICE_API_KEY, VENICE_CHAT_COMPLETIONS_URL, VENICE_MODEL — https://docs.venice.ai/
- **Bankr Gateway**: BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/

## Highest-sensitivity actions

- `venice_private_analysis` — Venice — Use Venice for a bounded action in this repo.
- `bankr_gateway_compute_route` — Bankr Gateway — Use Bankr Gateway for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for AutonomousArtSeries.
- Run python3 scripts/run_agent.py to produce a dry run for autonomous_brush.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
