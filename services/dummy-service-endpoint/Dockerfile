FROM python:3.10

WORKDIR /app

COPY services/dummy-service/poetry.lock services/dummy-service/pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry lock
RUN poetry install --no-interaction --no-ansi --no-root

WORKDIR /app/services/dummy-service
COPY services/dummy-service/dummy-service/ dummy-service/ 

ENTRYPOINT ["python", "dummy-service/main.py"]