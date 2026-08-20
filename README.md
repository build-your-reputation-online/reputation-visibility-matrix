# Reputation Visibility Matrix 🛡️📊

[![npm](https://img.shields.io/npm/v/@build-your-reputation-online/reputation-visibility-matrix)](https://npmjs.com/package/@build-your-reputation-online/reputation-visibility-matrix)
[![PyPI](https://img.shields.io/pypi/v/reputation-visibility-matrix)](https://pypi.org/project/reputation-visibility-matrix)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

Reputation Visibility Matrix is a digital reputation analysis framework from [BuildYourReputation.online](https://buildyourreputation.online), created to help businesses, professionals, founders, and brands better understand their online visibility and reputation signals.

## Overview

The project provides a structured framework for analyzing how a brand, business, or individual appears across different areas of the digital landscape. It brings together reputation signals such as branded search visibility, online mentions, published content, media references, reviews, digital assets, and other publicly available information.

Instead of examining individual search results or mentions separately, Reputation Visibility Matrix organizes these signals into a broader view of digital reputation — helping users identify visibility gaps, understand existing reputation patterns, discover areas that may require attention, and track changes over time.

## Key Use Cases

- **Reputation Audits** — Structured audit of a brand's full digital reputation footprint
- **Brand Visibility Analysis** — Measure and map brand visibility across search and digital platforms
- **Personal Brand Research** — Analyze individual professional reputation signals
- **Competitive Reputation Analysis** — Compare reputation signals against competitors
- **Digital Presence Assessments** — Assess the completeness and quality of digital presence
- **Reputation Monitoring** — Track reputation signal changes over time

## Key Capabilities

- **Branded Search Visibility** — Evaluate how a brand appears in branded search results
- **Online Mentions** — Track and analyze brand mentions across the web
- **Published Content** — Assess published content presence and quality signals
- **Media References** — Identify media coverage and authoritative references
- **Review Signals** — Aggregate and analyse review presence and sentiment
- **Digital Assets** — Map owned digital properties and their reputation contribution
- **Visibility Gap Analysis** — Identify areas where reputation signals are weak or missing
- **Reputation Scoring** — Quantified scoring of overall reputation visibility health

## Features

- Search Visibility Score — evaluates branded search presence and ranking signals
- Mention Score — measures online mention volume and sentiment quality
- Content Score — assesses published content presence and authority
- Media Score — tracks media references and authoritative brand mentions
- Review Score — aggregates review signals across platforms
- Digital Asset Score — evaluates owned digital property completeness
- CLI support in Node.js and Python
- Benchmark dataset included (20 reputation visibility cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @build-your-reputation-online/reputation-visibility-matrix
npx reputation-matrix "brand-name" full-audit 88 82 85 78 90 84
```

### Python

```bash
pip install reputation-visibility-matrix
python -m reputation_matrix "brand-name" full-audit 88 82 85 78 90 84
```

## Output

```
Brand: brand-name
Audit Type: Full Audit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Search Visibility Score:       88 / 100  [Excellent]
Mention Score:                 82 / 100  [Healthy]
Content Score:                 85 / 100  [Excellent]
Media Score:                   78 / 100  [Healthy]
Review Score:                  90 / 100  [Excellent]
Digital Asset Score:           84 / 100  [Excellent]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Reputation Index:      85 / 100
Priority Action:               Media (lowest — act first)

Reputation Channels:
  Branded Search:          88 / 100
  Social Mentions:         82 / 100
  Review Platforms:        90 / 100
  Media Coverage:          78 / 100
```

## Audit Types

| Type | Description |
|------|-------------|
| search-audit | Branded search visibility and ranking signals |
| mention-audit | Online mention volume, reach, and sentiment |
| content-audit | Published content presence and authority signals |
| media-audit | Media references and authoritative brand mentions |
| review-audit | Review signals across business review platforms |
| full-audit | Complete reputation visibility matrix across all signals |

## Extensibility

The framework is designed with extensibility in mind and can support future integrations for:
- Search analysis and branded SERP monitoring
- Content classification and topic mapping
- Brand entity detection and knowledge graph signals
- Sentiment analysis across mentions and reviews
- Reputation scoring models and dashboards
- Historical visibility tracking and trend analysis

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Immediate reputation intervention required |
| 31–60 | At Risk | Significant reputation improvements needed |
| 61–80 | Healthy | Monitor and strengthen reputation signals |
| 81–100 | Excellent | Strong reputation — scale visibility strategy |

## Keywords

Reputation Visibility Matrix · Digital Reputation Analysis · Brand Visibility · Reputation Audit · Online Mentions · Branded Search · Reputation Scoring · BuildYourReputation.online

## Links

| Platform | URL |
|----------|-----|
| Website | https://buildyourreputation.online |
| GitHub | https://github.com/build-your-reputation-online/reputation-visibility-matrix |
| GitHub Pages | https://build-your-reputation-online.github.io/reputation-visibility-matrix/ |
| NPM | https://npmjs.com/package/@build-your-reputation-online/reputation-visibility-matrix |
| PyPI | https://pypi.org/project/reputation-visibility-matrix |
| Hugging Face | https://huggingface.co/datasets/build-your-reputation-online/reputation-visibility-benchmarks |
| Kaggle | https://www.kaggle.com/datasets/buildyourreputationonline/reputation-visibility-benchmarks |
| Zenodo | https://zenodo.org/records/XXXXXXX |
| Docs | https://reputation-visibility-matrix.readthedocs.io |
| Quora | https://buildyourreputation.quora.com/ |
| SlideShare | https://www.slideshare.net/slideshow/build-your-reputation-online-online-reputation-management-digital-brand-protection/289362944 |
| Pinterest | https://www.pinterest.com/BuildYourReputation/ |
| Medium | https://medium.com/@build-your-reputation |

## About BuildYourReputation.online

BuildYourReputation.online is focused on helping brands and professionals understand, strengthen, and manage their digital reputation. The Reputation Visibility Matrix project aims to provide developers, researchers, marketers, and reputation professionals with a useful foundation for exploring the relationship between online visibility, brand presence, credibility, and digital reputation.

## License

MIT — [BuildYourReputation.online](https://buildyourreputation.online)
