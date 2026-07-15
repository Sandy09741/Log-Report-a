# Use a pinned, approved base image
FROM python:3.11-slim@sha256:baf89808ec37adeaab83cec287adb4a2afa4a11c1d51e961c7ec737877e61af6

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