import inspect
from typing import Callable, Union, List

from pyethiojobs.types import Job


class Filter:
    async def __call__(self, job: Job):
        raise NotImplementedError

    def __invert__(self):
        return Invert(self)

    def __and__(self, other):
        return And(self, other)

    def __or__(self, other):
        return Or(self, other)


class Invert(Filter):
    def __init__(self, base):
        self.base = base

    async def __call__(self, message: Job):
        if inspect.iscoroutinefunction(self.base.__call__):
            x = await self.base(message)
            return not x
        return


class And(Filter):
    def __init__(self, base, other):
        self.base = base
        self.other = other

    async def __call__(self, job: Job):
        x = await self.base(job)

        if not x:
            return False

        y = await self.other(client, message)

        return x and y


class Or(Filter):
    def __init__(self, base, other):
        self.base = base
        self.other = other

    async def __call__(self, job: Job):
        x = await self.base(job)
        if x:
            return True

        y = await self.other(job)

        return x or y


CUSTOM_FILTER_NAME = "CustomFilter"


def create(func: Callable, name: str = None, **kwargs) -> Filter:
    return type(
        name or func.__name__ or CUSTOM_FILTER_NAME,
        (Filter,),
        {"__call__": func, **kwargs},
    )()


def work_place(places: Union[str, List[str]]):
    async def func(flt, job: Job):
        if job.work_place in flt.places:
            return True

    return create(
        func, "PlacesFilter", place=places if isinstance(places, list) else [places]
    )


def date(dates: Union[str, List[str]]):
    async def func(flt, job: Job):
        if job.date_posted in flt.dates:
            return True

    return create(
        func, "PlacesFilter", dates=dates if isinstance(dates, list) else [dates]
    )
