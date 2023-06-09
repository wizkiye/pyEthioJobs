import httpx
from bs4 import BeautifulSoup

from .handler import HandlersHolder
from .methods import Methods
from .scaffold import Scaffold


class EthioJobs(Methods, Scaffold):
    def __init__(self):
        super().__init__()
        self._session = httpx.AsyncClient()
        self._soup = BeautifulSoup
        self._on_event_update = HandlersHolder(self)

    def soup(self, html: str) -> BeautifulSoup:
        return self._soup(html, "xml")

    async def _process_request(
        self, url: str, method="GET", **kwargs
    ) -> httpx.Response:
        if "http" in url:
            return await self._session.request(method, url, timeout=30, **kwargs)
        return await self._session.request(
            method=method,
            url=self._BASE_URL.format(url),
            timeout=30,
            **kwargs,
        )
