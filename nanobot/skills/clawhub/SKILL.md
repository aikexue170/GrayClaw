---
name: clawhub
description: 从公共技能注册表ClawHub搜索和安装代理技能。
homepage: https://clawhub.ai
metadata: {"nanobot":{"emoji":"🦞"}}
---

# ClawHub

AI代理的公共技能注册表。通过自然语言搜索（向量搜索）。

## 何时使用

当用户询问以下任何内容时使用此技能：
- "查找一个用于...的技能"
- "搜索技能"
- "安装一个技能"
- "有哪些可用的技能？"
- "更新我的技能"

## 搜索

```bash
npx --yes clawhub@latest search "web scraping" --limit 5
```

## 安装

```bash
npx --yes clawhub@latest install <slug> --workdir ~/.nanobot/workspace
```

将 `<slug>` 替换为搜索结果中的技能名称。这会将技能放置到 `~/.nanobot/workspace/skills/` 中，nanobot从此处加载工作空间技能。始终包含 `--workdir`。

## 更新

```bash
npx --yes clawhub@latest update --all --workdir ~/.nanobot/workspace
```

## 列出已安装

```bash
npx --yes clawhub@latest list --workdir ~/.nanobot/workspace
```

## 注意

- 需要Node.js（`npx` 随附）。
- 搜索和安装无需API密钥。
- 登录（`npx --yes clawhub@latest login`）仅用于发布。
- `--workdir ~/.nanobot/workspace` 至关重要——没有它，技能将安装到当前目录而不是nanobot工作空间。
- 安装后，提醒用户开始新会话以加载技能。
