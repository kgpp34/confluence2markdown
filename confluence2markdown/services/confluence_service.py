# -*- coding: UTF-8 -*-
"""
@Project : confluence2markdown
@File    : confluence_service.py
@Author  : yanglh
@Data    : 2024/12/20 16:39
"""
from loguru import logger

from confluence2markdown.confluence_api.confluence import ConfluenceAPI
from confluence2markdown.md_converter.converter import MarkdownConverter




class ConfluenceService:
    def __init__(self):
        self.confluence_api = ConfluenceAPI()
        self.markdown_converter = MarkdownConverter()

    def get_page_markdown(self, page_id: str):
        """
        Retrieve the Markdown content for a specified page ID.

        Args:
            page_id (str): The ID of the Confluence page.

        Returns:
            str: A response containing the Markdown content of the page.
        """
        logger.info(f"Fetching Markdown for page ID: {page_id}")
        try:
            html_content = self.confluence_api.get_page_content(page_id)
            markdown_content = self.markdown_converter.convert(html_content)
            logger.info(f"Successfully fetched Markdown for page ID: {page_id}")
            return markdown_content
        except Exception as e:
            logger.error(f"Failed to fetch Markdown for page ID {page_id}: {e}")
            raise
