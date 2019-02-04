import logging
import signal

from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management.base import BaseCommand

from drama.scheduler import JOBS
import drama.tasks  # noqa Need to import this to process the decorators

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


class Command(BaseCommand):
    help = "Start the task scheduler"

    """Implemented routines"""

    def add_arguments(self, parser):
        parser.add_argument(
            "--debug", action="store_true", dest="debug", help="Enable debug mode"
        )

    def handle(self, *args, **options):
        if options.get("debug") is not None:
            LOG.setLevel(logging.DEBUG)
        LOG.info("Starting scheduler...")
        self.schedule()

    """Main routine"""

    def schedule(self):
        scheduler = BlockingScheduler()
        for trigger, module_path, func_name in JOBS:
            job_path = f"{module_path}:{func_name}.send"
            job_name = f"{module_path}.{func_name}"
            LOG.info(f"Adding {job_name} to queue")
            scheduler.add_job(job_path, trigger=trigger, name=job_name)

        def shutdown(signum, frame):
            LOG.info("Shutting down scheduler")
            scheduler.shutdown()

        signal.signal(signal.SIGINT, shutdown)
        signal.signal(signal.SIGTERM, shutdown)

        scheduler.start()
        return 0
