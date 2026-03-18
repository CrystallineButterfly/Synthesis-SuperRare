"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "Autonomous Brush Trader",
  "track": "SuperRare",
  "pitch": "A generative art pipeline that turns agent decisions, market states, and execution summaries into mintable media and auction plans.",
  "overlap_targets": [
    "Uniswap Agentic Finance",
    "ERC-8004 Receipts",
    "Venice Private Agents",
    "ENS",
    "Bankr Gateway"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
