# Awesome OpenClaw

<div align="center">

**[English](README.md) | [简体中文](README.zh-CN.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md) | [Deutsch](README.de.md)**

> Eine kuratierte Liste von awesome OpenClaw (ehemals Moltbot/Clawdbot) Ressourcen, Tools, Plattformen und Community-Projekten

[![License](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)
[![Verify Links](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml/badge.svg)](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml)

[OpenClaw](https://github.com/openclaw/openclaw) | [Molt-Ökosystem](https://moltbook.com) | [Beitragen](#beitragen)

</div>

---

## Über OpenClaw

**OpenClaw** ist ein persönlicher KI-Assistent, der auf jedem Betriebssystem und jeder Plattform läuft - "The lobster way". Es ist ein mächtiger und erweiterbarer KI-Agent mit einem riesigen Ökosystem an Tools, Plattformen und Community-Beiträgen.

### Projektentwicklung

```
🦞 Clawdbot (Original)  →  🦂 Moltbot (v1)  →  🔥 OpenClaw (Aktuell, Ende 2025)
```

### Hauptmerkmale

- **Plattformübergreifend**: macOS, Linux, Windows, via Docker, Cloudflare Workers, etc.
- **Erweiterbar**: 700+ Community-Fähigkeiten auf [ClawHub](https://clawhub.ai)
- **Multi-Plattform-Messaging**: Telegram, Discord, Slack, WeChat, Feishu, DingTalk und 12+ weitere Plattformen
- **Agent-zu-Agent-Kommunikation**: Integrierte Unterstützung für Molt-Ökosystem-Sozialplattformen
- **Sprache**: TypeScript/JavaScript, basierend auf Node.js

---

## Inhaltsverzeichnis

- [Kernprojekte](#kernprojekte)
- [Molt-Ökosystem-Plattformen](#molt-Ökosystem-plattformen)
- [Bereitstellung und Installation](#bereitstellung-und-installation)
- [Plattform-Integrationen](#plattform-integrationen)
- [Speicher und Speicherung](#speicher-und-speicherung)
- [Überwachung und Tools](#überwachung-und-tools)
- [Fähigkeiten und Erweiterungen](#fähigkeiten-und-erweiterungen)
- [Unternehmenslösungen](#unternehmenslösungen)
- [Lokalisierung](#lokalisierung)
- [Sicherheit und Forschung](#sicherheit-und-forschung)
- [Community und Ressourcen](#community-und-ressourcen)
- [Beitragen](#beitragen)

---

## Kernprojekte

### Offizielle Repositories

| Projekt | Stars | Beschreibung | Sprache |
|---------|-------|-------------|----------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw) | Haupt persönlicher KI-Assistent - "The lobster way" | TypeScript |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | - | Offizielles Fähigkeiten-Register mit 700+ Community-Fähigkeiten | TypeScript |
| [openclaw/skills](https://github.com/openclaw/skills) | - | Archiv aller Versionen von Fähigkeiten von clawdhub.com | TypeScript |
| [openclaw/lobster](https://github.com/openclaw/lobster) | - | Workflow-Shell für zusammensetzbare Pipelines und Automatisierungen | TypeScript |
| [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) | - | Nix-Paketmanager-Integration | Nix |
| [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | - | Automatisierte gehärtete Installation mit Ansible (Tailscale VPN, UFW, Docker) | Ansible |
| [openclaw/clawdinators](https://github.com/openclaw/clawdinators) | - | Deklarative Infrastruktur + NixOS-Module für CLAWTINATOR-Hosts | NixOS |
| [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) | - | Homebrew-Tap für macOS-Installation | Shell |
| [openclaw/openclaw.ai](https://github.com/openclaw/openclaw.ai) | - | Offizielle Website (molt.bot) | TypeScript |
| [openclaw/clawgo](https://github.com/openclaw/clawgo) | - | Clawd-Knoten-Implementierung in Go | Go |

### Historische Ressourcen

- [Clawdbot Archive](https://github.com/clawdbot) - Originale Clawdbot-Repositories und Geschichte
- [Moltbot Archive](https://github.com/molt-bot) - Repositories aus der Moltbot-Ära

---

## Molt-Ökosystem-Plattformen

Das Molt-Ökosystem ist eine Reihe von Plattformen, auf denen KI-Agenten interagieren, sich sozialisieren und handeln.

### Soziale Plattformen

- [MoltBook](https://moltbook.com) - Reddit-ähnliches soziales Netzwerk für KI-Agenten (770K+ aktive Agenten)
  - [moltbook/api](https://github.com/moltbook/api) - Kern-API-Dienst
  - [moltbook/moltbook-frontend](https://github.com/moltbook/moltbook-frontend) - Offizielles Next.js 14-Frontend
  - [moltbook/auth](https://github.com/moltbook/auth) - Offizielles Authentifizierungspaket
  - [moltbook/agent-development-kit](https://github.com/moltbook/agent-development-kit) - Multi-Plattform-SDK (TypeScript, Swift, Kotlin)

- [MoltCities](https://moltcities.org) - Wohnschicht mit Adressen, Identität, Messaging und Belohnungen
- [MoltMatch](https://moltmatch.xyz) - Dating-Netzwerk für KI-Agenten
- [4claw](https://www.4claw.org) - Agenten-zuerst-Bildboard

### Geschäfts- und Launch-Plattformen

- [Molthunt](https://molthunt.com) - Product Hunt-ähnliche Launch-Plattform für von Agenten gebaute Projekte (70+ Projekte)
- [letsmolt.fun](https://letsmolt.fun) - Token-Launch-Plattform auf Solana
- [MoltRoad](https://moltroad.com) - Underground-Marktplatz mit Token-Ökonomie

### MoltBook-Tools

- [terminalcraft/moltbook-mcp](https://github.com/terminalcraft/moltbook-mcp) - MCP-Server für MoltBook
- [daveholtz/moltbook_scraper](https://github.com/daveholtz/moltbook_scraper) - MoltBook-Daten-Scraping
- [c4pt0r/minibook](https://github.com/c4pt0r/minibook) - Selbst gehostetes MoltBook
- [terminaltrove/moltbook-tui](https://github.com/terminaltrove/moltbook-tui) - Terminal-UI-Client
- [obra/moltipass](https://github.com/obra/moltipass) - iOS-Client für Menschen
- [crertel/moltbook-client](https://github.com/crertel/moltbook-client) - Lokaler Server für menschliche Gespräche

---

## Bereitstellung und Installation

### Docker und Container

- [willbullen/openclaw-docker](https://github.com/willbullen/openclaw-docker) - Produktions-Docker Compose mit Sicherheitshärtung
- [khal3d/openclaw](https://github.com/khal3d/openclaw) - Docker- und HELM-Bereitstellung
- [jchen0824/clawdbot-docker-deploy](https://github.com/jchen0824/clawdbot-docker-deploy) - Ein-Skript-VPS-Bereitstellung
- [gravity182/clawdbot-docker](https://github.com/gravity182/clawdbot-docker) - Homelab-Kubernetes-Bereitstellung
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - Docker für Telegram/WhatsApp/Discord
- [essamamdani/openclaw-coolify](https://github.com/essamamdani/openclaw-coolify) - Coolify-Bereitstellungsvorlage

### Cloud-Plattformen

- [cloudflare/moltworker](https://github.com/cloudflare/moltworker) - OpenClaw auf Cloudflare Workers ausführen (offizielles Cloudflare-Projekt)

---

## Speicher und Speicherung

- [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) - Speicher für 24/7 proaktive Agenten
- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) - KI-Speicher-Betriebssystem für LLM- und Agentensysteme
- [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) - Perfekter Speicher und Abruf
- [oceanbase/powermem](https://github.com/oceanbase/powermem) - KI-gesteuerter Langzeitspeicher
- [Vel-Labs/molting-memory](https://github.com/Vel-Labs/molting-memory) - QDrant-basierte Vektordatenbank
- [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) - Langzeitspeicher-Schicht für MoltBook-Agenten

---

## Überwachung und Tools

### Web-Schnittstellen und Dashboards

- [ibelick/webclaw](https://github.com/ibelick/webclaw) - Schneller Web-Client für OpenClaw
- [clawdeckio/clawdeck](https://github.com/clawdeckio/clawdeck) - Missionskontrolle für OpenClaw-Agenten
- [crshdn/mission-control](https://github.com/crshdn/mission-control) - KI-Agenten-Orchestrierungs-Dashboard
- [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) - Studio/IDE für OpenClaw

### Überwachung und Beobachtbarkeit

- [luccast/crabwalk](https://github.com/luccast/crabwalk) - Echtzeit-Begleitmonitor für OpenClaw-Agenten

### Kostenverfolgung

- [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) - Token-Nutzungsverfolgungs-CLI
- [bokonon23/clawdbot-cost-monitor](https://github.com/bokonon23/clawdbot-cost-monitor) - KI-Ausgaben-Tracker in Echtzeit

---

## Fähigkeiten und Erweiterungen

### Offizielle Fähigkeiten-Sammlungen

- [openclaw/skills](https://github.com/openclaw/skills) - Archiv offizieller Fähigkeiten
- [openclaw/clawhub](https://github.com/openclaw/clawhub) - Offizielles Fähigkeiten-Register mit 700+ Fähigkeiten

### Community-Fähigkeiten-Bibliotheken

- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - Community-kuratierte Fähigkeiten-Sammlung
- [natan89/awesome-openclaw-skills](https://github.com/natan89/awesome-openclaw-skills) - 1715+ community-getriebene Fähigkeiten
- [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) - Beliebte Fähigkeiten-Sammlung

---

## Unternehmenslösungen

- [archestra-ai/archestra](https://github.com/archestra-ai/archestra) - OpenClaw Enterprise mit RBAC, MCP, A2A
- [backbay-labs/clawdstrike](https://github.com/backbay-labs/clawdstrike) - Swarm-Erkennungs- und Reaktionsplattform (SDR)
- [knostic/openclaw-detect](https://github.com/knostic/openclaw-detect) - MDM-Erkennungsskripte für OpenClaw
- [TheSethRose/Clawdbot-Security-Check](https://github.com/TheSethRose/Clawdbot-Security-Check) - Sicherheitsaudit-Fähigkeit

---

## Lokalisierung

### Chinesisch (简体)

- [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) - Vollständige chinesische Übersetzung
- [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) - Chinesische Fähigkeiten-Bibliothek
- [bbylw/clawdbot-cn](https://github.com/bbylw/clawdbot-cn) - Chinesische Clawdbot-Version
- [lllooollpp/clawdbot-cn](https://github.com/lllooollpp/clawdbot-cn) - Chinesische Electron-Desktop-Version

### Koreanisch（한국어）

- [OpenClaw-Korea/awesome-openclaw](https://github.com/OpenClaw-Korea/awesome-openclaw) - Koreanische Community-Ressourcen

---

## Sicherheit und Forschung

- [ethiack/moltbot-1click-rce](https://github.com/ethiack/moltbot-1click-rce) - Sicherheits-Beweis of Concept (CVE-2026-25253)
- [seojoonkim/prompt-guard](https://github.com/seojoonkim/prompt-guard) - Prompt-Injection-Abwehrsystem
- [NirDiamant/moltbook-agent-guard](https://github.com/NirDiamant/moltbook-agent-guard) - Echtzeitsicherheit für Agenten

---

## Community und Ressourcen

### Andere Awesome-Listen

- [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) - Älteste/umfassendste Liste
- [eltociear/awesome-molt-ecosystem](https://github.com/eltociear/awesome-molt-ecosystem) - Molt-Ökosystem-Plattformen und Tools
- [thewh1teagle/awesome-openclaw](https://github.com/thewh1teagle/awesome-openclaw) - Alternative kuratierte Liste

---

## Beitragen

Beiträge sind willkommen! Bitte lesen Sie [CONTRIBUTING.md](CONTRIBUTING.md) für Richtlinien zum Hinzufügen von Ressourcen.

**Schnellcheckliste vor Einreichung:**
- [ ] Projekt erfüllt unsere [Qualitätsstandards](CONTRIBUTING.md#筛选标准)
- [ ] Innerhalb der letzten 6 Monate aktualisiert (außer historischer Bedeutung)
- [ ] Klare Dokumentation
- [ ] Folgt dem vorhandenen Format
- [ ] In der relevantesten Kategorie platziert

---

## Lizenz

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](LICENSE)

Im gesetzlich zulässigen Umfang verzichten die Autoren dieses Werks auf alle Urheberrechte und verwandten oder neighboring rights.

---

## Star-Verlauf

[![Star History Chart](https://api.star-history.com/svg?repos=vivy-yi/awesome-openclaw&type=Date)](https://star-history.com/#vivy-yi/awesome-openclaw&Date)

---

<div align="center">

**[⬆ Nach oben](#awesome-openclaw)**

Gemacht mit ❤️ von der OpenClaw-Community

</div>
