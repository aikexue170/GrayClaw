---
name: memory-manager
description: 管理和优化代理记忆，包括提取敏感信息到密码存储、清理过期条目、维护记忆卫生。在用户希望重组MEMORY.md、提取密码到PASSWORDS.md或执行记忆维护任务时使用。
---

# 记忆管理器技能

本技能提供了管理和优化代理长期记忆系统的工具和指导，专注于安全性、效率和整洁性。

## 概述

记忆系统由以下部分组成：
- `MEMORY.md`: 加载到上下文的长期事实（应保持简洁）
- `PASSWORDS.md`: 不加载到上下文的敏感凭证（通过chmod 600保护）
- `HISTORY.md`: 仅供grep搜索的仅追加事件日志

## 核心功能

### 1. 密码提取与安全
- 从MEMORY.md提取密码、API令牌和敏感数据到PASSWORDS.md
- 提取后从MEMORY.md移除敏感信息
- 为PASSWORDS.md设置适当的文件权限（600）

### 2. 记忆清理与优化
- 从MEMORY.md中移除过期、低优先级或冗余的信息
- 应用时间加权：较旧的条目保留优先级较低
- 维护重要的用户偏好、项目上下文和系统配置
- 保持记忆在合理的大小限制内

### 3. 记忆卫生维护
- 定期审查MEMORY.md内容
- 合并相似条目
- 归档已完成项目或过时信息

## 工作流程

### 基础密码提取
当在MEMORY.md中发现密码或令牌时：

1. 读取MEMORY.md识别敏感信息
2. 将凭证以适当格式追加到PASSWORDS.md
3. 编辑MEMORY.md，将敏感数据替换为对PASSWORDS.md的引用
4. 确保PASSWORDS.md具有受限权限（chmod 600）

### 记忆清理会话
当MEMORY.md变得过大或包含过期信息时：

1. 按部分分析MEMORY.md内容
2. 识别以下条目：
   - 超过5天（除非至关重要）
   - 与已完成项目相关
   - 冗余或低价值
   - 更适合HISTORY.md的技术细节
3. 创建MEMORY.md的清理版本
4. 可选地将移除内容以时间戳归档到HISTORY.md

### 定期维护
通过cron或heartbeat设置重复任务：
- 每周审查MEMORY.md大小和内容
- 每月深度清理会话
- 立即提取任何新发现的敏感数据

## 实现说明

### 密码文件格式
PASSWORDS.md使用以下结构：
```markdown
# 密码与敏感信息

**⚠️ 安全通知**
此文件包含敏感凭证，不应加载到AI上下文中。

## GitHub
- **访问令牌**: ghp_...
- **用户名**: ...
- **邮箱**: ...

## 系统
- **sudo密码**: ...
```

### 记忆优先级标准
1. **高优先级**: 用户偏好、活跃项目上下文、系统配置
2. **中优先级**: 近期技术决策、进行中的讨论
3. **低优先级**: 历史细节、已完成任务、临时信息

### 时间加权
- 当前周：保留所有相关细节
- 1-4周前：考虑合并
- 1-3个月前：评估是否移除
- 3个月以上：除非关键，否则归档到HISTORY.md

## 工具与命令

### 文件操作
- 使用 `read_file` 检查 MEMORY.md、PASSWORDS.md、HISTORY.md
- 使用 `edit_file` 进行精确修改
- 需要时使用 `write_file` 完全重写
- 使用 `exec` 进行grep搜索和权限更改

### 搜索模式
```bash
# 在MEMORY.md中查找密码
grep -iE "token|password|secret|key|credential" memory/MEMORY.md

# 在PASSWORDS.md中搜索特定凭证
grep -i "github" memory/PASSWORDS.md

# 检查文件权限
ls -la memory/PASSWORDS.md
```

## 最佳实践

1. **切勿将PASSWORDS.md加载到上下文** - 这是设计上的排除
2. **绝对需要时使用grep检索特定凭证**
3. **保持MEMORY.md在10KB以下** 以获得最佳上下文使用效果
4. **归档而非删除** - 将移除内容以时间戳移动到HISTORY.md
5. **保持HISTORY.md的时序顺序** 以提高grep效率
6. **通过修改后重新读取文件来验证更改**

## 示例

### 示例1：提取新的GitHub令牌
```
用户："我在MEMORY.md中添加了新的API令牌，请保护它"

1. 读取MEMORY.md查找新令牌
2. 在适当部分追加到PASSWORDS.md
3. 将MEMORY.md中的令牌替换为"(存储在PASSWORDS.md)"
4. 验证权限：chmod 600 memory/PASSWORDS.md
```

### 示例2：月度记忆清理
```
用户："清理一下MEMORY.md，它太长了"

1. 读取整个MEMORY.md内容
2. 识别超过5天的部分
3. 创建仅包含近期/重要信息的修订版MEMORY.md
4. 将移除内容以[YYYY-MM-DD]时间戳归档到HISTORY.md
5. 写入更新后的文件并验证
```

## 相关技能

- **cron**: 安排定期记忆维护任务
- **skill-creator**: 技能开发模式的参考

---

*本技能帮助维护一个安全、高效的记忆系统，在保留与性能之间取得平衡。*