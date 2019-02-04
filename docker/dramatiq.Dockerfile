FROM python:3.7.2

# Create application directory
RUN mkdir /app
WORKDIR /app

# Install dependencies
RUN pip install pipenv
COPY ./Pipfile* ./
RUN pipenv install --system

# Setup codebase
ADD ./example ./