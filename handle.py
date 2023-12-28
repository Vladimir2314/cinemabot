import telebot
import json
token = "6619867979:AAG9CJLcVkzeUAn5W_PExCz7SNx54zrDRwc"
bot = telebot.TeleBot(token)
films_list = {}


def show_info(message):
    global films_list
    info = films_list[int(message.text)-1]["description"]
    bot.send_message(message.chat.id, info)

def send_rating(callback, bot):
    global films_list
    with open("films.json", encoding='UTF-8') as file:
        films = json.load(file)
    films_list = sorted(films.values(), key=lambda f: f.get("rating"), reverse=True)
    text = 'рейтинг фильмов: \n \n'
    for n, film in enumerate(films_list):
        text += f"{n + 1}. {film.get('name')}:  {film.get('rating')} \n"
    bot.send_message(callback.message.chat.id, text)
    bot.send_message(callback.message.chat.id, 'выберите интересный фильм')
    bot.register_next_step_handler(callback.message, show_info)

def add_photo(message):
    with open("films.json", encoding='UTF-8') as file:
        films = json.load(file)
    num = str(len(films))
    films[num]['photo'] = message.text
    with open("films.json", 'w', encoding='UTF-8') as file:
        json.dump(films, file, ensure_ascii=False)
    bot.send_message(message.chat.id, 'спасибо')


def add_name(message):
    with open("films.json", encoding='UTF-8') as file:
        films = json.load(file)
    num = str(len(films))
    films[num] = {}
    films[num]['name'] = message.text.split()[0]
    films[num]['rating'] = int(message.text.split()[1])
    with open("films.json", 'w', encoding='UTF-8') as file:
        json.dump(films, file, ensure_ascii=False)
    bot.send_message(message.chat.id, 'отправьте ссылку на картинку фильма')
    bot.register_next_step_handler(message, add_photo)



def new_film(callback, bot):
    bot.send_message(callback.message.chat.id, 'введите название фильма и оценку')
    bot.register_next_step_handler(callback.message, add_name)
