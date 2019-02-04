import dramatiq

from drama.scheduler import cron


@dramatiq.actor
def count_chars(string):
    count = len(string)
    print(f"There are {count} characters in {string}")


@dramatiq.actor
def count_words(string):
    count = len(string.split("\n"))
    print(f"There are {count} words in {string}")


@cron("* * * * *")
@dramatiq.actor
def idempotent_method():
    print(f"Minute scheduler has been triggered")


@cron("*/2 * * * *")
@dramatiq.actor
def idempotent_method2():
    print(f"2 minute scheduler has been triggered")
