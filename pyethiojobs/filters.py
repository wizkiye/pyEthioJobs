import inspect
from datetime import datetime, timedelta
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

    async def __call__(self, job: Job):
        if inspect.iscoroutinefunction(self.base.__call__):
            x = await self.base(job)
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

        y = await self.other(job)

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


CUSTOM_FILTER_NAME = "MyCustomFilter"


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
        func, "DateFilter", dates=dates if isinstance(dates, list) else [dates]
    )


def valid_through(days: Union[str, int]):
    async def func(flt, job: Job):
        today = datetime.today()
        job_valid_through = datetime.strptime(job.valid_through, "%Y-%m-%d %H:%M:%S")
        if job_valid_through < today + timedelta(days=flt.days):
            return True

    return create(func, "ValidThroughFilter", days=days)


def hiring_organization(organizations: Union[str, List[str]]):
    async def func(flt, job: Job):
        if job.hiring_organization in flt.organizations:
            return True

    return create(
        func,
        "HiringOrganizationFilter",
        organizations=organizations
        if isinstance(organizations, list)
        else [organizations],
    )


def location(
    address_country: Union[str, List[str]] = "ETH",
    address_region: Union[str, List[str]] = None,
    address_locality: Union[str, List[str]] = None,
):
    async def func(flt, job: Job):
        if job.location.address_country in flt.address_country:
            if flt.address_region is not None:
                if job.location.address_region in flt.address_region:
                    if flt.address_locality is not None:
                        if job.location.address_locality in flt.address_locality:
                            return True
                    else:
                        return True
            else:
                return True

    return create(
        func,
        "LocationFilter",
        address_country=address_country,
        address_region=address_region,
        address_locality=address_locality,
    )
