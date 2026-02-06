from loguru import logger


def get_logger(name: str):
    logger.add("logs.log", rotation="1 MB", level="INFO")
    return logger.bind(name=name)
