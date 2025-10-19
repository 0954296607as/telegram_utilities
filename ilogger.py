from typing import Protocol
from abc import abstractmethod


class ILogger(Protocol):
    @abstractmethod
    def info(self, msg: str):
        raise NotImplementedError

    @abstractmethod
    def warn(self, msg: str):
        raise NotImplementedError

    @abstractmethod
    def error(self, msg: str):
        raise NotImplementedError
