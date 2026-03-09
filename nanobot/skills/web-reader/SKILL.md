---
name: web-reader
description: 提取网页正文内容，去除广告和导航噪音。支持纯文本、Markdown和JSON格式输出。适用于博客文章、文档、百科等静态页面。
metadata: {"nanobot":{"emoji":"🌐","requires":{"python_packages":["trafilatura","requests"]}}}
---

# 网页阅读器 (Web Reader)

基于 `trafilatura` 库的网页内容提取工具，能够智能识别并提取网页正文，去除广告、导航栏、侧边栏等无关内容。该工具已集成到 nanobot 框架中，可直接通过 `fetch_web` 工具调用。


## 使用方法

### 通过 fetch_web 工具调用（推荐）

工具已集成到 nanobot 中，可直接调用：

**基本用法**：
```python
fetch_web(url="https://example.com")
```

**完整参数**：
```python
fetch_web(
    url="https://example.com",
    format="markdown",           # 可选: "txt", "markdown", "json" (默认: "txt")
    include_metadata=False,      # 是否包含元数据 (标题、作者、日期等)
    timeout=30                   # 超时时间（秒，默认: 30）
)
```

**示例**：
```python
# 提取为纯文本格式
fetch_web(url="https://baike.baidu.com/item/Python")

# 提取为Markdown格式
fetch_web(url="https://example.com/blog/post", format="markdown")

# 提取为JSON格式（包含元数据）
fetch_web(url="https://example.com/article", format="json", include_metadata=True)

# 对慢速网站增加超时时间
fetch_web(url="https://slow-site.com", timeout=60)
```