import asyncio

from rich.pretty import pprint

from pyethiojobs.scaffold import Scaffold


class Run(Scaffold):
    def run(self, poll_interval: int = 60) -> None:
        """
        Run the scraper.
        """
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self._run(poll_interval))
            loop.close()
        except KeyboardInterrupt:
            print("Exiting...")
            loop.close()

    async def _run(self, poll_interval):
        """
        Run the scraper.
        """

        latest_jobs = await self.get_latest_jobs()
        first_job = latest_jobs[0]
        pprint(latest_jobs)
        while True:
            print("Checking for new jobs...")
            new_jobs = await self.get_latest_jobs()
            if new_jobs[0] != first_job:
                print("New job posted!")
                first_job = new_jobs[0]
                index_of_first_job = new_jobs.index(first_job)
                new_jobs = new_jobs[:index_of_first_job]
                for job in new_jobs:
                    pprint(job)
                    await self._on_event_update.incoming_job_handler(job=job)

            await asyncio.sleep(poll_interval)
