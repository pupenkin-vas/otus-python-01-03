FROM python:3.12.10-alpine3.21@sha256:c08bfdbffc9184cdfd225497bac12b2c0dac1d24bbe13287cfb7d99f1116cf43

RUN pip install --no-cache-dir black isort mypy

WORKDIR /app

ENTRYPOINT ["sh", "-c"]