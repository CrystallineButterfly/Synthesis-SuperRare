# Autonomous Brush Trader

        **Repo:** `Synthesis-SuperRare`  
        **Primary track:** SuperRare  
        **Submission hold:** wait for human approval before registration or live submission.

        A generative art pipeline that turns agent decisions, market states, and execution summaries into mintable media and auction plans.

        ## Selected concept

        A generative art pipeline turns agent decisions, market states, and execution summaries into mintable media and auction plans. The contract stores series metadata and release policies while Python scripts render outputs and draft the mint and auction sequence.

        ## Idea set

        1. Trading Decisions as Art
2. Self-Minting Market Diary
3. Receipt-Bound Auction Agent

        ## Prize overlap targets

        - Uniswap Agentic Finance
- ERC-8004 Receipts
- Venice Private Agents
- ENS
- Bankr Gateway

        ## Architecture

        ```mermaid
        flowchart TD
    Signals[SuperRare signals] --> Discover[Discover]
    Discover --> Plan[Plan bounded action]
    Plan --> DryRun[Dry run + policy check]
    DryRun --> Guard[AutonomousArtSeries]
    Guard --> Execute[Execute when live mode is enabled]
    Execute --> Verify[Verify proofs + receipts]
    Verify --> Persist[Write agent_log.json + submission snippet]
    Persist --> Storage[Store proof plan for Filecoin / receipts]
        ```

        ## Repo structure

        ```text
        Synthesis-SuperRare/
├── README.md
├── LICENSE
├── .env.example
├── .gitignore
├── agent.json
├── agent_log.json
├── pyproject.toml
├── Makefile
├── docs/
│   ├── architecture.mmd
│   ├── demo_video_script.md
│   └── security.md
├── src/
│   └── AutonomousArtSeries.sol
├── script/
│   └── Deploy.s.sol
├── agents/
│   ├── __init__.py
│   └── autonomous_brush.py
├── scripts/
│   ├── run_agent.py
│   └── plan_live_demo.py
├── submissions/
│   └── synthesis.md
└── tests/
    └── test_project_context.py
        ```

        ## Tech stack

        Solidity 0.8.24 skeleton, Python 3.13 standard library, JSON manifests, Foundry-style layout, MIT license

        ## Security guardrails

        - principal and spend policies are separated by design
        - whitelist, cap, and cooldown checks gate every action
        - dry-run hashes are recorded before any live execution path
        - compute budgets are explicit and live mode is opt-in
        - secrets are loaded from environment variables only
        - structured logs are appended for every discover-plan-execute-verify step

        ## Autonomy loop

        1. Discover candidate signals and external state.
2. Plan an action bundle with explicit budget, target, and purpose.
3. Run a dry-run check and policy validation before any execution path.
4. Execute only when live mode, wallets, and credentials are supplied.
5. Verify receipts, proofs, and notes, then append structured logs.

        ## Local MVP status

        - [x] README, manifests, and security notes created
        - [x] contract and agent-loop skeletons created
        - [x] local git repository initialized with an initial commit
        - [ ] operator wallet addresses attached
        - [ ] real API keys added through `.env`
        - [ ] live TxIDs recorded
        - [ ] registration and submission executed

        ## Live demo and TxID plan

        1. load real credentials into `.env`
        2. run `python3 scripts/plan_live_demo.py` to print the checklist
        3. replace placeholder wallet fields in `agent.json`
        4. enable `LIVE_MODE=true` for controlled execution
        5. record resulting TxIDs and paste them into `submissions/synthesis.md`

        ## Why this ranks first

        This concept ranks highest because it overlaps Uniswap Agentic Finance, ERC-8004 Receipts, Venice Private Agents while keeping the
        execution envelope explicit, dry-run-first, and honest about what still needs
        real credentials before anything touches a chain.
