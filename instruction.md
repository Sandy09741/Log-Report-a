# Task: Log Report

There is an Apache-style access log at `/app/access.log`.

Your goal is to analyze the traffic and produce a JSON report at `/app/report.json`.

## Success Criteria

1. **File exists and is valid JSON**: `/app/report.json` must exist and contain valid JSON.

2. **Total requests**: The field `total_requests` must contain the total number of log entries in `/app/access.log`.

3. **Unique clients**: The field `unique_clients` must contain the count of unique IP addresses found in `/app/access.log`.

4. **Popular pages**: The field `popular_pages` must be a list of the top 5 most requested URL paths, sorted by request count in descending order. If fewer than 5 unique paths exist, list all of them.

5. **Values derived from log**: All values in `report.json` must be computed from `/app/access.log`. Hardcoded values will fail verification.

## Example

Given a log with 6 requests from 3 unique IPs, where `/index.html` was requested 3 times, `/about.html` 2 times, and `/api/login` 1 time, the expected output is:

```json
{
  "total_requests": 6,
  "unique_clients": 3,
  "popular_pages": ["/index.html", "/about.html", "/api/login"]
}