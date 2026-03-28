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

## Our Stack & Costs

This isn't a theoretical project — it's running in production. Here's exactly what we use and what it costs:

| Component | Service | Model | Cost |
|-----------|---------|-------|------|
| **Primary LLM** | [DeepSeek](https://platform.deepseek.com/) | `deepseek-chat` (V3) | ~$0.01/simulation run |
| **Report LLM** | DeepSeek | `deepseek-chat` | Same key, same cost |
| **Fallback LLM** | [Groq](https://console.groq.com/) | `llama-4-scout-17b-16e-instruct` | Free |
| **Memory Graph** | [Zep Cloud](https://app.getzep.com/) | — | Free tier |
| **Web Scraping** | Cloudflare Browser Rendering | — | Free tier |

**Total cost per full simulation: ~$0.01-0.05.** That's not a typo. DeepSeek V3 delivers frontier-quality inference at 1/100th the cost of GPT-4. A full 12-market analysis costs less than a dollar.

We chose DeepSeek over Groq/OpenRouter as primary because:
- No rate limits (Groq's free tier throttles after ~30 requests/min)
- Consistent quality across long simulation runs (1000+ agent interactions)
- $2 of API credits lasts weeks of daily simulations

## Run Your Own Simulations

This repo includes a **complete, pre-configured MiroFish fork** — no need to clone separately.

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

# Set up your API keys
cp .env.example .env
```

Edit `.env` with your keys:

| Service | Cost | Sign up |
|---------|------|---------|
| **DeepSeek** (Primary LLM) | ~$0.01/run | [platform.deepseek.com](https://platform.deepseek.com/) |
| **Groq** (Fallback LLM) | Free | [console.groq.com](https://console.groq.com/) |
| **Zep Cloud** (Memory graph) | Free tier | [app.getzep.com](https://app.getzep.com/) |

```env
# .env — fill in your keys

# Primary LLM — DeepSeek V3 (recommended: cheap + no rate limits)
PRIMARY_LLM_API_KEY=sk-your_deepseek_key
PRIMARY_LLM_BASE_URL=https://api.deepseek.com/v1
PRIMARY_LLM_MODEL=deepseek-chat

# Report generation — same DeepSeek key works
REPORT_LLM_API_KEY=sk-your_deepseek_key
REPORT_LLM_BASE_URL=https://api.deepseek.com/v1
REPORT_LLM_MODEL=deepseek-chat

# Fallback LLM — Groq (free, kicks in if DeepSeek is down)
FALLBACK_LLM_API_KEY=gsk_your_groq_key
FALLBACK_LLM_BASE_URL=https://api.groq.com/openai/v1
FALLBACK_LLM_MODEL=meta-llama/llama-4-scout-17b-16e-instruct

# Memory graph
ZEP_API_KEY=your_zep_api_key
```

> **Budget option:** You can run entirely free by using Groq as primary and OpenRouter as fallback. But you'll hit rate limits on large simulations. DeepSeek at $0.01/run is worth it.

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

## Built With

This project stands on the shoulders of giants:

| Project | What it does | Why we use it |
|---------|-------------|---------------|
| [**MiroFish**](https://github.com/666ghj/MiroFish) | Multi-agent swarm intelligence engine | The core simulation engine — 1000+ agents debating outcomes |
| [**OASIS**](https://github.com/camel-ai/oasis) by CAMEL-AI | Open Agent Social Interaction Simulations | Powers MiroFish's dual-platform social simulation |
| [**DeepSeek V3**](https://platform.deepseek.com/) | Frontier LLM at $0.01/run | Primary inference — makes large-scale swarm simulation affordable |
| [**Groq**](https://groq.com/) + Llama 4 Scout | Ultra-fast free inference | Fallback LLM — zero-cost safety net |
| [**Zep**](https://www.getzep.com/) | Memory graph for AI agents | Agent long-term memory and belief tracking |
| [**Cloudflare Browser Rendering**](https://developers.cloudflare.com/browser-rendering/) | Serverless browser | Scraping JS-heavy odds pages |
| [**Polymarket**](https://polymarket.com/?r=777Dalahezt) | Prediction market platform | Where the fish puts its money where its mouth is |
| [**Claude Code**](https://claude.ai/claude-code) | AI development agent | Built, deployed, and automated this entire project |

Special thanks to the **MiroFish team** (backed by [Shanda Group](https://www.shanda.com/)) for open-sourcing a genuine swarm intelligence engine, and to **DeepSeek** for making frontier AI inference accessible at fractions of a cent.

## Trade on Polymarket

If you find the analysis useful, trade these markets yourself:

<div align="center">

### **[polymarket.com/?r=777Dalahezt](https://polymarket.com/?r=777Dalahezt)**

*Create an account, explore the markets, and put your predictions to the test.*

</div>

## Performance Tracking

We publish simulation results vs. actual outcomes as markets resolve. Transparency is the point.

| Market | Fish Said | Market Said | Actual | Edge? |
|--------|-----------|-------------|--------|-------|
| *Results will be added as markets resolve* | | | | |

## License

MIT — use it, fork it, run the fish.

---

<div align="center">

*The fish doesn't predict the future. It simulates thousands of possible futures and counts which ones survive.*

**[MiroFish Engine](https://github.com/666ghj/MiroFish)** | **[Trade on Polymarket](https://polymarket.com/?r=777Dalahezt)** | **[DeepSeek](https://platform.deepseek.com/)**

</div>
