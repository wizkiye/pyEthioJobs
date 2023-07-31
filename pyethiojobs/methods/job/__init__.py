from .get_job import GetJob
from .get_latest_jobs import GetLatestJobs


class Jobs(GetLatestJobs, GetJob):
    pass
