from bs4 import Tag

from pyethiojobs.scaffold import Scaffold
from pyethiojobs.types import GovJobDetails, JobType


class GetGovJobsDetails(Scaffold):
    def _get_gov_job_details(self, html) -> GovJobDetails:
        soup = self.soup(html)
        job_title = soup.find("h1", {"class": "details-header__title "}).text
        location, gov_type = soup.find_all(
            "li",
            {"class": "listing-item__info--item listing-item__info--item-location"},
        )
        company = soup.find(
            "li", {"class": "listing-item__info--item listing-item__info--item-company"}
        )
        deadline = soup.find(
            "li", {"class": "listing-item__info--item listing-item__info--item-date"}
        )
        job_: Tag = soup.find("div", {"class": "job-type"})
        job_t = job_.find_all("span", {"class": "job-type__value"})
        salary, working_time = job_t[:2]
        type = ", ".join([j.text.strip() for j in job_t[2:]])
        # Todo separate the discription to Education level, Work experience, Instruction ...
        description = soup.find("div", {"class": "pull-left details-body__left"})
        job = JobType(salary=salary.text, working_time=working_time.text, type=type)
        return GovJobDetails(
            job_title=job_title.strip(),
            company=company.text.strip(),
            location=location.text.strip(),
            gov_type=gov_type.text.strip(),
            deadline=deadline.text.strip(),
            job_type=job,
            description=description.text.strip(),
        )
