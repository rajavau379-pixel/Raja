import os
import sys
import time

# Script Information
AUTHOR_NAME = "Kamal"
CHANNEL_NAME = "TECHNICAL WORLD"
VERSION = "1.0.0"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    clear_screen()
    print("=" * 45)
    print(f"   WELCOME TO {CHANNEL_NAME} TOOL")
    print(f"   DEVELOPER : {AUTHOR_NAME}")
    print(f"   VERSION   : {VERSION}")
    print("=" * 45)
    print()


def run_tool():
    print_banner()
    print(f"[+] Starting tool processes by {AUTHOR_NAME}...")
    print("[+] Checking system requirements...")
    time.sleep(1.5)

    print("[✔] Process completed successfully!")
    input("\nPress Enter to return to the main menu...")


def show_about():
    print_banner()
    print(f"Tool Name   : {CHANNEL_NAME} Main Tool")
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
