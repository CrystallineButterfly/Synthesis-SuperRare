# Autonomous Brush Trader

- **Repo:** `Synthesis-SuperRare`
- **Primary track:** SuperRare
- **Category:** art
- **Submission status:** implementation ready, waiting for credentials and TxIDs.

A generative art pipeline that turns agent decisions, market states, and execution summaries into mintable media and auction plans.

## Selected concept

A generative art pipeline turns agent decisions, market states, and execution summaries into mintable media and auction plans. The contract stores series metadata and release policies while Python scripts render outputs and draft the mint and auction sequence.

## Idea shortlist

1. Trading Decisions as Art
2. Self-Minting Market Diary
3. Receipt-Bound Auction Agent

## Partners covered

SuperRare, Uniswap, ERC-8004 Receipts, Venice, ENS, Bankr Gateway

## Architecture

```mermaid
flowchart TD
    Signals[Discover signals]
    Planner[Agent runtime]
    DryRun[Dry-run artifact]
    Contract[AutonomousArtSeries policy contract]
    Verify[Verify and render submission]
    Signals --> Planner --> DryRun --> Contract --> Verify
    Contract --> superrare[SuperRare]
    Contract --> uniswap[Uniswap]
    Contract --> erc_8004_receipts[ERC-8004 Receipts]
    Contract --> venice[Venice]
    Contract --> ens[ENS]
    Contract --> bankr_gateway[Bankr Gateway]
```

## Repository layout

- `src/`: shared policy contracts plus the repo-specific wrapper contract.
- `script/`: Foundry deployment entrypoint.
- `agents/`: Python runtime, partner adapters, and project metadata.
- `scripts/`: CLI utilities for running the loop and rendering submissions.
- `docs/`: architecture, credentials, demo script, and security notes.
- `submissions/`: generated `synthesis.md` snippet for this repo.

## Action catalog

| Action | Partner | Purpose | Max USD | Sensitivity |
| --- | --- | --- | --- | --- |
| `superrare_mint_series` | SuperRare | Use SuperRare for a bounded action in this repo. | $40 | medium |
| `uniswap_quote_route` | Uniswap | Use Uniswap for a bounded action in this repo. | $220 | medium |
| `erc_8004_receipts_receipt_anchor` | ERC-8004 Receipts | Use ERC-8004 Receipts for a bounded action in this repo. | $1 | medium |
| `venice_private_analysis` | Venice | Use Venice for a bounded action in this repo. | $5 | high |
| `ens_ens_publish` | ENS | Use ENS for a bounded action in this repo. | $5 | low |
| `bankr_gateway_compute_route` | Bankr Gateway | Use Bankr Gateway for a bounded action in this repo. | $10 | high |

## Commands

```bash
python3 -m unittest discover -s tests
forge test
python3 scripts/run_agent.py
python3 scripts/plan_live_demo.py
python3 scripts/render_submission.py
```

## Credentials

| Partner | Variables | Docs |
| --- | --- | --- |
| SuperRare | SUPERRARE_API_KEY, SUPERRARE_MINT_URL | https://superrare.com/ |
| Uniswap | UNISWAP_API_KEY, UNISWAP_QUOTE_URL | https://developers.uniswap.org/ |
| ERC-8004 Receipts | RPC_URL | https://eips.ethereum.org/EIPS/eip-8004 |
| Venice | VENICE_API_KEY, VENICE_CHAT_COMPLETIONS_URL, VENICE_MODEL | https://docs.venice.ai/ |
| ENS | ENS_NAME | https://docs.ens.domains/ |
| Bankr Gateway | BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL | https://bankr.bot/ |

## Live demo plan

1. Copy .env.example to .env and fill the required keys.
2. Deploy the contract with forge script script/Deploy.s.sol --broadcast for AutonomousArtSeries.
3. Run python3 scripts/run_agent.py to produce a dry run for autonomous_brush.
4. Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
5. Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
