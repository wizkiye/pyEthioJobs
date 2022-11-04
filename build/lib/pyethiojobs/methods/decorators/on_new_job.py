from typing import Callable

from pyethiojobs.scaffold import Scaffold


class OnNewJob(Scaffold):
    def on_new_jobs(self, filters=None) -> Callable:
        """Decorator for handling when a new job is available
        Example:
            .. code-block:: python
                :emphasize-lines: 4-5
                ...
                app = EthioJobs(...)
                ...
                @app.on_new_jobs()
                async def handler(job: Job):
                    print(message.__dict__)
                ...
                app.run(...)
        """

        method = "NEW_JOB_HANDLER"

        # filters = card_recived & filters if filters else card_recived

        def decorator(func: Callable) -> Callable:
            if self is not None:
                self._on_event_update.set_handler(method, func, filters)
            return func

        return decorator
