from typing import List

from pyethiojobs import types


class Category:
    def __init__(
        self,
        name: str,
        link: str,
        count: int,
        base=None,
    ):
        self.name = name
        self.link = link
        self.count = count
        self._base = base

    async def get_jobs(self) -> List["types.Job"]:
        pass
