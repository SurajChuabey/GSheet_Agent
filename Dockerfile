FROM python:3.11-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ENV UV_COMPILE_BYTECODE=1

COPY pyproject.toml uv.lock* ./

RUN if [ -f uv.lock ]; then uv sync --frozen --no-dev; \
    elif [ -f pyproject.toml ]; then uv pip install --system .; \
    else uv pip install --system -r requirements.txt; fi

# Copy the rest of the application
COPY . .


ENV TRANSPORT=http
ENV MCP_HOST_DEFAULT=0.0.0.0
ENV MCP_PORT_DEFAULT=9001

# Expose the FastMCP port
EXPOSE 9001 

# Run FastAPI using uv to execute the module
CMD ["uv", "run", "main.py"]

# docker run -p 9001:9001 -v $(pwd)/assets/:/app/assets gsheet:latestv1 