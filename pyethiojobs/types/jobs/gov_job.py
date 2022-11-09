from typing import Union

import pyethiojobs
from pyethiojobs import types


class GovJob:
    def __init__(
        self,
        company: str,
        link: str,
        job: str,
        posted: str,
        base: "pyethiojobs.EthioJobs" = None,
    ):
        self.company = company
        self.link = link
        self.job = job
        self.posted = posted
        self._base = base

    async def get_details(self) -> Union["types.GovJobDetails", None]:
        if self._base is not None:
            res = await self._base._process_request(url=self.link)
            return self._base._get_gov_job_details(res.text)
