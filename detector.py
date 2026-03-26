import re
import json
from datetime import datetime

# Log file ka naam
log_file = "auth.log"

# Threshold (kitne attempts ke baad alert)
THRESHOLD = 3

# Dictionary to store IP counts
ip_count = {}

try:
    with open(log_file, "r") as file:
        for line in file:
            # Check for failed login
            if "Failed password" in line:
                
                # Extract IP using regex
                ip_match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
                
                if ip_match:
                    ip = ip_match.group()
                    
                    # Count attempts
                    ip_count[ip] = ip_count.get(ip, 0) + 1

except FileNotFoundError:
    print("❌ Log file not found!")
    exit()

# Alert generation
alerts = []

print("\n🔍 Checking for suspicious activity...\n")

for ip, count in ip_count.items():
    print(f"{ip} → {count} attempts")
    
    if count > THRESHOLD:
        alert = {
            "timestamp": str(datetime.now()),
            "source_ip": ip,
            "event": "Brute Force Detected",
            "attempts": count
        }
        alerts.append(alert)

# Print alerts
if alerts:
    print("\n🚨 ALERTS GENERATED:\n")
    print(json.dumps(alerts, indent=4))
    
    # Save to file (SIEM style)
    with open("alerts.json", "w") as f:
        json.dump(alerts, f, indent=4)

else:
    print("\n✅ No suspicious activity detected.")
