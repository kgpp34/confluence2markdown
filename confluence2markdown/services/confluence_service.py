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

    def _get_all_child_pages(self, page_id: str):
        """
        Recursively get all child pages of a specified page ID.

        Args:
            page_id (str): The ID of the Confluence page.

        Returns:
            list: A list of all child pages (including nested children).
        """
        child_pages = self.confluence_api.get_page_children(page_id)
        all_child_pages = []
        for child_page in child_pages:
            all_child_pages.append(child_page)
            # Recursively get child pages of the current child page
            all_child_pages.extend(self._get_all_child_pages(child_page['id']))
        return all_child_pages

    def get_page_markdown(self, page_id: str):
        """
        Retrieve the Markdown content for a specified page ID and all its child pages.

        Args:
            page_id (str): The ID of the Confluence page.

        Returns:
            dict: A response containing the Markdown content of the page and all its child pages.
                 Only pages with non-empty content are included.
        """
        logger.info(f"Fetching Markdown for page ID: {page_id}")
        try:
            page_title, current_page = self.confluence_api.get_page_content(page_id)
            all_child_pages = self._get_all_child_pages(page_id)

            result = {}

            # 转换当前页面内容为 Markdown（如果内容非空）
            if current_page:  # 检查 current_page 是否非空
                markdown_content = self.markdown_converter.convert(current_page)
                if markdown_content:  # 检查转换后的 Markdown 是否非空
                    result[page_title] = markdown_content

            # 转换所有子页面内容为 Markdown（如果内容非空）
            for child_page in all_child_pages:
                child_page_title = child_page['title']
                child_page_html_content = child_page.get("body", {}).get("storage", {}).get("value", "")
                if child_page_html_content:  # 检查子页面内容是否非空
                    child_markdown_content = self.markdown_converter.convert(child_page_html_content)
                    if child_markdown_content:  # 检查转换后的 Markdown 是否非空
                        result[child_page_title] = child_markdown_content

            logger.info(f"Successfully fetched Markdown for page ID: {page_id} and all its child pages")
            return result
        except Exception as e:
            logger.error(f"Failed to fetch Markdown for page ID {page_id}: {e}")
            raise
