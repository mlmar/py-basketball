FROM python:3.13-slim AS backend-build
WORKDIR /app

# Install runtime dependencies into the virtualenv
COPY src/server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/server .

# Run the script (use -u to force unbuffered stdout/stderr)
CMD ["python", "-u", "process_daily_players.py"]