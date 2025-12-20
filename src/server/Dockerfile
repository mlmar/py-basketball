FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m venv .venv
RUN . .venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3300 5678
CMD ["python3", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", \
    "uvicorn", "main:app","--host", "0.0.0.0", "--port", "3300", "--reload"]
