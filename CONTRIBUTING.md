# Contributing to Awesome OpenClaw

感谢你对Awesome OpenClaw的贡献！

## 如何贡献

### 多语言支持

我们支持多语言版本的README：

- **README.md** - English (英语)
- **README.zh-CN.md** - 简体中文
- **README.ko.md** - 한국어 (韩语)

#### 添加新语言

如果你想要添加新的语言版本：

1. 创建 `README.<lang-code>.md` 文件（例如 `README.ja.md` 表示日语）
2. 从 `README.md` 复制内容并翻译
3. 在所有README文件顶部添加语言切换链接
4. 更新本文件的语言列表

#### 更新现有翻译

当你更新主README（README.md）时，请同时：

1. 更新所有语言版本的README
2. 保持所有版本的结构一致
3. 确保语言切换器中的链接正确

**注意**: 如果你不精通某个语言，可以只更新你熟悉的版本，并在PR中说明需要其他语言的翻译帮助。

### 添加新资源

1. Fork这个仓库
2. 创建你的特性分支 (`git checkout -b add-amazing-project`)
3. 按照现有格式添加资源
4. 确保资源满足筛选标准
5. 提交更改 (`git commit -m 'Add amazing project'`)
6. 推送到分支 (`git push origin add-amazing-project`)
7. 创建Pull Request

### 筛选标准

在提交PR之前，请确保项目满足以下条件：

**活跃度要求:**
- ⭐ Stars > 10（核心项目除外）
- 📅 Last updated within 6 months（历史重要项目除外）
- ✅ 有清晰的README或文档

**质量要求:**
- 📝 完整的文档
- 🔧 可运行的代码（不是demo/placeholder）
- 👥 有社区使用（issues、PRs、forks）

**格式要求:**
- 使用正确的markdown语法
- 保持与现有条目一致的格式
- 添加简短准确的描述（1-2句话）
- 包含项目主页链接

### 添加格式

请在相应的分类下按以下格式添加：

```markdown
- [项目名称](https://github.com/username/repo) - 简短描述（1-2句话）
```

或者使用表格格式（对于核心项目）：

```markdown
| Project | Stars | Description | Language |
|---------|-------|-------------|----------|
| [username/repo](https://github.com/username/repo) | ![Stars](https://img.shields.io/github/stars/username/repo) | Description | Language |
```

### 分类指南

请将项目添加到最相关的分类下。如果不确定，可以：

1. 查看[分类体系说明](docs/taxonomy.md)
2. 在PR中说明你的理由
3. 使用"See also"在相关分类间交叉引用

### 提交前检查

- [ ] 链接有效且可访问
- [ ] 项目满足筛选标准
- [ ] 格式与现有条目一致
- [ ] 描述准确且简洁
- [ ] 放置在最相关的分类下

## 更新现有条目

如果发现某个项目：
- 已经归档或不再维护
- 链接失效
- 描述不准确
- 应该移动到其他分类

欢迎提交PR更新或移除。

## 代码审查

所有PR都需要经过审查才能合并。我们通常会：

1. 检查格式和语法
2. 验证链接有效性
3. 确认项目符合筛选标准
4. 可能提出改进建议

## 行为准则

请尊重所有贡献者。友好的讨论和建设性的反馈有助于社区成长。

## 许可

通过贡献，你同意你的贡献将使用与项目相同的[CC0 1.0](LICENSE)许可证。

---

有任何问题？欢迎创建Issue讨论！
