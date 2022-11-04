from pyethiojobs.scaffold import Scaffold


class GetSearch(Scaffold):
    async def search(self, query: str, limit: int = 10):
        url = self._BASE_URL.format("search-results-jobs/")
        params = {"action": query, "listings_per_page": limit}
        res = await self._process_request(url, params=params)
        return self._get_jobs(res.text)

    async def search_company(self, company: str):
        pass
