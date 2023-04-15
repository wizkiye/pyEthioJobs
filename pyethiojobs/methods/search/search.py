from typing import List

from pyethiojobs import types
from pyethiojobs.scaffold import Scaffold
from pyethiojobs.types import Job


class GetSearch(Scaffold):
    async def search(
        self, query: str, limit: int = 10, employment_type: types.EmploymentType = None
    ) -> List[Job]:
        url = self._BASE_URL.format("search-results-jobs/")
        params = {
            "action": "search",
            "listings_per_page": limit,
            "listing_type[equal]": "Job",
            "keywords[all_words]": query,
            "EmploymentType[multi_like][]": employment_type.value
            if employment_type
            else None,
        }
        res = await self._process_request(url, params=params)
        return self._get_jobs(res.text)

    async def search_company(self, company: str):
        pass


# https://www.ethiojobs.net/search-results-jobs/?action=search&listing_type[equal]=Job&keywords[all_words]=Graphics Designer&view=list&EmploymentType[multi_like][]=76
