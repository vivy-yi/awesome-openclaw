# Awesome OpenClaw 设计文档

> 创建时间: 2025-02-08
> 作者: Claude & User
> 状态: 设计阶段

## 项目概述

创建一个关于OpenClaw（曾用名Moltbot/Clawdbot）的awesome list，涵盖整个生态系统的优质资源。

### 项目目标

- 提供OpenClaw生态系统的全景地图
- 覆盖从核心项目到外围平台的完整资源
- 服务混合受众（新手+有经验的开发者）
- 与现有35+个awesome lists形成差异化

---

## 整体架构

```
awesome-openclaw/
├── README.md                    # 主文件（核心内容）
├── CONTRIBUTING.md              # 贡献指南
├── LICENSE                      # CC0或类似许可
├── .gitignore
└── .github/
    ├── workflows/
    │   └── verify-links.yml    # 链接检查CI
    └── ISSUE_TEMPLATE/
        └── submit-resource.md  # 资源提交模板
```

---

## 核心分类体系（10大分类）

### 1. 核心项目 Core Projects
- 官方仓库（openclaw、clawhub、lobster等）
- 更名历史说明（Clawdbot → Moltbot → OpenClaw）
- 官方技能仓库

### 2. Molt生态系统平台 Molt Ecosystem Platforms
- **社交平台**: MoltBook（Reddit风格）、MoltCities（身份+消息）、MoltMatch（约会）
- **商业平台**: Molthunt（Product Hunt风格）、letsmolt.fun（代币平台）
- **其他**: 4claw（图片板）、MoltRoad（市场）

### 3. 部署与安装 Deployment & Installation
- **容器化**: Docker、Docker Compose、Kubernetes
- **云平台**: Cloudflare Workers（官方支持）
- **配置管理**: Ansible、NixOS、Homebrew
- **一键安装**: VPS部署脚本

### 4. 平台集成 Platform Integrations
- **国际平台**: Telegram、Discord、Slack
- **中国平台**: 飞书、钉钉、企业微信、微信、QQ
- **其他**: KakaoTalk（韩国）

### 5. 记忆与存储 Memory & Storage
- **向量数据库**: QDrant、专用记忆系统
- **持久化**: memU、MemOS、SuperMemory、PowerMem
- **MoltBook专用**: MoltBrain

### 6. 监控与工具 Monitoring & Tools
- **Web界面**: webclaw、ClawDeck
- **监控工具**: crabwalk（实时监控）
- **成本追踪**: Token使用、AI花费追踪
- **开发工具**: OpenClaw Studio、Tokscale

### 7. 技能与扩展 Skills & Extensions
- **官方**: openclaw/skills
- **社区合集**: VoltAgent、natan89（1700+技能）
- **特定领域**: 交易、Obsidian、多代理框架

### 8. 企业解决方案 Enterprise Solutions
- **安全**: RBAC、MCP（Model Context Protocol）
- **检测**: Knostic、Clawdstrike（SDR）
- **商业版**: Archestra AI

### 9. 本地化 Localization
- **中文**: 翻译、本地化集成、中文技能库
- **韩文**: OpenClaw-Korea
- **其他语言社区**

### 10. 安全与研究 Security & Research
- **安全审计**: 官方安全检查、CVE研究
- **防御**: Prompt注入防御
- **研究工具**: 代理安全防护

---

## 筛选标准

### 活跃度要求
- ⭐ Stars > 10（核心项目除外）
- 📅 Last updated within 6 months（历史重要项目除外）
- ✅ 有清晰的README或文档

### 质量要求
- 📝 完整的文档
- 🔧 可运行的代码（不是demo/placeholder）
- 👥 有社区使用（issues、PRs、forks）

### 分类原则
- 每个项目只归入一个主分类
- 跨领域项目选择最核心的功能分类
- 相关分类使用"See also"交叉引用

---

## 差异化定位

| 特性 | 本列表 | 其他列表 |
|------|--------|----------|
| **Molt生态全景** | ✅ 包含所有50+平台 | ❌ 大部分只关注核心 |
| **部署多样性** | ✅ Docker/K8s/CF/Ansible/Nix | ❌ 通常是Docker为主 |
| **中文生态** | ✅ 专门的中文集成分类 | ❌ 很少提及 |
| **企业视角** | ✅ Enterprise独立分类 | ❌ 混在其他分类 |
| **安全审计** | ✅ 独立的安全研究分类 | ❌ 很少包含 |
| **记忆系统** | ✅ 独立的Memory分类 | ❌ 分散在工具中 |

**定位宣言:**
> "OpenClaw生态系统的全景地图 - 从核心到外围，从个人到企业，从开发到部署"

---

## README.md 结构模板

```markdown
# Awesome OpenClaw

> Curated list of awesome OpenClaw (formerly Moltbot/Clawdbot) resources

[![License](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)
[![Verify Links](https://github.com/yourusername/awesome-openclaw/actions/workflows/verify-links.yml/badge.svg)](https://github.com/yourusername/awesome-openclaw/actions/workflows/verify-links.yml)

## About OpenClaw

OpenClaw is a personal AI assistant that runs on any OS and platform.

**Project Evolution:** 🦞 Clawdbot → 🦂 Moltbot → 🔥 OpenClaw

## Contents

- [Core Projects](#core-projects)
- [Molt Ecosystem Platforms](#molt-ecosystem-platforms)
- [Deployment & Installation](#deployment--installation)
- ... (其他分类)

---

## 核心项目 Core Projects

### Official Repositories

| Project | Stars | Description | Language |
|---------|-------|-------------|----------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | ![Stars](https://img.shields.io/github/stars/openclaw/openclaw) | Main personal AI assistant | TypeScript |

---

## Contributing

PRs welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

[CC0 1.0](LICENSE)
```

---

## 实施计划

### 阶段1: 项目初始化（5分钟）
```bash
mkdir awesome-openclaw && cd awesome-openclaw
git init
gh repo create awesome-openclaw --public --source=. --remote=origin
```

### 阶段2: 内容填充（2-3小时）
- 复制调研数据到各分类
- 手动验证每个仓库
- 编写简短描述
- 添加徽章

### 阶段3: 质量检查（30分钟）
```bash
markdownlint README.md
```

### 阶段4: 自动化CI（15分钟）
添加 `.github/workflows/verify-links.yml`

### 阶段5: 发布与推广（1小时）
- 推送到GitHub
- 添加话题标签
- 社区分享

---

## 自动化工具

| 工具 | 用途 | 频率 |
|------|------|------|
| awesome-bot | 链接有效性检查 | 每周 |
| markdownlint | Markdown格式检查 | 每次PR |
| stale | 标记过期Issue | 自动 |

---

## 维护策略

1. **月度审查**: 检查新增重要项目
2. **季度大更新**: 移除不活跃项目（>6个月）
3. **社区贡献**: 通过PR接受提交

---

## 竞争分析

### 现有Awesome Lists
- **SamurAIGPT/awesome-openclaw**: 最全面但缺乏更新
- **VoltAgent/awesome-openclaw-skills**: 只聚焦技能
- **eltociear/awesome-molt-ecosystem**: 只聚焦Molt平台

### 本列表优势
- ✅ 全面性（核心+外围平台）
- ✅ 及时性（季度更新）
- ✅ 结构化（10大清晰分类）
- ✅ 国际化（中英文并重）

---

## 下一步

准备开始实施？
