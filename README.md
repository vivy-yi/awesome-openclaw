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
----------|-------|-------------|----------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | ![Stars](https://github.com/openclaw/openclaw/stargazers) | Main personal AI assistant - "The lobster way" | TypeScript | TypeScript |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | ![Stars](https://github.com/openclaw/clawhub/stargazers) | Official skill registry with 700+ skills | TypeScript | TypeScript |
| [openclaw/skills](https://github.com/openclaw/skills) | ![Stars](https://github.com/openclaw/skills/stargazers) | All versions of skills archived | TypeScript | TypeScript |
| [openclaw/lobster](https://github.com/openclaw/lobster) | ![Stars](https://github.com/openclaw/lobster/stargazers) | Workflow shell for pipelines and automations | TypeScript | TypeScript |
| [openclaw/openclaw.ai](https://github.com/openclaw/openclaw.ai) | ![Stars](https://github.com/openclaw/openclaw.ai/stargazers) | Official website (molt.bot) | TypeScript | TypeScript |
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

| Project | Stars | Description | Language |
----------|-------|-------------|----------|
| [qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | ![Stars](https://github.com/qwibitai/nanoclaw/stargazers) | Containerized lightweight with memory & scheduled jobs | TypeScript | TypeScript |
| [coollabsio/openclaw](https://github.com/coollabsio/openclaw) | ![Stars](https://github.com/coollabsio/openclaw/stargazers) | Fully featured & automated Docker images | TypeScript | TypeScript |
| [liam798/docker-openclawd](https://github.com/liam798/docker-openclawd) | ![Stars](https://github.com/liam798/docker-openclawd/stargazers) | 一键安装 Docker 部署方案 | TypeScript | TypeScript |
| [essamamdani/openclaw-coolify](https://github.com/essamamdani/openclaw-coolify) | ![Stars](https://github.com/essamamdani/openclaw-coolify/stargazers) | Coolify deployment template | TypeScript | TypeScript |
### 云平台

| Project | Stars | Description | Language |
----------|-------|-------------|----------|
| [1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel) | ![Stars](https://github.com/1Panel-dev/1Panel/stargazers) | VPS control panel with OpenClaw one-click deploy | Go | TypeScript |
| [getumbrel/umbrel](https://github.com/getumbrel/umbrel) | ![Stars](https://github.com/getumbrel/umbrel/stargazers) | Home server OS with OpenClaw support | Go | TypeScript |
| [cloudflare/moltworker](https://github.com/cloudflare/moltworker) | ![Stars](https://github.com/cloudflare/moltworker/stargazers) | Run on Cloudflare Workers (official Cloudflare) | TypeScript | TypeScript |
| [aws-samples/sample-OpenClaw-on-AWS-with-Bedrock](https://github.com/aws-samples/sample-OpenClaw-on-AWS-with-Bedrock) | ![Stars](https://github.com/aws-samples/sample-OpenClaw-on-AWS-with-Bedrock/stargazers) | AWS Bedrock integration | TypeScript | TypeScript |
| [miantiao-me/cloud-claw](https://github.com/miantiao-me/cloud-claw) | ![Stars](https://github.com/miantiao-me/cloud-claw/stargazers) | One-click on Cloudflare Containers | TypeScript | TypeScript |
| [digitalocean-labs/openclaw-appplatform](https://github.com/digitalocean-labs/openclaw-appplatform) | ![Stars](https://github.com/digitalocean-labs/openclaw-appplatform/stargazers) | DigitalOcean App Platform | TypeScript | TypeScript |
### 系统包管理

| Project | Stars | Description | Language |
----------|-------|-------------|----------|
| [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) | ![Stars](https://github.com/openclaw/nix-openclaw/stargazers) | Nix package manager integration | Nix | TypeScript |
| [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | ![Stars](https://github.com/openclaw/openclaw-ansible/stargazers) | Automated hardened installation with Ansible | YAML | TypeScript |
| [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) | ![Stars](https://github.com/openclaw/homebrew-tap/stargazers) | Homebrew tap for macOS | Ruby | TypeScript |
### 一键部署工具

| Project | Stars | Description | Language |
----------|-------|-------------|----------|
| [miaoxworld/OpenClawInstaller](https://github.com/miaoxworld/OpenClawInstaller) | ![Stars](https://github.com/miaoxworld/OpenClawInstaller/stargazers) | Chinese one-click deployment tool | TypeScript | TypeScript |
| [caopulan/fix-my-claw](https://github.com/caopulan/fix-my-claw) | ![Stars](https://github.com/caopulan/fix-my-claw/stargazers) | 24/7 watchdog with automatic recovery | TypeScript | TypeScript |
### 移动端 & 边缘部署

| Project | Stars | Description | Language |
----------|-------|-------------|----------|
| [mithun50/openclaw-termux](https://github.com/mithun50/openclaw-termux) | ![Stars](https://github.com/mithun50/openclaw-termux/stargazers) | Run on Android via Termux | Shell | TypeScript |
| [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | ![Stars](https://github.com/AidanPark/openclaw-android/stargazers) | Run on Android with single command | TypeScript | TypeScript |
| [joshavant/clawbox](https://github.com/joshavant/clawbox) | ![Stars](https://github.com/joshavant/clawbox/stargazers) | OpenClaw-ready macOS VMs | TypeScript | TypeScript |
### 平台集成

#### 国际平台

| Platform | Project | Stars | Description | Language |
----------|---------|-------|-------------|----------|
| Windows | [shanselman/openclaw-windows-hub](https://github.com/shanselman/openclaw-windows-hub) | ![Stars](https://github.com/shanselman/openclaw-windows-hub/stargazers) | System Tray + PowerToys | C# | TypeScript |
| Slack | [VizuaraAILabs/Slack-ClawdBot](https://github.com/VizuaraAILabs/Slack-ClawdBot) | ![Stars](https://github.com/VizuaraAILabs/Slack-ClawdBot/stargazers) | Slack integration | TypeScript | TypeScript |
| iOS Voice | [chrisherold/clawdy](https://github.com/chrisherold/clawdy) | ![Stars](https://github.com/chrisherold/clawdy/stargazers) | Voice interface | Swift | TypeScript |
#### 中国平台

| Platform | Project | Stars | Description | Language |
----------|---------|-------|-------------|----------|
| 飞书/Lark | [m1heng/clawdbot-feishu](https://github.com/m1heng/clawdbot-feishu) | ![Stars](https://github.com/m1heng/clawdbot-feishu/stargazers) | Feishu integration | TypeScript | TypeScript |
| Bundle | [justlovemaki/OpenClaw-Docker-CN-IM](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM) | ![Stars](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM/stargazers) | Docker 多平台集成 | TypeScript | TypeScript |
| Bundle | [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) | ![Stars](https://github.com/BytePioneer-AI/openclaw-china/stargazers) | Feishu, DingTalk, QQ, WeChat 插件集合 | TypeScript | TypeScript |
| 钉钉 | [soimy/openclaw-channel-dingtalk](https://github.com/soimy/openclaw-channel-dingtalk) | ![Stars](https://github.com/soimy/openclaw-channel-dingtalk/stargazers) | DingTalk channel | TypeScript | TypeScript |
| 飞书/Lark | [AlexAnys/feishu-openclaw](https://github.com/AlexAnys/feishu-openclaw) | ![Stars](https://github.com/AlexAnys/feishu-openclaw/stargazers) | Feishu/Lark integration | TypeScript | TypeScript |
| 微信 | [freestylefly/openclaw-wechat](https://github.com/freestylefly/openclaw-wechat) | ![Stars](https://github.com/freestylefly/openclaw-wechat/stargazers) | Personal WeChat | TypeScript | TypeScript |
| 微信 | [11haonb/wecom-openclaw-plugin](https://github.com/11haonb/wecom-openclaw-plugin) | ![Stars](https://github.com/11haonb/wecom-openclaw-plugin/stargazers) | WeChat Work plugin | TypeScript | TypeScript |
| QQ | [constansino/openclaw_qq](https://github.com/constansino/openclaw_qq) | ![Stars](https://github.com/constansino/openclaw_qq/stargazers) | QQ (OneBot v11) | Python | TypeScript |
| 轻量 | [openmozi/openmozi](https://github.com/openmozi/openmozi) | ![Stars](https://github.com/openmozi/openmozi/stargazers) | 轻量级支持中文 IM | Python | TypeScript |
#### 韩国平台

| Platform | Project | Stars | Description | Language |
----------|---------|-------|-------------|----------|
| KakaoTalk | [tornado1014/clawdbot-kakaotalk](https://github.com/tornado1014/clawdbot-kakaotalk) | ![Stars](https://github.com/tornado1014/clawdbot-kakaotalk/stargazers) | KakaoTalk integration | TypeScript | TypeScript |
### 运维监控

#### Web 管理界面

| Project | Stars | Description | Language |
----------|-------|-------------|----------|
| [ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | ![Stars](https://github.com/ringhyacinth/Star-Office-UI/stargazers) | Pixel office - visualize AI agent work status | TypeScript | TypeScript |
| [ibelick/webclaw](https://github.com/ibelick/webclaw) | ![Stars](https://github.com/ibelick/webclaw/stargazers) | Fast web client | TypeScript | TypeScript |
| [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) | ![Stars](https://github.com/grp06/openclaw-studio/stargazers) | Studio/IDE | TypeScript | TypeScript |
| [clawdeckio/clawdeck](https://github.com/clawdeckio/clawdeck) | ![Stars](https://github.com/clawdeckio/clawdeck/stargazers) | Mission control for agents | TypeScript | TypeScript |
| [Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | ![Stars](https://github.com/Curbob/LobsterBoard/stargazers) | Dashboard Builder - Create custom dashboards | TypeScript | TypeScript |
| [carlosazaustre/tenacitOS](https://github.com/carlosazaustre/tenacitOS) | ![Stars](https://github.com/carlosazaustre/tenacitOS/stargazers) | Mission Control Dashboard | TypeScript | TypeScript |
| [madrzak/vidclaw](https://github.com/madrzak/vidclaw) | ![Stars](https://github.com/madrzak/vidclaw/stargazers) | OpenClaw Dashboard | TypeScript | TypeScript |
#### 实时监控

| Project | Stars | Description | Language |
----------|-------|-------|-------------|
| [luccast/crabwalk](https://github.com/luccast/crabwalk) | ![Stars](https://github.com/luccast/crabwalk/stargazers) | Real-time companion monitor | TypeScript |
| [abhi1693/openclaw-mission-control](https://github.com/abhi1693/openclaw-mission-control) | ![Stars](https://github.com/abhi1693/openclaw-mission-control/stargazers) | AI Agent Orchestration Dashboard | TypeScript |
| [knostic/openclaw-telemetry](https://github.com/knostic/openclaw-telemetry) | ![Stars](https://github.com/knostic/openclaw-telemetry/stargazers) | Tool calls, LLM usage, lifecycle events | TypeScript |
#### 成本追踪

| Project | Stars | Description | Language |
----------|-------|-------|-------------|
| [mnfst/manifest](https://github.com/mnfst/manifest) | ![Stars](https://github.com/mnfst/manifest/stargazers) | Take Control of Your OpenClaw Costs | TypeScript |
| [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) | ![Stars](https://github.com/junhoyeo/tokscale/stargazers) | Token usage tracking CLI | TypeScript |
| [bokonon23/clawdbot-cost-monitor](https://github.com/bokonon23/clawdbot-cost-monitor) | ![Stars](https://github.com/bokonon23/clawdbot-cost-monitor/stargazers) | AI spending tracker | TypeScript |
---

## 3. 能力扩展

为 OpenClaw 扩展记忆、技能和安全能力。

### 记忆系统

| Project | Stars | Description | Language |
----------|-------|-------|-------------|
| [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | ![Stars](https://github.com/NevaMind-AI/memU/stargazers) | Memory for 24/7 proactive agents | TypeScript |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | ![Stars](https://github.com/MemTensor/MemOS/stargazers) | AI memory OS for LLM and Agent systems | TypeScript |
| [zilliztech/memsearch](https://github.com/zilliztech/memsearch) | ![Stars](https://github.com/zilliztech/memsearch/stargazers) | Markdown-first memory system | TypeScript |
| [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | ![Stars](https://github.com/supermemoryai/openclaw-supermemory/stargazers) | Perfect memory and recall | TypeScript |
| [oceanbase/powermem](https://github.com/oceanbase/powermem) | ![Stars](https://github.com/oceanbase/powermem/stargazers) | AI-powered long-term memory | TypeScript |
| [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) | ![Stars](https://github.com/nhevers/MoltBrain/stargazers) | Long-term memory for MoltBook agents | TypeScript |
| [memovai/memov](https://github.com/memovai/memov) | ![Stars](https://github.com/memovai/memov/stargazers) | Git-like & traceable memory for coding agents | TypeScript |
| [arosstale/openclaw-memory-template](https://github.com/arosstale/openclaw-memory-template) | ![Stars](https://github.com/arosstale/openclaw-memory-template/stargazers) | Production-ready memory template | TypeScript |
### 工作流 & 生产力

| Project | Stars | Description | Language |
----------|-------|-------|-------------|
| [HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | ![Stars](https://github.com/HKUDS/ClawWork/stargazers) | OpenClaw as Your AI Coworker - 💰 $10K earned in 7 Hours | TypeScript |
| [getclawe/clawe](https://github.com/getclawe/clawe) | ![Stars](https://github.com/getclawe/clawe/stargazers) | Multi-agent coordination system: Trello for OpenClaw agents | TypeScript |
### 模型集成

| Project | Stars | Description | Language |
----------|-------|-------|-------------|
| [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) | ![Stars](https://github.com/badrisnarayanan/antigravity-claude-proxy/stargazers) | Proxy for Antigravity models in OpenClaw | TypeScript |
### 技能库

| Project | Stars | Description | Language |
----------|-------|-------|-------------|
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | ![Stars](https://github.com/openclaw/clawhub/stargazers) | Official skill registry (700+ skills) | TypeScript |
| [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | ![Stars](https://github.com/VoltAgent/awesome-openclaw-skills/stargazers) | Community skills collection | TypeScript |
| [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) | ![Stars](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh/stargazers) | Chinese skills library | TypeScript |
| [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) | ![Stars](https://github.com/sundial-org/awesome-openclaw-skills/stargazers) | Popular skills collection | TypeScript |
| [jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills) | ![Stars](https://github.com/jdrhyne/agent-skills/stargazers) | Multi-agent framework skills | TypeScript |
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | ![Stars](https://github.com/kepano/obsidian-skills/stargazers) | Obsidian agent skills | TypeScript |
### 安全加固

| Project | Stars | Description | Language |
----------|-------|-------|-------------|
| [SuperagenticAI/superclaw](https://github.com/SuperagenticAI/superclaw) | ![Stars](https://github.com/SuperagenticAI/superclaw/stargazers) | Red-Team AI Agents | TypeScript |
| [ethiack/moltbot-1click-rce](https://github.com/ethiack/moltbot-1click-rce) | ![Stars](https://github.com/ethiack/moltbot-1click-rce/stargazers) | Security PoC (CVE-2026-25253) | TypeScript |
| [NirDiamant/moltbook-agent-guard](https://github.com/NirDiamant/moltbook-agent-guard) | ![Stars](https://github.com/NirDiamant/moltbook-agent-guard/stargazers) | Real-time security for agents | TypeScript |
| [clawshell/clawshell](https://github.com/clawshell/clawshell) | ![Stars](https://github.com/clawshell/clawshell/stargazers) | Runtime Security Layer for PII & credentials | TypeScript |
---

## 4. 开发构建

基于 OpenClaw 进行二次开发或使用替代实现。

### 轻量替代实现

| Project | Stars | Description | Language |
----------|-------|-------------|----------|
| [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | ![Stars](https://github.com/sipeed/picoclaw/stargazers) | Tiny, Fast, Deployable AI assistant | Go | TypeScript |
| [openclaw/clawgo](https://github.com/openclaw/clawgo) | ![Stars](https://github.com/openclaw/clawgo/stargazers) | Clawd node implementation in Go | Go | TypeScript |
| [zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | ![Stars](https://github.com/zeroclaw-labs/zeroclaw/stargazers) | Fast, small, autonomous AI assistant | Rust | TypeScript |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | ![Stars](https://github.com/HKUDS/nanobot/stargazers) | Ultra-lightweight (~4K LOC) | Python | TypeScript |
| [ysz/nanoClaw](https://github.com/ysz/nanoClaw) | ![Stars](https://github.com/ysz/nanoClaw/stargazers) | Secure (~3K LOC), 6-layer security | Python | TypeScript |
| [ApeCodeAI/nanoclaw-py](https://github.com/ApeCodeAI/nanoclaw-py) | ![Stars](https://github.com/ApeCodeAI/nanoclaw-py/stargazers) | ~500 LOC minimal Python | Python | TypeScript |
| [voocel/openclaw-mini](https://github.com/voocel/openclaw-mini) | ![Stars](https://github.com/voocel/openclaw-mini/stargazers) | Minimal core architecture | TypeScript | TypeScript |
| [FoundDream/miniclawd](https://github.com/FoundDream/miniclawd) | ![Stars](https://github.com/FoundDream/miniclawd/stargazers) | Lightweight TypeScript | TypeScript | TypeScript |
### 特色变体

| Project | Stars | Description | Language |
----------|-------|-------|-------------|
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | ![Stars](https://github.com/moeru-ai/airi/stargazers) | Self hosted AI companion with realtime voice chat, Minecraft, Factorio | TypeScript |
| [memovai/mimiclaw](https://github.com/memovai/mimiclaw) | ![Stars](https://github.com/memovai/mimiclaw/stargazers) | Run on $5 chip - No OS, No Node.js, No Raspberry Pi | TypeScript |
| [nearai/ironclaw](https://github.com/nearai/ironclaw) | ![Stars](https://github.com/nearai/ironclaw/stargazers) | Privacy-first Rust implementation with NEAR integration | TypeScript |
| [BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | ![Stars](https://github.com/BlockRunAI/ClawRouter/stargazers) | Agent-native LLM router | TypeScript |
| [snarktank/antfarm](https://github.com/snarktank/antfarm) | ![Stars](https://github.com/snarktank/antfarm/stargazers) | Build your agent team with one command | TypeScript |
| [SumeLabs/clawra](https://github.com/SumeLabs/clawra) | ![Stars](https://github.com/SumeLabs/clawra/stargazers) | OpenClaw as your girlfriend | TypeScript |
| [ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | ![Stars](https://github.com/ComposioHQ/secure-openclaw/stargazers) | Secure self-hosted AI assistant | TypeScript |
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | ![Stars](https://github.com/Gen-Verse/OpenClaw-RL/stargazers) | Personalize OpenClaw by talking to it | TypeScript |
| [rookiestar28/ComfyUI-OpenClaw](https://github.com/rookiestar28/ComfyUI-OpenClaw) | ![Stars](https://github.com/rookiestar28/ComfyUI-OpenClaw/stargazers) | Your own personal AIGC Factory | TypeScript |
| [andyhuo520/openclaw-assistant-mvp](https://github.com/andyhuo520/openclaw-assistant-mvp) | ![Stars](https://github.com/andyhuo520/openclaw-assistant-mvp/stargazers) | Electron-based AI voice assistant with Live2D | TypeScript |
### Rust 实现

| Project | Stars | Description | Language |
----------|-------|-------|-------------|
| [RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | ![Stars](https://github.com/RightNow-AI/openfang/stargazers) | Agent Operating System | TypeScript |
| [moltis-org/moltis](https://github.com/moltis-org/moltis) | ![Stars](https://github.com/moltis-org/moltis/stargazers) | Single binary, sandboxed, voice, memory, MCP | TypeScript |
| [microclaw/microclaw](https://github.com/microclaw/microclaw) | ![Stars](https://github.com/microclaw/microclaw/stargazers) | Session persistence, 22+ tools | TypeScript |
| [puremachinery/carapace](https://github.com/puremachinery/carapace) | ![Stars](https://github.com/puremachinery/carapace/stargazers) | Security-focused with WASM plugins | TypeScript |
### 其他语言实现

| Project | Stars | Description | Language |
----------|-------|-------------|----------|
| [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) | ![Stars](https://github.com/AstrBotDevs/AstrBot/stargazers) | Agentic IM Chatbot infrastructure | Python | TypeScript |
| [langbot-app/LangBot](https://github.com/langbot-app/LangBot) | ![Stars](https://github.com/langbot-app/LangBot/stargazers) | Production-grade IM bots | Python | TypeScript |
| [poco-ai/poco-agent](https://github.com/poco-ai/poco-agent) | ![Stars](https://github.com/poco-ai/poco-agent/stargazers) | Beautiful alternative with sandboxed runtime | Python | TypeScript |
### 开发者工具

| Project | Stars | Description | Language |
----------|-------|-------|-------------|
| [refly-ai/refly](https://github.com/refly-ai/refly) | ![Stars](https://github.com/refly-ai/refly/stargazers) | Self-learning API skill generator | TypeScript |
| [lekt9/openclaw-foundry](https://github.com/lekt9/openclaw-foundry) | ![Stars](https://github.com/lekt9/openclaw-foundry/stargazers) | Self-writing meta-extension | TypeScript |
| [unbrowse-ai/unbrowse](https://github.com/unbrowse-ai/unbrowse) | ![Stars](https://github.com/unbrowse-ai/unbrowse/stargazers) | Agent-native browser, auto-discovers APIs | TypeScript |
### 分支与变体

| Project | Stars | Description | Language |
----------|-------|-------|-------------|
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | ![Stars](https://github.com/moeru-ai/airi/stargazers) | AI agent framework (18K+ stars) | TypeScript |
| [agentscope-ai/CoPaw](https://github.com/agentscope-ai/CoPaw) | ![Stars](https://github.com/agentscope-ai/CoPaw/stargazers) | AgentScope-based OpenClaw variant (1.5K+ stars) | TypeScript |
| [sseanliu/VisionClaw](https://github.com/sseanliu/VisionClaw) | ![Stars](https://github.com/sseanliu/VisionClaw/stargazers) | Real-time AI for Meta Ray-Ban smart glasses (1.3K+ stars) | TypeScript |
| [clawd-meme/clawdbot](https://github.com/clawd-meme/clawdbot) | ![Stars](https://github.com/clawd-meme/clawdbot/stargazers) | Rebranded community fork | TypeScript |
| [skywalkerchn/clawdbot-augment](https://github.com/skywalkerchn/clawdbot-augment) | ![Stars](https://github.com/skywalkerchn/clawdbot-augment/stargazers) | Augmented architecture fork | TypeScript |
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
