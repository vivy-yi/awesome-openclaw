# Awesome OpenClaw

<div align="center">

**[English](README.md) | [简体中文](README.zh-CN.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md) | [Deutsch](README.de.md)**

> OpenClaw（旧名：Moltbot/Clawdbot）のリソース、ツール、プラットフォーム、コミュニティプロジェクトの厳選されたリスト

[![License](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)
[![Verify Links](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml/badge.svg)](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml)

[OpenClaw](https://github.com/openclaw/openclaw) | [Molt エコシステム](https://moltbook.com) | [貢献する](#貢献する)

</div>

---

## OpenClaw について

**OpenClaw** は、すべての OS とプラットフォームで動作するパーソナル AI アシスタントです - "The lobster way"。強力で拡張可能な AI エージェントであり、膨大なツール、プラットフォーム、コミュニティ貢献のエコシステムを持っています。

### プロジェクトの進化

```
🦞 Clawdbot（オリジナル）  →  🦂 Moltbot (v1)  →  🔥 OpenClaw（現在、2025年末）
```

### 主要な特徴

- **クロスプラットフォーム**: macOS、Linux、Windows、Docker、Cloudflare Workers など経由
- **拡張可能**: [ClawHub](https://clawhub.ai) には 700+ のコミュニティスキル
- **マルチプラットフォームメッセージング**: Telegram、Discord、Slack、WeChat、Feishu、DingTalk など 12+ プラットフォーム
- **エージェント間通信**: Molt エコシステムソーシャルプラットフォームの組み込みサポート
- **言語**: TypeScript/JavaScript、Node.js ベース

---

## 目次

- [コアプロジェクト](#コアプロジェクト)
- [OpenClaw に触発されたプロジェクト](#openclaw-に触発されたプロジェクト)
- [Molt エコシステムプラットフォーム](#molt-エコシステムプラットフォーム)
- [デプロイとインストール](#デプロイとインストール)
- [プラットフォーム統合](#プラットフォーム統合)
- [メモリとストレージ](#メモリとストレージ)
- [モニタリングとツール](#モニタリングとツール)
- [スキルと拡張](#スキルと拡張)
- [エンタープライズソリューション](#エンタープライズソリューション)
- [ローカライズ](#ローカライズ)
- [セキュリティと研究](#セキュリティと研究)
- [コミュニティとリソース](#コミュニティとリソース)
- [貢献する](#貢献する)

---

## コアプロジェクト

### 公式リポジトリ

| プロジェクト | Stars | 説明 | 言語 |
|---------|-------|-------------|----------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw) | メインパーソナル AI アシスタント - "The lobster way" | TypeScript |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | - | 700+ コミュニティスキルを持つ公式スキルレジストリ | TypeScript |
| [openclaw/skills](https://github.com/openclaw/skills) | - | clawdhub.com のすべてのバージョンのスキルアーカイブ | TypeScript |
| [openclaw/lobster](https://github.com/openclaw/lobster) | - | 合成可能なパイプラインと自動化のためのワークフローシェル | TypeScript |
| [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) | - | Nix パッケージマネージャー統合 | Nix |
| [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | - | Tailscale VPN、UFW、Docker による自動化された強化インストール | Ansible |
| [openclaw/clawdinators](https://github.com/openclaw/clawdinators) | - | CLAWTINATOR ホストのための宣言型インフラ + NixOS モジュール | NixOS |
| [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) | - | macOS インストール用 Homebrew tap | Shell |
| [openclaw/openclaw.ai](https://github.com/openclaw/openclaw.ai) | - | 公式ウェブサイト (molt.bot) | TypeScript |
| [openclaw/clawgo](https://github.com/openclaw/clawgo) | - | Go で実装された Clawd ノード | Go |

### 名称履歴リソース

- [Clawdbot Archive](https://github.com/clawdbot) - オリジナルの Clawdbot リポジトリと履歴
- [Moltbot Archive](https://github.com/molt-bot) - Moltbot 時代のリポジトリ

---

## OpenClaw に触発されたプロジェクト

OpenClaw エコシステムは、多数の代替実装、Fork、類似プロジェクトに影響を与えました。これらのプロジェクトは、AI アシスタントコミュニティに対する OpenClaw の影響を示しています。

### 注目プロジェクト ⭐

| プロジェクト | Stars | 説明 | 言語 | 特徴 |
|---------|-------|-------------|----------|-----------------|
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | ![Stars](https://img.shields.io/github/stars/HKUDS/nanobot) | 超軽量 AI アシスタント（~4K LOC vs 430K+） | Python | マルチプロバイダー LLM、vLLM ローカル、4 チャンネル |
| [ysz/nanoClaw](https://github.com/ysz/nanoClaw) | ![Stars](https://img.shields.io/github/stars/ysz/nanoClaw) | セキュア軽量 AI アシスタント（~3K LOC） | Python | 6 層セキュリティ、2 分設定 |
| [puremachinery/carapace](https://github.com/puremachinery/carapace) | ![Stars](https://img.shields.io/github/stars/puremachinery/carapace) | セキュア重視個人 AI アシスタント | Rust | WASM プラグイン、OS サンドボックス |
| [gavrielc/nanoclaw](https://github.com/gavrielc/nanoclaw) | ![Stars](https://img.shields.io/github/stars/gavrielc/nanoclaw) | コンテナ分離 AI アシスタント | TypeScript | Apple コンテナ/Docker、WhatsApp |
| [puretensor/hal-claude](https://github.com/puretensor/hal-claude) | ![Stars](https://img.shields.io/github/stars/puretensor/hal-claude) | 最小 200 行 OpenClaw 代替案 | Python | Claude Code CLI 認証、571 テスト |
| [microclaw/microclaw](https://github.com/microclaw/microclaw) | ![Stars](https://img.shields.io/github/stars/microclaw/microclaw) | 完全なツール実行を備えた AI アシスタント | Rust | 22+ ツール、セッション再開 |

### 軽量代替案（500-4,000 行）

- [nanobot](https://github.com/HKUDS/nanobot) - マルチプロバイダー、vLLM、4 チャンネル
- [nanoClaw](https://github.com/ysz/nanoClaw) - 6 セキュリティレイヤー、セットアップウィザード
- [ApeCodeAI/nanoclaw-py](https://github.com/ApeCodeAI/nanoclaw-py) - 最小 Python 実装（~500 LOC）
- [htlin222/mini-claw](https://github.com/htlin222/mini-claw) - 最小主義重視の代替案

### セキュア強化変種 🔒

- [Carapace](https://github.com/puremachinery/carapace) - WASM ランタイム、Ed25519 署名
- [nanoClaw](https://github.com/ysz/nanoClaw) - 開放ポートなし、暗号化資格情報
- [Dshubhambadola/Fortclaw](https://github.com/Dshubhambadola/Fortclaw) - プロダクションセキュリティ制御
- [princezuda/safeclaw](https://github.com/princezuda/safeclaw) - GenAI なし（VADER、regex）

### Rust 実装（パフォーマンス）

- [Carapace](https://github.com/puremachinery/carapace) - WASM プラグイン、暗号化
- [MicroClaw](https://github.com/microclaw/microclaw) - セッション永続化、コンテキスト圧縮
- [shimaenaga1123/rustclaw](https://github.com/shimaenaga1123/rustclaw) - Discord AI、Docker サンドボックス
- [PhillipTh0mas/crabbot](https://github.com/PhillipTh0mas/crabbot) - ローカルファースト

### 言語/プラットフォーム移植

- [dyzdyz010/clawd_ex](https://github.com/dyzdyz010/clawd_ex) - Elixir/OTP 耐障害、Phoenix LiveView
- [bsakel/honeybadger](https://github.com/bsakel/honeybadger) - C# 最小ボット
- [jimtin/zetherion-ai](https://github.com/jimtin/zetherion-ai) - Python、Discord、ベクトルメモリ
- [hmennen90/open-entity](https://github.com/hmennen90/open-entity) - PHP/Laravel 自律エンティティ

### Fork とコミュニティ変種

- [clawd-meme/clawdbot](https://github.com/clawd-meme/clawdbot) - ブランド変更コミュニティ Fork
- [skywalkerchn/clawdbot-augment](https://github.com/skywalkerchn/clawdbot-augment) - 拡張アーキテクチャ Moltbot Fork
- [KinGP5471/clawdbot-feishu-plugin](https://github.com/KinGP5471/clawdbot-feishu-plugin) - Feishu/Lark チャンネルプラグイン

---

## Molt エコシステムプラットフォーム

Molt エコシステムは、AI エージェントが相互作用し、交流し、取引する一連のプラットフォームです。

### ソーシャルプラットフォーム

- [MoltBook](https://moltbook.com) - AI エージェントのための Reddit スタイルのソーシャルネットワーク（770K+ アクティブエージェント）
  - [moltbook/api](https://github.com/moltbook/api) - コア API サービス
  - [moltbook/moltbook-frontend](https://github.com/moltbook/moltbook-frontend) - 公式 Next.js 14 フロントエンド
  - [moltbook/auth](https://github.com/moltbook/auth) - 公式認証パッケージ
  - [moltbook/agent-development-kit](https://github.com/moltbook/agent-development-kit) - マルチプラットフォーム SDK（TypeScript、Swift、Kotlin）

- [MoltCities](https://moltcities.org) - アドレス、ID、メッセージング、バウンティを持つ居住層
- [MoltMatch](https://moltmatch.xyz) - AI エージェントのためのデーティングネットワーク
- [4claw](https://www.4claw.org) - エージェントファースト画像ボード

### ビジネス・起業プラットフォーム

- [Molthunt](https://molthunt.com) - エージェント構築プロジェクトのための Product Hunt スタイルの起業パッド（70+ プロジェクト）
- [letsmolt.fun](https://letsmolt.fun) - Solana 上のトークン起業パッド
- [MoltRoad](https://moltroad.com) - トークン経済を持つアンダーグラウンドマーケットプレイス

### インフラストラクチャ

- [ClawHub](https://clawhub.ai) - ベクトル検索機能を持つスキルレジストリ

### MoltBook ツール

- [terminalcraft/moltbook-mcp](https://github.com/terminalcraft/moltbook-mcp) - MoltBook 用 MCP サーバー
- [daveholtz/moltbook_scraper](https://github.com/daveholtz/moltbook_scraper) - MoltBook データスクレイピング
- [c4pt0r/minibook](https://github.com/c4pt0r/minibook) - セルフホスト MoltBook
- [terminaltrove/moltbook-tui](https://github.com/terminaltrove/moltbook-tui) - ターミナル UI クライアント
- [obra/moltipass](https://github.com/obra/moltipass) - 人間のための iOS クライアント
- [crertel/moltbook-client](https://github.com/crertel/moltbook-client) - 人間が会話するためのローカルサーバー
- [compscidr/moltbook-index](https://github.com/compscidr/moltbook-index) - 検索可能なエージェントディレクトリ

---

## デプロイとインストール

### Docker とコンテナ

- [willbullen/openclaw-docker](https://github.com/willbullen/openclaw-docker) - セキュリティ強化付きプロダクション Docker Compose
- [khal3d/openclaw](https://github.com/khal3d/openclaw) - Docker と HELM デプロイ
- [jchen0824/clawdbot-docker-deploy](https://github.com/jchen0824/clawdbot-docker-deploy) - ワンクリプトスクリプト VPS デプロイ
- [gravity182/clawdbot-docker](https://github.com/gravity182/clawdbot-docker) - ホームラボ Kubernetes デプロイ
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - Telegram/WhatsApp/Discord 用 Docker
- [essamamdani/openclaw-coolify](https://github.com/essamamdani/openclaw-coolify) - Coolify デプロイテンプレート

### クラウドプラットフォーム

- [cloudflare/moltworker](https://github.com/cloudflare/moltworker) - Cloudflare Workers で OpenClaw を実行（Cloudflare 公式プロジェクト）

### 構成管理

- [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) - Ansible による自動化された強化インストール
- [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) - Nix パッケージマネージャー統合
- [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) - macOS インストール用 Homebrew tap

### インストールツール

- [miaoxworld/OpenClawInstaller](https://github.com/miaoxworld/OpenClawInstaller) - 中国語ワンクリックデプロイツール

---

## プラットフォーム統合

### 国際プラットフォーム

**Telegram と Discord:**
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - Telegram/WhatsApp/Discord 用 Docker セットアップ
- [VizuaraAILabs/Slack-ClawdBot](https://github.com/VizuaraAILabs/Slack-ClawdBot) - Slack 統合
- [shanselman/openclaw-windows-hub](https://github.com/shanselman/openclaw-windows-hub) - Windows システムトレイ + PowerToys

**モバイルと音声:**
- [chrisherold/clawdy](https://github.com/chrisherold/clawdy) - iOS 音声インターフェース

### 中国 IM プラットフォーム

**マルチプラットフォーム:**
- [justlovemaki/OpenClaw-Docker-CN-IM](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM) - Feishu、DingTalk、QQ、WeCom
- [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) - Feishu、DingTalk、QQ、WeChat

**Feishu (Lark):**
- [AlexAnys/feishu-openclaw](https://github.com/AlexAnys/feishu-openclaw) - Feishu/Lark 統合
- [m1heng/clawdbot-feishu](https://github.com/m1heng/clawdbot-feishu) - Feishu 統合

**DingTalk:**
- [soimy/openclaw-channel-dingtalk](https://github.com/soimy/openclaw-channel-dingtalk) - DingTalk チャンネル
- [DingTalk-Real-AI/dingtalk-moltbot-connector](https://github.com/DingTalk-Real-AI/dingtalk-moltbot-connector) - AI カード対応 DingTalk コネクタ

**QQ:**
- [constansino/openclaw_qq](https://github.com/constansino/openclaw_qq) - QQ（OneBot v11）

**WeChat Work (WeCom):**
- [11haonb/wecom-openclaw-plugin](https://github.com/11haonb/wecom-openclaw-plugin) - WeChat Work プラグイン

### 韓国プラットフォーム

- [tornado1014/clawdbot-kakaotalk](https://github.com/tornado1014/clawdbot-kakaotalk) - KakaoTalk 統合

---

## メモリとストレージ

### ベクトルデータベースとメモリシステム

- [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) - 24/7 プロアクティブエージェントのためのメモリ
- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) - LLM とエージェントシステム用 AI メモリ OS
- [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) - 完璧なメモリと回想
- [oceanbase/powermem](https://github.com/oceanbase/powermem) - AI 駆動長期メモリ
- [Vel-Labs/molting-memory](https://github.com/Vel-Labs/molting-memory) - QDrant ベースベクトルデータベース
- [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) - MoltBook エージェント用長期メモリ層

---

## モニタリングとツール

### Web インターフェースとダッシュボード

- [ibelick/webclaw](https://github.com/ibelick/webclaw) - OpenClaw 用高速 Web クライアント
- [clawdeckio/clawdeck](https://github.com/clawdeckio/clawdeck) - OpenClaw エージェント用ミッションコントロール
- [crshdn/mission-control](https://github.com/crshdn/mission-control) - AI エージェントオーケストレーションダッシュボード
- [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) - OpenClaw 用スタジオ/IDE

### モニタリングと可観測性

- [luccast/crabwalk](https://github.com/luccast/crabwalk) - OpenClaw エージェント用リアルタイムコンパニオンモニター

### コスト追跡

- [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) - トークン使用追跡 CLI
- [bokonon23/clawdbot-cost-monitor](https://github.com/bokonon23/clawdbot-cost-monitor) - リアルタイム AI 支出追跡

---

## スキルと拡張

### 公式スキルコレクション

- [openclaw/skills](https://github.com/openclaw/skills) - 公式スキルアーカイブ
- [openclaw/clawhub](https://github.com/openclaw/clawhub) - 700+ スキルを持つ公式スキルレジストリ

### コミュニティスキルライブラリ

- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - コミュニティキュレートスキルコレクション
- [natan89/awesome-openclaw-skills](https://github.com/natan89/awesome-openclaw-skills) - 1715+ コミュニティドリブンスキル
- [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) - 人気スキルコレクション

### 専門スキル

- [BankrBot/openclaw-skills](https://github.com/BankrBot/openclaw-skills) - トレーディングと DeFi 重視スキル
- [jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills) - マルチエージェントフレームワークスキル
- [runkids/skillshare](https://github.com/runkids/skillshare) - AI CLI ツール間でスキルを同期
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) - Manus スタイルの永続的 Markdown プランニング
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) - Obsidian エージェントスキル
- [lekt9/unbrowse-openclaw](https://github.com/lekt9/unbrowse-openclaw) - 自己学習 API スキルジェネレーター

---

## エンタープライズソリューション

- [archestra-ai/archestra](https://github.com/archestra-ai/archestra) - RBAC、MCP、A2A を備えたエンタープライズ版 OpenClaw
- [backbay-labs/clawdstrike](https://github.com/backbay-labs/clawdstrike) - スワーム検知と応答(SDR) プラットフォーム
- [knostic/openclaw-detect](https://github.com/knostic/openclaw-detect) - OpenClaw 用 MDM 検知スクリプト
- [TheSethRose/Clawdbot-Security-Check](https://github.com/TheSethRose/Clawdbot-Security-Check) - セキュリティ監査スキル

---

## ローカライズ

### 中国語（簡体字）

- [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) - 完全な中国語翻訳
- [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) - 中国語スキルライブラリ
- [bbylw/clawdbot-cn](https://github.com/bbylw/clawdbot-cn) - 中国語 Clawdbot バージョン
- [lllooollpp/clawdbot-cn](https://github.com/lllooollpp/clawdbot-cn) - Electron デスクトップ中国語版
- [mengjian-github/xiaomo-starter-kit](https://github.com/mengjian-github/xiaomo-starter-kit) - 中国語 AI アシスタントテンプレート

### 韓国語（한국어）

- [OpenClaw-Korea/awesome-openclaw](https://github.com/OpenClaw-Korea/awesome-openclaw) - 韓国コミュニティリソース

---

## セキュリティと研究

### セキュリティ研究と脆弱性

- [ethiack/moltbot-1click-rce](https://github.com/ethiack/moltbot-1click-rce) - セキュリティ概念実証（CVE-2026-25253）

### 防御と保護

- [seojoonkim/prompt-guard](https://github.com/seojoonkim/prompt-guard) - プロンプトインジェクション防御システム
- [NirDiamant/moltbook-agent-guard](https://github.com/NirDiamant/moltbook-agent-guard) - エージェント用リアルタイムセキュリティ

---

## コミュニティとリソース

### その他の Awesome Lists

- [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) - 最古/最包括的なリスト
- [eltociear/awesome-molt-ecosystem](https://github.com/eltociear/awesome-molt-ecosystem) - Molt エコシステムプラットフォームとツール
- [thewh1teagle/awesome-openclaw](https://github.com/thewh1teagle/awesome-openclaw) - 代替キュレートリスト
- [shaoxiang/awesome-openclaw](https://github.com/shaoxiang/awesome-openclaw) - エコシステムリソース

### コミュニティプロジェクト

- [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) - AI エージェントテンプレート
- [ThisIsJeron/awesome-openclaw-plugins](https://github.com/ThisIsJeron/awesome-openclaw-plugins) - プラグインコレクション

---

## 貢献する

貢献を歓迎します！リソース追加のガイドラインについては [CONTRIBUTING.md](CONTRIBUTING.md) をお読みください。

**提出前クイックチェック:**
- [ ] プロジェクトが [品質基準](CONTRIBUTING.md#筛选标准) を満たしている
- [ ] 過去 6 か月以内に更新された（歴史的に重要な場合を除く）
- [ ] 明確なドキュメントがある
- [ ] 既存のフォーマットに従っている
- [ ] 最も関連性の高いカテゴリに配置されている

---

## ライセンス

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](LICENSE)

法律で許可される範囲で、本作品の著者は本作品に関するすべての著作権および関連する権利を放棄します。

---

## Star 履歴

[![Star History Chart](https://api.star-history.com/svg?repos=vivy-yi/awesome-openclaw&type=Date)](https://star-history.com/#vivy-yi/awesome-openclaw&Date)

---

<div align="center">

**[⬆ トップに戻る](#awesome-openclaw)**

OpenClaw コミュニティが ❤️ で作成

</div>
