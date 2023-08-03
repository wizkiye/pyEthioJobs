from .convert_to_pdf import ConvertToPdf
from .get_job_detail import GetJobsDetails
from .get_jobs import GetJobs
from .run import Run


class Utils(GetJobs, GetJobsDetails, Run, ConvertToPdf):
    pass
