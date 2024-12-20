# -*- coding: UTF-8 -*-
"""
@Project : confluence2markdown
@File    : converter.py
@Author  : yanglh
@Data    : 2024/12/20 16:12
"""
from markdownify import markdownify as md


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

        markdown_content = md(html_content, heading_style="ATX")
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