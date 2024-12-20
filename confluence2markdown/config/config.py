# -*- coding: UTF-8 -*-
"""
@Project : confluence2markdown
@File    : config.py
@Author  : yanglh
@Data    : 2024/12/20 16:40
"""
import os

from dotenv import load_dotenv

# load .env file
load_dotenv()


# read env variables
CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASE_URL")
CONFLUENCE_USERNAME = os.getenv("CONFLUENCE_USERNAME")
CONFLUENCE_PASSWORD = os.getenv("CONFLUENCE_PASSWORD")

# check env variables available
if not CONFLUENCE_BASE_URL:
    raise ValueError("CONFLUENCE_BASE_URL environment variable is not set.")

if not CONFLUENCE_USERNAME:
    raise ValueError("CONFLUENCE_USERNAME environment variable is not set.")

if not CONFLUENCE_PASSWORD:
    raise ValueError("CONFLUENCE_PASSWORD environment variable is not set.")


SERVER_PORT = os.getenv("SERVER_PORT")
if not SERVER_PORT:
    SERVER_PORT = 8080
else:
    SERVER_PORT = int(SERVER_PORT)