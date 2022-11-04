from typing import Union, List

from pyethiojobs.scaffold import Scaffold
from pyethiojobs.types import Category, Job


class GetCategory(Scaffold):
    async def get_category(
        self, category: Union[int, str, Category], limit: int = 10
    ) -> List[Job]:
        link = (
            category.link
            if isinstance(category, Category)
            else self._BASE_URL.format("browse-by-category/" + category)
        )
        res = await self._process_request(url=link, params={"listings_per_page": limit})
        return self._get_jobs(res.text)
