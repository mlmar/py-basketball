# -----------------------------
# 1) BACKEND BUILD (FastAPI)
# -----------------------------
FROM python:3.13-slim AS backend-build

WORKDIR /app/server

# Install backend dependencies
COPY src/server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source
COPY src/server .

# -----------------------------
# 2) FRONTEND BUILD (Vite)
# -----------------------------
FROM node:18 AS frontend-build

ARG VITE_CLIENT_URL
ARG VITE_SERVER_URL
ENV VITE_CLIENT_URL=$VITE_CLIENT_URL
ENV VITE_SERVER_URL=$VITE_SERVER_URL

WORKDIR /app/client
COPY src/client/package.json src/client/package-lock.json ./
RUN npm install

# Copy client source
COPY src/client .
RUN npm run build

# -----------------------------
# 3) PRODUCTION IMAGE
# -----------------------------
FROM python:3.13-slim
WORKDIR /app/server

# Install runtime dependencies
COPY src/server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source 
COPY --from=backend-build /app/server .

# Copy built front end
COPY --from=frontend-build /app/server/static ./static

EXPOSE 3300

# Start FastAPI (which now serves the frontend)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3300"]
