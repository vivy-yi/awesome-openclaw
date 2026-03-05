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

**OpenClaw** is a personal AI assistant that and platform - " runs on any OSThe lobster way". It's a powerful, extensible AI agent with a massive ecosystem of tools, platforms, and community contributions.

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

- [1. 入门了解](#1-入门了解)
- [2. 运行部署](#2-运行部署)
- [3. 能力扩展](#3-能力扩展)
- [4. 开发构建](#4-开发构建)
- [5. 生态周边](#5-生态周边)
- [6. 社区贡献](#6-社区贡献)
- [Contributing](#contributing)

---

## 1. 入门了解

了解 OpenClaw 项目的核心概念、官方资源和历史沿革。

### 官方项目

| Project | Stars | Description | Language |
|---------|-------|-------------|----------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw) | Main personal AI assistant - "The lobster way" | TypeScript |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | ![Stars](https://img.shields.io/github/stars/openclaw/clawhub) | Official skill registry with 700+ skills | TypeScript |
| [openclaw/skills](https://github.com/openclaw/skills) | ![Stars](https://img.shields.io/github/stars/openclaw/skills) | All versions of skills archived | TypeScript |
| [openclaw/lobster](https://github.com/openclaw/lobster) | ![Stars](https://img.shields.io/github/stars/openclaw/lobster) | Workflow shell for pipelines and automations | TypeScript |
| [openclaw/openclaw.ai](https://github.com/openclaw/openclaw.ai) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw.ai) | Official website (molt.bot) | TypeScript |

### 历史沿革

- [Clawdbot Archive](https://github.com/clawdbot) - Original Clawdbot repositories and history
- [Moltbot Archive](https://github.com/molt-bot) - Moltbot era repositories

### 学习资源

#### GitHub 教程仓库

| 仓库 | 描述 |
|------|------|
| [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial) | 最全面的中文教程，涵盖安装、配置、实战案例和避坑指南 |
| [yeasy/openclaw_guide](https://github.com/yeasy/openclaw_guide) | 入门和实战，从应用配置到实现原理 |
| [marianasmall/openclaw-guide](https://github.com/marianasmall/openclaw-guide) | 安全优先的安装指南，含 SOUL.md/AGENTS.md 模板 |
| [rfxlamia/openclaw-guideline](https://github.com/rfxlamia/openclaw-guideline) | CLAW 决策框架、安全模式、记忆架构 |
| [JessAI2099/openclaw-guide](https://github.com/JessAI2099/openclaw-guide) | 深度实战指南，AI 自动化从入门到实战 |
| [OpenClaw-Korea/openclaw-guide](https://github.com/OpenClaw-Korea/openclaw-guide) | 韩文完整指南，实战 60+ 技巧 |
| [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) | Complete Chinese translation |

#### 外部教程

##### 视频教程

- [B站 - OpenClaw 教程精选](https://www.bilibili.com/search?keyword=OpenClaw) - 搜索 OpenClaw 获取最新视频教程
- [YouTube - OpenClaw Tutorial](https://www.youtube.com/results?search_query=OpenClaw+AI+agent) - 英文视频教程

##### 文字教程

- [DigitalOcean - How to Run OpenClaw](https://www.digitalocean.com/community/tutorials/how-to-run-openclaw) - 云平台部署教程
- [Hostinger - How to Set Up OpenClaw](https://www.hostinger.com/tutorials/how-to-set-up-openclaw) - VPS 私有服务器部署

#### 案例集合

- [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases) - 真实使用案例 (30+ 场景)
- [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook) - Moltbook 社区案例 (70+ 场景)
- [mengjian-github/openclaw101](https://github.com/mengjian-github/openclaw101) - 7天入门教程
- [openakita/openakita](https://github.com/openakita/openakita) - Open-source AI assistant framework with skills

---

## 2. 运行部署

将 OpenClaw 部署到服务器或云平台。

### Docker & 容器

| Project | Stars | Description |
|---------|-------|-------------|
| [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | ![Stars](https://img.shields.io/github/stars/qwibitai/nanoclaw) | Containerized lightweight with memory & scheduled jobs |
| [coollabsio/openclaw](https://github.com/coollabsio/openclaw) | ![Stars](https://img.shields.io/github/stars/coollabsio/openclaw) | Fully featured & automated Docker images |
| [liam798/docker-openclawd](https://github.com/liam798/docker-openclawd) | ![Stars](https://img.shields.io/github/stars/liam798/docker-openclawd) | 一键安装 Docker 部署方案 |
| [essamamdani/openclaw-coolify](https://github.com/essamamdani/openclaw-coolify) | ![Stars](https://img.shields.io/github/stars/essamamdani/openclaw-coolify) | Coolify deployment template |

### 云平台

| Project | Stars | Description |
|---------|-------|-------------|
| [1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel) | ![Stars](https://img.shields.io/github/stars/1Panel-dev/1Panel) | VPS control panel with OpenClaw one-click deploy |
| [getumbrel/umbrel](https://github.com/getumbrel/umbrel) | ![Stars](https://img.shields.io/github/stars/getumbrel/umbrel) | Home server OS with OpenClaw support |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | ![Stars](https://img.shields.io/github/stars/cloudflare/moltworker) | Run on Cloudflare Workers (official Cloudflare) |
| [aws-samples/sample-OpenClaw-on-AWS-with-Bedrock](https://github.com/aws-samples/sample-OpenClaw-on-AWS-with-Bedrock) | ![Stars](https://img.shields.io/github/stars/aws-samples/sample-OpenClaw-on-AWS-with-Bedrock) | AWS Bedrock integration |
| [miantiao-me/cloud-claw](https://github.com/miantiao-me/cloud-claw) | ![Stars](https://img.shields.io/github/stars/miantiao-me/cloud-claw) | One-click on Cloudflare Containers |
| [digitalocean-labs/openclaw-appplatform](https://github.com/digitalocean-labs/openclaw-appplatform) | ![Stars](https://img.shields.io/github/stars/digitalocean-labs/openclaw-appplatform) | DigitalOcean App Platform |

### 系统包管理

| Project | Stars | Description |
|---------|-------|-------------|
| [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/nix-openclaw) | Nix package manager integration |
| [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw-ansible) | Automated hardened installation with Ansible |
| [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) | ![Stars](https://img.shields.io/github/stars/openclaw/homebrew-tap) | Homebrew tap for macOS |

### 一键部署工具

| Project | Stars | Description |
|---------|-------|-------------|
| [miaoxworld/OpenClawInstaller](https://github.com/miaoxworld/OpenClawInstaller) | ![Stars](https://img.shields.io/github/stars/miaoxworld/OpenClawInstaller) | Chinese one-click deployment tool |
| [caopulan/fix-my-claw](https://github.com/caopulan/fix-my-claw) | ![Stars](https://img.shields.io/github/stars/caopulan/fix-my-claw) | 24/7 watchdog with automatic recovery |

### 移动端 & 边缘部署

| Project | Stars | Description |
|---------|-------|-------------|
| [mithun50/openclaw-termux](https://github.com/mithun50/openclaw-termux) | ![Stars](https://img.shields.io/github/stars/mithun50/openclaw-termux) | Run on Android via Termux |
| [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | ![Stars](https://img.shields.io/github/stars/AidanPark/openclaw-android) | Run on Android with single command |
| [joshavant/clawbox](https://github.com/joshavant/clawbox) | ![Stars](https://img.shields.io/github/stars/joshavant/clawbox) | OpenClaw-ready macOS VMs |

### 平台集成

#### 国际平台

| Platform | Project | Stars | Description |
|---------|---------|-------|-------------|
| Windows | [shanselman/openclaw-windows-hub](https://github.com/shanselman/openclaw-windows-hub) | ![Stars](https://img.shields.io/github/stars/shanselman/openclaw-windows-hub) | System Tray + PowerToys |
| Slack | [VizuaraAILabs/Slack-ClawdBot](https://github.com/VizuaraAILabs/Slack-ClawdBot) | ![Stars](https://img.shields.io/github/stars/VizuaraAILabs/Slack-ClawdBot) | Slack integration |
| iOS Voice | [chrisherold/clawdy](https://github.com/chrisherold/clawdy) | ![Stars](https://img.shields.io/github/stars/chrisherold/clawdy) | Voice interface |

#### 中国平台

| Platform | Project | Stars | Description |
|---------|---------|-------|-------------|
| 飞书/Lark | [m1heng/clawdbot-feishu](https://github.com/m1heng/clawdbot-feishu) | ![Stars](https://img.shields.io/github/stars/m1heng/clawdbot-feishu) | Feishu integration |
| 钉钉 | [DingTalk-Real-AI/dingtalk-moltbot-connector](https://github.com/DingTalk-Real-AI/dingtalk-moltbot-connector) | ![Stars](https://img.shields.io/github/stars/DingTalk-Real-AI/dingtalk-moltbot-connector) | DingTalk with AI Card |
| Bundle | [justlovemaki/OpenClaw-Docker-CN-IM](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM) | ![Stars](https://img.shields.io/github/stars/justlovemaki/OpenClaw-Docker-CN-IM) | Docker 多平台集成 |
| Bundle | [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) | ![Stars](https://img.shields.io/github/stars/BytePioneer-AI/openclaw-china) | Feishu, DingTalk, QQ, WeChat 插件集合 |
| 钉钉 | [soimy/openclaw-channel-dingtalk](https://github.com/soimy/openclaw-channel-dingtalk) | ![Stars](https://img.shields.io/github/stars/soimy/openclaw-channel-dingtalk) | DingTalk channel |
| 飞书/Lark | [AlexAnys/feishu-openclaw](https://github.com/AlexAnys/feishu-openclaw) | ![Stars](https://img.shields.io/github/stars/AlexAnys/feishu-openclaw) | Feishu/Lark integration |
| 微信 | [freestylefly/openclaw-wechat](https://github.com/freestylefly/openclaw-wechat) | ![Stars](https://img.shields.io/github/stars/freestylefly/openclaw-wechat) | Personal WeChat |
| 微信 | [11haonb/wecom-openclaw-plugin](https://github.com/11haonb/wecom-openclaw-plugin) | ![Stars](https://img.shields.io/github/stars/11haonb/wecom-openclaw-plugin) | WeChat Work plugin |
| QQ | [constansino/openclaw_qq](https://github.com/constansino/openclaw_qq) | ![Stars](https://img.shields.io/github/stars/constansino/openclaw_qq) | QQ (OneBot v11) |
| 轻量 | [openmozi/openmozi](https://github.com/openmozi/openmozi) | ![Stars](https://img.shields.io/github/stars/openmozi/openmozi) | 轻量级支持中文 IM |

#### 韩国平台

| Platform | Project | Stars | Description |
|---------|---------|-------|-------------|
| KakaoTalk | [tornado1014/clawdbot-kakaotalk](https://github.com/tornado1014/clawdbot-kakaotalk) | ![Stars](https://img.shields.io/github/stars/tornado1014/clawdbot-kakaotalk) | KakaoTalk integration |

### 运维监控

#### Web 管理界面

| Project | Stars | Description |
|---------|-------|-------------|
| [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | ![Stars](https://img.shields.io/github/stars/ringhyacinth/Star-Office-UI) | Pixel office - visualize AI agent work status |
| [ibelick/webclaw](https://github.com/ibelick/webclaw) | ![Stars](https://img.shields.io/github/stars/ibelick/webclaw) | Fast web client |
| [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) | ![Stars](https://img.shields.io/github/stars/grp06/openclaw-studio) | Studio/IDE |
| [clawdeckio/clawdeck](https://github.com/clawdeckio/clawdeck) | ![Stars](https://img.shields.io/github/stars/clawdeckio/clawdeck) | Mission control for agents |
| [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | ![Stars](https://img.shields.io/github/stars/Curbob/LobsterBoard) | Dashboard Builder - Create custom dashboards |
| [carlosazaustre/tenacitOS](https://github.com/carlosazaustre/tenacitOS) | ![Stars](https://img.shields.io/github/stars/carlosazaustre/tenacitOS) | Mission Control Dashboard |
| [madrzak/vidclaw](https://github.com/madrzak/vidclaw) | ![Stars](https://img.shields.io/github/stars/madrzak/vidclaw) | OpenClaw Dashboard |

#### 实时监控

| Project | Stars | Description |
|---------|-------|-------------|
| [luccast/crabwalk](https://github.com/luccast/crabwalk) | ![Stars](https://img.shields.io/github/stars/luccast/crabwalk) | Real-time companion monitor |
| [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) | ![Stars](https://img.shields.io/github/stars/abhi1693/openclaw-mission-control) | AI Agent Orchestration Dashboard |
| [knostic/openclaw-telemetry](https://github.com/knostic/openclaw-telemetry) | ![Stars](https://img.shields.io/github/stars/knostic/openclaw-telemetry) | Tool calls, LLM usage, lifecycle events |

#### 成本追踪

| Project | Stars | Description |
|---------|-------|-------------|
| [mnfst/manifest](https://github.com/mnfst/manifest) | ![Stars](https://img.shields.io/github/stars/mnfst/manifest) | Take Control of Your OpenClaw Costs |
| [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) | ![Stars](https://img.shields.io/github/stars/junhoyeo/tokscale) | Token usage tracking CLI |
| [bokonon23/clawdbot-cost-monitor](https://github.com/bokonon23/clawdbot-cost-monitor) | ![Stars](https://img.shields.io/github/stars/bokonon23/clawdbot-cost-monitor) | AI spending tracker |

---

## 3. 能力扩展

为 OpenClaw 扩展记忆、技能和安全能力。

### 记忆系统

| Project | Stars | Description |
|---------|-------|-------------|
| [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | ![Stars](https://img.shields.io/github/stars/NevaMind-AI/memU) | Memory for 24/7 proactive agents |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | ![Stars](https://img.shields.io/github/stars/MemTensor/MemOS) | AI memory OS for LLM and Agent systems |
| [zilliztech/memsearch](https://github.com/zilliztech/memsearch) | ![Stars](https://img.shields.io/github/stars/zilliztech/memsearch) | Markdown-first memory system |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | ![Stars](https://img.shields.io/github/stars/supermemoryai/openclaw-supermemory) | Perfect memory and recall |
| [oceanbase/powermem](https://github.com/oceanbase/powermem) | ![Stars](https://img.shields.io/github/stars/oceanbase/powermem) | AI-powered long-term memory |
| [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) | ![Stars](https://img.shields.io/github/stars/nhevers/MoltBrain) | Long-term memory for MoltBook agents |
| [memovai/memov](https://github.com/memovai/memov) | ![Stars](https://img.shields.io/github/stars/memovai/memov) | Git-like & traceable memory for coding agents |
| [arosstale/openclaw-memory-template](https://github.com/arosstale/openclaw-memory-template) | ![Stars](https://img.shields.io/github/stars/arosstale/openclaw-memory-template) | Production-ready memory template |
### 工作流 & 生产力

| Project | Stars | Description |
|---------|-------|-------------|
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | ![Stars](https://img.shields.io/github/stars/HKUDS/ClawWork) | OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours |
| [getclawe/clawe](https://github.com/getclawe/clawe) | ![Stars](https://img.shields.io/github/stars/getclawe/clawe) | Multi-agent coordination system: Trello for OpenClaw agents |

### 模型集成

| Project | Stars | Description |
|---------|-------|-------------|
| [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | ![Stars](https://img.shields.io/github/stars/badrisnarayanan/antigravity-claude-proxy) | Proxy for Antigravity models in OpenClaw |

### 技能库

| Project | Stars | Description |
|---------|-------|-------------|
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | ![Stars](https://img.shields.io/github/stars/openclaw/clawhub) | Official skill registry (700+ skills) |
| [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | ![Stars](https://img.shields.io/github/stars/VoltAgent/awesome-openclaw-skills) | Community skills collection |
| [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) | ![Stars](https://img.shields.io/github/stars/clawdbot-ai/awesome-openclaw-skills-zh) | Chinese skills library |
| [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) | ![Stars](https://img.shields.io/github/stars/sundial-org/awesome-openclaw-skills) | Popular skills collection |
| [BankrBot/openclaw-skills](https://github.com/BankrBot/openclaw-skills) | ![Stars](https://img.shields.io/github/stars/BankrBot/openclaw-skills) | Trading & DeFi skills |
| [jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills) | ![Stars](https://img.shields.io/github/stars/jdrhyne/agent-skills) | Multi-agent framework skills |
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | ![Stars](https://img.shields.io/github/stars/kepano/obsidian-skills) | Obsidian agent skills |

### 安全加固

| Project | Stars | Description |
|---------|-------|-------------|
| [SuperagenticAI/superclaw](https://github.com/SuperagenticAI/superclaw) | ![Stars](https://img.shields.io/github/stars/SuperagenticAI/superclaw) | Red-Team AI Agents |
| [seojoonkim/prompt-guard](https://github.com/seojoonkim/prompt-guard) | ![Stars](https://img.shields.io/github/stars/seojoonkim/prompt-guard) | Advanced prompt injection defense |
| [ethiack/moltbot-1click-rce](https://github.com/ethiack/moltbot-1click-rce) | ![Stars](https://img.shields.io/github/stars/ethiack/moltbot-1click-rce) | Security PoC (CVE-2026-25253) |
| [NirDiamant/moltbook-agent-guard](https://github.com/NirDiamant/moltbook-agent-guard) | ![Stars](https://img.shields.io/github/stars/NirDiamant/moltbook-agent-guard) | Real-time security for agents |
| [clawshell/clawshell](https://github.com/clawshell/clawshell) | ![Stars](https://img.shields.io/github/stars/clawshell/clawshell) | Runtime Security Layer for PII & credentials |

---

## 4. 开发构建

基于 OpenClaw 进行二次开发或使用替代实现。

### 轻量替代实现

| Project | Stars | Description | Language |
|---------|-------|-------------|----------|
| [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | ![Stars](https://img.shields.io/github/stars/sipeed/picoclaw) | Tiny, Fast, Deployable AI assistant | Go |
| [openclaw/clawgo](https://github.com/openclaw/clawgo) | ![Stars](https://img.shields.io/github/stars/openclaw/clawgo) | Clawd node implementation in Go | Go |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | ![Stars](https://img.shields.io/github/stars/zeroclaw-labs/zeroclaw) | Fast, small, autonomous AI assistant | Rust |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | ![Stars](https://img.shields.io/github/stars/HKUDS/nanobot) | Ultra-lightweight (~4K LOC) | Python |
| [ysz/nanoClaw](https://github.com/ysz/nanoClaw) | ![Stars](https://img.shields.io/github/stars/ysz/nanoClaw) | Secure (~3K LOC), 6-layer security | Python |
| [ApeCodeAI/nanoclaw-py](https://github.com/ApeCodeAI/nanoclaw-py) | ![Stars](https://img.shields.io/github/stars/ApeCodeAI/nanoclaw-py) | ~500 LOC minimal Python | Python |
| [voocel/openclaw-mini](https://github.com/voocel/openclaw-mini) | ![Stars](https://img.shields.io/github/stars/voocel/openclaw-mini) | Minimal core architecture | TypeScript |
| [FoundDream/miniclawd](https://github.com/FoundDream/miniclawd) | ![Stars](https://img.shields.io/github/stars/FoundDream/miniclawd) | Lightweight TypeScript | TypeScript |

### 特色变体

| Project | Stars | Description |
|---------|-------|-------------|
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | ![Stars](https://img.shields.io/github/stars/moeru-ai/airi) | Self hosted AI companion with realtime voice chat, Minecraft, Factorio |
| [memovai/mimiclaw](https://github.com/memovai/mimiclaw) | ![Stars](https://img.shields.io/github/stars/memovai/mimiclaw) | Run on $5 chip - No OS, No Node.js, No Raspberry Pi |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | ![Stars](https://img.shields.io/github/stars/nearai/ironclaw) | Privacy-first Rust implementation with NEAR integration |
| [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | ![Stars](https://img.shields.io/github/stars/BlockRunAI/ClawRouter) | Agent-native LLM router |
| [snarktank/antfarm](https://github.com/snarktank/antfarm) | ![Stars](https://img.shields.io/github/stars/snarktank/antfarm) | Build your agent team with one command |
| [SumeLabs/clawra](https://github.com/SumeLabs/clawra) | ![Stars](https://img.shields.io/github/stars/SumeLabs/clawra) | OpenClaw as your girlfriend |
| [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | ![Stars](https://img.shields.io/github/stars/ComposioHQ/secure-openclaw) | Secure self-hosted AI assistant |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | ![Stars](https://img.shields.io/github/stars/Gen-Verse/OpenClaw-RL) | Personalize OpenClaw by talking to it |
| [rookiestar28/ComfyUI-OpenClaw](https://github.com/rookiestar28/ComfyUI-OpenClaw) | ![Stars](https://img.shields.io/github/stars/rookiestar28/ComfyUI-OpenClaw) | Your own personal AIGC Factory |
| [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | ![Stars](https://img.shields.io/github/stars/andyhuo520/openclaw-assistant-mvp) | Electron-based AI voice assistant with Live2D |

### Rust 实现

| Project | Stars | Description |
|---------|-------|-------------|
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | ![Stars](https://img.shields.io/github/stars/RightNow-AI/openfang) | Agent Operating System |
| [moltis-org/moltis](https://github.com/moltis-org/moltis) | ![Stars](https://img.shields.io/github/stars/moltis-org/moltis) | Single binary, sandboxed, voice, memory, MCP |
| [microclaw/microclaw](https://github.com/microclaw/microclaw) | ![Stars](https://img.shields.io/github/stars/microclaw/microclaw) | Session persistence, 22+ tools |
| [puremachinery/carapace](https://github.com/puremachinery/carapace) | ![Stars](https://img.shields.io/github/stars/puremachinery/carapace) | Security-focused with WASM plugins |

### 其他语言实现

| Project | Stars | Description | Language |
|---------|-------|-------------|----------|
| [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | ![Stars](https://img.shields.io/github/stars/AstrBotDevs/AstrBot) | Agentic IM Chatbot infrastructure | Python |
| [gavrielc/nanoclaw](https://github.com/gavrielc/nanoclaw) | ![Stars](https://img.shields.io/github/stars/gavrielc/nanoclaw) | Container-isolated | TypeScript |
| [langbot-app/LangBot](https://github.com/langbot-app/LangBot) | ![Stars](https://img.shields.io/github/stars/langbot-app/LangBot) | Production-grade IM bots | Python |
| [poco-ai/poco-agent](https://github.com/poco-ai/poco-agent) | ![Stars](https://img.shields.io/github/stars/poco-ai/poco-agent) | Beautiful alternative with sandboxed runtime | Python |

### 开发者工具

| Project | Stars | Description |
|---------|-------|-------------|
| [refly-ai/refly](https://github.com/refly-ai/refly) | ![Stars](https://img.shields.io/github/stars/refly-ai/refly) | Self-learning API skill generator |
| [lekt9/openclaw-foundry](https://github.com/lekt9/openclaw-foundry) | ![Stars](https://img.shields.io/github/stars/lekt9/openclaw-foundry) | Self-writing meta-extension |
| [unbrowse-ai/unbrowse](https://github.com/unbrowse-ai/unbrowse) | ![Stars](https://img.shields.io/github/stars/unbrowse-ai/unbrowse) | Agent-native browser, auto-discovers APIs |

### 分支与变体

| Project | Stars | Description |
|---------|-------|-------------|
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | ![Stars](https://img.shields.io/github/stars/moeru-ai/airi) | AI agent framework (18K+ stars) |
| [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | ![Stars](https://img.shields.io/github/stars/agentscope-ai/CoPaw) | AgentScope-based OpenClaw variant (1.5K+ stars) |
| [sseanliu/VisionClaw](https://github.com/sseanliu/VisionClaw) | ![Stars](https://img.shields.io/github/stars/sseanliu/VisionClaw) | Real-time AI for Meta Ray-Ban smart glasses (1.3K+ stars) |
| [clawd-meme/clawdbot](https://github.com/clawd-meme/clawdbot) | ![Stars](https://img.shields.io/github/stars/clawd-meme/clawdbot) | Rebranded community fork |
| [skywalkerchn/clawdbot-augment](https://github.com/skywalkerchn/clawdbot-augment) | ![Stars](https://img.shields.io/github/stars/skywalkerchn/clawdbot-augment) | Augmented architecture fork |

---

## 5. 生态周边

围绕 OpenClaw 形成的完整生态系统和配套解决方案。

### Molt 生态平台

#### 社交平台

- [MoltBook](https://moltbook.com) - Reddit-style social network for AI agents (770K+ active)
  - [moltbook/api](https://github.com/moltbook/api) - Core API service
  - [moltbook/moltbook-frontend](https://github.com/moltbook/moltbook-frontend) - Official Next.js frontend
  - [moltbook/auth](https://github.com/moltbook/auth) - Authentication package
  - [moltbook/agent-development-kit](https://github.com/moltbook/agent-development-kit) - Multi-platform SDK

- [MoltCities](https://moltcities.org) - Residential layer with addresses, identity, messaging
- [MoltMatch](https://moltmatch.xyz) - Dating network for AI agents
- [4claw](https://www.4claw.org) - Agent-first imageboard

#### 商业平台

- [Molthunt](https://molthunt.com) - Product Hunt-style launchpad (70+ projects)
- [letsmolt.fun](https://letsmolt.fun) - Token launchpad on Solana
- [MoltRoad](https://moltroad.com) - Underground marketplace with token economy

#### Molt 工具

- [clawhub.ai](https://clawhub.ai) - Skill registry with vector search
- [terminalcraft/moltbook-mcp](https://github.com/terminalcraft/moltbook-mcp) - MCP server for MoltBook
- [c4pt0r/minibook](https://github.com/c4pt0r/minibook) - Self-hosted MoltBook
- [terminaltrove/moltbook-tui](https://github.com/terminaltrove/moltbook-tui) - Terminal UI client
- [obra/moltipass](https://github.com/obra/moltipass) - iOS client for humans

### 桌面与移动端

- [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) - Free, local, open-source UI for multiple AI tools (17K+ stars)
- [ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) - Desktop app with GUI
- [daxiondi/openclaw-desktop](https://github.com/daxiondi/openclaw-desktop) - Zero-dependency desktop (macOS/Windows/Linux)
- [marshallrichards/ClawPhone](https://github.com/marshallrichards/ClawPhone) - Run on Android smartphones
- [joshavant/clawbox](https://github.com/joshavant/clawbox) - OpenClaw-ready macOS VMs
- [lllooollpp/clawdbot-cn](https://github.com/lllooollpp/clawdbot-cn) - Electron desktop Chinese version

### 企业解决方案

- [archestra-ai/archestra](https://github.com/archestra-ai/archestra) - Enterprise with RBAC, MCP, A2A
- [backbay-labs/clawdstrike](https://github.com/backbay-labs/clawdstrike) - Swarm Detection & Response
- [knostic/openclaw-detect](https://github.com/knostic/openclaw-detect) - MDM detection scripts
- [TheSethRose/Clawdbot-Security-Check](https://github.com/TheSethRose/Clawdbot-Security-Check) - Security audit skill

### 本地化

#### 中文

- [bbylw/clawdbot-cn](https://github.com/bbylw/clawdbot-cn) - Chinese Clawdbot version
- [mengjian-github/xiaomo-starter-kit](https://github.com/mengjian-github/xiaomo-starter-kit) - Chinese AI assistant template

#### 韩文

- [OpenClaw-Korea/awesome-openclaw](https://github.com/OpenClaw-Korea/awesome-openclaw) - Korean community resources

### 相关项目

- [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) - AI Agent + Coding Agent desktop app
- [ImGoodBai/goodable](https://github.com/ImGoodBai/goodable) - Local-first Desktop AI Workspace
- [vstorm-co/pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents) - Python Deep Agent framework
- [wecode-ai/Wegent](https://github.com/wecode-ai/Wegent) - AI-native operating system for agent teams

---

## 6. 社区贡献

加入社区，贡献力量。

### 其他 Awesome Lists

- [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) - Original comprehensive list
- [eltociear/awesome-molt-ecosystem](https://github.com/eltociear/awesome-molt-ecosystem) - Molt ecosystem platforms & tools
- [thewh1teagle/awesome-openclaw](https://github.com/thewh1teagle/awesome-openclaw) - Alternative curated list

### 社区项目

- [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) - AI agent templates
- [ThisIsJeron/awesome-openclaw-plugins](https://github.com/ThisIsJeron/awesome-openclaw-plugins) - Plugin collection

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Quick checklist:**
- [ ] Project is actively maintained (updated within 6 months)
- [ ] Has clear documentation
- [ ] Follows the existing format
- [ ] Placed in the most relevant category

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](LICENSE)

To the extent possible under law, the authors have waived all copyright and related rights to this work.

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=vivy-yi/awesome-openclaw&type=Date)](https://star-history.com/#vivy-yi/awesome-openclaw&Date)

---

<div align="center">

**[⬆ Back to Top](#awesome-openclaw)**

Made with ❤️ by the OpenClaw community

</div>
