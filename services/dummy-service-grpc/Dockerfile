FROM python:3.10

WORKDIR /app

COPY services/dummy-service-grpc/poetry.lock services/dummy-service-grpc/pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry lock
RUN poetry install --no-interaction --no-ansi --no-root

WORKDIR /app/services/dummy-service-grpc
COPY services/dummy-service-grpc/dummy-service-grpc/ dummy-service-grpc/ 

ENTRYPOINT ["python", "dummy-service-grpc/main.py"]