# -*- coding: UTF-8 -*-
"""
@Project : confluence2markdown
@File    : converter.py
@Author  : yanglh
@Data    : 2024/12/20 16:12
"""
import re

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from loguru import logger
import markdown


def fix_markdown(markdown_content: str) -> str:
    # 保护代码块中的内容
    def protect_code_blocks(content: str):
        # 使用正则表达式匹配代码块
        code_block_pattern = re.compile(r'```.*?```', re.DOTALL)
        code_blocks = code_block_pattern.findall(content)

        # 将代码块替换为占位符
        for i, code_block in enumerate(code_blocks):
            content = content.replace(code_block, f"__CODE_BLOCK_{i}__")

        return content, code_blocks

    # 恢复代码块中的内容
    def restore_code_blocks(content: str, code_blocks: list) -> str:
        for i, code_block in enumerate(code_blocks):
            content = content.replace(f"__CODE_BLOCK_{i}__", code_block)
        return content

    # 保护代码块
    markdown_content, code_blocks = protect_code_blocks(markdown_content)

    # 修复标题
    markdown_content = re.sub(r'^(={3,})$', r'# \1', markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'^(-{3,})$', r'## \1', markdown_content, flags=re.MULTILINE)

    # 修复列表
    markdown_content = re.sub(r'^\s*([*-])\s', r'* ', markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'^\s*(\d+)\.\s', r'\1. ', markdown_content, flags=re.MULTILINE)

    # 修复引用
    markdown_content = re.sub(r'^>\s', r'> ', markdown_content, flags=re.MULTILINE)

    # 修复代码块
    markdown_content = re.sub(r'^```\n', r'```', markdown_content, flags=re.MULTILINE)

    # 恢复代码块
    markdown_content = restore_code_blocks(markdown_content, code_blocks)

    # 替换代码块中的 Markdown 标题为注释
    def replace_headers_in_code_blocks(content: str) -> str:
        # 使用正则表达式匹配代码块
        code_block_pattern = re.compile(r'```.*?```', re.DOTALL)
        return code_block_pattern.sub(lambda match: match.group(0).replace('#', '//'), content)

    markdown_content = replace_headers_in_code_blocks(markdown_content)

    return markdown_content


def is_valid_markdown(markdown_content: str) -> bool:
    try:
        # 尝试将 Markdown 转换为 HTML
        html = markdown.markdown(markdown_content)
        return True
    except Exception as e:
        logger.error(f"Markdown 格式验证失败: {e}")
        return False


class MarkdownConverter:

    @staticmethod
    def convert(html_content: str) -> str:
        """
        Convert HTML content to Markdown format.

        Args:
            html_content (str): The input HTML content.

        Returns:
            str: The converted Markdown content.
        """
        if not html_content:
            raise ValueError("HTML content cannot be empty.")

        # 使用 BeautifulSoup 预处理 HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # 修复嵌套列表
        for ul in soup.find_all("ul"):
            ul.smooth()  # 修复嵌套列表的缩进

        # 修复表格
        for table in soup.find_all("table"):
            table.attrs["border"] = "1"  # 添加表格边框

        # 修复代码块
        for pre in soup.find_all("pre"):
            pre.attrs["class"] = "language-plaintext"  # 添加代码块语言

        markdown_content = md(html_content, heading_style="ATX")

        # 修复 Markdown 格式
        markdown_content = fix_markdown(markdown_content)
        logger.debug(f"Fixed Markdown content:\n{markdown_content}")

        # 验证 Markdown 格式
        if not is_valid_markdown(markdown_content):
            raise ValueError("Markdown 格式不正确")
        return markdown_content

    def convert_to_file(self, html_content: str, output_file: str):
        """
        Convert HTML content to Markdown format and save it to a file.

        Args:
            html_content (str): The input HTML content.
            output_file (str): The file path for the output Markdown file.
        """
        markdown_content = self.convert(html_content)
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(markdown_content)
