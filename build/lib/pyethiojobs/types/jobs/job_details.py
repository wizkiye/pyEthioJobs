import pyethiojobs
from pyethiojobs import types


class JobDetails:
    def __init__(
        self,
        id: int,
        title: str,
        description: str,
        link: str,
        views: int,
        category: str,
        salary: str,
        print_link: str,
        identifier: "types.Identifier",
        date_posted: str,
        valid_through: str,
        hiring_organization: str,
        location: "types.Location",
        work_place: str,
        type: str,
    ):
        self.id = id
        self.print_link = print_link
        self.salary = salary
        self.category = category
        self.views = views
        self.work_place = work_place
        self.title = title
        self.description = description
        self.link = link
        self.identifier = identifier
        self.date_posted = date_posted
        self.valid_through = valid_through
        self.hiring_organization = hiring_organization
        self.location = location
        self.type = type
