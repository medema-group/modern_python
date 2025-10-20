"""TODO: ADD ONE-LINE DESCRIPTION OF PURPOSE (WHY) OF FILE/CODE

TODO: ADD COPYRIGHT INFORMATION (YEAR-YEAR, NAME)

TODO: ADD COPYRIGHT TEXT
"""

import logging
import sys

import coloredlogs


def config_logger() -> logging.Logger:
    """Set up a module-specific logger with nice formatting

    :return
        A Logger object
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(
        coloredlogs.ColoredFormatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    )
    logger.addHandler(console_handler)
    return logger


def main() -> None:
    """Function to execute main body of code"""
    logger = config_logger()
    logger.debug("Hello, world")


if __name__ == "__main__":
    main()
