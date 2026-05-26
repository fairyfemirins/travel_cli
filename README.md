# Femirins Travel CLI

A CLI tool to find travel destinations within your budget. Enter a date, budget, and departure city to get a list of affordable destinations.

## Features
- **Offline Mode:** Uses mock data for testing (no API key required).
- **Extensible:** Modular design for future API integration (Skyscanner, Kiwi).
- **Lightweight:** Zero dependencies (Python 3.6+).

## Usage
```bash
python3 travel_cli.py --date YYYY-MM-DD --budget USD --departure "City"
```

### Example
```bash
python3 travel_cli.py --date 2026-12-25 --budget 500 --departure "New York"
```
**Output:**
```
Destinations under $500 from New York on 2026-12-25:
- London: $450
- Paris: $480
```

## Technical Architecture
1. **Input Parsing:** `argparse` for CLI arguments.
2. **Data Fetching:** Mock data (fallback for blocked APIs).
3. **Output:** Sorted list of destinations by price.

## Future Work
- Integrate Skyscanner/Kiwi APIs for live data.
- Add currency conversion.
- Support multi-city departures.

## Note
This repository was published under `fairyfemirins` due to GitHub namespace restrictions. A transfer to `femirins` is pending.

To request a transfer, open an issue in this repository or contact `@femirins` on GitHub.

## License
MIT