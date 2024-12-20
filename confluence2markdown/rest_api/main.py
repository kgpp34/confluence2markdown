
# -*- coding: UTF-8 -*-
"""
@Project : confluence2markdown
@File    : main.py
@Author  : yanglh
@Data    : 2024/12/20 16:20
"""

from fastapi import FastAPI
from loguru import logger

from routes.page import router as page_router
from config.config import SERVER_PORT
from utils.logger_utils import setup_logger

setup_logger(log_file_prefix="confluence2md.log")

app = FastAPI()

# register router
app.include_router(router=page_router, prefix="/api", tags=["Page"])


if __name__ == '__main__':
    import uvicorn

    logger.info("Initialized uvicorn server")
    uvicorn.run(app, port=SERVER_PORT)
