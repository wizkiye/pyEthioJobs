from typing import List

from bs4 import Tag

from pyethiojobs.scaffold import Scaffold
from pyethiojobs.types import Category


class GetCategories(Scaffold):
    async def get_categories(self) -> List[Category]:
        """
        Get all categories from the site.
        """
        res = await self._process_request(url="")
        soup = self.soup(res.text)
        div: Tag = soup.find("div", {"id": "job_category"})
        uls: Tag = div.find("ul", {"class": "list-group"})
        categories = []
        for anchor in uls.find_all("a", {"class": "list-group-item"}):
            name = anchor["title"]
            link = anchor["href"]
            count = int(anchor.find("span").text)
            categories.append(Category(name=name, link=link, count=count))
        return categories
