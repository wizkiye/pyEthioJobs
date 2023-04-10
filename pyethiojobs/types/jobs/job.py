from typing import Union

import pyethiojobs
from pyethiojobs import types


class Job:
    def __init__(
        self,
        title: str,
        description: str,
        link: str,
        identifier: "types.Identifier",
        experience: str,
        date_posted: str,
        valid_through: str,
        hiring_organization: str,
        location: "types.Location",
        work_place: Union[str, None],
        type: str,
        base: "pyethiojobs.pyEthioJobs" = None,
    ):
        self.experience = experience
        self.work_place = work_place
        self.title = title
        self.description = description
        self.link = link
        self.identifier = identifier
        self.date_posted = date_posted
        self.valid_through = valid_through
        self.hiring_organization = hiring_organization
        self.location = location
        self._base = base
        self.type = type

    async def get_details(self):
        if self._base is not None:
            res = await self._base._process_request(url=self.link)
            return self._base._get_job_details(res.text)
