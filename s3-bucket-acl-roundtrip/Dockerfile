FROM python:3.14-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
RUN uv pip install boto3 --system
COPY main.py .
CMD ["uv", "run", "main.py"]
