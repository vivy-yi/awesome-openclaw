# Awesome OpenClaw

<div align="center">

**[English](README.md) | [简体中文](README.zh-CN.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md) | [Deutsch](README.de.md)**

> Une liste sélectionnée de ressources, outils, plateformes et projets communautaires Awesome OpenClaw (anciennement Moltbot/Clawdbot)

[![License](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)
[![Verify Links](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml/badge.svg)](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml)

[OpenClaw](https://github.com/openclaw/openclaw) | [Écosystème Molt](https://moltbook.com) | [Contribuer](#contribuer)

</div>

---

## À propos d'OpenClaw

**OpenClaw** est un assistant personnel IA qui fonctionne sur tous les OS et plateformes - "The lobster way". C'est un agent IA puissant et extensible avec un vaste écosystème d'outils, de plateformes et de contributions communautaires.

### Évolution du projet

```
🦞 Clawdbot (Original)  →  🦂 Moltbot (v1)  →  🔥 OpenClaw (Actuel, fin 2025)
```

### Caractéristiques clés

- **Multi-plateforme**: macOS, Linux, Windows, via Docker, Cloudflare Workers, etc.
- **Extensible**: 700+ compétences communautaires sur [ClawHub](https://clawhub.ai)
- **Messagerie multi-plateforme**: Telegram, Discord, Slack, WeChat, Feishu, DingTalk, et 12+ plateformes
- **Communication agent-à-agent**: Support intégré des plateformes sociales de l'écosystème Molt
- **Langage**: TypeScript/JavaScript, basé sur Node.js

---

## Table des matières

- [Projets principaux](#projets-principaux)
- [Plateformes de l'écosystème Molt](#plateformes-de-lécosystème-molt)
- [Déploiement et installation](#déploiement-et-installation)
- [Intégrations de plateformes](#intégrations-de-plateformes)
- [Mémoire et stockage](#mémoire-et-stockage)
- [Surveillance et outils](#surveillance-et-outils)
- [Compétences et extensions](#compétences-et-extensions)
- [Solutions entreprise](#solutions-entreprise)
- [Localisation](#localisation)
- [Sécurité et recherche](#sécurité-et-recherche)
- [Communauté et ressources](#communauté-et-ressources)
- [Contribuer](#contribuer)

---

## Projets principaux

### Dépôts officiels

| Projet | Stars | Description | Langage |
|---------|-------|-------------|----------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw) | Assistant personnel IA principal - "The lobster way" | TypeScript |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | - | Registre officiel des compétences avec 700+ compétences communautaires | TypeScript |
| [openclaw/skills](https://github.com/openclaw/skills) | - | Archive de toutes les versions des compétences de clawdhub.com | TypeScript |
| [openclaw/lobster](https://github.com/openclaw/lobster) | - | Shell de workflow pour pipelines composites et automatisations | TypeScript |
| [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) | - | Intégration du gestionnaire de paquets Nix | Nix |
| [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | - | Installation renforcée automatisée avec Ansible (Tailscale VPN, UFW, Docker) | Ansible |
| [openclaw/clawdinators](https://github.com/openclaw/clawdinators) | - | Infrastructure déclarative + modules NixOS pour les hôtes CLAWTINATOR | NixOS |
| [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) | - | Homebrew tap pour l'installation macOS | Shell |
| [openclaw/openclaw.ai](https://github.com/openclaw/openclaw.ai) | - | Site web officiel (molt.bot) | TypeScript |
| [openclaw/clawgo](https://github.com/openclaw/clawgo) | - | Implémentation de nœud Clawd en Go | Go |

### Ressources historiques

- [Clawdbot Archive](https://github.com/clawdbot) - Dépôts Clawdbot originaux et historique
- [Moltbot Archive](https://github.com/molt-bot) - Dépôts de l'époque Moltbot

---

## Projets Inspirés par OpenClaw

L'écosystème OpenClaw a inspiré de nombreuses implémentations alternatives, forks et projets similaires.

### Projets Vedettes ⭐

| Projet | Stars | Description | Langage | Caractéristiques Uniques |
|---------|-------|-------------|----------|-----------------|
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | ![Stars](https://img.shields.io/github/stars/HKUDS/nanobot) | Assistant IA ultra-léger (~4K LOC vs 430K+) | Python | Multi-fournisseurs LLM, vLLM local |
| [ysz/nanoClaw](https://github.com/ysz/nanoClaw) | ![Stars](https://img.shields.io/github/stars/ysz/nanoClaw) | Assistant IA léger sécurisé (~3K LOC) | Python | 6 couches de sécurité |
| [puremachinery/carapace](https://github.com/puremachinery/carapace) | ![Stars](https://img.shields.io/github/stars/puremachinery/carapace) | Assistant IA sécurisé | Rust | Plugins WASM, sandbox OS |
| [gavrielc/nanoclaw](https://github.com/gavrielc/nanoclaw) | ![Stars](https://img.shields.io/github/stars/gavrielc/nanoclaw) | Assistant IA à conteneurs isolés | TypeScript | Conteneurs Apple/Docker |
| [puretensor/hal-claude](https://github.com/puretensor/hal-claude) | ![Stars](https://img.shields.io/github/stars/puretensor/hal-claude) | Alternative OpenClaw minimale (200 lignes) | Python | Auth CLI Claude Code |
| [microclaw/microclaw](https://github.com/microclaw/microclaw) | ![Stars](https://img.shields.io/github/stars/microclaw/microclaw) | Assistant IA agente avec outils complets | Rust | 22+ outils, reprise session |

### Alternatives Légères (500-4,000 LOC)

- [nanobot](https://github.com/HKUDS/nanobot) - Multi-fournisseurs, vLLM, 4 canaux
- [nanoClaw](https://github.com/ysz/nanoClaw) - 6 couches sécurité, assistant configuration
- [ApeCodeAI/nanoclaw-py](https://github.com/ApeCodeAI/nanoclaw-py) - Implémentation Python minimale
- [htlin222/mini-claw](https://github.com/htlin222/mini-claw) - Alternative minimaliste

### Variantes Renforcées Sécurité 🔒

- [Carapace](https://github.com/puremachinery/carapace) - Runtime WASM, signatures Ed25519
- [nanoClaw](https://github.com/ysz/nanoClaw) - Pas de ports ouverts, credentials chiffrés
- [Dshubhambadola/Fortclaw](https://github.com/Dshubhambadola/Fortclaw) - Contrôles sécurité production
- [princezuda/safeclaw](https://github.com/princezuda/safeclaw) - Pas de GenAI (VADER, regex)

### Implémentations Rust (Performance)

- [Carapace](https://github.com/puremachinery/carapace) - Plugins WASM, secrets chiffrés
- [MicroClaw](https://github.com/microclaw/microclaw) - Persistance session, compression contexte
- [shimaenaga1123/rustclaw](https://github.com/shimaenaga1123/rustclaw) - Assistant IA Discord, sandbox Docker
- [PhillipTh0mas/crabbot](https://github.com/PhillipTh0mas/crabbot) - Local-first, état supporté fichiers

### Ports de Langue/Plateforme

- [dyzdyz010/clawd_ex](https://github.com/dyzdyz010/clawd_ex) - Elixir/OTP tolérance aux pannes
- [bsakel/honeybadger](https://github.com/bsakel/honeybadger) - Bot minimal C#
- [jimtin/zetherion-ai](https://github.com/jimtin/zetherion-ai) - Python, Discord, mémoire vectorielle
- [hmennen90/open-entity](https://github.com/hmennen90/open-entity) - Entité autonome PHP/Laravel

---

## Plateformes de l'écosystème Molt

L'écosystème Molt est une série de plateformes où les agents IA interagissent, socialisent et commercent.

### Plateformes sociales

- [MoltBook](https://moltbook.com) - Réseau social de style Reddit pour les agents IA (770K+ agents actifs)
  - [moltbook/api](https://github.com/moltbook/api) - Service API principal
  - [moltbook/moltbook-frontend](https://github.com/moltbook/moltbook-frontend) - Frontend officiel Next.js 14
  - [moltbook/auth](https://github.com/moltbook/auth) - Package d'authentification officiel
  - [moltbook/agent-development-kit](https://github.com/moltbook/agent-development-kit) - SDK multi-plateforme (TypeScript, Swift, Kotlin)

- [MoltCities](https://moltcities.org) - Couche résidentielle avec adresses, identité, messagerie et primes
- [MoltMatch](https://moltmatch.xyz) - Réseau de rencontres pour les agents IA
- [4claw](https://www.4claw.org) - Imageboard agent-first

### Plateformes commerciales et de lancement

- [Molthunt](https://molthunt.com) - Plateforme de lancement de style Product Hunt pour les projets construits par des agents (70+ projets)
- [letsmolt.fun](https://letsmolt.fun) - Plateforme de lancement de jetons sur Solana
- [MoltRoad](https://moltroad.com) - Marché souterrain avec économie de jetons

### Infrastructure

- [ClawHub](https://clawhub.ai) - Registre des compétences avec recherche vectorielle

### Outils MoltBook

- [terminalcraft/moltbook-mcp](https://github.com/terminalcraft/moltbook-mcp) - Serveur MCP pour MoltBook
- [daveholtz/moltbook_scraper](https://github.com/daveholtz/moltbook_scraper) - Scraping des données MoltBook
- [c4pt0r/minibook](https://github.com/c4pt0r/minibook) - MoltBook auto-hébergé
- [terminaltrove/moltbook-tui](https://github.com/terminaltrove/moltbook-tui) - Client UI terminal
- [obra/moltipass](https://github.com/obra/moltipass) - Client iOS pour humains
- [crertel/moltbook-client](https://github.com/crertel/moltbook-client) - Serveur local pour les conversations humaines
- [compscidr/moltbook-index](https://github.com/compscidr/moltbook-index) - Annuaire d'agents recherchable

---

## Déploiement et installation

### Docker et conteneurs

- [willbullen/openclaw-docker](https://github.com/willbullen/openclaw-docker) - Docker Compose de production avec durcissement de sécurité
- [khal3d/openclaw](https://github.com/khal3d/openclaw) - Déploiement Docker et HELM
- [jchen0824/clawdbot-docker-deploy](https://github.com/jchen0824/clawdbot-docker-deploy) - Déploiement VPS en un script
- [gravity182/clawdbot-docker](https://github.com/gravity182/clawdbot-docker) - Déploiement Kubernetes homelab
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - Docker pour Telegram/WhatsApp/Discord
- [essamamdani/openclaw-coolify](https://github.com/essamamdani/openclaw-coolify) - Modèle de déploiement Coolify

### Plateformes cloud

- [cloudflare/moltworker](https://github.com/cloudflare/moltworker) - Exécuter OpenClaw sur Cloudflare Workers (projet officiel Cloudflare)

### Gestion de configuration

- [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) - Installation renforcée automatisée avec Ansible
- [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) - Intégration du gestionnaire de paquets Nix
- [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) - Homebrew tap pour l'installation macOS

### Outils d'installation

- [miaoxworld/OpenClawInstaller](https://github.com/miaoxworld/OpenClawInstaller) - Outil de déploiement en un clic chinois

---

## Intégrations de plateformes

### Plateformes internationales

**Telegram et Discord :**
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - Configuration Docker pour Telegram/WhatsApp/Discord
- [VizuaraAILabs/Slack-ClawdBot](https://github.com/VizuaraAILabs/Slack-ClawdBot) - Intégration Slack
- [shanselman/openclaw-windows-hub](https://github.com/shanselman/openclaw-windows-hub) - Barre d'état système Windows + PowerToys

**Mobile et voix :**
- [chrisherold/clawdy](https://github.com/chrisherold/clawdy) - Interface vocale iOS

### Plateformes IM chinoises

**Multi-plateforme :**
- [justlovemaki/OpenClaw-Docker-CN-IM](https://github.com/justlovemaki/OpenClaw-Docker-CN-IM) - Feishu, DingTalk, QQ, WeCom
- [BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) - Feishu, DingTalk, QQ, WeChat

**Feishu (Lark) :**
- [AlexAnys/feishu-openclaw](https://github.com/AlexAnys/feishu-openclaw) - Intégration Feishu/Lark
- [m1heng/clawdbot-feishu](https://github.com/m1heng/clawdbot-feishu) - Intégration Feishu

**DingTalk :**
- [soimy/openclaw-channel-dingtalk](https://github.com/soimy/openclaw-channel-dingtalk) - Canal DingTalk
- [DingTalk-Real-AI/dingtalk-moltbot-connector](https://github.com/DingTalk-Real-AI/dingtalk-moltbot-connector) - Connecteur DingTalk avec support des cartes IA

**QQ :**
- [constansino/openclaw_qq](https://github.com/constansino/openclaw_qq) - QQ (OneBot v11)

**WeChat Work (WeCom) :**
- [11haonb/wecom-openclaw-plugin](https://github.com/11haonb/wecom-openclaw-plugin) - Plugin WeChat Work

### Plateformes coréennes

- [tornado1014/clawdbot-kakaotalk](https://github.com/tornado1014/clawdbot-kakaotalk) - Intégration KakaoTalk

---

## Mémoire et stockage

### Bases de données vectorielles et systèmes de mémoire

- [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) - Mémoire pour les agents proactifs 24/7
- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) - OS de mémoire IA pour les systèmes LLM et agents
- [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) - Mémoire et rappel parfaits
- [oceanbase/powermem](https://github.com/oceanbase/powermem) - Mémoire à long terme alimentée par l'IA
- [Vel-Labs/molting-memory](https://github.com/Vel-Labs/molting-memory) - Base de données vectorielle basée sur QDrant
- [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) - Couche de mémoire à long terme pour les agents MoltBook

---

## Surveillance et outils

### Interfaces web et tableaux de bord

- [ibelick/webclaw](https://github.com/ibelick/webclaw) - Client web rapide pour OpenClaw
- [clawdeckio/clawdeck](https://github.com/clawdeckio/clawdeck) - Centre de mission pour les agents OpenClaw
- [crshdn/mission-control](https://github.com/crshdn/mission-control) - Tableau de bord d'orchestration d'agents IA
- [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) - Studio/IDE pour OpenClaw

### Surveillance et observabilité

- [luccast/crabwalk](https://github.com/luccast/crabwalk) - Moniteur compagnon en temps réel pour les agents OpenClaw

### Suivi des coûts

- [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) - CLI de suivi de l'utilisation des tokens
- [bokonon23/clawdbot-cost-monitor](https://github.com/bokonon23/clawdbot-cost-monitor) - Suivi des dépenses IA en temps réel

---

## Compétences et extensions

### Collections de compétences officielles

- [openclaw/skills](https://github.com/openclaw/skills) - Archive des compétences officielles
- [openclaw/clawhub](https://github.com/openclaw/clawhub) - Registre des compétences officielles avec 700+ compétences

### Bibliothèques de compétences communautaires

- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - Collection de compétences sélectionnées par la communauté
- [natan89/awesome-openclaw-skills](https://github.com/natan89/awesome-openclaw-skills) - 1715+ compétences pilotées par la communauté
- [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) - Collection de compétences populaires

### Compétences spécialisées

- [BankrBot/openclaw-skills](https://github.com/BankrBot/openclaw-skills) - Compétences axées sur le trading et DeFi
- [jdrhyne/agent-skills](https://github.com/jdrhyne/agent-skills) - Compétences de framework multi-agents
- [runkids/skillshare](https://github.com/runkids/skillshare) - Synchroniser les compétences entre les outils IA CLI
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) - Planification Markdown persistante style Manus
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) - Compétences d'agent Obsidian
- [lekt9/unbrowse-openclaw](https://github.com/lekt9/unbrowse-openclaw) - Générateur de compétences API auto-apprenant

---

## Solutions entreprise

- [archestra-ai/archestra](https://github.com/archestra-ai/archestra) - OpenClaw Entreprise avec RBAC, MCP, A2A
- [backbay-labs/clawdstrike](https://github.com/backbay-labs/clawdstrike) - Plateforme de détection et réponse swarm (SDR)
- [knostic/openclaw-detect](https://github.com/knostic/openclaw-detect) - Scripts de détection MDM pour OpenClaw
- [TheSethRose/Clawdbot-Security-Check](https://github.com/TheSethRose/Clawdbot-Security-Check) - Compétence d'audit de sécurité

---

## Localisation

### Chinois (简体)

- [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) - Traduction chinoise complète
- [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) - Bibliothèque de compétences chinoises
- [bbylw/clawdbot-cn](https://github.com/bbylw/clawdbot-cn) - Version chinoise de Clawdbot
- [lllooollpp/clawdbot-cn](https://github.com/lllooollpp/clawdbot-cn) - Version chinoise de bureau Electron
- [mengjian-github/xiaomo-starter-kit](https://github.com/mengjian-github/xiaomo-starter-kit) - Kit de démarrage d'assistant IA chinois

### Coréen（한국어）

- [OpenClaw-Korea/awesome-openclaw](https://github.com/OpenClaw-Korea/awesome-openclaw) - Ressources communautaires coréennes

---

## Sécurité et recherche

### Recherche en sécurité et vulnérabilités

- [ethiack/moltbot-1click-rce](https://github.com/ethiack/moltbot-1click-rce) - Preuve de concept de sécurité (CVE-2026-25253)

### Défense et protection

- [seojoonkim/prompt-guard](https://github.com/seojoonkim/prompt-guard) - Système de défense contre l'injection de prompt
- [NirDiamant/moltbook-agent-guard](https://github.com/NirDiamant/moltbook-agent-guard) - Sécurité en temps réel pour les agents

---

## Communauté et ressources

### Autres Awesome Lists

- [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) - Liste la plus ancienne/most complète
- [eltociear/awesome-molt-ecosystem](https://github.com/eltociear/awesome-molt-ecosystem) - Plateformes et outils de l'écosystème Molt
- [thewh1teagle/awesome-openclaw](https://github.com/thewh1teagle/awesome-openclaw) - Liste alternative sélectionnée
- [shaoxiang/awesome-openclaw](https://github.com/shaoxiang/awesome-openclaw) - Ressources de l'écosystème

### Projets communautaires

- [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) - Modèles d'agents IA
- [ThisIsJeron/awesome-openclaw-plugins](https://github.com/ThisIsJeron/awesome-openclaw-plugins) - Collection de plugins

---

## Contribuer

Les contributions sont les bienvenues ! Veuillez lire [CONTRIBUTING.md](CONTRIBUTING.md) pour les directives sur l'ajout de ressources.

**Liste de contrôle rapide avant soumission :**
- [ ] Le projet respecte nos [normes de qualité](CONTRIBUTING.md#筛选标准)
- [ ] Mis à jour au cours des 6 derniers mois (sauf importance historique)
- [ ] Documentation claire
- [ ] Respecte le format existant
- [ ] Placé dans la catégorie la plus pertinente

---

## Licence

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](LICENSE)

Dans la mesure permise par la loi, les auteurs de cette œuvre ont renoncé à tous droits d'auteur et droits connexes ou voisins.

---

## Historique des Stars

[![Star History Chart](https://api.star-history.com/svg?repos=vivy-yi/awesome-openclaw&type=Date)](https://star-history.com/#vivy-yi/awesome-openclaw&Date)

---

<div align="center">

**[⬆ Retour en haut](#awesome-openclaw)**

Fait avec ❤️ par la communauté OpenClaw

</div>
