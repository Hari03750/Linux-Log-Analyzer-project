import re
import os

# Use sample log file for Windows testing
log_file = "sample_log.txt"

error_count = 0
warning_count = 0
info_count = 0

if os.path.exists(log_file):
    with open(log_file, "r") as f:
        for line in f:
            if re.search(r"error", line, re.IGNORECASE):
                error_count += 1
            elif re.search(r"warn", line, re.IGNORECASE):
                warning_count += 1
            elif re.search(r"info", line, re.IGNORECASE):
                info_count += 1

    print("===== Log Analyzer (Windows Test) =====")
    print(f"Errors   : {error_count}")
    print(f"Warnings : {warning_count}")
    print(f"Info     : {info_count}")
else:
    print(f"⚠️ Log file {log_file} not found.")
