FROM python:3.10

WORKDIR /app

COPY services/dummy-service-endpoint/poetry.lock services/dummy-service-endpoint/pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry lock
RUN poetry install --no-interaction --no-ansi --no-root

WORKDIR /app/services/dummy-service-endpoint
COPY services/dummy-service-endpoint/dummy-service-endpoint/ dummy-service-endpoint/ 

ENTRYPOINT ["python", "dummy-service-endpoint/main.py"]