import pyethiojobs


class GovJob:
    def __init__(
        self,
        company: str,
        link: str,
        job: str,
        posted: str,
        base: "pyethiojobs.EthioJobs" = None,
    ):
        self.company = company
        self.link = link
        self.job = job
        self.posted = posted
        self._base = base

    def get_detail(self):
        pass
