from typing import List, Callable, Union

import httpx
from bs4 import BeautifulSoup

from pyethiojobs.filters import Filter
from pyethiojobs.handler import HandlersHolder
from pyethiojobs.types import Job, JobDetails, EmploymentType, GovJobDetails, Category
from pyethiojobs.types.jobs import GovJob


class Scaffold:
    def __init__(self):
        self._session = None
        self._soup = None
        self._BASE_URL = "https://www.ethiojobs.net/{}"
        self._on_event_update: HandlersHolder = None

    async def _process_request(
        self, url: str, method="GET", **kwargs
    ) -> httpx.Response:
        pass

    def soup(self, html: str) -> BeautifulSoup:
        pass

    def _get_jobs(self, html) -> List[Job]:
        pass

    def _get_job_details(self, html) -> JobDetails:
        pass

    async def get_categories(self) -> List[Category]:
        """
        Get all categories from the site.
        :return: List of categories.
        """
        pass

    async def get_category(
        self, category: Union[int, str, Category], limit: int = 10
    ) -> List[Job]:
        """
        Get jobs from a category.
        :param category: Category to get jobs from. Can be a Category object, a string or an int.
        :param limit: Number of jobs to get. Default is 10.
        :return: List of jobs.
        """
        pass

    def on_new_jobs(self, filters: Filter = None) -> Callable:
        """
        Decorator to listen for new jobs.
        :param filters: Filters to apply to the jobs.
        :return: Decorator.
        """
        pass

    def _get_gov_job_details(self, html) -> GovJobDetails:
        pass

    async def get_gov_jobs(self) -> List[GovJob]:
        """
        Get the latest government jobs from the site.
        :return: List of Gov jobs.
        """
        pass

    async def get_latest_jobs(self) -> List[Job]:
        """
        Get the latest jobs from the site.
        :return: List of jobs.
        """
        pass

    async def search(
        self, query: str, limit: int = 10, employment_type: EmploymentType = None
    ) -> List[Job]:
        """
        Search for jobs.
        :param query: Query to search for.
        :param limit: Number of jobs to return. Default is 10.
        :param employment_type: Type of employment to search for. Default is None. Can be FULL_TIME, PART_TIME,
        CONTRACT, INTERNSHIP, VOLUNTEER.
        :return: List of jobs.
        """
        pass

    def run(self, poll_interval: int = 60) -> None:
        """
        Run the listener.
        :param poll_interval: Interval to poll for new jobs. Default is 60 seconds.
        """
        pass
