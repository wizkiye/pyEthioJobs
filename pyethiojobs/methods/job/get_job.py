from typing import Union

from pyethiojobs.scaffold import Scaffold
from pyethiojobs.types import Job, JobDetails


class GetJob(Scaffold):
    async def get_job(self, job: Union[int, str, Job]) -> JobDetails:
        link = (
            job.link
            if isinstance(job, Job)
            else self._BASE_URL.format("display-job/" + job)
        )
        res = await self._process_request(url=link)
        return self._get_job_details(res.text)
