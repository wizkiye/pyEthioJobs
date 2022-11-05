from typing import List

from bs4 import Tag

from pyethiojobs.scaffold import Scaffold
from pyethiojobs.types.jobs import GovJob


class GetGovernmentJobs(Scaffold):
    async def get_gov_jobs(self) -> List[GovJob]:
        res = await self._process_request(url="")
        soup = self.soup(res.text)
        div: Tag = soup.find("div", {"id": "public_latest"})
        gov_jobs = []
        for job in div.find_all("div", {"class": "single_listing"}):
            anchor = job.find("a")
            link = anchor.get("href")
            job_ = anchor.text
            company = job.find("p", {"class": "no-marign"}).text
            posted = job.find("span", {"class": "pull-right"}).text
            gov_jobs.append(GovJob(company=company, link=link, job=job_, posted=posted))
        return gov_jobs
