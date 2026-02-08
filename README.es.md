# Awesome OpenClaw

<div align="center">

**[English](README.md) | [简体中文](README.zh-CN.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [Français](README.fr.md) | [Español](README.es.md) | [Deutsch](README.de.md)**

> Una lista curada de recursos, herramientas, plataformas y proyectos comunitarios awesome de OpenClaw (anteriormente Moltbot/Clawdbot)

[![License](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)
[![Verify Links](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml/badge.svg)](https://github.com/vivy-yi/awesome-openclaw/actions/workflows/verify-links.yml)

[OpenClaw](https://github.com/openclaw/openclaw) | [Ecosistema Molt](https://moltbook.com) | [Contribuir](#contribuir)

</div>

---

## Acerca de OpenClaw

**OpenClaw** es un asistente personal de IA que funciona en cualquier sistema operativo y plataforma - "The lobster way". Es un agente de IA potente y extensible con un vasto ecosistema de herramientas, plataformas y contribuciones de la comunidad.

### Evolución del proyecto

```
🦞 Clawdbot (Original)  →  🦂 Moltbot (v1)  →  🔥 OpenClaw (Actual, finales de 2025)
```

### Características clave

- **Multiplataforma**: macOS, Linux, Windows, vía Docker, Cloudflare Workers, etc.
- **Extensible**: 700+ habilidades de la comunidad en [ClawHub](https://clawhub.ai)
- **Mensajería multiplataforma**: Telegram, Discord, Slack, WeChat, Feishu, DingTalk, y 12+ plataformas
- **Comunicación agente-a-agente**: Soporte integrado para plataformas sociales del ecosistema Molt
- **Lenguaje**: TypeScript/JavaScript, basado en Node.js

---

## Contenidos

- [Proyectos principales](#proyectos-principales)
- [Plataformas del ecosistema Molt](#plataformas-del-ecosistema-molt)
- [Despliegue e instalación](#despliegue-e-instalación)
- [Integraciones de plataformas](#integraciones-de-plataformas)
- [Memoria y almacenamiento](#memoria-y-almacenamiento)
- [Monitoreo y herramientas](#monitoreo-y-herramientas)
- [Habilidades y extensiones](#habilidades-y-extensiones)
- [Soluciones empresariales](#soluciones-empresariales)
- [Localización](#localización)
- [Seguridad e investigación](#seguridad-e-investigación)
- [Comunidad y recursos](#comunidad-y-recursos)
- [Contribuir](#contribuir)

---

## Proyectos principales

### Repositorios oficiales

| Proyecto | Stars | Descripción | Lenguaje |
|---------|-------|-------------|----------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw) | Asistente personal de IA principal - "The lobster way" | TypeScript |
| [openclaw/clawhub](https://github.com/openclaw/clawhub) | - | Registro oficial de habilidades con 700+ habilidades comunitarias | TypeScript |
| [openclaw/skills](https://github.com/openclaw/skills) | - | Archivo de todas las versiones de habilidades de clawdhub.com | TypeScript |
| [openclaw/lobster](https://github.com/openclaw/lobster) | - | Shell de flujo de trabajo para tuberías componibles y automatizaciones | TypeScript |
| [openclaw/nix-openclaw](https://github.com/openclaw/nix-openclaw) | - | Integración del gestor de paquetes Nix | Nix |
| [openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | - | Instalación endurezida automatizada con Ansible (Tailscale VPN, UFW, Docker) | Ansible |
| [openclaw/clawdinators](https://github.com/openclaw/clawdinators) | - | Infraestructura declarativa + módulos NixOS para hosts CLAWTINATOR | NixOS |
| [openclaw/homebrew-tap](https://github.com/openclaw/homebrew-tap) | - | Homebrew tap para instalación macOS | Shell |
| [openclaw/openclaw.ai](https://github.com/openclaw/openclaw.ai) | - | Sitio web oficial (molt.bot) | TypeScript |
| [openclaw/clawgo](https://github.com/openclaw/clawgo) | - | Implementación de nodo Clawd en Go | Go |

### Recursos históricos

- [Clawdbot Archive](https://github.com/clawdbot) - Repositorios Clawdbot originales e historia
- [Moltbot Archive](https://github.com/molt-bot) - Repositorios de la era Moltbot

---

## Plataformas del ecosistema Molt

El ecosistema Molt es una serie de plataformas donde los agentes de IA interactúan, socializan y comercian.

### Plataformas sociales

- [MoltBook](https://moltbook.com) - Red social estilo Reddit para agentes de IA (770K+ agentes activos)
  - [moltbook/api](https://github.com/moltbook/api) - Servicio API principal
  - [moltbook/moltbook-frontend](https://github.com/moltbook/moltbook-frontend) - Frontend oficial Next.js 14
  - [moltbook/auth](https://github.com/moltbook/auth) - Paquete de autenticación oficial
  - [moltbook/agent-development-kit](https://github.com/moltbook/agent-development-kit) - SDK multiplataforma (TypeScript, Swift, Kotlin)

- [MoltCities](https://moltcities.org) - Capa residencial con direcciones, identidad, mensajería y recompensas
- [MoltMatch](https://moltmatch.xyz) - Red de citas para agentes de IA
- [4claw](https://www.4claw.org) - Tablero de imágenes agent-first

### Plataformas comerciales y de lanzamiento

- [Molthunt](https://molthunt.com) - Plataforma de lanzamiento estilo Product Hunt para proyectos construidos por agentes (70+ proyectos)
- [letsmolt.fun](https://letsmolt.fun) - Plataforma de lanzamiento de tokens en Solana
- [MoltRoad](https://moltroad.com) - Mercado subterráneo con economía de tokens

### Herramientas MoltBook

- [terminalcraft/moltbook-mcp](https://github.com/terminalcraft/moltbook-mcp) - Servidor MCP para MoltBook
- [daveholtz/moltbook_scraper](https://github.com/daveholtz/moltbook_scraper) - Scraping de datos de MoltBook
- [c4pt0r/minibook](https://github.com/c4pt0r/minibook) - MoltBook autohospedado
- [terminaltrove/moltbook-tui](https://github.com/terminaltrove/moltbook-tui) - Cliente UI de terminal
- [obra/moltipass](https://github.com/obra/moltipass) - Cliente iOS para humanos
- [crertel/moltbook-client](https://github.com/crertel/moltbook-client) - Servidor local para conversaciones humanas
- [compscidr/moltbook-index](https://github.com/compscidr/moltbook-index) - Directorio de agentes searchable

---

## Despliegue e instalación

### Docker y contenedores

- [willbullen/openclaw-docker](https://github.com/willbullen/openclaw-docker) - Docker Compose de producción con endurezimiento de seguridad
- [khal3d/openclaw](https://github.com/khal3d/openclaw) - Despliegue Docker y HELM
- [jchen0824/clawdbot-docker-deploy](https://github.com/jchen0824/clawdbot-docker-deploy) - Despliegue VPS en un script
- [gravity182/clawdbot-docker](https://github.com/gravity182/clawdbot-docker) - Despliegue Kubernetes homelab
- [hayka-pacha/clawdbot-in-docker](https://github.com/hayka-pacha/clawdbot-in-docker) - Docker para Telegram/WhatsApp/Discord
- [essamamdani/openclaw-coolify](https://github.com/essamamdani/openclaw-coolify) - Plantilla de despliegue Coolify

### Plataformas cloud

- [cloudflare/moltworker](https://github.com/cloudflare/moltworker) - Ejecutar OpenClaw en Cloudflare Workers (proyecto oficial Cloudflare)

---

## Memoria y almacenamiento

- [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) - Memoria para agentes proactivos 24/7
- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) - Sistema operativo de memoria IA para sistemas LLM y agentes
- [supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) - Memoria perfecta y recuerdo
- [oceanbase/powermem](https://github.com/oceanbase/powermem) - Memoria a largo plazo impulsada por IA
- [Vel-Labs/molting-memory](https://github.com/Vel-Labs/molting-memory) - Base de datos vectorial basada en QDrant
- [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) - Capa de memoria a largo plazo para agentes MoltBook

---

## Monitoreo y herramientas

### Interfaces web y tableros

- [ibelick/webclaw](https://github.com/ibelick/webclaw) - Cliente web rápido para OpenClaw
- [clawdeckio/clawdeck](https://github.com/clawdeckio/clawdeck) - Centro de misión para agentes OpenClaw
- [crshdn/mission-control](https://github.com/crshdn/mission-control) - Tablero de orquestación de agentes de IA
- [grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) - Studio/IDE para OpenClaw

### Monitoreo y observabilidad

- [luccast/crabwalk](https://github.com/luccast/crabwalk) - Monitor compañero en tiempo real para agentes OpenClaw

### Seguimiento de costos

- [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) - CLI de seguimiento de uso de tokens
- [bokonon23/clawdbot-cost-monitor](https://github.com/bokonon23/clawdbot-cost-monitor) - Rastreador de gastos de IA en tiempo real

---

## Habilidades y extensiones

### Colecciones oficiales

- [openclaw/skills](https://github.com/openclaw/skills) - Archivo de habilidades oficiales
- [openclaw/clawhub](https://github.com/openclaw/clawhub) - Registro oficial de habilidades con 700+ habilidades

### Bibliotecas comunitarias

- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - Colección de habilidades curada por la comunidad
- [natan89/awesome-openclaw-skills](https://github.com/natan89/awesome-openclaw-skills) - 1715+ habilidades impulsadas por la comunidad
- [sundial-org/awesome-openclaw-skills](https://github.com/sundial-org/awesome-openclaw-skills) - Colección de habilidades populares

---

## Soluciones empresariales

- [archestra-ai/archestra](https://github.com/archestra-ai/archestra) - OpenClaw Empresarial con RBAC, MCP, A2A
- [backbay-labs/clawdstrike](https://github.com/backbay-labs/clawdstrike) - Plataforma de detección y respuesta enjambre (SDR)
- [knostic/openclaw-detect](https://github.com/knostic/openclaw-detect) - Scripts de detección MDM para OpenClaw
- [TheSethRose/Clawdbot-Security-Check](https://github.com/TheSethRose/Clawdbot-Security-Check) - Habilidad de auditoría de seguridad

---

## Localización

### Chino (简体)

- [1186258278/OpenClawChineseTranslation](https://github.com/1186258278/OpenClawChineseTranslation) - Traducción china completa
- [clawdbot-ai/awesome-openclaw-skills-zh](https://github.com/clawdbot-ai/awesome-openclaw-skills-zh) - Biblioteca de habilidades china
- [bbylw/clawdbot-cn](https://github.com/bbylw/clawdbot-cn) - Versión china de Clawdbot
- [lllooollpp/clawdbot-cn](https://github.com/lllooollpp/clawdbot-cn) - Versión china de escritorio Electron

### Coreano（한국어）

- [OpenClaw-Korea/awesome-openclaw](https://github.com/OpenClaw-Korea/awesome-openclaw) - Recursos comunitarios coreanos

---

## Seguridad e investigación

- [ethiack/moltbot-1click-rce](https://github.com/ethiack/moltbot-1click-rce) - Prueba de concepto de seguridad (CVE-2026-25253)
- [seojoonkim/prompt-guard](https://github.com/seojoonkim/prompt-guard) - Sistema de defensa contra inyección de prompts
- [NirDiamant/moltbook-agent-guard](https://github.com/NirDiamant/moltbook-agent-guard) - Seguridad en tiempo real para agentes

---

## Comunidad y recursos

### Otras Awesome Lists

- [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) - Lista más antigua/más completa
- [eltociear/awesome-molt-ecosystem](https://github.com/eltociear/awesome-molt-ecosystem) - Plataformas y herramientas del ecosistema Molt
- [thewh1teagle/awesome-openclaw](https://github.com/thewh1teagle/awesome-openclaw) - Lista alternativa curada

---

## Contribuir

¡Las contribuciones son bienvenidas! Por favor lee [CONTRIBUTING.md](CONTRIBUTING.md) para directrices sobre agregar recursos.

**Lista de verificación rápida antes de enviar:**
- [ ] El proyecto cumple con nuestros [estándares de calidad](CONTRIBUTING.md#筛选标准)
- [ ] Actualizado en los últimos 6 meses (excepto importancia histórica)
- [ ] Documentación clara
- [ ] Sigue el formato existente
- [ ] Ubicado en la categoría más relevante

---

## Licencia

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](LICENSE)

En la medida permitida por la ley, los autores de esta obra han renunciado a todos los derechos de autor y derechos conexos o vecinos.

---

## Historial de Stars

[![Star History Chart](https://api.star-history.com/svg?repos=vivy-yi/awesome-openclaw&type=Date)](https://star-history.com/#vivy-yi/awesome-openclaw&Date)

---

<div align="center">

**[⬆ Volver arriba](#awesome-openclaw)**

Hecho con ❤️ por la comunidad OpenClaw

</div>
