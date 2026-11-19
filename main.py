

from datetime import datetime, timezone
import os
import threading

from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BOT_NAME = "BELY"
MODE = "PAPER_TRADING"
INITIAL_BALANCE = 50.0

balance = INITIAL_BALANCE
bot_status = "RUNNING"
engine_status = "WAITING_FOR_MARKET_DATA"
market_data_connected = False
trading_enabled = False
last_heartbeat = None

_stop_event = threading.Event()
_engine_thread = None
_engine_lock = threading.Lock()


def trading_engine():
    global engine_status, last_heartbeat

    while not _stop_event.is_set():
        engine_status = "WAITING_FOR_MARKET_DATA"
        last_heartbeat = datetime.now(timezone.utc).isoformat()

        print(
            f"[{last_heartbeat}] BELY waiting for market data. "
            "Paper mode only. No orders sent.",
            flush=True
        )

        _stop_event.wait(60)


def start_engine():
    global _engine_thread

    with _engine_lock:
        if _engine_thread is None or not _engine_thread.is_alive():
            _stop_event.clear()
            _engine_thread = threading.Thread(
                target=trading_engine,
                name="bely-paper-monitor",
                daemon=True
            )
            _engine_thread.start()


@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/status")
@app.route("/api/status")
def status():
    return jsonify({
        "bot": BOT_NAME,
        "status": bot_status,
        "mode": MODE,
        "engine": engine_status,
        "market_data_connected": market_data_connected,
        "trading_enabled": trading_enabled,
        "virtual_balance": balance,
        "last_heartbeat": last_heartbeat,
        "time": datetime.now(timezone.utc).isoformat()
    })


start_engine()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
