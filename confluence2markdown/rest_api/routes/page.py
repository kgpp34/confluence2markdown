# -*- coding: UTF-8 -*-
"""
@Project : confluence2markdown
@File    : page.py
@Author  : yanglh
@Data    : 2024/12/20 16:22
"""
from fastapi import APIRouter, HTTPException
from starlette.responses import FileResponse, Response

from confluence2markdown.services.confluence_service import ConfluenceService

router = APIRouter()


@router.get("/page/{page_id}")
async def get_page_markdown(page_id: str):
    try:
        service = ConfluenceService()
        markdown_content = service.get_page_markdown(page_id)

        # 返回 text/plain 格式的 Markdown 文本
        return Response(content=markdown_content, media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/page/file/{page_id}")
async def get_page_markdown_file(page_id: str):
    try:
        service = ConfluenceService()
        markdown_content = service.get_page_markdown(page_id)

        # 将 Markdown 内容写入临时文件
        with open("temp.txt", "w", encoding="utf-8") as f:
            f.write(markdown_content)

        return FileResponse("temp.txt", media_type="text/plain", filename="temp.txt")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
