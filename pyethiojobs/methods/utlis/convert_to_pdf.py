from ctypes import Union

from weasyprint import HTML

from pyethiojobs.scaffold import Scaffold
from pyethiojobs.types import JobDetails


class ConvertToPdf(Scaffold):
    async def convert_to_pdf(self, job: Union[str, JobDetails], filename: str) -> str:
        link = job.print_link if isinstance(job, JobDetails) else job
        html = HTML(link)
        html.write_pdf(filename)
        return filename
