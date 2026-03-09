"""Web reader tool for extracting clean content from web pages."""

import json
from typing import Any, Optional

import requests
import trafilatura
from requests.exceptions import RequestException

from nanobot.agent.tools.base import Tool


class WebReaderTool(Tool):
    """Tool to fetch and extract clean content from web pages."""

    def __init__(self, timeout: int = 30):
        self.timeout = timeout

    @property
    def name(self) -> str:
        return "fetch_web"

    @property
    def description(self) -> str:
        return (
            "Fetch and extract clean content from a web page. "
            "Removes ads, navigation, and other noise. "
            "Supports plain text, Markdown, and JSON output formats."
        )

    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "URL of the web page to fetch",
                },
                "format": {
                    "type": "string",
                    "enum": ["txt", "markdown", "json"],
                    "default": "txt",
                    "description": "Output format: txt (plain text), markdown, or json",
                },
                "include_metadata": {
                    "type": "boolean",
                    "default": False,
                    "description": "Whether to include metadata (title, author, date) in output",
                },
                "timeout": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 120,
                    "default": 30,
                    "description": "Timeout in seconds for the HTTP request",
                },
            },
            "required": ["url"],
        }

    async def execute(
        self,
        url: str,
        format: str = "txt",
        include_metadata: bool = False,
        timeout: int = 30,
        **kwargs: Any,
    ) -> str:
        """Execute the web reader tool."""
        # Validate URL
        if not url.startswith(("http://", "https://")):
            return f"Error: URL must start with http:// or https://, got: {url}"

        try:
            # Fetch HTML
            html = await self._fetch_html(url, timeout)
            if html is None:
                return f"Error: Failed to fetch HTML from {url}"

            # Extract content
            content = self._extract_content(html, format, include_metadata)
            if content is None or content.strip() == "":
                return (
                    f"Error: Failed to extract content from {url}. "
                    "The page might require JavaScript rendering or have an unusual structure."
                )

            # Build result with statistics
            stats = self._build_statistics(html, content)
            result = f"Successfully extracted content from {url}\n\n"
            result += f"Output format: {format}\n"
            result += f"Include metadata: {include_metadata}\n"
            result += f"Content size: {len(content)} characters\n"
            result += f"Noise removal rate: {stats['retention_rate']:.1%}\n\n"
            result += "=" * 60 + "\n"
            result += "CONTENT PREVIEW (first 500 characters):\n"
            result += "=" * 60 + "\n"
            preview = content[:500] + ("..." if len(content) > 500 else "")
            result += preview + "\n\n"
            
            # If content is too long, truncate for context
            max_chars = 15000
            if len(content) > max_chars:
                result += f"Note: Content truncated to {max_chars} characters (full content has {len(content)} characters)\n"
                result += "=" * 60 + "\n"
                result += content[:max_chars] + "\n... (truncated)"
            else:
                result += "=" * 60 + "\n"
                result += "FULL CONTENT:\n"
                result += "=" * 60 + "\n"
                result += content

            return result

        except Exception as e:
            return f"Error processing {url}: {str(e)}"

    async def _fetch_html(self, url: str, timeout: int) -> Optional[str]:
        """Fetch HTML content from URL."""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
        }
        
        try:
            # Use requests in a thread pool to make it async-friendly
            import asyncio
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, 
                lambda: requests.get(url, headers=headers, timeout=timeout)
            )
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text
        except RequestException as e:
            return None
        except Exception as e:
            return None

    def _extract_content(self, html: str, output_format: str, include_metadata: bool) -> Optional[str]:
        """Extract clean content from HTML using trafilatura."""
        try:
            if include_metadata or output_format == "json":
                # Extract with metadata
                result = trafilatura.extract(
                    html,
                    include_comments=False,
                    include_tables=True,
                    no_fallback=False,
                    include_links=True,
                    output_format="json",
                    with_metadata=True
                )
                if not result:
                    return None
                
                if output_format == "json":
                    return result
                
                # For txt/markdown, extract text from JSON
                data = json.loads(result)
                if output_format == "txt":
                    return data.get('raw_text', '') or data.get('text', '')
                else:  # markdown
                    return data.get('text', '')
            else:
                # Extract without metadata
                text = trafilatura.extract(
                    html,
                    include_comments=False,
                    include_tables=True,
                    no_fallback=False,
                    include_links=(output_format == "markdown"),
                    output_format=output_format
                )
                return text
        except Exception:
            return None

    def _build_statistics(self, html: str, content: str) -> dict:
        """Build extraction statistics."""
        html_len = len(html)
        content_len = len(content)
        retention_rate = content_len / max(html_len, 1)
        
        lines = content.split('\n')
        words = content.split()
        
        return {
            "html_size": html_len,
            "content_size": content_len,
            "retention_rate": retention_rate,
            "line_count": len(lines),
            "word_count": len(words),
        }