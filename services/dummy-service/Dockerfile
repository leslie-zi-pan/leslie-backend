FROM python:3.13

WORKDIR /app

COPY services/dummy_service/poetry.lock services/dummy_service/pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry lock
RUN poetry install --no-interaction --no-ansi --no-root

WORKDIR /app/services/dummy_service
COPY services/dummy_service/dummy_service/ dummy_service/ 

ENTRYPOINT ["python", "dummy_service/main.py"]