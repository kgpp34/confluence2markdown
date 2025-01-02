# -*- coding: UTF-8 -*-
"""
@Project : confluence2markdown
@File    : confluence.py
@Author  : yanglh
@Data    : 2024/12/20 16:51
"""

from atlassian import Confluence
from loguru import logger

from confluence2markdown.config.config import CONFLUENCE_BASE_URL, CONFLUENCE_USERNAME, CONFLUENCE_PASSWORD


class ConfluenceAPI:
    def __init__(self):
        self.confluence = Confluence(
            url=CONFLUENCE_BASE_URL,
            username=CONFLUENCE_USERNAME,
            password=CONFLUENCE_PASSWORD,
        )
        logger.info("ConfluenceAPI initialized.")

    def get_pages_in_space(self, space_key: str):
        """
        Retrieve all pages within a specified Confluence space.

        Args:
            space_key (str): The key of the Confluence space.

        Returns:
            list: A list containing all pages, each page includes 'id' and 'title'.
        """
        logger.info(f"Fetching pages in space: {space_key}")
        try:
            pages = self.confluence.get_all_pages_from_space(space_key, expand="body.storage")
            logger.info(f"Successfully fetched {len(pages)} pages from space: {space_key}")
            return pages
        except Exception as e:
            logger.error(f"Failed to fetch pages in space {space_key}: {e}")
            raise

    def get_page_content(self, page_id: str):
        """
        Retrieve the content of a specified page.

        Args:
            page_id (str): The ID of the Confluence page.

        Returns:
            str: the page title
            str: The HTML content of the page.
        """
        logger.info(f"Fetching content for page ID: {page_id}")
        try:
            page = self.confluence.get_page_by_id(page_id, expand="body.storage")
            logger.info(f"Successfully fetched content for page ID: {page_id}")
            return page["title"], page["body"]["storage"]["value"]
        except Exception as e:
            logger.error(f"Failed to fetch content for page ID {page_id}: {e}")
            raise

    def get_page_children(self, page_id: str):
        """
        Retrieve the children content of a specified page.

        Args:
            page_id (str): The ID of the Confluence page.

        Returns:
            list: the child pages of page_id
        """
        logger.info(f"Fetching content for page ID children: {page_id}")
        try:
            child_pages = self.confluence.get_page_child_by_type(page_id, type="page", start=None, limit=None, expand="body.storage")
            logger.info(f"Successfully fetched content for page ID children: {page_id}")
            return child_pages
        except Exception as e:
            logger.error(f"Failed to fetch content for page ID children {page_id}: {e}")
            raise

