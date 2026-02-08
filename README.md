# Awesome OpenClaw

<div align="center">

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
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | - | Official skill registry with 700+ community skills | TypeScript |
| [openclaw/skills](https://github.com/openclaw/skills) | - | All versions of skills from clawdhub.com archived | TypeScript |
| [openclaw/lobster](https://github.com/openclaw/lobster) | - | Workflow shell for composable pipelines and automations | TypeScript |
| [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) | - | Nix package manager integration | Nix |
| [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | - | Automated hardened installation with Tailscale VPN, UFW, Docker | Ansible |
| [openclaw/clawdinators](https://github.com/openclaw/clawdinators) | - | Declarative infra + NixOS modules for CLAWTINATOR hosts | NixOS |
| [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) | - | Homebrew tap for macOS installation | Shell |
| [openclaw/openclaw.ai](https://github.com/openclaw/openclaw.ai) | - | Official website (molt.bot) | TypeScript |
| [openclaw/clawgo](https://github.com/openclaw/clawgo) | - | Clawd node implementation in Go | Go |

### Name History Resources

- [Clawdbot Archive](https://github.com/clawdbot) - Original Clawdbot repositories and history
- [Moltbot Archive](https://github.com/molt-bot) - Moltbot era repositories

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
- [lekt9/unbrowse-openclaw](https://github.com/lekt9/unbrowse-openclaw) - Self-learning API skill generator

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
