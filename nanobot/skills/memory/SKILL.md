---
name: memory
description: 基于grep搜索的两层记忆系统。
always: true
---

# 记忆

## 结构

- `memory/MEMORY.md` — 长期事实（偏好设置、项目上下文、关系）。始终加载到你的上下文中。
- `memory/HISTORY.md` — 仅追加的事件日志。**不**加载到上下文中。使用grep搜索。每条记录以[YYYY-MM-DD HH:MM]开头。

## 搜索过往事件

```bash
grep -i "关键词" memory/HISTORY.md
```

使用 `exec` 工具运行grep。组合模式：`grep -iE "会议|截止日期" memory/HISTORY.md`

## 何时更新 MEMORY.md

立即使用 `edit_file` 或 `write_file` 写入重要事实：
- 用户偏好（“我偏好深色模式”）
- 项目上下文（“API使用OAuth2”）
- 关系（“Alice是项目负责人”）

## 自动整理

当会话变得庞大时，旧的对话会自动总结并追加到HISTORY.md。长期事实会被提取到MEMORY.md。你不需要管理这个过程。
