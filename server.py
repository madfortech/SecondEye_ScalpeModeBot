from flask import Flask, request
import requests

# ===== TELEGRAM CONFIG =====
BOT_TOKEN = "8352840574:AAFbVjEN-nefbe9zYRIzIISKCxpJmAfGm-Y"
CHAT_ID = "7826747633"

# ===== TELEGRAM API URL =====
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

app = Flask(__name__)

# ===== WEBHOOK ROUTE =====
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json

        # TradingView alert message
        message = data.get("message", "No message received")

        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        response = requests.post(TELEGRAM_URL, json=payload)

        return {
            "status": "success",
            "telegram_response": response.json()
        }, 200

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500

# ===== RUN SERVER =====
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
