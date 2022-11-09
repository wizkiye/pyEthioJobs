from .get_gov_job_details import GetGovJobsDetails
from .get_gov_jobs import GetGovernmentJobs


class Gov(GetGovernmentJobs, GetGovJobsDetails):
    pass
