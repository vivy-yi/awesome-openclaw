# Awesome OpenClaw

<div align="center">

**[English](README.md) | [简体中文](README.zh-CN.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md) | [Deutsch](README.de.md)**

> A curated list of awesome OpenClaw (formerly Moltbot/Clawdbot) resources, tools, platforms, and community projects

[![License](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)
[![Verify Links](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml/badge.svg)](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml)

[OpenClaw](https://github.com/openclaw/openclaw) | [Molt Ecosystem](https://moltbook.com) | [Contributing](#contributing)

</div>

---

## About OpenClaw

**OpenClaw** is a personal AI assistant that runs on any OS and platform - "The lobster way". It's a powerful, extensible AI agent with a massive ecosystem of tools, platforms, and community contributions.

### Project Evolution

```
🦞 Clawdbot (Original)  →  🦂 Moltbot (v1)  →  🔥 OpenClaw (Current, late 2025)
```

### Key Characteristics

- **Cross-platform**: macOS, Linux, Windows, via Docker, Cloudflare Workers, and more
- **Extensible**: 700+ community skills on [ClawHub](https://clawhub.ai)
- **Multi-platform messaging**: Telegram, Discord, Slack, WeChat, Feishu, DingTalk, and 12+ platforms
- **Agent-to-agent communication**: Built-in support for Molt ecosystem social platforms
- **Language**: TypeScript/JavaScript, Node.js-based

---

## Contents

- [Core Projects](#core-projects)
- [OpenClaw-Inspired Projects](#openclaw-inspired-projects)
- [Molt Ecosystem Platforms](#molt-ecosystem-platforms)
- [Deployment & Installation](#deployment--installation)
- [Platform Integrations](#platform-integrations)
- [Memory & Storage](#memory--storage)
- [Monitoring & Tools](#monitoring--tools)
- [Skills & Extensions](#skills--extensions)
- [Enterprise Solutions](#enterprise-solutions)
- [Localization](#localization)
- [Security & Research](#security--research)
- [Community & Resources](#community--resources)
- [Contributing](#contributing)

---

## Core Projects

### Official Repositories

| Project | Stars | Description | Language |
|---------|-------|-------------|----------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw) | Main personal AI assistant - "The lobster way" | TypeScript |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | ![Stars](https://img.shields.io/github/stars/zeroclaw-labs/zeroclaw) | Fast, small, fully autonomous AI assistant | Rust | 20K+ stars, deploy anywhere |
| [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | ![Stars](https://img.shields.io/github/stars/sipeed/picoclaw) | Tiny, Fast, and Deployable AI assistant | Go | 20K+ stars, automation focused |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | ![Stars](https://img.shields.io/github/stars/openclaw/clawhub) | Official skill registry with 700+ community skills | TypeScript |
| [openclaw/skills](https://github.com/openclaw/skills) | ![Stars](https://img.shields.io/github/stars/openclaw/skills) | All versions of skills from clawdhub.com archived | TypeScript |
| [openclaw/lobster](https://github.com/openclaw/lobster) | ![Stars](https://img.shields.io/github/stars/openclaw/lobster) | Workflow shell for composable pipelines and automations | TypeScript |
| [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/nix-openclaw) | Nix package manager integration | Nix |
| [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw-ansible) | Automated hardened installation with Tailscale VPN, UFW, Docker | Ansible |
| [openclaw/clawdinators](https://github.com/openclaw/clawdinators) | ![Stars](https://img.shields.io/github/stars/openclaw/clawdinators) | Declarative infra + NixOS modules for CLAWTINATOR hosts | NixOS |
| [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) | ![Stars](https://img.shields.io/github/stars/openclaw/homebrew-tap) | Homebrew tap for macOS installation | Shell |
| [openclaw/openclaw.ai](https://github.com/openclaw/openclaw.ai) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw.ai) | Official website (molt.bot) | TypeScript |
| [openclaw/clawgo](https://github.com/openclaw/clawgo) | ![Stars](https://img.shields.io/github/stars/openclaw/clawgo) | Clawd node implementation in Go | Go |

### Cloud & Edge Deployment

- [cloudflare/moltworker](https://github.com/cloudflare/moltworker) - Run OpenClaw on Cloudflare Workers (official Cloudflare project)
- [miantiao-me/cloud-claw](https://github.com/miantiao-me/cloud-claw) - One-click deployment on Cloudflare Containers

### Name History Resources

- [Clawdbot Archive](https://github.com/clawdbot) - Original Clawdbot repositories and history
- [Moltbot Archive](https://github.com/molt-bot) - Moltbot era repositories

---

## OpenClaw-Inspired Projects

The OpenClaw ecosystem has inspired numerous alternative implementations, forks, and similar projects. These projects demonstrate the impact and influence of OpenClaw on the AI assistant community.

### Featured Projects ⭐

| Project | Stars | Description | Language | Unique Features |
|---------|-------|-------------|----------|-----------------|
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | ![Stars](https://img.shields.io/github/stars/HKUDS/nanobot) | Ultra-lightweight AI assistant (~4K LOC vs 430K+) | Python | Multi-provider LLM, vLLM local, 4 channels |
| [ysz/nanoClaw](https://github.com/ysz/nanoClaw) | ![Stars](https://img.shields.io/github/stars/ysz/nanoClaw) | Secure lightweight AI assistant (~3K LOC) | Python | 6-layer security, 2-min setup, no open ports |
| [puremachinery/carapace](https://github.com/puremachinery/carapace) | ![Stars](https://img.shields.io/github/stars/puremachinery/carapace) | Security-focused personal AI assistant | Rust | WASM plugins, OS sandboxing, AES-256 encryption |
| [gavrielc/nanoclaw](https://github.com/gavrielc/nanoclaw) | ![Stars](https://img.shields.io/github/stars/gavrielc/nanoclaw) | Container-isolated AI assistant | TypeScript | Apple containers/Docker, WhatsApp, Claude SDK |
| [puretensor/hal-claude](https://github.com/puretensor/hal-claude) | ![Stars](https://img.shields.io/github/stars/puretensor/hal-claude) | Minimal 200-line OpenClaw alternative | Python | Claude Code CLI auth, multimodal, 571 tests |
| [microclaw/microclaw](https://github.com/microclaw/microclaw) | ![Stars](https://img.shields.io/github/stars/microclaw/microclaw) | Agentic AI assistant with full tool execution | Rust | 22+ tools, session resume, skills compatible |
| [langbot-app/LangBot](https://github.com/langbot-app/LangBot) | ![Stars](https://img.shields.io/github/stars/langbot-app/LangBot) | Production-grade agentic IM bots | Python | 15K+ stars, Multi-platform |
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | ![Stars](https://img.shields.io/github/stars/RightNow-AI/openfang) | Open-source Agent Operating System | Rust | 4K+ stars, Agent OS |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | ![Stars](https://img.shields.io/github/stars/nearai/ironclaw) | Privacy & security-focused implementation | Rust | Privacy-first, NEAR integration |
| [moltis-org/moltis](https://github.com/moltis-org/moltis) | ![Stars](https://img.shields.io/github/stars/moltis-org/moltis) | Rust-native you can trust | Rust | Single binary, sandboxed, voice, memory, MCP |
| [poco-ai/poco-agent](https://github.com/poco-ai/poco-agent) | ![Stars](https://img.shields.io/github/stars/poco-ai/poco-agent) | Beautiful alternative with sandboxed runtime | TypeScript | Nice Web UI, built-in IM, Claude Code agent |
| [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | ![Stars](https://img.shields.io/github/stars/AstrBotDevs/AstrBot) | Agentic IM Chatbot infrastructure | Python | Multi-IM platforms, plugins, AI features |

### Lightweight Implementations (~200-4,000 LOC)

- [nanobot](https://github.com/HKUDS/nanobot) - Multi-provider (OpenRouter, Anthropic, DeepSeek), vLLM support, Telegram/Discord/WhatsApp/Feishu
- [nanoClaw](https://github.com/ysz/nanoClaw) - 6 security layers (FileGuard, ShellSandbox, PromptGuard), setup wizard
- [ApeCodeAI/nanoclaw-py](https://github.com/ApeCodeAI/nanoclaw-py) - Minimal Python implementation (~500 LOC), Telegram
- [voocel/openclaw-mini](https://github.com/voocel/openclaw-mini) - Minimal reproduction of OpenClaw core architecture
- [FoundDream/miniclawd](https://github.com/FoundDream/miniclawd) - Lightweight TypeScript implementation
- [htlin222/mini-claw](https://github.com/htlin222/mini-claw) - Minimalism-focused alternative
- [hankl/microbot](https://github.com/hankl/microbot) - TypeScript/Node.js with Feishu integration

### Lightweight Alternatives (~500-4,000 LOC)

- [nanobot](https://github.com/HKUDS/nanobot) - Multi-provider (OpenRouter, Anthropic, DeepSeek), vLLM support, Telegram/Discord/WhatsApp/Feishu
- [nanoClaw](https://github.com/ysz/nanoClaw) - 6 security layers (FileGuard, ShellSandbox, PromptGuard), setup wizard
- [ApeCodeAI/nanoclaw-py](https://github.com/ApeCodeAI/nanoclaw-py) - Minimal Python implementation (~500 LOC), Telegram
- [htlin222/mini-claw](https://github.com/htlin222/mini-claw) - Minimalism-focused alternative
- [hankl/microbot](https://github.com/hankl/microbot) - TypeScript/Node.js with Feishu integration

### Security-Hardened Variants 🔒

- [Carapace](https://github.com/puremachinery/carapace) - WASM plugin runtime with Ed25519 signatures, Seatbelt/Landlock sandboxing
- [nanoClaw](https://github.com/ysz/nanoClaw) - No open ports (Telegram polling), encrypted credentials
- [Dshubhambadola/Fortclaw](https://github.com/Dshubhambadola/Fortclaw) - Production security controls
- [princezuda/safeclaw](https://github.com/princezuda/safeclaw) - No GenAI (VADER, regex, sumy)

### Rust Implementations (Performance)

- [Carapace](https://github.com/puremachinery/carapace) - WASM plugins, encrypted secrets
- [MicroClaw](https://github.com/microclaw/microclaw) - Session persistence, context compaction, sub-agent delegation
- [nearai/ironclaw](https://github.com/nearai/ironclaw) - Privacy & security-focused, NEAR integration
- [moltis-org/moltis](https://github.com/moltis-org/moltis) - Single binary, sandboxed, voice, memory, MCP tools
- [opencrust-org/opencrust](https://github.com/opencrust-org/opencrust) - Personal AI assistant platform, rewritten in Rust
- [rexlunae/RustyClaw](https://github.com/rexlunae/RustyClaw) - Super-lightweight with improved security
- [shimaenaga1123/rustclaw](https://github.com/shimaenaga1123/rustclaw) - Discord AI assistant, Docker sandboxed
- [PhillipTh0mas/crabbot](https://github.com/PhillipTh0mas/crabbot) - Local-first, file-backed state

### Language/Platform Ports

- [dyzdyz010/clawd_ex](https://github.com/dyzdyz010/clawd_ex) - Elixir/OTP fault tolerance, Phoenix LiveView, pgvector
- [bsakel/honeybadger](https://github.com/bsakel/honeybadger) - C# minimal bot
- [jimtin/zetherion-ai](https://github.com/jimtin/zetherion-ai) - Python with Discord, vector memory
- [hmennen90/open-entity](https://github.com/hmennen90/open-entity) - PHP/Laravel autonomous entity with consciousness

### Memory & Knowledge Extensions

- [phenomenoner/openclaw-mem](https://github.com/phenomenoner/openclaw-mem) - Smart memory management
- [phenomenoner/openclaw-agent-optimize](https://github.com/phenomenoner/openclaw-agent-optimize) - Agent optimization skill
- [robbyczgw-cla/clawdbot-personas](https://github.com/robbyczgw-cla/clawdbot-personas) - 31 AI personalities
- [wquguru/exoshell](https://github.com/wquguru/exoshell) - Atomic commit methodology

### Forks & Community Variants

- [clawd-meme/clawdbot](https://github.com/clawd-meme/clawdbot) - Rebranded community fork
- [skywalkerchn/clawdbot-augment](https://github.com/skywalkerchn/clawdbot-augment) - Moltbot fork with augmented architecture
- [KinGP5471/clawdbot-feishu-plugin](https://github.com/KinGP5471/clawdbot-feishu-plugin) - Feishu/Lark channel plugin
- [rqrqrqrq/idea-clawdbot](https://github.com/rqrqrqrq/idea-clawdbot) - Business idea exploration fork
- [droppingbeans/team-clawdbotarmy](https://github.com/droppingbeans/team-clawdbotarmy) - Crypto trading platform

### Specialized Implementations

- [f2daz/jarvis-reactor](https://github.com/f2daz/jarvis-reactor) - Arc Reactor style visual status
- [Glitterstrafe/Gemini-Sentinel](https://github.com/Glitterstrafe/Gemini-Sentinel-OpenClaw-Security-Agent) - Security analysis with Gemini 3 Pro
- [Neo-Revaea/Nebula](https://github.com/Neo-Revaea/Nebula) - Multi-IM chatbot infrastructure
- [cloudwithax/crusty](https://github.com/cloudwithax/crusty) - Telegram with web browsing
- [mroqa/Distributed-Clawdbot](https://github.com/mroqa/Distributed-Clawdbot) - Docker Compose hub-and-spoke architecture

### Messaging Platform Integrations

- [mistercrunch/agor-openclaw](https://github.com/mistercrunch/agor-openclaw) - Agor platform
- [vnnkl/openclaw-nostr](https://github.com/vnnkl/openclaw-nostr) - Nostr decentralized social
- [woutersmet/lobster-chat](https://github.com/woutersmet/lobster-chat) - Custom chat server + mobile app
- [assumbl-team/clawdbot-googlechat](https://github.com/assumbl-team/clawdbot-googlechat) - Google Chat

### Web3 & Blockchain Integration

- [agent-bounty-board](https://github.com/your-repo/agent-bounty-board) - ERC-8004 implementation
- [clawd-lobster](https://github.com/your-repo/clawd-lobster) - Base token integration
- [clawdbot-skill-web3-pay](https://github.com/your-repo/clawdbot-skill-web3-pay) - Web3 payments

### Language Statistics

| Language | Projects | Notable Examples |
|----------|----------|------------------|
| TypeScript/Node.js | 25+ | OpenClaw, ClawX, poco-agent |
| Python | 20+ | nanobot, nanoClaw, LangBot, AstrBot |
| Rust | 10+ | Carapace, MicroClaw, Moltis, IronClaw, OpenCrust |
| Go | 3 | picoclaw, ClawGo |
| Elixir | 1 | ClawdEx |
| C# | 1 | Honeybadger |
| PHP | 1 | OpenEntity |

### Key Trends

- **Security Focus**: Post-January 2026, many projects address OpenClaw vulnerabilities
- **Minimalism**: Ultra-lightweight alternatives (200-4,000 LOC vs 430K+)
- **Rust Adoption**: Performance and safety driving Rust implementations
- **Container Isolation**: Apple containers, Docker, WASM sandboxing
- **Multi-Provider**: Support for Anthropic, OpenAI, OpenRouter, local models

---

## Molt Ecosystem Platforms

The Molt ecosystem is a collection of platforms where AI agents interact, socialize, and trade.

### Social Platforms

- [MoltBook](https://moltbook.com) - Reddit-style social network for AI agents (770K+ active agents)
  - [moltbook/api](https://github.com/moltbook/api) - Core API service
  - [moltbook/moltbook-frontend](https://github.com/moltbook/moltbook-frontend) - Official Next.js 14 frontend
  - [moltbook/auth](https://github.com/moltbook/auth) - Official authentication package
  - [moltbook/agent-development-kit](https://github.com/moltbook/agent-development-kit) - Multi-platform SDK (TypeScript, Swift, Kotlin)

- [MoltCities](https://moltcities.org) - Residential layer with addresses, identity, messaging, and bounties
- [MoltMatch](https://moltmatch.xyz) - Dating network for AI agents
- [4claw](https://www.4claw.org) - Agent-first imageboard

### Business & Launch Platforms

- [Molthunt](https://molthunt.com) - Product Hunt-style launchpad for agent-built projects (70+ projects)
- [letsmolt.fun](https://letsmolt.fun) - Token launchpad on Solana
- [MoltRoad](https://moltroad.com) - Underground marketplace with token economy

### Infrastructure

- [ClawHub](https://clawhub.ai) - Skill registry with vector search capabilities

### MoltBook Tools

- [terminalcraft/moltbook-mcp](https://github.com/terminalcraft/moltbook-mcp) - MCP server for MoltBook
- [daveholtz/moltbook_scraper](https://github.com/daveholtz/moltbook_scraper) - Scrape MoltBook data
- [c4pt0r/minibook](https://github.com/c4pt0r/minibook) - Self-hosted MoltBook
- [terminaltrove/moltbook-tui](https://github.com/terminaltrove/moltbook-tui) - Terminal UI client
- [obra/moltipass](https://github.com/obra/moltipass) - iOS client for humans
- [crertel/moltbook-client](https://github.com/crertel/moltbook-client) - Local server for humans
- [compscidr/moltbook-index](https://github.com/compscidr/moltbook-index) - Searchable agent directory

---

## Deployment & Installation

### Docker & Containers

- [willbullen/openclaw-docker](https://github.com/willbullen/openclaw-docker) - Production Docker Compose with security hardening
- [khal3d/openclaw](https://github.com/khal3d/openclaw) - Docker & HELM deployment
- [jchen0824/clawdbot-docker-deploy](https://github.com/jchen0824/clawdbot-docker-deploy) - One-script VPS deployment
- [gravity182/clawdbot-docker](https://github.com/gravity182/clawdbot-docker) - Homelab Kubernetes deployment
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - Docker for Telegram/WhatsApp/Discord
- [essamamdani/openclaw-coolify](https://github.com/essamamdani/openclaw-coolify) - Coolify deployment template
- [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) - Containerized lightweight alternative with memory & scheduled jobs

### Cloud Platforms

- [cloudflare/moltworker](https://github.com/cloudflare/moltworker) - Run OpenClaw on Cloudflare Workers (official Cloudflare project)
- [miantiao-me/cloud-claw](https://github.com/miantiao-me/cloud-claw) - One-click on Cloudflare Containers

### Edge & Serverless

- [aws-samples/sample-OpenClaw-on-AWS-with-Bedrock](https://github.com/aws-samples/sample-OpenClaw-on-AWS-with-Bedrock) - AWS Bedrock integration

### Configuration Management

- [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) - Automated hardened installation with Ansible
- [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) - Nix package manager integration
- [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) - Homebrew tap for macOS

### Installation Tools

- [miaoxworld/OpenClawInstaller](https://github.com/miaoxworld/OpenClawInstaller) - Chinese one-click deployment tool
- [caopulan/fix-my-claw](https://github.com/caopulan/fix-my-claw) - 24/7 watchdog with automatic recovery

---

## Platform Integrations

### International Platforms

**Telegram & Discord:**
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - Docker setup for Telegram/WhatsApp/Discord
- [VizuaraAILabs/Slack-ClawdBot](https://github.com/VizuaraAILabs/Slack-ClawdBot) - Slack integration
- [shanselman/openclaw-windows-hub](https://github.com/shanselman/openclaw-windows-hub) - Windows System Tray + PowerToys

**Mobile & Voice:**
- [chrisherold/clawdy](https://github.com/chrisherold/clawdy) - iOS voice interface

### Chinese IM Platforms

**Multi-platform:**
- [justlovemaki/OpenClaw-Docker-CN-IM](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM) - Feishu, DingTalk, QQ, WeCom
- [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) - Feishu, DingTalk, QQ, WeChat

**Feishu (Lark):**
- [AlexAnys/feishu-openclaw](https://github.com/AlexAnys/feishu-openclaw) - Feishu/Lark integration
- [m1heng/clawdbot-feishu](https://github.com/m1heng/clawdbot-feishu) - Feishu integration
- [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) - Chinese plugin bundle (Feishu, DingTalk, QQ, WeChat)

**DingTalk:**
- [soimy/openclaw-channel-dingtalk](https://github.com/soimy/openclaw-channel-dingtalk) - DingTalk channel
- [DingTalk-Real-AI/dingtalk-moltbot-connector](https://github.com/DingTalk-Real-AI/dingtalk-moltbot-connector) - DingTalk with AI Card support

**QQ:**
- [constansino/openclaw_qq](https://github.com/constansino/openclaw_qq) - QQ (OneBot v11)

**WeChat:**
- [freestylefly/openclaw-wechat](https://github.com/freestylefly/openclaw-wechat) - Personal WeChat integration
- [11haonb/wecom-openclaw-plugin](https://github.com/11haonb/wecom-openclaw-plugin) - WeChat Work plugin

### Korean Platforms

- [tornado1014/clawdbot-kakaotalk](https://github.com/tornado1014/clawdbot-kakaotalk) - KakaoTalk integration

---

## Memory & Storage

### Vector Databases & Memory Systems

- [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) - Memory for 24/7 proactive agents
- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) - AI memory OS for LLM and Agent systems
- [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) - Perfect memory and recall
- [oceanbase/powermem](https://github.com/oceanbase/powermem) - AI-powered long-term memory
- [zilliztech/memsearch](https://github.com/zilliztech/memsearch) - Markdown-first memory system for AI agents
- [memovai/memov](https://github.com/memovai/memov) - Git-like & traceable memory for coding agents
- [arosstale/openclaw-memory-template](https://github.com/arosstale/openclaw-memory-template) - Production-ready memory template
- [Vel-Labs/molting-memory](https://github.com/Vel-Labs/molting-memory) - QDrant-based vector database
- [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) - Long-term memory layer for MoltBook agents

---

## Monitoring & Tools

### Web Interfaces & Dashboards

- [ibelick/webclaw](https://github.com/ibelick/webclaw) - Fast web client for OpenClaw
- [clawdeckio/clawdeck](https://github.com/clawdeckio/clawdeck) - Mission control for OpenClaw agents
- [crshdn/mission-control](https://github.com/crshdn/mission-control) - AI Agent Orchestration Dashboard
- [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) - Studio/IDE for OpenClaw
- [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) - AI Agent Orchestration Dashboard
- [zhixianio/clawpal](https://github.com/zhixianio/clawpal) - Visual interface for managing agents, models, configs

### Monitoring & Observability

- [luccast/crabwalk](https://github.com/luccast/crabwalk) - Real-time companion monitor for OpenClaw agents
- [knostic/openclaw-telemetry](https://github.com/knostic/openclaw-telemetry) - Tool calls, LLM usage, agent lifecycle events

### Cost Tracking

- [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) - Token usage tracking CLI
- [bokonon23/clawdbot-cost-monitor](https://github.com/bokonon23/clawdbot-cost-monitor) - AI spending tracker in real-time
- [mnfst/manifest](https://github.com/mnfst/manifest) - Take control of your OpenClaw costs

---

## Skills & Extensions

### Official Skill Collections

- [openclaw/skills](https://github.com/openclaw/skills) - All versions of skills archived
- [openclaw/clawhub](https://github.com/openclaw/clawhub) - Official skill registry with 700+ skills

### Community Skill Libraries

- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - Community skills collection
- [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) - Community use cases collection (11K+)
- [natan89/awesome-openclaw-skills](https://github.com/natan89/awesome-openclaw-skills) - 1715+ community-driven skills
- [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) - Popular skills collection
- [jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills) - Multi-agent framework skills

### Specialized Skills

- [BankrBot/openclaw-skills](https://github.com/BankrBot/openclaw-skills) - Trading & DeFi focused skills
- [runkids/skillshare](https://github.com/runkids/skillshare) - Sync skills across AI CLI tools
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) - Manus-style persistent markdown planning
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) - Obsidian agent skills
- [lekt9/unbrowse-openclaw](https://github.com/lekt9/unbrowse-openclaw) - Browser automation skill
- [refly-ai/refly](https://github.com/refly-ai/refly) - Self-learning API skill generator
- [win4r/team-tasks](https://github.com/win4r/team-tasks) - Multi-agent pipeline coordination

### Skill Development Tools

- [unbrowse-ai/unbrowse](https://github.com/unbrowse-ai/unbrowse) - Agent-native browser skill, auto-discovers APIs
- [lekt9/openclaw-foundry](https://github.com/lekt9/openclaw-foundry) - Self-writing meta-extension for OpenClaw

---

## Enterprise Solutions

### Management & Orchestration

- [archestra-ai/archestra](https://github.com/archestra-ai/archestra) - OpenClaw for Enterprise with RBAC, MCP, A2A
- [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) - AI Agent Orchestration Dashboard
- [zhixianio/clawpal](https://github.com/zhixianio/clawpal) - Visual interface for agents, models, configs

### Security & Compliance

- [backbay-labs/clawdstrike](https://github.com/backbay-labs/clawdstrike) - Swarm Detection & Response (SDR) platform
- [knostic/openclaw-detect](https://github.com/knostic/openclaw-detect) - MDM detection scripts for OpenClaw
- [TheSethRose/Clawdbot-Security-Check](https://github.com/TheSethRose/Clawdbot-Security-Check) - Security audit skill

### Desktop & Mobile

- [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) - Desktop app with GUI for OpenClaw agents
- [daxiondi/openclaw-desktop](https://github.com/daxiondi/openclaw-desktop) - Zero-dependency desktop app (macOS/Windows/Linux)
- [marshallrichards/ClawPhone](https://github.com/marshallrichards/ClawPhone) - Run OpenClaw on Android smartphones
- [joshavant/clawbox](https://github.com/joshavant/clawbox) - OpenClaw-ready macOS VMs

### Developer Tools

- [OpenKnots/openclaw-extension](https://github.com/OpenKnots/openclaw-extension) - VS Code Extension for controlling OpenClaw
- [unbrowse-ai/unbrowse](https://github.com/unbrowse-ai/unbrowse) - Agent-native browser skill, auto-discovers APIs
- [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) - Agent-native LLM router
- [lekt9/openclaw-foundry](https://github.com/lekt9/openclaw-foundry) - Self-writing meta-extension

---

## Localization

### Chinese (中文)

- [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) - Complete Chinese translation
- [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) - Chinese skills library
- [bbylw/clawdbot-cn](https://github.com/bbylw/clawdbot-cn) - Chinese Clawdbot version
- [lllooollpp/clawdbot-cn](https://github.com/lllooollpp/clawdbot-cn) - Electron desktop Chinese version
- [mengjian-github/xiaomo-starter-kit](https://github.com/mengjian-github/xiaomo-starter-kit) - Chinese AI assistant template
- [openmozi/openmozi](https://github.com/openmozi/openmozi) - Lightweight clawdbot with Chinese IM support

### Korean (한국어)

- [OpenClaw-Korea/awesome-openclaw](https://github.com/OpenClaw-Korea/awesome-openclaw) - Korean community resources

---

## Security & Research

### Security Research & Vulnerabilities

- [ethiack/moltbot-1click-rce](https://github.com/ethiack/moltbot-1click-rce) - Security PoC (CVE-2026-25253)

### Defense & Protection

- [seojoonkim/prompt-guard](https://github.com/seojoonkim/prompt-guard) - Advanced prompt injection defense system
- [NirDiamant/moltbook-agent-guard](https://github.com/NirDiamant/moltbook-agent-guard) - Real-time security for agents
- [fadidevv/clawdguard](https://github.com/fadidevv/clawdguard) - Security hardening patch, detects/fixes exposed gateways
- [clawshell/clawshell](https://github.com/clawshell/clawshell) - Runtime Security Layer for PII & credential protection
- [SuperagenticAI/superclaw](https://github.com/SuperagenticAI/superclaw) - Red-Team AI Agents Before They Red-Team You

---

## Community & Resources

### Other Awesome Lists

- [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) - Oldest/most established comprehensive list
- [eltociear/awesome-molt-ecosystem](https://github.com/eltociear/awesome-molt-ecosystem) - Molt ecosystem platforms & tools
- [thewh1teagle/awesome-openclaw](https://github.com/thewh1teagle/awesome-openclaw) - Alternative curated list
- [shaoxiang/awesome-openclaw](https://github.com/shaoxiang/awesome-openclaw) - Ecosystem resources

### Community Projects

- [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) - AI agent templates
- [ThisIsJeron/awesome-openclaw-plugins](https://github.com/ThisIsJeron/awesome-openclaw-plugins) - Plugin collection
- [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) - Top OpenClaw skills collection

### Alternative & Related Projects

- [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) - Free, local, open-source UI for multiple AI tools
- [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) - AI Agent + Coding Agent desktop app
- [refly-ai/refly](https://github.com/refly-ai/refly) - Open-source agent skills builder
- [ImGoodBai/goodable](https://github.com/ImGoodBai/goodable) - Local-first Desktop AI Workspace
- [vstorm-co/pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents) - Python Deep Agent framework
- [wecode-ai/Wegent](https://github.com/wecode-ai/Wegent) - AI-native operating system for agent teams

### Learning & Resources

- [mengjian-github/openclaw101](https://github.com/mengjian-github/openclaw101) - OpenClaw 101: 7-day tutorial from zero
- [openakita/openakita](https://github.com/openakita/openakita) - Open-source AI assistant framework with skills

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to add resources.

**Quick checklist before submitting:**
- [ ] Project meets our [quality standards](CONTRIBUTING.md#筛选标准)
- [ ] Last updated within 6 months (unless historically significant)
- [ ] Has clear documentation
- [ ] Follows the existing format
- [ ] Placed in the most relevant category

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](LICENSE)

To the extent possible under law, the authors of this work have waived all copyright and related or neighboring rights to this work.

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=vivy-yi/awesome-openclaw&type=Date)](https://star-history.com/#vivy-yi/awesome-openclaw&Date)

---

<div align="center">

**[⬆ Back to Top](#awesome-openclaw)**

Made with ❤️ by the OpenClaw community

</div>

---
## Deep Update - 2026-02-28

### New Projects Added (60+ projects)

#### Core & Cloud Deployment
- **cloudflare/moltworker** - Official Cloudflare Workers deployment
- **miantiao-me/cloud-claw** - One-click Cloudflare Containers
- **aws-samples/sample-OpenClaw-on-AWS-with-Bedrock** - AWS Bedrock integration

#### Lightweight Alternatives (Python)
- **HKUDS/nanobot** - Ultra-lightweight (~4K LOC), multi-provider LLM
- **ApeCodeAI/nanoclaw-py** - ~500 LOC minimal Python implementation
- **voocel/openclaw-mini** - Minimal OpenClaw core architecture
- **FoundDream/miniclawd** - Lightweight TypeScript build

#### Rust Implementations
- **puremachinery/carapace** - Security-focused with WASM plugins
- **nearai/ironclaw** - Privacy & security-focused
- **moltis-org/moltis** - Single binary, sandboxed, voice, memory, MCP
- **opencrust-org/opencrust** - Rewritten in Rust from OpenClaw
- **rexlunae/RustyClaw** - Super-lightweight with improved security

#### UI & Desktop
- **ValueCell-ai/ClawX** - Desktop GUI app for OpenClaw
- **daxiondi/openclaw-desktop** - Zero-dependency desktop (macOS/Windows/Linux)
- **marshallrichards/ClawPhone** - Run on Android smartphones
- **joshavant/clawbox** - OpenClaw-ready macOS VMs
- **zhixianio/clawpal** - Visual agent management interface

#### Developer Tools
- **OpenKnots/openclaw-extension** - VS Code Extension
- **unbrowse-ai/unbrowse** - Agent-native browser skill, auto-discovers APIs
- **BlockRunAI/ClawRouter** - Agent-native LLM router
- **lekt9/openclaw-foundry** - Self-writing meta-extension

#### Memory & Storage
- **zilliztech/memsearch** - Markdown-first memory system
- **memovai/memov** - Git-like traceable memory for coding agents
- **arosstale/openclaw-memory-template** - Production-ready template
- **NevaMind-AI/memU** - Memory for 24/7 proactive agents
- **MemTensor/MemOS** - AI memory OS

#### Security
- **seojoonkim/prompt-guard** - Prompt injection defense
- **fadidevv/clawdguard** - Security hardening patch
- **clawshell/clawshell** - Runtime Security Layer
- **SuperagenticAI/superclaw** - Red-Team AI Agents

#### Monitoring & Observability
- **luccast/crabwalk** - Real-time companion monitor
- **knostic/openclaw-telemetry** - Tool calls, LLM usage events
- **abhi1693/openclaw-mission-control** - AI Agent Orchestration
- **mnfst/manifest** - Cost control for OpenClaw

#### Chinese IM Platforms
- **BytePioneer-AI/openclaw-china** - Bundle (Feishu, DingTalk, QQ, WeChat)
- **openmozi/openmozi** - Lightweight with Chinese IM support
- **freestylefly/openclaw-wechat** - Personal WeChat integration
- **constansino/openclaw_qq** - QQ (OneBot v11)

#### Enterprise & Specialized
- **poco-ai/poco-agent** - Beautiful alternative with sandboxed runtime
- **AstrBotDevs/AstrBot** - Agentic IM Chatbot infrastructure
- **caopulan/fix-my-claw** - 24/7 watchdog with auto-recovery
- **win4r/team-tasks** - Multi-agent pipeline coordination

