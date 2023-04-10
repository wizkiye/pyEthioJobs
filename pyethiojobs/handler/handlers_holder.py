import inspect
from typing import Callable, Optional, List, Dict

from pyethiojobs.types import Job


class HandlersHolder:
    def __init__(self, base):
        self._base = base
        self._events: Dict[str, List] = {
            "ON_NEW_JOB": [],
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

    async def incoming_job_handler(self, message: Job):
        for event_name, events in self._events.items():
            for event in events:
                if event.get("filters"):
                    res = await event["filters"](self._base, message)
                    if res:
                        await event["func"](self._base, message)
                else:
                    await event["func"](self._base, message)
