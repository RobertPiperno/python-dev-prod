import os
import sys
import platform
import socket
import psutil
import requests
from datetime import datetime

# 1. Print system info
def print_system_info():
    print("System Information:")
    print(f"OS: {platform.system()} {platform.version()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Processor: {platform.processor()}")
    print("-" * 30)

# 2. Check network connectivity
def test_network_connectivity():
    print('Test Changes 2')
    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            print("Network Test: Connectivity successful.")
        else:
            print("Network Test: Failed to connect.")
    except requests.exceptions.RequestException as e:
        print(f"Network Test: Failed to connect. Error: {e}")
    print("-" * 30)

# 3. Log file write test
def write_to_log_file():
    log_message = f"{datetime.now()} - Test Log: All systems operational."
    log_file = "test_log.txt"
    
    with open(log_file, "a") as file:
        file.write(log_message + "\n")
    
    print(f"Log file updated: {log_message}")
    print("-" * 30)

# 4. Check disk space
def check_disk_space():
    disk_usage = psutil.disk_usage('/')
    print(f"Disk Space Info: {disk_usage.percent}% used of {disk_usage.total / (1024 ** 3):.2f} GB total.")
    if disk_usage.percent > 80:
        print("Warning: Disk space usage is over 80%!")
    print("-" * 30)

# Main function to run the test
def run_test():
    print_system_info()
    test_network_connectivity()
    write_to_log_file()
    check_disk_space()
    
if __name__ == "__main__":
    run_test()

