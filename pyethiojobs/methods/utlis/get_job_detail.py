import json
import re

from pyethiojobs.scaffold import Scaffold
from pyethiojobs.types import Identifier, JobDetails, Location
from pyethiojobs.utils import remove_newline


class GetJobsDetails(Scaffold):
    def _get_job_details(self, html) -> JobDetails:
        soup = self.soup(html)
        job = json.loads(
            remove_newline(soup.find("script", {"type": "application/ld+json"}).text)
        )
        views = soup.find("span", {"class": "jobs_by"}).text
        id = int(re.search(r"(\d+)\s+\|", views).group(1))
        views = int(re.search(r"(\d+)\s+Views", views).group(1))
        div = soup.find("div", {"id": "col-wide"})
        (category, location, career_level, employment_type, salary) = div.find_all(
            "div", {"class": "displayFieldBlock"}
        )
        return JobDetails(
            id=id,
            views=views,
            title=job["title"],
            work_place=location.text.split(":")[1].strip(),
            location=Location(
                address_locality=job["jobLocation"]["address"][
                    "addressLocality"
                ].strip(),
                address_region=job["jobLocation"]["address"]["addressRegion"].strip(),
                address_country=job["jobLocation"]["address"]["addressCountry"].strip(),
            ),
            date_posted=job["datePosted"],
            valid_through=job["validThrough"],
            type=employment_type.find("div", {"class": "displayField"}).text,
            hiring_organization=job["hiringOrganization"]["name"],
            link=self._BASE_URL.format(f"display-job/{id}"),
            description=job["description"],
            identifier=Identifier(
                name=job["identifier"]["name"],
                id=job["identifier"]["value"],
            ),
            print_link=self._BASE_URL.format(f"print-job/?listing_id={id}"),
            category=category.text.split(":")[1].strip(),
            salary=salary.text.split(":")[1].strip(),
            career_level=career_level.find("div", {"class": "displayField"}).text,
        )
