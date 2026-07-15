#!/bin/bash
set -euo pipefail

# Create verifier logs directory if it doesn't exist
mkdir -p /logs/verifier

# Run pytest with verbose output and CTRF JSON report
# Tests are at /app/tests/ as copied by the Dockerfile
pytest /app/tests/test_outputs.py -v --ctrf /logs/verifier/ctrf.json

# Write reward to Harbor's expected path
# pytest exit code: 0 = all passed, non-zero = some failed
if [ $? -eq 0 ]; then
    echo "1.0" > /logs/verifier/reward.txt
else
    echo "0.0" > /logs/verifier/reward.txt
fi