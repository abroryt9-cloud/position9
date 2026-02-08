import telebot
import os

# Получаем токен бота из переменных окружения
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Проверяем, что токен существует
if not TOKEN:
    print("Токен не найден! Убедитесь, что он передан через переменные окружения.")
    exit(1)

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Приветственное сообщение по команде /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Position — это не ярлык. Это репутация. \nКоманды: /catalog /order /help")

# Команда /catalog — отправка ссылки на сайт
@bot.message_handler(commands=['catalog'])
def send_catalog(message):
    bot.reply_to(message, "Каталог: https://abroryt9-cloud.github.io/position/")

# Команда /order — инструкция для оформления заказа
@bot.message_handler(commands=['order'])
def send_order_instructions(message):
    bot.reply_to(message, "Для заказа укажите одним сообщением: 1) модель, 2) размер, 3) телефон")

# Команда /help — отвечает на частые вопросы
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Частые вопросы:\nТкань - египетский хлопок ELS\nДоставка - Москва 1-2 дня\nКрой - индивидуальный")

# Обработка простых фраз
@bot.message_handler(func=lambda message: 'привет' in message.text.lower())
def greet(message):
    bot.reply_to(message, "Здравствуйте")

@bot.message_handler(func=lambda message: 'заказ' in message.text.lower())
def order_response(message):
    bot.reply_to(message, "Используйте /order для оформления заказа")

# Запуск бота (работает в фоне)
if __name__ == '__main__':
    print("Бот запущен")
    bot.polling(none_stop=True, timeout=60)  # Это гарантирует работу бота 24/7
