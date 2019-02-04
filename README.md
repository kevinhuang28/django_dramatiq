# Django w/ Dramatiq and APScheduler example

This is an example of using Dramatiq with Django and using APScheduler for trigger periodic tasks.
A custom middleware was also created to track tasks through the message lifecycle.

The scheduler script was based off of https://defn.io/2018/01/11/dramatiq-cron/

# Setup

## Requirements

Docker and Docker Compose are required.

## Building & Deploying

1. > docker-compose -f compose.yml build
2. > docker-compose -f compose.yml up -d

3. To teardown:
   > docker-compose -f compose.yml down
