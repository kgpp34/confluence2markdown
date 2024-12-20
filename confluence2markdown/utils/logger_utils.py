# -*- coding: UTF-8 -*-
"""
@Project : confluence2markdown
@File    : logger_utils.py
@Author  : yanglh
@Data    : 2024/12/20 17:14
"""
import os

from datetime import datetime
from loguru import logger


def setup_logger(log_dir_name: str = "logs", log_file_prefix: str = "app", level: str = "INFO"):
    """
    Set up a logger with the specified log directory, log file prefix, and logging level.

    Args:
        log_dir_name (str): The name of the log directory (default is "logs").
        log_file_prefix (str): The prefix of the log file (default is "app").
        level (str): The logging level (default is "INFO").
    """
    # 获取项目根目录
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 创建日志目录
    log_dir_path = os.path.join(project_root, log_dir_name)
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)

    # 生成日志文件名（格式：prefix-YYYY-MM-DD.log）
    log_file_name = f"{log_file_prefix}-{datetime.now().strftime('%Y-%m-%d')}.log"
    log_file_path = os.path.join(log_dir_path, log_file_name)

    # 配置日志输出到文件
    logger.add(log_file_path, level=level, rotation="500 MB", retention="7 days", compression="zip")

    # 配置日志输出到控制台
    logger.add(lambda msg: print(msg), level=level)

    # 记录初始化日志
    logger.info(f"Logger initialized. Log file: {log_file_path}")
