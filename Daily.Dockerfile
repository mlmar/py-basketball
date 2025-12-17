FROM python:3.13-slim AS backend-build
WORKDIR /app

# Use an isolated virtual environment for Python packages
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install runtime dependencies into the virtualenv
COPY src/server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/server .

# Run the script (use -u to force unbuffered stdout/stderr)
CMD ["python", "-u", "process_daily_players.py"]