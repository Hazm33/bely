
import time
import json
from datetime import datetime

BOT_NAME = "BELY"
MODE = "PAPER_TRADING"
INITIAL_BALANCE = 50.0

balance = INITIAL_BALANCE
trades = []

def log(message):
    print(f"[{datetime.now()}] {message}", flush=True)

def show_status():
    log(f"{BOT_NAME} is running")
    log(f"Mode: {MODE}")
    log(f"Virtual balance: ${balance:.2f}")
    log("Waiting for market data...")

def main():
    log("Starting BELY trading engine")
    show_status()

    while True:
        log("Paper trading monitor is active")
        time.sleep(60)

if __name__ == "__main__":
    main()
