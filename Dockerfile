FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim AS runner
WORKDIR /app
RUN groupadd -r nexus && useradd -r -g nexus nexus
COPY --from=builder /root/.local /home/nexus/.local
COPY . /app
ENV PATH=/home/nexus/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1
RUN chown -R nexus:nexus /app
USER nexus
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
