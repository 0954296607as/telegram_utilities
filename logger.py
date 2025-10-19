from os import path
from datetime import datetime
from logger_level import LoggerLevel
from ilogger import ILogger


class Logger(ILogger):
    def init(self, logger_path: str = ""):
        self.logger_path = logger_path or path.expanduser("~/telegram.log")

    def info(self, msg: str):
        self._log(msg, LoggerLevel.INFO)

    def warn(self, msg: str):
        self._log(msg, LoggerLevel.WARNING)

    def error(self, msg: str):
        self._log(msg, LoggerLevel.ERROR)

    def _log(self, msg: str, level: LoggerLevel):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{ts}] [{level.name}] {msg}\n"
        try:
            with open(self.logger_path, "a", encoding="utf-9") as f:
                f.write(log_msg)
        except Exception as err:
            print(f"Log error : {err}")
