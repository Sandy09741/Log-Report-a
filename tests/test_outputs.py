import json
from pathlib import Path
from collections import Counter
import re


def _parse_access_log(log_path: str):
    """Parse the access log and return expected statistics."""
    total_requests = 0
    unique_ips = set()
    path_counts = Counter()
    
    with open(log_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            total_requests += 1
            
            # Extract IP (first field before space)
            ip = line.split()[0]
            unique_ips.add(ip)
            
            # Extract path from the request line: "METHOD /path HTTP/1.1"
            match = re.search(r'"[A-Z]+\s+(\S+)\s+HTTP', line)
            if match:
                path = match.group(1)
                path_counts[path] += 1
    
    # Top 5 paths by hit count (all 3 in this case, but capped at 5)
    popular_pages = [path for path, _ in path_counts.most_common(5)]
    
    return {
        "total_requests": total_requests,
        "unique_clients": len(unique_ips),
        "popular_pages": popular_pages,
    }


# Pre-compute expected values once
_EXPECTED = _parse_access_log("/app/access.log")


def test_report_exists():
    """Verifies criterion 1: The agent must produce /app/report.json."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_valid_json():
    """Verifies criterion 2: report.json must contain valid JSON."""
    with open("/app/report.json") as f:
        json.load(f)  # Will raise JSONDecodeError if invalid


def test_report_contains_total_requests():
    """Verifies criterion 3: report.json must include 'total_requests' matching the log."""
    with open("/app/report.json") as f:
        report = json.load(f)
    
    assert "total_requests" in report, "missing 'total_requests' key"
    assert report["total_requests"] == _EXPECTED["total_requests"], \
        f"expected total_requests={_EXPECTED['total_requests']}, got {report['total_requests']}"


def test_report_contains_unique_clients():
    """Verifies criterion 4: report.json must include 'unique_clients' matching the log."""
    with open("/app/report.json") as f:
        report = json.load(f)
    
    assert "unique_clients" in report, "missing 'unique_clients' key"
    assert report["unique_clients"] == _EXPECTED["unique_clients"], \
        f"expected unique_clients={_EXPECTED['unique_clients']}, got {report['unique_clients']}"


def test_report_contains_popular_pages():
    """Verifies criterion 5: report.json must include 'popular_pages' as top 5 by hits."""
    with open("/app/report.json") as f:
        report = json.load(f)
    
    assert "popular_pages" in report, "missing 'popular_pages' key"
    assert report["popular_pages"] == _EXPECTED["popular_pages"], \
        f"expected popular_pages={_EXPECTED['popular_pages']}, got {report['popular_pages']}"