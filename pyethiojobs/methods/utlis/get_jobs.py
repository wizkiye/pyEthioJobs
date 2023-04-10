import json
import re
from typing import List

from bs4 import Tag

from pyethiojobs.scaffold import Scaffold
from pyethiojobs.types import Identifier, Job, Location
from pyethiojobs.utils import remove_newline


class GetJobs(Scaffold):
    def _get_jobs(self, html) -> List[Job]:
        if "There are no postings meeting the criteria you specified" in html:
            return []
        soup = self.soup(
            html.split("<!-- start: JOB INFO -->")[1].split("<!-- end: JOB INFO -->")[0]
        )
        tbody: Tag = soup.find("tbody", {"class": "searchResultsJobs"})
        json_jobs = tbody.find_all("script", {"type": "application/ld+json"})
        trs = tbody.find_all("tr", class_="evenrow")
        jobs = []
        for job, tr in zip(json_jobs, trs):
            job = json.loads(remove_newline(job.text))
            link = tr.find("a", {"title": "View Job"})
            work_place = tr.find("span", {"class": "work-palce captions-field"})
            experience = tr.find(
                "span", {"class": "captions-field"}, text=re.compile("Level")
            ).text
            jobs.append(
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
                    hiring_organization=job["hiringOrganization"]["name"],
                    link=link["href"],
                    base=self,
                    work_place=work_place.text.strip(),
                )
            )
        return jobs
