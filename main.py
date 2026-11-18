
from flask import Flask, jsonify
from datetime import datetime
import os
import time
import threading

app = Flask(__name__)

BOT_NAME = "BELY"
MODE = "PAPER_TRADING"
INITIAL_BALANCE = 50.0

balance = INITIAL_BALANCE
bot_status = "RUNNING"

@app.route("/")
def home():
    return jsonify({
        "bot": BOT_NAME,
        "status": bot_status,
        "mode": MODE,
        "virtual_balance": balance,
        "message": "BELY is online",
        "time": datetime.now().isoformat()
    })

@app.route("/status")
def status():
    return jsonify({
        "bot": BOT_NAME,
        "status": bot_status,
        "mode": MODE,
        "virtual_balance": balance
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
