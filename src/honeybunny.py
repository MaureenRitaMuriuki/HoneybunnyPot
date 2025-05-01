import socket
import logging
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

PORT = 2222  # fake SSH
HOST = '0.0.0.0'

logging.basicConfig(filename='logs/attack_log.txt', level=logging.INFO)

def log_attempt(ip, port):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    alert = f"💌 ALERT: Connection from {ip}:{port} at {timestamp}"
    print(Fore.MAGENTA + alert)
    logging.info(alert)

def start_honeybunny():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print(Fore.LIGHTYELLOW_EX + f"🍯 Honeybunny listening on {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()
        log_attempt(addr[0], addr[1])
        conn.send(b"Access Denied. Go away, cutie hacker.\n")
        conn.close()

if __name__ == "__main__":
    start_honeybunny()
