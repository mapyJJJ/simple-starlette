from abc import ABCMeta, abstractmethod


class StatusCode(metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
    ) -> None:
        pass
