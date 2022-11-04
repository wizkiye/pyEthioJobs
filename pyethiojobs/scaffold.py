from typing import List

import httpx
from bs4 import BeautifulSoup

from pyethiojobs.types import Job, JobDetails


class Scaffold:
    def __init__(self):
        self._session = None
        self._soup = None
        self._BASE_URL = "https://www.ethiojobs.net/{}"
        self._on_event_update = None

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
