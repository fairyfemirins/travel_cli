#!/usr/bin/env python3
"""
Femirins Travel CLI: Find destinations within your budget.
Usage: python travel_cli.py --date 2026-12-25 --budget 500 --departure "New York"
"""

import argparse
import json
from pathlib import Path
from typing import List, Dict

# Mock data (fallback for blocked APIs)
MOCK_DATA = {
    "New York": {
        "2026-12-25": [
            {"destination": "London", "price": 450},
            {"destination": "Paris", "price": 480},
            {"destination": "Tokyo", "price": 800},
        ]
    }
}

def fetch_destinations(departure: str, date: str, budget: int) -> List[Dict]:
    """Fetch destinations within budget (mock or API)."""
    return [d for d in MOCK_DATA.get(departure, {}).get(date, []) if d["price"] <= budget]

def main():
    parser = argparse.ArgumentParser(description="Find travel destinations within your budget.")
    parser.add_argument("--date", required=True, help="Travel date (YYYY-MM-DD)")
    parser.add_argument("--budget", type=int, required=True, help="Max budget in USD")
    parser.add_argument("--departure", default="New York", help="Departure city")
    args = parser.parse_args()

    destinations = fetch_destinations(args.departure, args.date, args.budget)
    if not destinations:
        print(f"No destinations found under ${args.budget} from {args.departure} on {args.date}.")
        return

    print(f"Destinations under ${args.budget} from {args.departure} on {args.date}:")
    for dest in sorted(destinations, key=lambda x: x["price"]):
        print(f"- {dest['destination']}: ${dest['price']}")

if __name__ == "__main__":
    main()