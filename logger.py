import psutil
import csv
import time
from datetime import datetime



def get_stats():
    return psutil.cpu_percent(interval=1), psutil.virtual_memory().percent, psutil.disk_usage('/').percent



with open("system_log.csv", "a", newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'cpu', 'ram', 'disk'])



try:
    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cpu, ram, disk = get_stats()
        print(f"Cpu is at: {cpu}% | Ram is at: {ram}% | Disk is at: {disk}%")
        with open("system_log.csv", "a", newline = "") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, cpu, ram, disk])
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopped")