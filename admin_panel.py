#!/usr/bin/env python3
import os

VERSION = "ADMIN PANEL v1.0"
AUTHOR = "GeminiXD Labs"

W = "\033[0m"; R = "\033[91m"; G = "\033[92m"; Y = "\033[93m"; C = "\033[96m"; P = "\033[95m"; K = "\033[1m"

BANNER = f"""
{C}{K}  █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
 ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║
 ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║
 ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║
 ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
 ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝{W}
{G}  ⚡ {VERSION} — Lihat Hasil Curian ⚡{W}
{P}  {AUTHOR}{W}
"""

def print_banner():
    os.system('clear')
    print(BANNER)
    print(f"{Y}[✓] Admin Panel — Data terenkripsi{W}\n")

def show_logs():
    try:
        with open('log.txt', 'r') as f:
            print(f"{G}=== LOG DATA ==={W}")
            print(f.read())
    except:
        print(f"{R}[✗] Belum ada data.{W}")

def main():
    print_banner()
    print(f"{Y}Pilih menu:{W}")
    print(f"  {C}1. Lihat semua data{W}")
    print(f"  {C}2. Hapus data{W}")
    print(f"  {C}3. Exit{W}")
    choice = input(f"{Y}Pilih: {W}")
    if choice == '1':
        show_logs()
    elif choice == '2':
        open('log.txt', 'w').close()
        print(f"{G}[✓] Data dihapus.{W}")
    else:
        print(f"{G}[✓] Sampai jumpa!{W}")

if __name__ == "__main__":
    main()