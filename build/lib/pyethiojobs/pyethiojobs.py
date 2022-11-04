import httpx
from bs4 import BeautifulSoup

from .scaffold import Scaffold
from .methods import Methods


class EthioJobs(Methods, Scaffold):
    def __init__(self):
        super().__init__()
        self._session = httpx.AsyncClient()
        self._soup = BeautifulSoup

    def soup(self, html: str) -> BeautifulSoup:
        return self._soup(html, "xml")

    async def _process_request(
        self, url: str, method="GET", **kwargs
    ) -> httpx.Response:
        if "http" in url:
            return await self._session.request(method, url, **kwargs)
        return await self._session.request(
            method=method, url=self._BASE_URL.format(url), **kwargs
        )
