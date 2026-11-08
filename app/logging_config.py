import logging


def configure_logging(level: str) -> logging.Logger:
    logger = logging.getLogger("serviceops")
    logger.setLevel(level)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
