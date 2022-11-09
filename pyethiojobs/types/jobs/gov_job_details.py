from pyethiojobs import types


class GovJobDetails:
    def __init__(
        self,
        job_title: str,
        company: str,
        location: str,
        gov_type: str,
        deadline: str,
        job_type: "types.JobType",
        description: str,
    ):
        self.job_title = job_title
        self.job_type = job_type
        self.company = company
        self.location = location
        self.gov_type = gov_type
        self.deadline = deadline
        self.description = description
