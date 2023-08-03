from typing import Union

from pyethiojobs import types, pyethiojobs


class Job:
    def __init__(
        self,
        job_id: str,
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
        base: "pyethiojobs.EthioJobs" = None,
    ):
        self.job_id = job_id
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

    async def get_details(self) -> "types.JobDetails":
        if self._base is not None:
            return await self._base.get_job(self.job_id)

    def __repr__(self):
        return f"Job(title={self.title}, link={self.link})"

    def __str__(self):
        return f"Job(title={self.title}, link={self.link})"

    def __eq__(self, other):
        return self.title == other.title and self.link == other.link
