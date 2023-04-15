from .category import Categories
from .decorators import Decorators
from .gov import Gov
from .job import Jobs
from .search import Search
from .utlis import Utils


class Methods(Search, Categories, Utils, Gov, Decorators, Jobs):
    pass
