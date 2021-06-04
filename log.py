# 과거 실행 이력을 확인하기 위한 파일
import logging
import sys
from logging.handlers import RotatingFileHandler

def create_logger(logger_name, file_name, mode="dev"):
    #https://docs.python.org/3/library/logging.html
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(linenod)d] - %(message)s"
    )
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    if mode == 'dev':
        handler = logging.StreamHandler(sys.stdout)
    else:
        handler = RotatingFileHandler(file_name, maxBytes = 20000000, backupCount=5)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger