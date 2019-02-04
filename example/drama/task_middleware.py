import dramatiq

from drama.models import Tasks


class JobMiddleware(dramatiq.middleware.Middleware):
    def job_update_or_create(self, message, status):
        Tasks.objects.update_or_create(
            message_id=message.message_id,
            defaults={"name": message.actor_name, "status": status},
        )

    def after_nack(self, broker, message):
        self.job_update_or_create(message, "REJECTED")

    def after_enqueue(self, broker, message, delay):
        self.job_update_or_create(message, "QUEUED")

    def before_process_message(self, broker, message):
        self.job_update_or_create(message, "RUNNING")

    def after_process_message(self, broker, message, *, result=None, exception=None):
        status = "SUCCESS"
        if exception is not None:
            status = "FAILURE"
        self.job_update_or_create(message, status)
