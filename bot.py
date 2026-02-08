import telebot
import os
import sys

print("=== ЗАПУСК БОТА POSITION ===")

# 1. Получаем токен
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
print(f"1. Проверяю токен...")

if not TOKEN:
    print("❌ ОШИБКА: TELEGRAM_BOT_TOKEN не найден!")
    print("   Проверьте GitHub: Settings → Secrets → Actions")
    sys.exit(1)

print(f"   ✅ Токен получен: {TOKEN[:10]}...")

# 2. Создаём бота
try:
    bot = telebot.TeleBot(TOKEN)
    print("2. ✅ Бот создан")
except Exception as e:
    print(f"❌ Ошибка создания бота: {e}")
    sys.exit(1)

# 3. Команды
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Position — это репутация.\n/catalog /order /help")

@bot.message_handler(commands=['catalog'])
def catalog(message):
    bot.reply_to(message, "https://abroryt9-cloud.github.io/position/")

@bot.message_handler(commands=['order'])
def order(message):
    bot.reply_to(message, "Модель, размер, телефон — одним сообщением.")

# 4. Запуск
print("3. 🚀 Запускаю polling...")
try:
    bot.polling(none_stop=True, timeout=30)
    print("✅ Бот работает")
except Exception as e:
    print(f"❌ Ошибка polling: {e}")
    sys.exit(1)
