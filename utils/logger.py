import logging
import sys
import os
from logging.handlers import TimedRotatingFileHandler


class Logger:
    COLORS = {
        "DEBUG": "\033[36m",     # Cyan
        "INFO": "\033[32m",      # Green
        "WARNING": "\033[33m",   # Yellow
        "ERROR": "\033[31m",     # Red
        "CRITICAL": "\033[41m",  # Red background
        "RESET": "\033[0m",
    }

    class TerminalFormatter(logging.Formatter):
        COLORS = {
            "DEBUG": "\033[36m",
            "INFO": "\033[32m",
            "WARNING": "\033[33m",
            "ERROR": "\033[31m",
            "CRITICAL": "\033[41m",
        }
        RESET = "\033[0m"

        def format(self, record):
            original_levelname = record.levelname

            color = self.COLORS.get(original_levelname, "")
            record.levelname = f"{color}{original_levelname}{self.RESET}"

            message = super().format(record)
            record.levelname = original_levelname

            return message


    def __init__(
        self,
        name: str = "app",
        log_dir: str = "logs",
        level: int = logging.INFO,
        retention_days: int = 7,
    ):
        os.makedirs(log_dir, exist_ok=True)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.propagate = False

        if self.logger.handlers:
            return

        # -------- Formats --------
        terminal_format = "%(asctime)s | %(levelname)-8s | %(message)s"
        file_format = "%(asctime)s | %(levelname)-8s | %(message)s"

        terminal_datefmt = "%H:%M:%S"
        file_datefmt = "%Y-%m-%d %H:%M:%S"

        # -------- Terminal Handler --------
        terminal_handler = logging.StreamHandler(sys.stdout)
        terminal_handler.setLevel(level)
        terminal_handler.setFormatter(
            self.TerminalFormatter(
                terminal_format,
                datefmt=terminal_datefmt,
            )
        )

        # -------- File Handler --------
        file_handler = TimedRotatingFileHandler(
            filename=os.path.join(log_dir, f"{name}.log"),
            when="midnight",
            backupCount=retention_days,
            encoding="utf-8",
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(
            logging.Formatter(
                file_format,
                datefmt=file_datefmt,
            )
        )

        self.logger.addHandler(terminal_handler)
        self.logger.addHandler(file_handler)

    # -------- Public API --------
    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)



logger = Logger(name="Expensedature-Management(Client)",log_dir='./logs',level=logging.INFO,retention_days=1)