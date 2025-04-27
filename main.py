from flask import Flask, request
import requests

app = Flask(__name__)

# Telegram Bilgileri
TELEGRAM_TOKEN = "7980649588:AAGaAlPBgTVO72NoyBnX5FWzK-kNlcKMuQo"  # <-- Buraya kendi bot tokenını yaz
TELEGRAM_CHAT_ID = "-4699679454"        # <-- Grup ID zaten doğru

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if not data:
        return "No data received", 400

    try:
        symbol = data.get('symbol', 'Unknown')
        interval = data.get('interval', 'Unknown')
        indicator = data.get('indicator', 'Unknown')
        signal = data.get('signal', 'Unknown')

        message = f"🚀 **Sinyal Geldi!**\n\n" \
                  f"🔹 Coin: {symbol}\n" \
                  f"🔹 Zaman Dilimi: {interval}\n" \
                  f"🔹 İndikatör: {indicator}\n" \
                  f"🔹 Sinyal Türü: {signal}"

        send_telegram_message(message)
        return "Success", 200

    except Exception as e:
        return str(e), 500

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
