FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN pip install poetry && poetry install --no-root

COPY . /app

CMD ["poetry", "run", "python", "fuzzy_broccoli/azure_openai_client.py"]
