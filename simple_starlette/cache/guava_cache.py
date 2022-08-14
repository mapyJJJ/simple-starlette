#  -- guava cache --
import logging
import operator
import threading
import time
import typing


class GuavaCache:
    def __init__(
        self,
        interval: int,
        refresh_callable: typing.Callable,
    ) -> None:
        self.interval = interval
        self.refresh_callback = refresh_callable
        self._status = 0

    @property
    def status(self):
        return self._status

    def stop(self):
        self._status = 0

    def daemon_task(self):
        while self._status > 0:
            try:
                operator.methodcaller("refresh_callback")(self)
            except Exception as e:
                logging.error(f"guava executor error : {e}")
                break
            time.sleep(self.interval)

    def start(self):
        self._status = 1
        t = threading.Thread(target=self.daemon_task, daemon=True)
        t.start()
