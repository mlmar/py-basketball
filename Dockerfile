# -----------------------------
# 1) FRONTEND BUILD (Vite)
# -----------------------------
FROM node:18 AS frontend-build

WORKDIR /app/client
COPY src/client/package.json src/client/package-lock.json ./
RUN npm install

COPY src/client .
RUN npm run build


# -----------------------------
# 2) BACKEND BUILD (FastAPI)
# -----------------------------
FROM python:3.13-slim AS backend-build

WORKDIR /app

# Install backend dependencies
COPY src/server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source
COPY src/server ./server


# -----------------------------
# 3) PRODUCTION IMAGE
# -----------------------------
FROM python:3.13-slim

WORKDIR /app

# Install runtime dependencies
COPY src/server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source (including built frontend)
COPY --from=backend-build /app/server ./server

EXPOSE 3300

# Start FastAPI (which now serves the frontend)
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "3300"]
