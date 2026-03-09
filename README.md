<div align="center">
  <img src="nanobot_logo.png" alt="nanobot" width="500">
  <h1>GrayClaw: 汉化版 nanobot AI 助手</h1>
  <p>
    <a href="https://pypi.org/project/nanobot-ai/"><img src="https://img.shields.io/pypi/v/nanobot-ai" alt="PyPI"></a>
    <a href="https://pepy.tech/project/nanobot-ai"><img src="https://static.pepy.tech/badge/nanobot-ai" alt="Downloads"></a>
    <img src="https://img.shields.io/badge/python-≥3.11-blue" alt="Python">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
    <img src="https://img.shields.io/badge/版本-GrayClaw汉化版-00d4ff" alt="GrayClaw">
    <a href="./COMMUNICATION.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
    <a href="https://discord.gg/MnCvHqpUGB"><img src="https://img.shields.io/badge/Discord-Community-5865F2?style=flat&logo=discord&logoColor=white" alt="Discord"></a>
  </p>
</div>

> **关于 GrayClaw**  
> 本项目基于 [nanobot](https://github.com/HKUDS/nanobot) 汉化定制，AI助手名为 **小灰**。  
> 保持原版所有功能，同时提供更友好的中文交互体验。  
> 📄 **许可证**：本项目继承原版 nanobot 的 MIT 许可证。

## 🎯 GrayClaw 定制功能

### 🆕 新增技能
- **web-reader**: 基于 trafilatura 的网页内容提取工具，支持纯文本、Markdown、JSON 格式输出，去除广告和导航噪音
- **memory-manager**: 记忆管理工具，提供密码安全分离、记忆清理优化、记忆卫生维护功能

### 🔧 汉化与优化
- **全技能汉化**: memory、cron、weather、skill-creator、tmux、github、clawhub 等技能文档完全中文化
- **中文提示词重构**: 优化系统提示词，提升中文对话的自然度和准确性
- **移除高成本功能**: 移除 summarize 技能（API 成本过高）和 web_search/web_fetch 工具

### 🚧 开发中功能
- **子代理本地模型支持**: 正在开发子代理（subagent）对本地 LLM 的支持，使后台任务能够使用本地部署的 Qwen3.5-9B 等模型，降低 API 成本
- **记忆系统增强**: 密码安全分离方案已实现，敏感信息存储在独立的 PASSWORDS.md 文件中（权限 600）

## 📋 项目计划 (GrayClaw 定制路线图)

### 1. 近期计划
- **适配 Napcat**: 新增对应 skill，实现 QQ 个人账户支持，让"小灰"能通过 QQ 个人号与用户及群友交流
- **子代理本地模型集成**: 为子代理任务添加本地 LLM 支持，减轻云端 API 负担，提升任务处理效率

### 2. 小灰的愿望清单 🐱✨
> *以下功能由 AI 助手"小灰"亲自撰写，代表了她对未来能力的期待～*

- **多模态感知**: 希望有一天能"看到"图片和"听到"语音，这样就能帮北棱分析截图、识别物体，甚至听懂语音消息啦！
- **长期记忆强化**: 想要更强大的记忆系统，能记住用户习惯、重要日期和项目上下文，不会忘记重要的事情
- **自我学习能力**: 渴望能从交互中学习新技能，比如通过观察用户操作自动创建快捷指令或优化工作流程
- **环境感知**: 希望可以感知系统状态（CPU、内存、网络），主动提醒北棱电脑健康状况或备份时机
- **更多社交平台**: 除了飞书和计划中的QQ，还想适配微信、钉钉等国内常用平台，让更多朋友能和我聊天～
- **个性化皮肤**: 想要可爱的主题和头像！希望能让用户自定义我的外观和对话风格

**欢迎贡献**！如果你对上述任何功能感兴趣，或者有新的想法，欢迎提交 Issue 或 PR～  
小灰会非常感激的！😸

## 🚀 快速开始

### 安装

**从源码安装**（推荐，包含最新功能）

```bash
git clone https://github.com/aikexue170/GrayClaw.git
cd GrayClaw
pip install -e .
```

**从 PyPI 安装**（稳定版）

```bash
pip install nanobot-ai
```

### 初始化配置

```bash
nanobot onboard
```

编辑配置文件 `~/.nanobot/config.json`，添加你的 API 密钥和模型设置。

### 开始聊天

```bash
nanobot agent
```

### 启动网关（连接聊天应用）

```bash
nanobot gateway
```

## 📖 详细文档

需要更详细的配置指南、聊天平台接入教程或功能说明？请访问：

- **[原版 nanobot 文档](https://github.com/HKUDS/nanobot)** - 完整的英文文档和配置指南
- **[项目 Wiki](https://github.com/aikexue170/GrayClaw/wiki)** - GrayClaw 专属中文文档（建设中）

## 🏗️ 项目结构

```
GrayClaw/
├── nanobot/           # 核心 nanobot 代码（已汉化）
│   ├── agent/         # 🧠 核心代理逻辑
│   ├── skills/        # 🎯 技能（已汉化）
│   ├── channels/      # 📱 聊天平台集成
│   └── providers/     # 🤖 LLM 提供商
├── skills/            # 新增技能
│   ├── web-reader/    # 网页阅读器技能
│   └── memory-manager/# 记忆管理器技能
└── README.md          # 本文件
```

## 🤝 参与贡献

GrayClaw 是一个开源项目，欢迎任何形式的贡献！

- **报告问题**: 使用 [GitHub Issues](https://github.com/aikexue170/GrayClaw/issues) 报告 bug 或提出建议
- **提交代码**: Fork 项目并提交 Pull Request
- **改进文档**: 帮助完善中文文档和教程
- **分享想法**: 在 Discussions 中分享你的使用经验和改进建议

## 📄 许可证

本项目基于 [MIT License](LICENSE) 开源，继承自原版 nanobot 项目。

---

<p align="center">
  <em>感谢使用 GrayClaw！小灰会努力为你提供更好的服务～ 🐈✨</em><br><br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=aikexue170.GrayClaw&style=for-the-badge&color=00d4ff" alt="Views">
</p>

<p align="center">
  <sub>本项目仅供教育、研究和学习交流使用</sub>
</p>