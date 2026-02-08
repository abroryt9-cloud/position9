import telebot
from telebot import types
import os

# Вставь сюда токен, который получишь от @BotFather в Telegram
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Создание бота
bot = telebot.TeleBot(TOKEN)

# Стартовое приветствие
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 
                 "Добро пожаловать в Position! — это не ярлык, это репутация.\n\n"
                 "Мы создаём рубашки из египетского хлопка ELS с индивидуальным кроем.\n\n"
                 "Используйте команду /catalog, чтобы узнать о нашем ассортименте, или /order для оформления заказа.")

# Команда /catalog — ссылка на сайт
@bot.message_handler(commands=['catalog'])
def send_catalog(message):
    bot.reply_to(message, 
                 "Посмотрите наш каталог здесь: https://abroryt9-cloud.github.io/position/")

# Команда /order — запрос модели, размера и телефона
@bot.message_handler(commands=['order'])
def ask_order(message):
    msg = bot.reply_to(message, "Какую модель рубашки вы хотите заказать? Напишите название.")
    bot.register_next_step_handler(msg, ask_size)

def ask_size(message):
    model = message.text
    msg = bot.reply_to(message, f"Вы выбрали модель: {model}. Какой размер вам нужен?")
    bot.register_next_step_handler(msg, ask_phone, model)

def ask_phone(message, model):
    size = message.text
    msg = bot.reply_to(message, "Пожалуйста, оставьте ваш номер телефона для связи.")
    bot.register_next_step_handler(msg, complete_order, model, size)

def complete_order(message, model, size):
    phone = message.text
    bot.reply_to(message, f"Спасибо за ваш заказ!\nМодель: {model}\nРазмер: {size}\nТелефон: {phone}\n\n"
                          "Мы свяжемся с вами для подтверждения.")

# Команда /help — ответы на частые вопросы
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 
                 "Ответы на ваши вопросы:\n\n"
                 "1. Какие ткани используются?\n"
                 "Наши рубашки изготовлены из египетского хлопка ELS — лучший выбор для долговечности и комфорта.\n\n"
                 "2. Как я могу получить рубашку?\n"
                 "Мы предлагаем индивидуальный крой. Доставка доступна по всей стране.\n")

# Ответ на обычные фразы
@bot.message_handler(func=lambda message: True)
def default_response(message):
    text = message.text.lower()
    
    if "привет" in text:
        bot.reply_to(message, "Здравствуйте! Чем могу помочь?")
    elif "заказ" in text:
        bot.reply_to(message, "Для оформления заказа используйте команду /order.")
    else:
        bot.reply_to(message, "Если вам нужно больше информации, используйте команду /help.")

# Запуск бота
bot.polling(none_stop=True)
