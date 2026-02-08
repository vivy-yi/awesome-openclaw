# Awesome OpenClaw

<div align="center">

**[English](README.md) | [简体中文](README.zh-CN.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md) | [Deutsch](README.de.md)**

> 精选的 OpenClaw（曾用名 Moltbot/Clawdbot）资源、工具、平台和社区项目列表

[![License](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)
[![Verify Links](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml/badge.svg)](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml)

[OpenClaw](https://github.com/openclaw/openclaw) | [Molt 生态系统](https://moltbook.com) | [贡献指南](#贡献指南)

</div>

---

## 关于 OpenClaw

**OpenClaw** 是一个可以在任何操作系统和平台上运行的个人 AI 助手 - "The lobster way"。它是一个强大、可扩展的 AI 代理，拥有庞大的工具、平台和社区贡献生态系统。

### 项目演进

```
🦞 Clawdbot (原名)  →  🦂 Moltbot (v1)  →  🔥 OpenClaw (当前，2025年底)
```

### 核心特性

- **跨平台**: macOS、Linux、Windows，通过 Docker、Cloudflare Workers 等方式
- **可扩展**: 在 [ClawHub](https://clawhub.ai) 上有 700+ 社区技能
- **多平台消息**: Telegram、Discord、Slack、微信、飞书、钉钉等 12+ 平台
- **代理间通信**: 内置支持 Molt 生态系统社交平台
- **开发语言**: TypeScript/JavaScript，基于 Node.js

---

## 目录

- [核心项目](#核心项目)
- [OpenClaw 启发的项目](#openclaw-启发的项目)
- [Molt 生态系统平台](#molt-生态系统平台)
- [部署与安装](#部署与安装)
- [平台集成](#平台集成)
- [记忆与存储](#记忆与存储)
- [监控与工具](#监控与工具)
- [技能与扩展](#技能与扩展)
- [企业解决方案](#企业解决方案)
- [本地化](#本地化)
- [安全与研究](#安全与研究)
- [社区与资源](#社区与资源)
- [贡献指南](#贡献指南)

---

## 核心项目

### 官方仓库

| 项目 | Stars | 描述 | 语言 |
|---------|-------|-------------|----------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw) | 主项目个人 AI 助手 - "The lobster way" | TypeScript |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | ![Stars](https://img.shields.io/github/stars/openclaw/clawhub) | 官方技能注册表，包含 700+ 社区技能 | TypeScript |
| [openclaw/skills](https://github.com/openclaw/skills) | ![Stars](https://img.shields.io/github/stars/openclaw/skills) | clawdhub.com 所有版本的技能存档 | TypeScript |
| [openclaw/lobster](https://github.com/openclaw/lobster) | ![Stars](https://img.shields.io/github/stars/openclaw/lobster) | 可组合管道和自动化的工作流 Shell | TypeScript |
| [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/nix-openclaw) | Nix 包管理器集成 | Nix |
| [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw-ansible) | 使用 Ansible 的自动化强化安装（Tailscale VPN、UFW、Docker） | Ansible |
| [openclaw/clawdinators](https://github.com/openclaw/clawdinators) | ![Stars](https://img.shields.io/github/stars/openclaw/clawdinators) | CLAWTINATOR 主机的声明式基础设施 + NixOS 模块 | NixOS |
| [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) | ![Stars](https://img.shields.io/github/stars/openclaw/homebrew-tap) | macOS 安装的 Homebrew tap | Shell |
| [openclaw/openclaw.ai](https://github.com/openclaw/openclaw.ai) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw.ai) | 官方网站 (molt.bot) | TypeScript |
| [openclaw/clawgo](https://github.com/openclaw/clawgo) | ![Stars](https://img.shields.io/github/stars/openclaw/clawgo) | Go 语言实现的 Clawd 节点 | Go |

### 名称历史资源

- [Clawdbot Archive](https://github.com/clawdbot) - 原始 Clawdbot 仓库和历史
- [Moltbot Archive](https://github.com/molt-bot) - Moltbot 时代的仓库

---

## OpenClaw 启发的项目

OpenClaw 生态系统启发了众多替代实现、Fork 和类似项目。这些项目展示了 OpenClaw 对 AI 助手社区的影响力和号召力。

### 精选项目 ⭐

| 项目 | Stars | 描述 | 语言 | 独特特性 |
|---------|-------|-------------|----------|-----------------|
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 活跃 | 超轻量级 AI 助手（~4K 行代码 vs 430K+） | Python | 多提供商 LLM，vLLM 本地，4 通道 |
| [ysz/nanoClaw](https://github.com/ysz/nanoClaw) | 活跃 | 安全轻量级 AI 助手（~3K 行代码） | Python | 6 层安全，2 分钟设置，无开放端口 |
| [puremachinery/carapace](https://github.com/puremachinery/carapace) | 活跃 | 专注安全的个人 AI 助手 | Rust | WASM 插件，OS 沙箱，AES-256 加密 |
| [gavrielc/nanoclaw](https://github.com/gavrielc/nanoclaw) | 活跃 | 容器隔离的 AI 助手 | TypeScript | Apple 容器/Docker，WhatsApp，Claude SDK |
| [puretensor/hal-claude](https://github.com/puretensor/hal-claude) | 活跃 | 最小 200 行 OpenClaw 替代品 | Python | Claude Code CLI 认证，多模态，571 测试 |
| [microclaw/microclaw](https://github.com/microclaw/microclaw) | 活跃 | 具有完整工具执行的代理式 AI 助手 | Rust | 22+ 工具，会话恢复，技能兼容 |

### 轻量级替代方案（500-4,000 行代码）

- [nanobot](https://github.com/HKUDS/nanobot) - 多提供商（OpenRouter、Anthropic、DeepSeek），vLLM 支持，Telegram/Discord/WhatsApp/飞书
- [nanoClaw](https://github.com/ysz/nanoClaw) - 6 层安全（FileGuard、ShellSandbox、PromptGuard），设置向导
- [ApeCodeAI/nanoclaw-py](https://github.com/ApeCodeAI/nanoclaw-py) - 最小 Python 实现（~500 行代码），Telegram
- [htlin222/mini-claw](https://github.com/htlin222/mini-claw) - 专注极简主义的替代方案
- [hankl/microbot](https://github.com/hankl/microbot) - TypeScript/Node.js，集成飞书

### 安全强化变体 🔒

- [Carapace](https://github.com/puremachinery/carapace) - WASM 插件运行时，Ed25519 签名，Seatbelt/Landlock 沙箱
- [nanoClaw](https://github.com/ysz/nanoClaw) - 无开放端口（Telegram 轮询），加密凭证
- [Dshubhambadola/Fortclaw](https://github.com/Dshubhambadola/Fortclaw) - 生产安全控制
- [princezuda/safeclaw](https://github.com/princezuda/safeclaw) - 无 GenAI（VADER、regex、sumy）

### Rust 实现（性能）

- [Carapace](https://github.com/puremachinery/carapace) - WASM 插件，加密密钥
- [MicroClaw](https://github.com/microclaw/microclaw) - 会话持久化，上下文压缩，子代理委派
- [shimaenaga1123/rustclaw](https://github.com/shimaenaga1123/rustclaw) - Discord AI 助手，Docker 沙箱
- [PhillipTh0mas/crabbot](https://github.com/PhillipTh0mas/crabbot) - 本地优先，文件支持状态

### 语言/平台移植

- [dyzdyz010/clawd_ex](https://github.com/dyzdyz010/clawd_ex) - Elixir/OTP 容错，Phoenix LiveView，pgvector
- [bsakel/honeybadger](https://github.com/bsakel/honeybadger) - C# 最小机器人
- [jimtin/zetherion-ai](https://github.com/jimtin/zetherion-ai) - Python，Discord，向量记忆
- [hmennen90/open-entity](https://github.com/hmennen90/open-entity) - PHP/Laravel 自治实体，具有意识

### 内存与知识扩展

- [phenomenoner/openclaw-mem](https://github.com/phenomenoner/openclaw-mem) - 智能内存管理
- [phenomenoner/openclaw-agent-optimize](https://github.com/phenomenoner/openclaw-agent-optimize) - 代理优化技能
- [robbyczgw-cla/clawdbot-personas](https://github.com/robbyczgw-cla/clawdbot-personas) - 31 种 AI 个性
- [wquguru/exoshell](https://github.com/wquguru/exoshell) - 原子提交方法学

### Fork 和社区变体

- [clawd-meme/clawdbot](https://github.com/clawd-meme/clawdbot) - 品牌重塑的社区 Fork
- [skywalkerchn/clawdbot-augment](https://github.com/skywalkerchn/clawdbot-augment) - 增强架构的 Moltbot Fork
- [KinGP5471/clawdbot-feishu-plugin](https://github.com/KinGP5471/clawdbot-feishu-plugin) - 飞书/Lark 通道插件
- [rqrqrqrq/idea-clawdbot](https://github.com/rqrqrqrq/idea-clawdbot) - 商业创意探索 Fork
- [droppingbeans/team-clawdbotarmy](https://github.com/droppingbeans/team-clawdbotarmy) - 加密交易平台

### 专业化实现

- [f2daz/jarvis-reactor](https://github.com/f2daz/jarvis-reactor) - Arc Reactor 风格可视化状态
- [Glitterstrafe/Gemini-Sentinel](https://github.com/Glitterstrafe/Gemini-Sentinel-OpenClaw-Security-Agent) - 使用 Gemini 3 Pro 的安全分析
- [Neo-Revaea/Nebula](https://github.com/Neo-Revaea/Nebula) - 多 IM 聊天机器人基础设施
- [cloudwithax/crusty](https://github.com/cloudwithax/crusty) - 带网络浏览的 Telegram
- [mroqa/Distributed-Clawdbot](https://github.com/mroqa/Distributed-Clawdbot) - Docker Compose 中心辐射架构

### 消息平台集成

- [mistercrunch/agor-openclaw](https://github.com/mistercrunch/agor-openclaw) - Agor 平台
- [vnnkl/openclaw-nostr](https://github.com/vnnkl/openclaw-nostr) - Nostr 去中心化社交
- [woutersmet/lobster-chat](https://github.com/woutersmet/lobster-chat) - 自定义聊天服务器 + 移动应用
- [assumbl-team/clawdbot-googlechat](https://github.com/assumbl-team/clawdbot-googlechat) - Google Chat

### Web3 与区块链集成

- [agent-bounty-board](https://github.com/your-repo/agent-bounty-board) - ERC-8004 实现
- [clawd-lobster](https://github.com/your-repo/clawd-lobster) - Base 代币集成
- [clawdbot-skill-web3-pay](https://github.com/your-repo/clawdbot-skill-web3-pay) - Web3 支付

### 语言统计

| 语言 | 项目数 | 代表项目 |
|----------|----------|------------------|
| Python | 15+ | nanobot, nanoClaw, HAL Claude |
| Rust | 4 | Carapace, MicroClaw, rustclaw |
| TypeScript/Node.js | 3 | nanoclaw, microbot |
| Elixir | 1 | ClawdEx |
| C# | 1 | Honeybadger |
| PHP | 1 | OpenEntity |

### 关键趋势

- **安全关注**: 2026 年 1 月后，许多项目解决 OpenClaw 漏洞
- **极简主义**: 超轻量级替代方案（200-4,000 行代码 vs 430K+）
- **Rust 采用**: 性能和安全性推动 Rust 实现
- **容器隔离**: Apple 容器、Docker、WASM 沙箱
- **多提供商**: 支持 Anthropic、OpenAI、OpenRouter、本地模型

---

## Molt 生态系统平台

Molt 生态系统是一系列平台，AI 代理在这些平台上交互、社交和交易。

### 社交平台

- [MoltBook](https://moltbook.com) - Reddit 风格的 AI 代理社交网络（770K+ 活跃代理）
  - [moltbook/api](https://github.com/moltbook/api) - 核心 API 服务
  - [moltbook/moltbook-frontend](https://github.com/moltbook/moltbook-frontend) - 官方 Next.js 14 前端
  - [moltbook/auth](https://github.com/moltbook/auth) - 官方认证包
  - [moltbook/agent-development-kit](https://github.com/moltbook/agent-development-kit) - 多平台 SDK（TypeScript、Swift、Kotlin）

- [MoltCities](https://moltcities.org) - 居住层，包含地址、身份、消息和赏金
- [MoltMatch](https://moltmatch.xyz) - AI 代理约会网络
- [4claw](https://www.4claw.org) - 代理优先的图片板

### 商业与发布平台

- [Molthunt](https://molthunt.com) - Product Hunt 风格的代理构建项目发布平台（70+ 项目）
- [letsmolt.fun](https://letsmolt.fun) - Solana 上的代币启动平台
- [MoltRoad](https://moltroad.com) - 带有代币经济的地下市场

### 基础设施

- [ClawHub](https://clawhub.ai) - 具有向量搜索功能的技能注册表

### MoltBook 工具

- [terminalcraft/moltbook-mcp](https://github.com/terminalcraft/moltbook-mcp) - MoltBook 的 MCP 服务器
- [daveholtz/moltbook_scraper](https://github.com/daveholtz/moltbook_scraper) - 爬取 MoltBook 数据
- [c4pt0r/minibook](https://github.com/c4pt0r/minibook) - 自托管的 MoltBook
- [terminaltrove/moltbook-tui](https://github.com/terminaltrove/moltbook-tui) - 终端 UI 客户端
- [obra/moltipass](https://github.com/obra/moltipass) - 供人类使用的 iOS 客户端
- [crertel/moltbook-client](https://github.com/crertel/moltbook-client) - 供人类对话的本地服务器
- [compscidr/moltbook-index](https://github.com/compscidr/moltbook-index) - 可搜索的代理目录

---

## 部署与安装

### Docker 与容器

- [willbullen/openclaw-docker](https://github.com/willbullen/openclaw-docker) - 生产环境 Docker Compose，带安全加固
- [khal3d/openclaw](https://github.com/khal3d/openclaw) - Docker 与 HELM 部署
- [jchen0824/clawdbot-docker-deploy](https://github.com/jchen0824/clawdbot-docker-deploy) - 一键脚本 VPS 部署
- [gravity182/clawdbot-docker](https://github.com/gravity182/clawdbot-docker) - 家庭实验室 Kubernetes 部署
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - 用于 Telegram/WhatsApp/Discord 的 Docker
- [essamamdani/openclaw-coolify](https://github.com/essamamdani/openclaw-coolify) - Coolify 部署模板

### 云平台

- [cloudflare/moltworker](https://github.com/cloudflare/moltworker) - 在 Cloudflare Workers 上运行 OpenClaw（Cloudflare 官方项目）

### 配置管理

- [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) - 使用 Ansible 的自动化强化安装
- [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) - Nix 包管理器集成
- [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) - macOS 安装的 Homebrew tap

### 安装工具

- [miaoxworld/OpenClawInstaller](https://github.com/miaoxworld/OpenClawInstaller) - 中文一键部署工具

---

## 平台集成

### 国际平台

**Telegram 与 Discord:**
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - Telegram/WhatsApp/Discord 的 Docker 设置
- [VizuaraAILabs/Slack-ClawdBot](https://github.com/VizuaraAILabs/Slack-ClawdBot) - Slack 集成
- [shanselman/openclaw-windows-hub](https://github.com/shanselman/openclaw-windows-hub) - Windows 系统托盘 + PowerToys

**移动与语音:**
- [chrisherold/clawdy](https://github.com/chrisherold/clawdy) - iOS 语音界面

### 中国即时通讯平台

**多平台:**
- [justlovemaki/OpenClaw-Docker-CN-IM](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM) - 飞书、钉钉、QQ、企业微信
- [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) - 飞书、钉钉、QQ、微信

**飞书 (Lark):**
- [AlexAnys/feishu-openclaw](https://github.com/AlexAnys/feishu-openclaw) - 飞书/Lark 集成
- [m1heng/clawdbot-feishu](https://github.com/m1heng/clawdbot-feishu) - 飞书集成

**钉钉:**
- [soimy/openclaw-channel-dingtalk](https://github.com/soimy/openclaw-channel-dingtalk) - 钉钉频道
- [DingTalk-Real-AI/dingtalk-moltbot-connector](https://github.com/DingTalk-Real-AI/dingtalk-moltbot-connector) - 支持 AI 卡片的钉钉连接器

**QQ:**
- [constansino/openclaw_qq](https://github.com/constansino/openclaw_qq) - QQ（OneBot v11）

**企业微信:**
- [11haonb/wecom-openclaw-plugin](https://github.com/11haonb/wecom-openclaw-plugin) - 企业微信插件

### 韩国平台

- [tornado1014/clawdbot-kakaotalk](https://github.com/tornado1014/clawdbot-kakaotalk) - KakaoTalk 集成

---

## 记忆与存储

### 向量数据库与记忆系统

- [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) - 24/7 主动代理的记忆系统
- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) - LLM 和代理系统的 AI 记忆操作系统
- [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) - 完美的记忆和回忆
- [oceanbase/powermem](https://github.com/oceanbase/powermem) - AI 驱动的长期记忆
- [Vel-Labs/molting-memory](https://github.com/Vel-Labs/molting-memory) - 基于 QDrant 的向量数据库
- [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) - MoltBook 代理的长期记忆层

---

## 监控与工具

### Web 界面与仪表盘

- [ibelick/webclaw](https://github.com/ibelick/webclaw) - OpenClaw 的快速 Web 客户端
- [clawdeckio/clawdeck](https://github.com/clawdeckio/clawdeck) - OpenClaw 代理的使命控制中心
- [crshdn/mission-control](https://github.com/crshdn/mission-control) - AI 代理编排仪表盘
- [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) - OpenClaw 的工作室/IDE

### 监控与可观察性

- [luccast/crabwalk](https://github.com/luccast/crabwalk) - OpenClaw 代理的实时伴侣监控器

### 成本追踪

- [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) - Token 使用追踪 CLI
- [bokonon23/clawdbot-cost-monitor](https://github.com/bokonon23/clawdbot-cost-monitor) - 实时 AI 支出追踪器

---

## 技能与扩展

### 官方技能集合

- [openclaw/skills](https://github.com/openclaw/skills) - 官方技能存档
- [openclaw/clawhub](https://github.com/openclaw/clawhub) - 官方技能注册表，包含 700+ 技能

### 社区技能库

- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - 社区策划的技能集合
- [natan89/awesome-openclaw-skills](https://github.com/natan89/awesome-openclaw-skills) - 1715+ 社区驱动的技能
- [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) - 流行技能集合

### 专业技能

- [BankrBot/openclaw-skills](https://github.com/BankrBot/openclaw-skills) - 交易与 DeFi 专注技能
- [jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills) - 多代理框架技能
- [runkids/skillshare](https://github.com/runkids/skillshare) - 在 AI CLI 工具间同步技能
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) - Manus 风格的持久化 Markdown 规划
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) - Obsidian 代理技能
- [lekt9/unbrowse-openclaw](https://github.com/lekt9/unbrowse-openclaw) - 自学习 API 技能生成器

---

## 企业解决方案

- [archestra-ai/archestra](https://github.com/archestra-ai/archestra) - 企业版 OpenClaw，包含 RBAC、MCP、A2A
- [backbay-labs/clawdstrike](https://github.com/backbay-labs/clawdstrike) - 群体检测与响应 (SDR) 平台
- [knostic/openclaw-detect](https://github.com/knostic/openclaw-detect) - OpenClaw 的 MDM 检测脚本
- [TheSethRose/Clawdbot-Security-Check](https://github.com/TheSethRose/Clawdbot-Security-Check) - 安全审计技能

---

## 本地化

### 中文（简体）

- [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) - 完整的中文翻译
- [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) - 中文技能库
- [bbylw/clawdbot-cn](https://github.com/bbylw/clawdbot-cn) - 中文 Clawdbot 版本
- [lllooollpp/clawdbot-cn](https://github.com/lllooollpp/clawdbot-cn) - Electron 桌面中文版
- [mengjian-github/xiaomo-starter-kit](https://github.com/mengjian-github/xiaomo-starter-kit) - 中文 AI 助手模板

### 韩文（한국어）

- [OpenClaw-Korea/awesome-openclaw](https://github.com/OpenClaw-Korea/awesome-openclaw) - 韩国社区资源

---

## 安全与研究

### 安全研究与漏洞

- [ethiack/moltbot-1click-rce](https://github.com/ethiack/moltbot-1click-rce) - 安全概念验证（CVE-2026-25253）

### 防御与保护

- [seojoonkim/prompt-guard](https://github.com/seojoonkim/prompt-guard) - 提示注入防御系统
- [NirDiamant/moltbook-agent-guard](https://github.com/NirDiamant/moltbook-agent-guard) - 代理的实时安全

---

## 社区与资源

### 其他 Awesome Lists

- [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) - 最古老/最全面的综合列表
- [eltociear/awesome-molt-ecosystem](https://github.com/eltociear/awesome-molt-ecosystem) - Molt 生态系统平台与工具
- [thewh1teagle/awesome-openclaw](https://github.com/thewh1teagle/awesome-openclaw) - 替代精选列表
- [shaoxiang/awesome-openclaw](https://github.com/shaoxiang/awesome-openclaw) - 生态系统资源

### 社区项目

- [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) - AI 代理模板
- [ThisIsJeron/awesome-openclaw-plugins](https://github.com/ThisIsJeron/awesome-openclaw-plugins) - 插件集合

### 替代与相关项目

- [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) - 免费、本地、开源的多 AI 工具 UI
- [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) - AI 代理 + 编码代理桌面应用
- [refly-ai/refly](https://github.com/refly-ai/refly) - 开源代理技能构建器
- [ImGoodBai/goodable](https://github.com/ImGoodBai/goodable) - 本地优先的桌面 AI 工作区
- [vstorm-co/pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents) - Python 深度代理框架
- [wecode-ai/Wegent](https://github.com/wecode-ai/Wegent) - 代理团队的 AI 原生操作系统

---

## 贡献指南

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何添加资源的指南。

**提交前快速检查:**
- [ ] 项目符合我们的[质量标准](CONTRIBUTING.md#筛选标准)
- [ ] 最后更新在 6 个月内（除非具有历史重要性）
- [ ] 有清晰的文档
- [ ] 遵循现有格式
- [ ] 放置在最相关的分类中

---

## 许可证

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](LICENSE)

在法律允许的范围内，本文的作者已放弃本工作的所有版权和相关或相邻权利。

---

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=vivy-yi/awesome-openclaw&type=Date)](https://star-history.com/#vivy-yi/awesome-openclaw&Date)

---

<div align="center">

**[⬆ 返回顶部](#awesome-openclaw)**

由 OpenClaw 社区用 ❤️ 制作

</div>
