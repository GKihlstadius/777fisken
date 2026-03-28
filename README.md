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

This repo includes a **complete, pre-configured MiroFish fork** — no need to clone separately. Everything runs on free API tiers.

### Prerequisites

| Tool | Version | Get it |
|------|---------|--------|
| Node.js | 18+ | [nodejs.org](https://nodejs.org/) |
| Python | 3.11-3.12 | [python.org](https://www.python.org/) |
| uv | Latest | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |

### Step 1: Clone & Configure

```bash
git clone https://github.com/GKihlstadius/777fisken.git
cd 777fisken/mirofish

# Set up your API keys (all free)
cp .env.example .env
```

Edit `.env` with your keys:

| Service | Cost | Sign up |
|---------|------|---------|
| **Groq** (Primary LLM) | Free | [console.groq.com](https://console.groq.com/) |
| **OpenRouter** (Fallback LLM) | Free tier | [openrouter.ai](https://openrouter.ai/) |
| **Zep Cloud** (Memory graph) | Free tier | [app.getzep.com](https://app.getzep.com/) |

```env
# .env — fill in your keys
PRIMARY_LLM_API_KEY=gsk_your_groq_key
PRIMARY_LLM_BASE_URL=https://api.groq.com/openai/v1
PRIMARY_LLM_MODEL=llama-3.3-70b-versatile

FALLBACK_LLM_API_KEY=sk-or-your_openrouter_key
FALLBACK_LLM_BASE_URL=https://openrouter.ai/api/v1
FALLBACK_LLM_MODEL=meta-llama/llama-3.3-70b-instruct:free

ZEP_API_KEY=your_zep_api_key
```

### Step 2: Install & Run

```bash
# One command installs everything (Node + Python deps)
npm run setup:all

# Start the engine
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) — frontend is ready. Backend API runs on port 5001.

### Step 3: Run a Simulation

1. Open the MiroFish UI at `localhost:3000`
2. Upload any seed file from the `seeds/` directory
3. Describe your prediction question in natural language
4. Watch 1000+ agents debate the outcome
5. Get your prediction report

### Docker Alternative

```bash
cd mirofish
cp .env.example .env   # edit with your keys
docker compose up -d
# Frontend: localhost:3000 | Backend: localhost:5001
```

## Seed Files

| File | Description |
|------|-------------|
| `seeds/polymarket-12-markets.txt` | 12 high-value Polymarket markets with cross-correlation analysis |
| `seeds/eurojackpot.txt` | Lottery pattern analysis seed |
| `mirofish/shl-*.txt` | SHL hockey prediction seeds (Swedish Hockey League playoffs) |
| `mirofish/the-kihlstadius*.pine` | TradingView Pine Script strategies |

## Project Structure

```
777fisken/
├── README.md              # You are here
├── content-library.md     # Ready-to-post social content
├── seeds/                 # Seed files for simulations
│   ├── polymarket-12-markets.txt
│   └── eurojackpot.txt
└── mirofish/              # Complete MiroFish engine (pre-configured)
    ├── .env.example       # API key template
    ├── backend/           # Python backend (FastAPI)
    ├── frontend/          # React frontend (Vite)
    ├── package.json       # npm scripts (setup, dev, build)
    ├── Dockerfile         # Docker support
    └── docker-compose.yml
```

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
