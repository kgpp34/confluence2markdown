# -*- coding: UTF-8 -*-
"""
@Project : confluence2markdown
@File    : page.py
@Author  : yanglh
@Data    : 2024/12/20 16:22
"""
from fastapi import APIRouter, HTTPException
from loguru import logger
from starlette.responses import FileResponse, Response

from confluence2markdown.services.confluence_service import ConfluenceService

router = APIRouter()


@router.get("/page/{page_id}")
async def get_page_markdown(page_id: str):
    try:
        service = ConfluenceService()
        markdown_content_dict = service.get_page_markdown(page_id)

        # 将字典中的 Markdown 内容组合成一个字符串，使用 HTML 注释分隔
        combined_markdown = ""
        for title, content in markdown_content_dict.items():
            combined_markdown += f"<!-- Page: {title} -->\n\n{content}\n\n"

        # 返回 text/plain 格式的 Markdown 文本
        return Response(content=combined_markdown, media_type="text/plain")
    except Exception as e:
        logger.error(f"Failed to fetch Markdown for page ID {page_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

