import logging  # Importing the standard Python logging module
from dataclasses import dataclass

# Importing the dataclass decorator from Python's built-in dataclasses module
from pathlib import Path


# Define a dataclass for the application's configuration.
# Dataclasses are a way to make classes that mainly store values,
# without needing to write explicit methods for tasks like printing or comparing objects.
@dataclass
class Config:
    # Define the root folder path as the grandparent of the folder containing this file
    foldername_root: Path = Path(__file__).parent.parent.parent.resolve()
    # Define the log folder path as a subfolder named 'logs' in the root folder
    foldername_log: Path = foldername_root / "logs"
    # Define the debug log file path as a file named 'debug.log' in the log folder
    filename_debug_log: Path = foldername_log / "debug.log"

    # Define the log levels for the logger and the two handlers
    # These levels represent the lowest severity of messages that will be handled.
    logger_level: int = logging.DEBUG
    logger_shell_level: int = logging.DEBUG
    logger_file_level: int = logging.DEBUG

    # Define the log formats for shell and file handlers
    # These formats determine how the log messages will be formatted
    logger_shell_fmt: str = "%(message)s"
    logger_file_fmt: (
        str
    ) = "%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] \t%(message)s"
