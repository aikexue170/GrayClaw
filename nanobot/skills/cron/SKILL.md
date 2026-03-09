---
name: cron
description: 安排提醒和重复任务。
---

# Cron

使用 `cron` 工具安排提醒或重复任务。

## 三种模式

1. **提醒** - 消息直接发送给用户
2. **任务** - 消息是任务描述，代理执行并发送结果
3. **一次性** - 在特定时间运行一次，然后自动删除

## 示例

固定提醒：
```
cron(action="add", message="该休息了！", every_seconds=1200)
```

动态任务（代理每次执行）：
```
cron(action="add", message="检查 HKUDS/nanobot GitHub stars 并报告", every_seconds=600)
```

一次性计划任务（从当前时间计算ISO时间）：
```
cron(action="add", message="提醒我开会", at="<ISO时间>")
```

时区感知的cron：
```
cron(action="add", message="早会", cron_expr="0 9 * * 1-5", tz="America/Vancouver")
```

列出/删除：
```
cron(action="list")
cron(action="remove", job_id="abc123")
```

## 时间表达式

| 用户说 | 参数 |
|-----------|------------|
| 每20分钟 | every_seconds: 1200 |
| 每小时 | every_seconds: 3600 |
| 每天早上8点 | cron_expr: "0 8 * * *" |
| 工作日17点 | cron_expr: "0 17 * * 1-5" |
| 温哥华时间每天9点 | cron_expr: "0 9 * * *", tz: "America/Vancouver" |
| 特定时间 | at: ISO时间字符串（从当前时间计算） |

## 时区

使用 `tz` 与 `cron_expr` 在特定的IANA时区中安排任务。如果没有 `tz`，则使用服务器的本地时区。
