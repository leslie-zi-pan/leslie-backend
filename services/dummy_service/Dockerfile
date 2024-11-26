
FROM python:3.11 

WORKDIR /app

COPY services/dummy_service/poetry.lock services/dummy_service/pyproject.toml ./

RUN pip install poetry  # Install Poetry
RUN poetry config virtualenvs.create false
RUN poetry lock --no-update
RUN poetry install --no-interaction --no-ansi --no-root

WORKDIR /app/services/dummy_service
COPY services/dummy_service/src/ src/  

ENTRYPOINT ["python", "src/main.py"]