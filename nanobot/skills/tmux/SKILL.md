---
name: tmux
description: 通过发送按键和抓取窗格输出来远程控制tmux会话，用于交互式CLI。
metadata: {"nanobot":{"emoji":"🧵","os":["darwin","linux"],"requires":{"bins":["tmux"]}}}
---

# tmux 技能

仅在需要交互式TTY时使用tmux。对于长时间运行的非交互式任务，优先使用exec后台模式。

## 快速开始（独立socket，exec工具）

```bash
SOCKET_DIR="${NANOBOT_TMUX_SOCKET_DIR:-${TMPDIR:-/tmp}/nanobot-tmux-sockets}"
mkdir -p "$SOCKET_DIR"
SOCKET="$SOCKET_DIR/nanobot.sock"
SESSION=nanobot-python

tmux -S "$SOCKET" new -d -s "$SESSION" -n shell
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- 'PYTHON_BASIC_REPL=1 python3 -q' Enter
tmux -S "$SOCKET" capture-pane -p -J -t "$SESSION":0.0 -S -200
```

启动会话后，始终打印监控命令：

```
监控方法：
  tmux -S "$SOCKET" attach -t "$SESSION"
  tmux -S "$SOCKET" capture-pane -p -J -t "$SESSION":0.0 -S -200
```

## Socket约定

- 使用 `NANOBOT_TMUX_SOCKET_DIR` 环境变量。
- 默认socket路径：`"$NANOBOT_TMUX_SOCKET_DIR/nanobot.sock"`。

## 定位窗格和命名

- 目标格式：`session:window.pane`（默认为 `:0.0`）。
- 保持名称简短；避免空格。
- 检查：`tmux -S "$SOCKET" list-sessions`，`tmux -S "$SOCKET" list-panes -a`。

## 查找会话

- 在你的socket上列出会话：`{baseDir}/scripts/find-sessions.sh -S "$SOCKET"`。
- 扫描所有socket：`{baseDir}/scripts/find-sessions.sh --all`（使用 `NANOBOT_TMUX_SOCKET_DIR`）。

## 安全发送输入

- 优先使用字面发送：`tmux -S "$SOCKET" send-keys -t target -l -- "$cmd"`。
- 控制键：`tmux -S "$SOCKET" send-keys -t target C-c`。

## 监视输出

- 捕获最近历史：`tmux -S "$SOCKET" capture-pane -p -J -t target -S -200`。
- 等待提示符：`{baseDir}/scripts/wait-for-text.sh -t session:0.0 -p 'pattern'`。
- 附加会话是可以的；使用 `Ctrl+b d` 分离。

## 生成进程

- 对于python REPL，设置 `PYTHON_BASIC_REPL=1`（非基本REL会中断send-keys流程）。

## Windows / WSL

- tmux在macOS/Linux上受支持。在Windows上，使用WSL并在WSL内部安装tmux。
- 此技能仅限于 `darwin`/`linux` 并需要PATH中有 `tmux`。

## 编排编码代理（Codex、Claude Code）

tmux擅长并行运行多个编码代理：

```bash
SOCKET="${TMPDIR:-/tmp}/codex-army.sock"

# 创建多个会话
for i in 1 2 3 4 5; do
  tmux -S "$SOCKET" new-session -d -s "agent-$i"
done

# 在不同的工作目录中启动代理
tmux -S "$SOCKET" send-keys -t agent-1 "cd /tmp/project1 && codex --yolo '修复bug X'" Enter
tmux -S "$SOCKET" send-keys -t agent-2 "cd /tmp/project2 && codex --yolo '修复bug Y'" Enter

# 轮询完成情况（检查提示符是否返回）
for sess in agent-1 agent-2; do
  if tmux -S "$SOCKET" capture-pane -p -t "$sess" -S -3 | grep -q "❯"; then
    echo "$sess: 完成"
  else
    echo "$sess: 运行中..."
  fi
done

# 从完成的会话获取完整输出
tmux -S "$SOCKET" capture-pane -p -t agent-1 -S -500
```

**提示：**
- 为并行修复使用单独的git工作树（无分支冲突）
- 在新克隆中运行codex前先执行 `pnpm install`
- 检查shell提示符（`❯` 或 `$`）以检测完成
- Codex需要 `--yolo` 或 `--full-auto` 用于非交互式修复

## 清理

- 终止会话：`tmux -S "$SOCKET" kill-session -t "$SESSION"`。
- 终止socket上的所有会话：`tmux -S "$SOCKET" list-sessions -F '#{session_name}' | xargs -r -n1 tmux -S "$SOCKET" kill-session -t`。
- 移除私有socket上的所有内容：`tmux -S "$SOCKET" kill-server`。

## 辅助脚本：wait-for-text.sh

`{baseDir}/scripts/wait-for-text.sh` 轮询窗格以匹配正则表达式（或固定字符串），具有超时功能。

```bash
{baseDir}/scripts/wait-for-text.sh -t session:0.0 -p 'pattern' [-F] [-T 20] [-i 0.5] [-l 2000]
```

- `-t`/`--target` 窗格目标（必需）
- `-p`/`--pattern` 要匹配的正则表达式（必需）；添加 `-F` 表示固定字符串
- `-T` 超时秒数（整数，默认15）
- `-i` 轮询间隔秒数（默认0.5）
- `-l` 要搜索的历史行数（整数，默认1000）
