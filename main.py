import sqlite3
from random import choice

from telebot import TeleBot
from telebot.types import KeyboardButton,ReplyKeyboardMarkup, InlineKeyboardButton,InlineKeyboardMarkup

from utils import get_name_of_cities

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


@bot.message_handler(func=lambda message: message.text == 'Начать игру▶️')
def start_game(message):
    keyboard = InlineKeyboardMarkup()
    keyboard_cities = InlineKeyboardButton(text='"Игра в города"', callback_data='cities')
    keyboard.add(keyboard_cities)
    bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard)


game_stared = False
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global game_stared
    if call.data == 'cities':
        bot.send_message(call.message.chat.id, 'Напишите город')
        game_stared = True




def game_keyboard():
    stop = KeyboardButton('Стоп🛑')
    giveup = KeyboardButton('Сдаться🏳️')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(stop)
    keyboard.add(giveup)

    return keyboard

@bot.message_handler(func=lambda message: message.text == "Стоп🛑")
def stop_game(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,)




@bot.message_handler(content_types=['text'])
def game_handler(message):

    if game_stared:
        goroda_kotoriye_mojno_otvetit = []
        allcities = get_name_of_cities()
        user_city = message.text
        for i in allcities:
            if i.lower()[0] == user_city.lower()[-1]:
                goroda_kotoriye_mojno_otvetit.append(i)
            elif user_city.lower()[-1] == 'ь' or user_city.lower()[-1] == 'ъ' or user_city.lower()[-1] == 'й' or \
                    user_city.lower()[-1] == 'ы':
                if i.lower()[0] == user_city.lower()[-2]:
                    goroda_kotoriye_mojno_otvetit.append(i)
        gorod = choice(goroda_kotoriye_mojno_otvetit)
        bot.send_message(message.chat.id, gorod, reply_markup=game_keyboard())
        goroda_kotoriye_mojno_otvetit.clear()
bot.infinity_polling()













