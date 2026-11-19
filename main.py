

from flask import Flask, jsonify
from datetime import datetime
import os
import threading
import time

app = Flask(__name__)

BOT_NAME = "BELY"
MODE = "PAPER_TRADING"
INITIAL_BALANCE = 50.0

balance = INITIAL_BALANCE
bot_status = "RUNNING"
engine_status = "WAITING_FOR_MARKET_DATA"

def trading_engine():
    global engine_status

    while True:
        engine_status = "PAPER_MONITOR_ACTIVE"
        print(
            f"[{datetime.now().isoformat()}] "
            "BELY monitoring in paper mode",
            flush=True
        )
        time.sleep(60)

@app.route("/")
def home():
    return jsonify({
        "bot": BOT_NAME,
        "status": bot_status,
        "mode": MODE,
        "engine": engine_status,
        "virtual_balance": balance,
        "time": datetime.now().isoformat()
    })

@app.route("/status")
def status():
    return jsonify({
        "bot": BOT_NAME,
        "status": bot_status,
        "mode": MODE,
        "engine": engine_status,
        "virtual_balance": balance
    })

if __name__ == "__main__":
    thread = threading.Thread(
        target=trading_engine,
        daemon=True
    )
    thread.start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
