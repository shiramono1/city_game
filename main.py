import sqlite3

from telebot import TeleBot
from telebot.types import KeyboardButton,ReplyKeyboardMarkup, InlineKeyboardButton,InlineKeyboardMarkup

TOKEN="5573199594:AAE3eUQBWc6SGJOT-I-t-JnvyxhprIN0teU"

bot=TeleBot(TOKEN, parse_mode=None)

def main_menu_keyboard():
    start=KeyboardButton("Начать игру▶️")
    rules=KeyboardButton("Правила🗒")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(start)
    keyboard.add(rules)

    return keyboard


@bot.message_handler(commands=['start'])
def message_handler(message):
    bot.send_message(message.chat.id, "Здравствуйте!Вас приветствует бот,в котором вы можете поиграть в игру города", reply_markup=main_menu_keyboard())


@bot.message_handler(func=lambda message: message.text == "Правила🗒")
def explain_rules(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Игра в города - словесная игра, где участники поочередно называют... города. Смысл в том, чтобы каждое следующее название начиналось с той буквы, на которую заканчивалось предыдущее название. Например, если первым назван город Санкт-Петербург, то смотрим: он заканчивается на букву Г. Соответственно, название следующего города должно начинаться на Г.")


bot.infinity_polling()






