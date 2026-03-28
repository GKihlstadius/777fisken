# Reddit Post — Ready to Copy-Paste

## Subreddit targets (in order):
1. r/polymarket (Strategy flair)
2. r/algotrading (Infrastructure flair)
3. r/artificial (Discussion flair)
4. r/CryptoCurrency (no flair needed, but needs 500+ karma)

## Title:
Open-sourced an AI swarm system that analyzes prediction market odds — 12 markets, $0.01/run, full code and methodology

## Body:

been building this for a few weeks and wanted to share since i haven't seen anyone try this approach on polymarket.

instead of building one prediction model, i use an open-source engine called MiroFish to spawn 1000+ AI agents with different trading personas. contrarians, fundamental analysts, risk managers, momentum traders, macro bears. they interact on simulated social media — posting takes, arguing, updating beliefs over time. consensus emerges through the social dynamics, same way real prediction markets aggregate info from diverse traders.

runs on DeepSeek V3 at about a penny per simulation. total cost for all 12 markets: under a dollar. tried gpt-4 and claude but at 1000+ agent interactions per run only deepseek makes economic sense.

the 12 markets i'm tracking are all genuinely contested with high enough volume to trade:

iran ceasefire april at 32.5%, june at 52%
crude oil $110 march 31 at 40.6%, $120 at 23.5%
bitcoin $100k by 2026 at 38%, dip to $45k at 46.5%
finland eurovision at 36.2%
lula brazil 2026 at 42.5%
orban hungary at 34.5%
poland world cup at 33%
china gdp q1 at 60.5%
netanyahu out june at 16.5%

the most interesting finding isn't about any single market — it's about correlations most traders seem to ignore.

iran-oil: ceasefire probability directly affects oil. long ceasefire AND long oil spike means you're hedging against yourself.

bitcoin: dip to $45k and recovery to $100k aren't contradictory. crash-then-recover is the most common simulated path in volatile regimes. market prices these as independent but they're clearly linked.

thin markets: china gdp has $10k total volume. anyone with a real model can move that price.

swarm consensus is surprisingly stable — run it 5 times and estimates converge within 2-3 percentage points. better calibration than i expected.

first markets resolve in days — oil by march 31. logging everything, will publish results publicly.

everything is open source on github under GKihlstadius/777fisken — engine, seed files, scraping tools. happy to answer questions about methodology.

not financial advice, just an experiment in whether AI swarms can find inefficiencies in prediction markets.
