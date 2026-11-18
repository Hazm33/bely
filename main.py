import time
from datetime import datetime

BOT_NAME = "BELY"
MODE = "PAPER_TRADING"
INITIAL_BALANCE = 50.0

balance = INITIAL_BALANCE

def log(message):
    print(f"[{datetime.now()}] {message}", flush=True)

def main():
    log(f"Starting {BOT_NAME}")
    log(f"Mode: {MODE}")
    log(f"Virtual balance: ${balance:.2f}")

    while True:
        log("BELY is monitoring...")
        time.sleep(60)

if __name__ == "__main__":
    main()