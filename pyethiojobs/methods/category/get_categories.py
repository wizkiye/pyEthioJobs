from typing import Any, List

from bs4 import Tag
from rich.pretty import pprint

from pyethiojobs.scaffold import Scaffold
from pyethiojobs.types import Category


class GetCategories(Scaffold):
    async def get_categories(self) -> List[Category]:
        """
        Get all categories from the site.
        """
        res = await self._process_request(url="")
        soup = self.soup(res.text)
        div: Tag = soup.find("div", {"class": "browse_by panel panel-default"})
        uls = div.find_all("ul", {"class": "list-group"})
        categories = []
        for ul in uls:
            anchor = ul.find("a", class_="list-group-item")
            name = anchor["title"]
            link = anchor["href"]
            count = int(anchor.find("span").text)
            categories.append(Category(name=name, link=link, count=count))
        return categories
