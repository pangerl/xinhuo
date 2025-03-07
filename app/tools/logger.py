# -*- coding: utf-8 -*-
# @Author  : lanpang
# @Time    : 2025/3/7 上午10:57

import logging.config
import sys
from pathlib import Path
import os

# 日志文件路径
env_mode = os.environ.get('ENV_MODE', 'dev')
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)  # 创建 logs 目录

log_name = 'app_dev.log' if env_mode == 'dev' else 'app_prod.log'
LOG_FILE = LOG_DIR / log_name

# 定义日志格式
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "detailed": {
            "format": "[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
        },
        "file": {
            "level": "DEBUG",
            "formatter": "detailed",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_FILE,
            "maxBytes": 10 * 1024 * 1024,  # 10MB
            "backupCount": 5,
            "encoding": "utf-8",
        },
    },
    "root": {
        "level": "DEBUG" if env_mode == 'dev' else "INFO",
        "handlers": ["console", "file"],
    }
}

# 应用日志配置
logging.config.dictConfig(LOGGING_CONFIG)

# 获取 logger 实例
logger = logging.getLogger("fastapi-app")
