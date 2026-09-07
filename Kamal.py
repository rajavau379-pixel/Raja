import os
import sys
import time

# Script Details
AUTHOR_NAME = "Kamal"
CHANNEL_NAME = "TECHNICAL WORLD"
VERSION = "1.0.0"

# ANSI Color Codes for Better UI
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
RESET = "\033[0m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    clear_screen()
    print(
        f"""{GREEN}
██╗  ██╗ █████╗ ███╗   ███╗█████╗ ██╗     
██║ ██╔╝██╔══██╗████╗ ████║██╔══██╗██║     
█████═╝ ███████║██╔████╔██║███████║██║     
██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══██║██║     
██║  ██╗██║  ██║██║ ╚═╝ ██║██║  ██║███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
{RESET}"""
    )
    print(f"{CYAN}============================================={RESET}")
    print(f"{YELLOW}   WELCOME TO {CHANNEL_NAME} TOOL{RESET}")
    print(f"   DEVELOPER : {AUTHOR_NAME}")
    print(f"   VERSION   : {VERSION}")
    print(f"{CYAN}============================================={RESET}\n")


def run_tool():
    print_banner()
    print(f"{GREEN}[+] Starting tool process by {AUTHOR_NAME}...{RESET}")
    print("[+] System check in progress...")
    time.sleep(1.5)
    print(f"\n{GREEN}[✔] Process completed successfully!{RESET}")
    input(f"\n{YELLOW}Press [ENTER] to return to the main menu...{RESET}")


def show_about():
    print_banner()
    print(f"Tool Name   : {CHANNEL_NAME} Main Tool")
    print(f"Developer   : {AUTHOR_NAME}")
    print("Description : Public GitHub Testing Script.")
    input(f"\n{YELLOW}Press [ENTER] to return to the main menu...{RESET}")


def main():
    while True:
        print_banner()
        print(f" {GREEN}[01]{RESET} Start Tool")
        print(f" {GREEN}[02]{RESET} About Developer")
        print(f" {GREEN}[03]{RESET} Exit")
        print(f"{CYAN}---------------------------------------------{RESET}")

        choice = input(
            f"\n{YELLOW}Select an option [01-03] : {RESET}"
        ).strip()

        if choice in ["1", "01"]:
            run_tool()
        elif choice in ["2", "02"]:
            show_about()
        elif choice in ["3", "03"]:
            print(
                f"\n{RED}Thank you for using the tool by {AUTHOR_NAME}!{RESET}\n"
            )
            sys.exit()
        else:
            print(f"\n{RED}[!] Invalid Selection! Try again.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    main()    print(f"   DEVELOPER : {AUTHOR_NAME}")
    print(f"   VERSION   : {VERSION}")
    print(f"{CYAN}============================================={RESET}\n")


def run_tool():
    print_banner()
    print(f"{GREEN}[+] Starting tool process by {AUTHOR_NAME}...{RESET}")
    print("[+] System check in progress...")
    time.sleep(1.5)
    print(f"\n{GREEN}[✔] Process completed successfully!{RESET}")
    input(f"\n{YELLOW}Press [ENTER] to return to the main menu...{RESET}")


def show_about():
    print_banner()
    print(f"Tool Name   : {CHANNEL_NAME} Main Tool")
    print(f"Developer   : {AUTHOR_NAME}")
    print("Description : Public GitHub Testing Script.")
    input(f"\n{YELLOW}Press [ENTER] to return to the main menu...{RESET}")


def main():
    while True:
        print_banner()
        print(f" {GREEN}[01]{RESET} Start Tool")
        print(f" {GREEN}[02]{RESET} About Developer")
        print(f" {GREEN}[03]{RESET} Exit")
        print(f"{CYAN}---------------------------------------------{RESET}")

        choice = input(
            f"\n{YELLOW}Select an option [01-03] : {RESET}"
        ).strip()

        if choice in ["1", "01"]:
            run_tool()
        elif choice in ["2", "02"]:
            show_about()
        elif choice in ["3", "03"]:
            print(
                f"\n{RED}Thank you for using the tool by {AUTHOR_NAME}!{RESET}\n"
            )
            sys.exit()
        else:
            print(f"\n{RED}[!] Invalid Selection! Try again.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    main()    print(f"Tool Name   : {CHANNEL_NAME} Main Tool")
    print(f"Developer   : {AUTHOR_NAME}")
    print("Description : GitHub testing and automation script template.")
    input("\nPress Enter to return to the main menu...")


def main():
    while True:
        print_banner()
        print("1. Start Tool")
        print("2. About Developer")
        print("3. Exit")
        print("-" * 45)

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            run_tool()
        elif choice == "2":
            show_about()
        elif choice == "3":
            print(f"\nThank you for using the tool by {AUTHOR_NAME}!")
            sys.exit()
        else:
            print("\n[!] Invalid selection! Please try again.")
            time.sleep(1)


if __name__ == "__main__":
    main()
