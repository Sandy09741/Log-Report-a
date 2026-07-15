# Use a pinned, approved base image (replace <REAL_DIGEST> with actual 64-char hex digest)
FROM python:3.11-slim@sha256:REPLACE_WITH_REAL_DIGEST

# Install test dependencies at build time (no install at verify time)
RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

# Set working directory
WORKDIR /app

# Copy only the files the agent genuinely needs to solve the task
COPY access.log /app/access.log
COPY instruction.md /app/instruction.md

# Copy the verifier tests (needed for verification)
COPY tests/ /app/tests/

# Do NOT copy solution_hint.py — it leaks the reference solution