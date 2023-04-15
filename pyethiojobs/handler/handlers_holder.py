import inspect
from typing import Callable, Optional, List, Dict

from pyethiojobs.types import Job


class HandlersHolder:
    def __init__(self, base):
        self._base = base
        self._events: Dict[str, List] = {
            "NEW_JOB_HANDLER": [],
        }

    def set_handler(
        self, event_name: str, func: Callable, filters: Optional[Callable] = None
    ):
        if inspect.iscoroutinefunction(func):
            return self._events[event_name].append({"func": func, "filters": filters})
        raise TypeError(f"{func.__name__} is not a coroutine function")

    def remove_handler(self, event_name: str, func: Callable):
        self._events[event_name] = [
            event for event in self._events[event_name] if event["func"] != func
        ]

    async def incoming_job_handler(self, job: Job):
        for event in self._events["NEW_JOB_HANDLER"]:
            if event["filters"] is not None:
                if event["filters"](job):
                    await event["func"](job)
            else:
                await event["func"](job)
