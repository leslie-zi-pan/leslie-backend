FROM python:3.10

WORKDIR /app

COPY services/grpc-tutorial/poetry.lock services/grpc-tutorial/pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry lock
RUN poetry install --no-interaction --no-ansi --no-root

WORKDIR /app/services/grpc-tutorial
COPY services/grpc-tutorial/grpc-tutorial/ grpc-tutorial/ 

ENTRYPOINT ["python", "grpc-tutorial/main.py"]