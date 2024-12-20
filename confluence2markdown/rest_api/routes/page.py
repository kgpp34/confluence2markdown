# -*- coding: UTF-8 -*-
"""
@Project : confluence2markdown
@File    : page.py
@Author  : yanglh
@Data    : 2024/12/20 16:22
"""
from fastapi import APIRouter, HTTPException

from services.confluence_service import ConfluenceService

router = APIRouter()


@router.get("/page/{page_id}")
async def get_page_markdown(page_id: str):
    try:
        service = ConfluenceService()
        return service.get_page_markdown(page_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
