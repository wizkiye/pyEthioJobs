import json
import re
from typing import List

from bs4 import Tag

from pyethiojobs.scaffold import Scaffold
from pyethiojobs.types import Job, Identifier, Location
from pyethiojobs.utils import remove_newline


class GetLatestJobs(Scaffold):
    async def get_latest_jobs(self) -> List[Job]:
        """
        Get the latest jobs from the site.
        """
        res = await self._process_request("jobs-in-ethiopia/")
        soup = self.soup(res.text)
        job_container = soup.find("div", {"class": "content_latest marg-1"})
        listing = job_container.find_all("div", {"class": "single_listing col-md-6"})
        json_scripts: List[Tag] = job_container.find_all(
            "script", {"type": "application/ld+json"}
        )
        latest_jobs = []
        for job, single_list in zip(json_scripts, listing):
            link = single_list.find("a")
            text = re.sub(r'\w+\s+"(\w+)"\s+\w+', r" '\1' ", remove_newline(job.text))
            job = json.loads(text)
            experience = (
                re.search(
                    r".+\s*Required Experience:\s*(?:<\/\w+>|)(.+\s*.+)(?:\s*<\w+>|)",
                    job["description"],
                )
                .group(1)
                .strip()
            )
            latest_jobs.append(
                Job(
                    title=job["title"].strip(),
                    description=job["description"],
                    identifier=Identifier(
                        name=job["identifier"]["name"],
                        id=job["identifier"]["value"],
                    ),
                    experience=experience,
                    location=Location(
                        address_locality=job["jobLocation"]["address"][
                            "addressLocality"
                        ].strip(),
                        address_region=job["jobLocation"]["address"][
                            "addressRegion"
                        ].strip(),
                        address_country=job["jobLocation"]["address"][
                            "addressCountry"
                        ].strip(),
                    ),
                    date_posted=job["datePosted"],
                    valid_through=job["validThrough"],
                    type=job.get("employmentType"),
                    hiring_organization=job["hiringOrganization"]["name"].strip(),
                    link=link["href"],
                    base=self,
                    work_place=None,
                )
            )
        return latest_jobs
