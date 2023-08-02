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
        job_id = int(re.search(r"(\d+)\s+\|", views).group(1))
        try:
            views = int(re.search(r"(\d+)\s+Views", views).group(1))
        except AttributeError:
            views = 0
        div = soup.find("div", {"id": "col-wide"})
        salary = div.find("div", string="Salary:")
        salary = salary.find_next_sibling().text if salary else None
        category = div.find("div", string="Category:")
        category = category.find_next_sibling().text if category else None
        location = div.find("div", string="Location:")
        location = (
            location.find_next_sibling().get_text(strip=True) if location else None
        )
        career_level = div.find("div", string="Career Level:")
        career_level = career_level.find_next_sibling().text if career_level else None
        employment_type = div.find("div", string="Employment Type:")
        employment_type = (
            employment_type.find_next_sibling().text if employment_type else None
        )
        return JobDetails(
            id=job_id,
            views=views,
            title=job["title"],
            work_place=location,
            location=Location(
                address_locality=job["jobLocation"]["address"][
                    "addressLocality"
                ].strip(),
                address_region=job["jobLocation"]["address"]["addressRegion"].strip(),
                address_country=job["jobLocation"]["address"]["addressCountry"].strip(),
            ),
            date_posted=job["datePosted"],
            valid_through=job["validThrough"],
            type=employment_type,
            hiring_organization=job["hiringOrganization"]["name"],
            link=self._BASE_URL.format(f"display-job/{job_id}"),
            description=job["description"],
            identifier=Identifier(
                name=job["identifier"]["name"],
                id=job["identifier"]["value"],
            ),
            print_link=self._BASE_URL.format(f"print-job/?listing_id={job_id}"),
            category=category,
            salary=salary,
            career_level=career_level,
        )
