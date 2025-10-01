# Stage 1: Build React frontend
FROM node:18 AS frontend
WORKDIR /app/frontend
COPY chatbot-frontend/package*.json ./
RUN npm install
COPY chatbot-frontend/ ./
RUN npm run build

# Stage 2: Backend
FROM python:3.11-slim AS backend
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ .

# Copy built frontend to a folder inside backend
COPY --from=frontend /app/frontend/dist ./static

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
