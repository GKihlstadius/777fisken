<div align="center">

# 777fisken

### AI Swarm Intelligence Meets Prediction Markets

*Thousands of AI agents debate the future. The fish just watches the consensus emerge.*

[![Powered by MiroFish](https://img.shields.io/badge/Powered%20by-MiroFish-DAA520?style=flat-square)](https://github.com/666ghj/MiroFish)
[![Polymarket](https://img.shields.io/badge/Trade-Polymarket-4A90D9?style=flat-square)](https://polymarket.com/?r=777Dalahezt)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

</div>

---

## What is this?

**777fisken** uses [MiroFish](https://github.com/666ghj/MiroFish) — an open-source multi-agent swarm intelligence engine — to generate prediction reports on real-world markets.

The idea is simple:

1. Feed real-world data (odds, news, signals) into MiroFish as seed material
2. Thousands of AI agents with different personalities and reasoning styles simulate social dynamics
3. The swarm's collective intelligence surfaces probabilities that diverge from market consensus
4. We publish the analysis and track performance

No black box. No "trust me bro." The entire simulation pipeline is open source.

## How It Works

```
Seed Data (odds, news, signals)
        |
        v
   MiroFish Engine
   - Knowledge Graph Construction
   - Entity Extraction & Persona Generation
   - Dual-platform Social Simulation
        |
        v
   Swarm Consensus
   - 1000+ agents debate outcomes
   - Dynamic memory & belief updates
   - Emergent collective intelligence
        |
        v
   Prediction Report
   - Probability estimates vs. market odds
   - Confidence levels & edge identification
   - Position sizing (Kelly criterion)
```

## Current Markets

We're actively running simulations on contested prediction markets where the crowd is genuinely split:

| Market | Category | Market Price | Status |
|--------|----------|-------------|--------|
| US-Iran Ceasefire by April 30 | Geopolitics | 32.5% | Active |
| Crude Oil $110 by March 31 | Commodities | 40.6% | Active |
| Bitcoin $100k by End of 2026 | Crypto | 38.0% | Active |
| Bitcoin Dip to $45k | Crypto | 46.5% | Active |
| Finland Wins Eurovision 2026 | Culture | 36.2% | Active |
| Lula Wins Brazil 2026 | Politics | 42.5% | Active |
| Orban Stays PM Hungary | Politics | 34.5% | Active |
| Iran Ceasefire by June 30 | Geopolitics | 52.0% | Active |
| Oil $120 by March 31 | Commodities | 23.5% | Active |
| Poland World Cup Qualification | Sports | 33.0% | Active |
| China GDP Q1 4.5-5.0% | Economics | 60.5% | Active |
| Netanyahu Out by June 30 | Geopolitics | 16.5% | Active |

**Cross-market correlations matter.** Iran tensions affect oil prices. Bitcoin dip and recovery can both happen. We model these dependencies.

## Why Swarm Intelligence?

Traditional prediction models use one brain. MiroFish uses thousands.

Each agent has:
- **Independent personality** — contrarians, analysts, risk managers, momentum traders
- **Long-term memory** — agents remember and update beliefs as new information arrives
- **Social dynamics** — agents influence each other, form consensus, and disagree

The result: emergent collective intelligence that catches edge cases single models miss.

> "The best collective predictions come from diverse, independent thinkers who aggregate information differently." — Wisdom of Crowds, applied to AI.

## Run Your Own Simulations

Want to run the fish yourself?

### Prerequisites

| Tool | Version |
|------|---------|
| Node.js | 18+ |
| Python | 3.11-3.12 |
| uv | Latest |

### Quick Start

```bash
# Clone MiroFish
git clone https://github.com/666ghj/MiroFish.git
cd MiroFish

# Configure (free API keys)
cp .env.example .env
# Edit .env with your keys:
# - Groq (free): https://console.groq.com/
# - OpenRouter (free tier): https://openrouter.ai/
# - Zep Cloud (free tier): https://app.getzep.com/

# Install & run
npm run setup:all
npm run dev
# Open http://localhost:3000
```

### Using Our Seed Files

Drop any of the seed files from this repo into MiroFish's upload interface. The engine will automatically construct the knowledge graph and start the simulation.

```bash
# Clone this repo for seed data
git clone https://github.com/GKihlstadius/777fisken.git
```

## Seed Files

| File | Description |
|------|-------------|
| `seeds/polymarket-12-markets.txt` | 12 high-value Polymarket markets with cross-correlation analysis |
| `seeds/eurojackpot.txt` | Lottery pattern analysis seed |

## Trade

If you find the analysis useful and want to trade on Polymarket:

**[polymarket.com/?r=777Dalahezt](https://polymarket.com/?r=777Dalahezt)**

## Performance Tracking

We'll publish simulation results vs. actual outcomes as markets resolve. Transparency is the point.

| Market | Fish Said | Market Said | Actual | Edge? |
|--------|-----------|-------------|--------|-------|
| *Results will be added as markets resolve* | | | | |

## License

MIT — use it, fork it, run the fish.

---

<div align="center">

*The fish doesn't predict the future. It simulates thousands of possible futures and counts which ones survive.*

**[MiroFish Engine](https://github.com/666ghj/MiroFish)** | **[Trade on Polymarket](https://polymarket.com/?r=777Dalahezt)**

</div>
