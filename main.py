import telebot
import random
import json
import handle
token = "6619867979:AAG9CJLcVkzeUAn5W_PExCz7SNx54zrDRwc"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def answer_user2(message):
    kb = telebot.types.InlineKeyboardMarkup()
    btn_rating = telebot.types.InlineKeyboardButton('рейтинг фильмов', callback_data='film_rating')
    btn_set_rate = telebot.types.InlineKeyboardButton('оценить фильм', callback_data='set_rate')
    kb.add(btn_rating, btn_set_rate)
    bot.send_message(message.chat.id, 'Привет, доступные команды', reply_markup=kb)

@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    kb = telebot.types.InlineKeyboardMarkup()
    if callback.data == 'film_rating':
        handle.send_rating(callback, bot)
    if callback.data == 'set_rate':
        btn_new = telebot.types.InlineKeyboardButton('новый фильм', callback_data='new_film')
        btn_edit = telebot.types.InlineKeyboardButton('редактировать', callback_data='edit')
        kb.row(btn_new, btn_edit)
    if callback.data == 'new_film':
        handle.new_film(callback, bot)
    bot.edit_message_reply_markup(callback.message.chat.id, callback.message.id, reply_markup=kb)
bot.polling(non_stop=True, interval=1)