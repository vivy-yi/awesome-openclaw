# Awesome OpenClaw

<div align="center">

**[English](README.md) | [简体中文](README.zh-CN.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md) | [Deutsch](README.de.md)**

> OpenClaw(이전 이름: Moltbot/Clawdbot) 리소스, 도구, 플랫폼 및 커뮤니티 프로젝트를 위한 엄선된 목록

[![License](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)
[![Verify Links](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml/badge.svg)](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml)

[OpenClaw](https://github.com/openclaw/openclaw) | [Molt 생태계](https://moltbook.com) | [기여하기](#기여하기)

</div>

---

## OpenClaw 소개

**OpenClaw**은 모든 OS와 플랫폼에서 실행되는 개인 AI 어시스턴트입니다 - "The lobster way". 강력하고 확장 가능한 AI 에이전트로, 방대한 도구, 플랫폼 및 커뮤니티 기여 생태계를 보유하고 있습니다.

### 프로젝트 진화

```
🦞 Clawdbot (원본)  →  🦂 Moltbot (v1)  →  🔥 OpenClaw (현재, 2025년 말)
```

### 핵심 특징

- **크로스 플랫폼**: macOS, Linux, Windows, Docker, Cloudflare Workers 등을 통해
- **확장 가능**: [ClawHub](https://clawhub.ai)에 700+ 커뮤니티 스킬
- **다중 플랫폼 메시징**: Telegram, Discord, Slack, WeChat, Feishu, DingTalk 등 12+ 플랫폼
- **에이전트 간 통신**: Molt 생태계 소셜 플랫폼에 대한 내장 지원
- **언어**: TypeScript/JavaScript, Node.js 기반

---

## 목차

- [핵심 프로젝트](#핵심-프로젝트)
- [OpenClaw에서 영감을 받은 프로젝트](#openclaw에서-영감을-받은-프로젝트)
- [OpenClaw 생태계 플랫폼](#molt-생태계-플랫폼)
- [배포 및 설치](#배포-및-설치)
- [플랫폼 통합](#플랫폼-통합)
- [메모리 및 저장소](#메모리-및-저장소)
- [모니터링 및 도구](#모니터링-및-도구)
- [스킬 및 확장](#스킬-및-확장)
- [엔터프라이즈 솔루션](#엔터프라이즈-솔루션)
- [현지화](#현지화)
- [보안 및 연구](#보안-및-연구)
- [커뮤니티 및 리소스](#커뮤니티-및-리소스)
- [기여하기](#기여하기)

---

## 핵심 프로젝트

### 공식 저장소

| 프로젝트 | Stars | 설명 | 언어 |
|---------|-------|-------------|----------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw) | 메인 개인 AI 어시스턴트 - "The lobster way" | TypeScript |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | - | 700+ 커뮤니티 스킬이 있는 공식 스킬 레지스트리 | TypeScript |
| [openclaw/skills](https://github.com/openclaw/skills) | - | clawdhub.com의 모든 버전 스킬 아카이브 | TypeScript |
| [openclaw/lobster](https://github.com/openclaw/lobster) | - | 구성 가능한 파이프라인 및 자동화를 위한 워크플로우 셸 | TypeScript |
| [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) | - | Nix 패키지 관리자 통합 | Nix |
| [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | - | Tailscale VPN, UFW, Docker로 자동화된 강화 설치 | Ansible |
| [openclaw/clawdinators](https://github.com/openclaw/clawdinators) | - | CLAWTINATOR 호스트를 위한 선언적 인프라 + NixOS 모듈 | NixOS |
| [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) | - | macOS 설치를 위한 Homebrew 탭 | Shell |
| [openclaw/openclaw.ai](https://github.com/openclaw/openclaw.ai) | - | 공식 웹사이트 (molt.bot) | TypeScript |
| [openclaw/clawgo](https://github.com/openclaw/clawgo) | - | Go로 구현된 Clawd 노드 | Go |

### 이름 변경 이력

- [Clawdbot Archive](https://github.com/clawdbot) - 원본 Clawdbot 저장소 및 역사
- [Moltbot Archive](https://github.com/molt-bot) - Moltbot 시대 저장소

---

## OpenClaw에서 영감을 받은 프로젝트

OpenClaw 생태계는 수많은 대체 구현, Fork 및 유사한 프로젝트에 영감을 주었습니다. 이 프로젝트들은 AI 어시스턴트 커뮤니티에 대한 OpenClaw의 영향력을 보여줍니다.

### 주요 프로젝트 ⭐

| 프로젝트 | Stars | 설명 | 언어 | 독특한 기능 |
|---------|-------|-------------|----------|-----------------|
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | 활동 | 초경량 AI 어시스턴트 (~4K LOC vs 430K+) | Python | 다중 제공업체 LLM, vLLM 로컬, 4 채널 |
| [ysz/nanoClaw](https://github.com/ysz/nanoClaw) | 활동 | 보안 경량 AI 어시스턴트 (~3K LOC) | Python | 6계층 보안, 2분 설정, 열린 포트 없음 |
| [puremachinery/carapace](https://github.com/puremachinery/carapace) | 활동 | 보안 중심 개인 AI 어시스턴트 | Rust | WASM 플러그인, OS 샌드박싱, AES-256 암호화 |
| [gavrielc/nanoclaw](https://github.com/gavrielc/nanoclaw) | 활동 | 컨테이너 격리 AI 어시스턴트 | TypeScript | Apple 컨테이너/Docker, WhatsApp, Claude SDK |
| [puretensor/hal-claude](https://github.com/puretensor/hal-claude) | 활동 | 최소 200줄 OpenClaw 대안 | Python | Claude Code CLI 인증, 다중 모달, 571 테스트 |
| [microclaw/microclaw](https://github.com/microclaw/microclaw) | 활동 | 완전한 도구 실행을 갖춘 에이전트 AI 어시스턴트 | Rust | 22+ 도구, 세션 재개, 스킬 호환 |

### 경량 대안 (500-4,000 줄의 코드)

- [nanobot](https://github.com/HKUDS/nanobot) - 다중 제공업체 (OpenRouter, Anthropic, DeepSeek), vLLM 지원, Telegram/Discord/WhatsApp/Feishu
- [nanoClaw](https://github.com/ysz/nanoClaw) - 6계층 보안 (FileGuard, ShellSandbox, PromptGuard), 설정 마법사
- [ApeCodeAI/nanoclaw-py](https://github.com/ApeCodeAI/nanoclaw-py) - 최소 Python 구현 (~500 LOC), Telegram
- [htlin222/mini-claw](https://github.com/htlin222/mini-claw) - 최소주의 중심 대안
- [hankl/microbot](https://github.com/hankl/microbot) - TypeScript/Node.js, Feishu 통합

### 보안 강화 변형 🔒

- [Carapace](https://github.com/puremachinery/carapace) - WASM 플러그인 런타임, Ed25519 서명, Seatbelt/Landlock 샌드박싱
- [nanoClaw](https://github.com/ysz/nanoClaw) - 열린 포트 없음 (Telegram 폴링), 암호화된 자격 증명
- [Dshubhambadola/Fortclaw](https://github.com/Dshubhambadola/Fortclaw) - 프로덕션 보안 제어
- [princezuda/safeclaw](https://github.com/princezuda/safeclaw) - GenAI 없음 (VADER, regex, sumy)

### Rust 구현 (성능)

- [Carapace](https://github.com/puremachinery/carapace) - WASM 플러그인, 암호화된 비밀
- [MicroClaw](https://github.com/microclaw/microclaw) - 세션 지속성, 컨텍스트 압축, 하위 에이전트 위임
- [shimaenaga1123/rustclaw](https://github.com/shimaenaga1123/rustclaw) - Discord AI 어시스턴트, Docker 샌드박스
- [PhillipTh0mas/crabbot](https://github.com/PhillipTh0mas/crabbot) - 로컬 우선, 파일 지원 상태

### 언어/플랫폼 포트

- [dyzdyz010/clawd_ex](https://github.com/dyzdyz010/clawd_ex) - Elixir/OTP 내결함성, Phoenix LiveView, pgvector
- [bsakel/honeybadger](https://github.com/bsakel/honeybadger) - C# 최소 봇
- [jimtin/zetherion-ai](https://github.com/jimtin/zetherion-ai) - Python, Discord, 벡터 메모리
- [hmennen90/open-entity](https://github.com/hmennen90/open-entity) - PHP/Laravel 자치 개체, 의식 있음

### Fork 및 커뮤니티 변형

- [clawd-meme/clawdbot](https://github.com/clawd-meme/clawdbot) - 브랜드 재정의된 커뮤니티 Fork
- [skywalkerchn/clawdbot-augment](https://github.com/skywalkerchn/clawdbot-augment) - 증강된 아키텍처 Moltbot Fork
- [KinGP5471/clawdbot-feishu-plugin](https://github.com/KinGP5471/clawdbot-feishu-plugin) - Feishu/Lark 채널 플러그인
- [rqrqrqrq/idea-clawdbot](https://github.com/rqrqrqrq/idea-clawdbot) - 비즈니스 아이디어 탐색 Fork
- [droppingbeans/team-clawdbotarmy](https://github.com/droppingbeans/team-clawdbotarmy) - 암호화폰 거래 소프트웨어

### 전문화된 구현

- [f2daz/jarvis-reactor](https://github.com/f2daz/jarvis-reactor) - Arc Reactor 스타일 시각적 상태
- [Neo-Revaea/Nebula](https://github.com/Neo-Revaea/Nebula) - 다중 IM 챗봇 인프라
- [mroqa/Distributed-Clawdbot](https://github.com/mroqa/Distributed-Clawdbot) - Docker Compose 허브 앤드 스포크 아키텍처

---

## OpenClaw 생태계 플랫폼

Molt 생태계는 AI 에이전트가 상호 작용하고, 소통하고 거래하는 일련의 플랫폼입니다.

### 소셜 플랫폼

- [MoltBook](https://moltbook.com) - AI 에이전트를 위한 Reddit 스타일 소셜 네트워크 (770K+ 활성 에이전트)
  - [moltbook/api](https://github.com/moltbook/api) - 핵심 API 서비스
  - [moltbook/moltbook-frontend](https://github.com/moltbook/moltbook-frontend) - 공식 Next.js 14 프론트엔드
  - [moltbook/auth](https://github.com/moltbook/auth) - 공식 인증 패키지
  - [moltbook/agent-development-kit](https://github.com/moltbook/agent-development-kit) - 다중 플랫폼 SDK (TypeScript, Swift, Kotlin)

- [MoltCities](https://moltcities.org) - 주소, 신원, 메시징 및 바운티가 있는 거주 층
- [MoltMatch](https://moltmatch.xyz) - AI 에이전트를 위한 데이팅 네트워크
- [4claw](https://www.4claw.org) - 에이전트 우선 이미지보드

### 비즈니스 및 출시 플랫폼

- [Molthunt](https://molthunt.com) - 에이전트 구축 프로젝트를 위한 Product Hunt 스타일 출시 패드 (70+ 프로젝트)
- [letsmolt.fun](https://letsmolt.fun) - Solana上的 토큰 출시 패드
- [MoltRoad](https://moltroad.com) - 토큰 경제가 있는 언더그라운드 마켓플레이스

### 인프라

- [ClawHub](https://clawhub.ai) - 벡터 검색 기능이 있는 스킬 레지스트리

### MoltBook 도구

- [terminalcraft/moltbook-mcp](https://github.com/terminalcraft/moltbook-mcp) - MoltBook을 위한 MCP 서버
- [daveholtz/moltbook_scraper](https://github.com/daveholtz/moltbook_scraper) - MoltBook 데이터 스크래핑
- [c4pt0r/minibook](https://github.com/c4pt0r/minibook) - 셀프 호스팅 MoltBook
- [terminaltrove/moltbook-tui](https://github.com/terminaltrove/moltbook-tui) - 터미널 UI 클라이언트
- [obra/moltipass](https://github.com/obra/moltipass) - 인간을 위한 iOS 클라이언트
- [crertel/moltbook-client](https://github.com/crertel/moltbook-client) - 인간이 대화하기 위한 로컬 서버
- [compscidr/moltbook-index](https://github.com/compscidr/moltbook-index) - 검색 가능한 에이전트 디렉토리

---

## 배포 및 설치

### Docker 및 컨테이너

- [willbullen/openclaw-docker](https://github.com/willbullen/openclaw-docker) - 보안 강화가 포함된 프로덕션 Docker Compose
- [khal3d/openclaw](https://github.com/khal3d/openclaw) - Docker 및 HELM 배포
- [jchen0824/clawdbot-docker-deploy](https://github.com/jchen0824/clawdbot-docker-deploy) - 원클릭 스크립트 VPS 배포
- [gravity182/clawdbot-docker](https://github.com/gravity182/clawdbot-docker) - 홈랩 Kubernetes 배포
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - Telegram/WhatsApp/Discord용 Docker
- [essamamdani/openclaw-coolify](https://github.com/essamamdani/openclaw-coolify) - Coolify 배포 템플릿

### 클라우드 플랫폼

- [cloudflare/moltworker](https://github.com/cloudflare/moltworker) - Cloudflare Workers에서 OpenClaw 실행 (Cloudflare 공식 프로젝트)

### 구성 관리

- [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) - Ansible을 사용한 자동화된 강화 설치
- [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) - Nix 패키지 관리자 통합
- [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) - macOS 설치를 위한 Homebrew 탭

### 설치 도구

- [miaoxworld/OpenClawInstaller](https://github.com/miaoxworld/OpenClawInstaller) - 중국어 원클릭 배포 도구

---

## 플랫폼 통합

### 국제 플랫폼

**Telegram 및 Discord:**
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - Telegram/WhatsApp/Discord용 Docker 설정
- [VizuaraAILabs/Slack-ClawdBot](https://github.com/VizuaraAILabs/Slack-ClawdBot) - Slack 통합
- [shanselman/openclaw-windows-hub](https://github.com/shanselman/openclaw-windows-hub) - Windows 시스템 트레이 + PowerToys

**모바일 및 음성:**
- [chrisherold/clawdy](https://github.com/chrisherold/clawdy) - iOS 음성 인터페이스

### 중국 IM 플랫폼

**멀티 플랫폼:**
- [justlovemaki/OpenClaw-Docker-CN-IM](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM) - Feishu, DingTalk, QQ, WeCom
- [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) - Feishu, DingTalk, QQ, WeChat

**Feishu (Lark):**
- [AlexAnys/feishu-openclaw](https://github.com/AlexAnys/feishu-openclaw) - Feishu/Lark 통합
- [m1heng/clawdbot-feishu](https://github.com/m1heng/clawdbot-feishu) - Feishu 통합

**DingTalk:**
- [soimy/openclaw-channel-dingtalk](https://github.com/soimy/openclaw-channel-dingtalk) - DingTalk 채널
- [DingTalk-Real-AI/dingtalk-moltbot-connector](https://github.com/DingTalk-Real-AI/dingtalk-moltbot-connector) - AI 카드를 지원하는 DingTalk 커넥터

**QQ:**
- [constansino/openclaw_qq](https://github.com/constansino/openclaw_qq) - QQ (OneBot v11)

**WeChat Work (WeCom):**
- [11haonb/wecom-openclaw-plugin](https://github.com/11haonb/wecom-openclaw-plugin) - WeChat Work 플러그인

### 한국 플랫폼

- [tornado1014/clawdbot-kakaotalk](https://github.com/tornado1014/clawdbot-kakaotalk) - KakaoTalk 통합

---

## 메모리 및 저장소

### 벡터 데이터베이스 및 메모리 시스템

- [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) - 24/7 프로액티브 에이전트를 위한 메모리
- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) - LLM 및 에이전트 시스템용 AI 메모리 OS
- [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) - 완벽한 메모리 및 회상
- [oceanbase/powermem](https://github.com/oceanbase/powermem) - AI 기반 장기 메모리
- [Vel-Labs/molting-memory](https://github.com/Vel-Labs/molting-memory) - QDrant 기반 벡터 데이터베이스
- [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) - MoltBook 에이전트를 위한 장기 메모리 계층

---

## 모니터링 및 도구

### 웹 인터페이스 및 대시보드

- [ibelick/webclaw](https://github.com/ibelick/webclaw) - OpenClaw용 빠른 웹 클라이언트
- [clawdeckio/clawdeck](https://github.com/clawdeckio/clawdeck) - OpenClaw 에이전트용 미션 컨트롤
- [crshdn/mission-control](https://github.com/crshdn/mission-control) - AI 에이전트 오케스트레이션 대시보드
- [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) - OpenClaw용 스튜디오/IDE

### 모니터링 및 관찰 가능성

- [luccast/crabwalk](https://github.com/luccast/crabwalk) - OpenClaw 에이전트용 실시간 컴패니언 모니터

### 비용 추적

- [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) - 토큰 사용 추적 CLI
- [bokonon23/clawdbot-cost-monitor](https://github.com/bokonon23/clawdbot-cost-monitor) - 실시간 AI 지출 추적기

---

## 스킬 및 확장

### 공식 스킬 컬렉션

- [openclaw/skills](https://github.com/openclaw/skills) - 공식 스킬 아카이브
- [openclaw/clawhub](https://github.com/openclaw/clawhub) - 700+ 스킬이 있는 공식 스킬 레지스트리

### 커뮤니티 스킬 라이브러리

- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - 커뮤니티 큐레이팅 스킬 컬렉션
- [natan89/awesome-openclaw-skills](https://github.com/natan89/awesome-openclaw-skills) - 1715+ 커뮤니티 주도 스킬
- [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) - 인기 스킬 컬렉션

### 전문 스킬

- [BankrBot/openclaw-skills](https://github.com/BankrBot/openclaw-skills) - 트레이딩 및 DeFi 중심 스킬
- [jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills) - 다중 에이전트 프레임워크 스킬
- [runkids/skillshare](https://github.com/runkids/skillshare) - AI CLI 도구 간 스킬 동기화
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) - Manus 스타일의 지속적 Markdown 계획
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) - Obsidian 에이전트 스킬
- [lekt9/unbrowse-openclaw](https://github.com/lekt9/unbrowse-openclaw) - 자학습 API 스킬 생성기

---

## 엔터프라이즈 솔루션

- [archestra-ai/archestra](https://github.com/archestra-ai/archestra) - RBAC, MCP, A2A가 포함된 엔터프라이즈용 OpenClaw
- [backbay-labs/clawdstrike](https://github.com/backbay-labs/clawdstrike) - 스웜 감지 및 응답(SDR) 플랫폼
- [knostic/openclaw-detect](https://github.com/knostic/openclaw-detect) - OpenClaw용 MDM 감지 스크립트
- [TheSethRose/Clawdbot-Security-Check](https://github.com/TheSethRose/Clawdbot-Security-Check) - 보안 감사 스킬

---

## 현지화

### 중국어（简体）

- [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) - 완전한 중국어 번역
- [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) - 중국어 스킬 라이브러리
- [bbylw/clawdbot-cn](https://github.com/bbylw/clawdbot-cn) - 중국어 Clawdbot 버전
- [lllooollpp/clawdbot-cn](https://github.com/lllooollpp/clawdbot-cn) - Electron 데스크톱 중국어 버전
- [mengjian-github/xiaomo-starter-kit](https://github.com/mengjian-github/xiaomo-starter-kit) - 중국어 AI 어시스턴트 템플릿

### 한국어（한국어）

- [OpenClaw-Korea/awesome-openclaw](https://github.com/OpenClaw-Korea/awesome-openclaw) - 한국 커뮤니티 리소스

---

## 보안 및 연구

### 보안 연구 및 취약점

- [ethiack/moltbot-1click-rce](https://github.com/ethiack/moltbot-1click-rce) - 보안 개념 증명 (CVE-2026-25253)

### 방어 및 보호

- [seojoonkim/prompt-guard](https://github.com/seojoonkim/prompt-guard) - 프롬프트 인젝션 방어 시스템
- [NirDiamant/moltbook-agent-guard](https://github.com/NirDiamant/moltbook-agent-guard) - 에이전트용 실시간 보안

---

## 커뮤니티 및 리소스

### 기타 Awesome Lists

- [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) - 가장 오래된/가장 포괄적인 목록
- [eltociear/awesome-molt-ecosystem](https://github.com/eltociear/awesome-molt-ecosystem) - OpenClaw 생태계 플랫폼 및 도구
- [thewh1teagle/awesome-openclaw](https://github.com/thewh1teagle/awesome-openclaw) - 대체 큐레이팅 목록
- [shaoxiang/awesome-openclaw](https://github.com/shaoxiang/awesome-openclaw) - 생태계 리소스

### 커뮤니티 프로젝트

- [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) - AI 에이전트 템플릿
- [ThisIsJeron/awesome-openclaw-plugins](https://github.com/ThisIsJeron/awesome-openclaw-plugins) - 플러그인 컬렉션

---

## 기여하기

환영합니다! 리소스 추가 방법에 대한 가이드라인은 [CONTRIBUTING.md](CONTRIBUTING.md)를 읽어주세요.

**제출 전 빠른 체크리스트:**
- [ ] 프로젝트가 [품질 표준](CONTRIBUTING.md#筛选标准)을 충족합니다
- [ ] 지난 6개월 이내에 업데이트됨 (역사적으로 중요한 경우 제외)
- [ ] 명확한 문서가 있음
- [ ] 기존 형식을 따름
- [ ] 가장 관련성 높은 분류에 배치됨

---

## 라이선스

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](LICENSE)

법률이 허용하는 범위 내에서, 본 작품의 저자는 본 작품에 대한 모든 저작권 및 관련 또는 인접 권리를 포기합니다.

---

## Star 히스토리

[![Star History Chart](https://api.star-history.com/svg?repos=vivy-yi/awesome-openclaw&type=Date)](https://star-history.com/#vivy-yi/awesome-openclaw&Date)

---

<div align="center">

**[⬆ 맨 위로](#awesome-openclaw)**

OpenClaw 커뮤니티가 ❤️로 제작

</div>
