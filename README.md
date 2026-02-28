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
| [openclaw/openclaw](https://github.com/openclaw/openclaw)

| [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | ![Stars](https://img.shields.io/github/stars/sipeed/picoclaw) | Tiny, Fast, and Deployable AI assistant | Go | 20K+ stars, automation focused | | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw) | Main personal AI assistant - "The lobster way" | TypeScript |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | ![Stars](https://img.shields.io/github/stars/openclaw/clawhub) | Official skill registry with 700+ community skills | TypeScript |
| [openclaw/skills](https://github.com/openclaw/skills) | ![Stars](https://img.shields.io/github/stars/openclaw/skills) | All versions of skills from clawdhub.com archived | TypeScript |
| [openclaw/lobster](https://github.com/openclaw/lobster) | ![Stars](https://img.shields.io/github/stars/openclaw/lobster) | Workflow shell for composable pipelines and automations | TypeScript |
| [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/nix-openclaw) | Nix package manager integration | Nix |
| [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw-ansible) | Automated hardened installation with Tailscale VPN, UFW, Docker | Ansible |
| [openclaw/clawdinators](https://github.com/openclaw/clawdinators) | ![Stars](https://img.shields.io/github/stars/openclaw/clawdinators) | Declarative infra + NixOS modules for CLAWTINATOR hosts | NixOS |
| [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) | ![Stars](https://img.shields.io/github/stars/openclaw/homebrew-tap) | Homebrew tap for macOS installation | Shell |
| [openclaw/openclaw.ai](https://github.com/openclaw/openclaw.ai) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw.ai) | Official website (molt.bot) | TypeScript |
| [openclaw/clawgo](https://github.com/openclaw/clawgo) | ![Stars](https://img.shields.io/github/stars/openclaw/clawgo) | Clawd node implementation in Go | Go |

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
| [microclaw/microclaw](https://github.com/microclaw/microclaw)

| [langbot-app/LangBot](https://github.com/langbot-app/LangBot) | ![Stars](https://img.shields.io/github/stars/langbot-app/LangBot) | Production-grade agentic IM bots | Python | 15K+ stars, Multi-platform | | ![Stars](https://img.shields.io/github/stars/microclaw/microclaw) | Agentic AI assistant with full tool execution | Rust | 22+ tools, session resume, skills compatible |

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
| Python | 15+ | nanobot, nanoClaw, HAL Claude |
| Rust | 4 | Carapace, MicroClaw, rustclaw |
| TypeScript/Node.js | 3 | nanoclaw, microbot |
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

### Cloud Platforms

- [cloudflare/moltworker](https://github.com/cloudflare/moltworker) - Run OpenClaw on Cloudflare Workers (official Cloudflare project)

### Configuration Management

- [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) - Automated hardened installation with Ansible
- [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) - Nix package manager integration
- [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) - Homebrew tap for macOS

### Installation Tools

- [miaoxworld/OpenClawInstaller](https://github.com/miaoxworld/OpenClawInstaller) - Chinese one-click deployment tool

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

**DingTalk:**
- [soimy/openclaw-channel-dingtalk](https://github.com/soimy/openclaw-channel-dingtalk) - DingTalk channel
- [DingTalk-Real-AI/dingtalk-moltbot-connector](https://github.com/DingTalk-Real-AI/dingtalk-moltbot-connector) - DingTalk with AI Card support

**QQ:**
- [constansino/openclaw_qq](https://github.com/constansino/openclaw_qq) - QQ (OneBot v11)

**WeChat Work (WeCom):**
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
- [Vel-Labs/molting-memory](https://github.com/Vel-Labs/molting-memory) - QDrant-based vector database
- [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) - Long-term memory layer for MoltBook agents

---

## Monitoring & Tools

### Web Interfaces & Dashboards

- [ibelick/webclaw](https://github.com/ibelick/webclaw) - Fast web client for OpenClaw
- [clawdeckio/clawdeck](https://github.com/clawdeckio/clawdeck) - Mission control for OpenClaw agents
- [crshdn/mission-control](https://github.com/crshdn/mission-control) - AI Agent Orchestration Dashboard
- [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) - Studio/IDE for OpenClaw

### Monitoring & Observability

- [luccast/crabwalk](https://github.com/luccast/crabwalk) - Real-time companion monitor for OpenClaw agents

### Cost Tracking

- [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) - Token usage tracking CLI
- [bokonon23/clawdbot-cost-monitor](https://github.com/bokonon23/clawdbot-cost-monitor) - AI spending tracker in real-time

---

## Skills & Extensions

### Official Skill Collections

- [openclaw/skills](https://github.com/openclaw/skills) - Official skills archive
- [openclaw/clawhub](https://github.com/openclaw/clawhub) - Official skill registry with 700+ skills

### Community Skill Libraries

- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - Community curated skills collection
- [natan89/awesome-openclaw-skills](https://github.com/natan89/awesome-openclaw-skills) - 1715+ community-driven skills
- [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) - Popular skills collection

### Specialized Skills

- [BankrBot/openclaw-skills](https://github.com/BankrBot/openclaw-skills) - Trading & DeFi focused skills
- [jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills) - Multi-agent framework skills
- [runkids/skillshare](https://github.com/runkids/skillshare) - Sync skills across AI CLI tools
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) - Manus-style persistent markdown planning
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) - Obsidian agent skills
- [lekt9/unbrowse-openclaw](https://github.com/lekt9/unbrowse-openclaw)
- [refly-ai/refly](https://github.com/refly-ai/refly) - Self-learning API skill generator

---

## Enterprise Solutions

- [archestra-ai/archestra](https://github.com/archestra-ai/archestra) - OpenClaw for Enterprise with RBAC, MCP, A2A
- [backbay-labs/clawdstrike](https://github.com/backbay-labs/clawdstrike) - Swarm Detection & Response (SDR) platform
- [knostic/openclaw-detect](https://github.com/knostic/openclaw-detect) - MDM detection scripts for OpenClaw
- [TheSethRose/Clawdbot-Security-Check](https://github.com/TheSethRose/Clawdbot-Security-Check) - Security audit skill

---

## Localization

### Chinese (中文)

- [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) - Complete Chinese translation
- [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) - Chinese skills library
- [bbylw/clawdbot-cn](https://github.com/bbylw/clawdbot-cn) - Chinese Clawdbot version
- [lllooollpp/clawdbot-cn](https://github.com/lllooollpp/clawdbot-cn) - Electron desktop Chinese version
- [mengjian-github/xiaomo-starter-kit](https://github.com/mengjian-github/xiaomo-starter-kit) - Chinese AI assistant template

### Korean (한국어)

- [OpenClaw-Korea/awesome-openclaw](https://github.com/OpenClaw-Korea/awesome-openclaw) - Korean community resources

---

## Security & Research

### Security Research & Vulnerabilities

- [ethiack/moltbot-1click-rce](https://github.com/ethiack/moltbot-1click-rce) - Security PoC (CVE-2026-25253)

### Defense & Protection

- [seojoonkim/prompt-guard](https://github.com/seojoonkim/prompt-guard) - Prompt injection defense system
- [NirDiamant/moltbook-agent-guard](https://github.com/NirDiamant/moltbook-agent-guard) - Real-time security for agents

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

### Alternative & Related Projects

- [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) - Free, local, open-source UI for multiple AI tools
- [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) - AI Agent + Coding Agent desktop app
- [refly-ai/refly](https://github.com/refly-ai/refly) - Open-source agent skills builder
- [ImGoodBai/goodable](https://github.com/ImGoodBai/goodable) - Local-first Desktop AI Workspace
- [vstorm-co/pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents) - Python Deep Agent framework
- [wecode-ai/Wegent](https://github.com/wecode-ai/Wegent) - AI-native operating system for agent teams

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

### New Projects Added
1. **sipeed/picoclaw** (20K+ stars) - Core Projects - Tiny, Fast, Deployable AI assistant
2. **langbot-app/LangBot** (15K+ stars) - OpenClaw-Inspired - Production-grade IM bots
3. **refly-ai/refly** (6.8K stars) - Skills & Extensions - Agent skills builder

