from telegram import Bot
import schedule
import time
import os
import random

# Lấy token và chat ID từ biến môi trường
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TOKEN or not CHAT_ID:
    raise ValueError("Thiếu TELEGRAM_BOT_TOKEN hoặc TELEGRAM_CHAT_ID!")

bot = Bot(token=TOKEN)

def send_prediction():
    """Gửi dự đoán Loto 6 vào Telegram"""
    predicted_numbers = sorted(random.sample(range(1, 44), 6))
    message = f"🔥 Dự đoán Loto 6 hôm nay: {', '.join(map(str, predicted_numbers))}\nChúc anh may mắn! 🍀"
    
    bot.send_message(chat_id=CHAT_ID, text=message)
    print("[✔] Đã gửi dự đoán Loto 6!")

# Lên lịch gửi tin nhắn vào 8h sáng thứ 2 & thứ 5
schedule.every().monday.at("08:00").do(send_prediction)
schedule.every().thursday.at("08:00").do(send_prediction)

print("[🚀] Bot đã chạy! Sẽ tự động gửi số vào 8h sáng thứ 2 & thứ 5.")

while True:
    schedule.run_pending()
    time.sleep(60)
