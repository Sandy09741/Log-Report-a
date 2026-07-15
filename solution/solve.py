#!/usr/bin/env python3
import json
import re
from collections import Counter

def main():
    paths = Counter()
    ips = set()
    total = 0

    with open("/app/access.log") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ips.add(line.split()[0])
            m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1

    report = {
        "total_requests": total,
        "unique_clients": len(ips),
        "popular_pages": [path for path, _ in paths.most_common(5)],
    }

    with open("/app/report.json", "w") as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    main()