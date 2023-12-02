import telebot
from telebot import types
import webbrowser
from golovolomka import Golovolomka
from Gonka import Gonka
from Simulator import Simulator

bot = telebot.TeleBot('6425757827:AAFom6wJs2H-AFdj6kJMqc1fDXboK99i89o')

@bot.message_handler(commands = ['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
    btn1 = types.KeyboardButton(text = '🎮Перейти на сайт с акциями на игры🎮')
    markup.row(btn1)
    btn2 = types.KeyboardButton(text='🔎Начать поиск игр🔍')
    markup.row(btn2)
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>! Я <b>GameHunter</b> –  бот для подбора игр. Я стану вашим лучшим помощником в поиске игр!🤖', parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, on_click1)

def maincopy(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
    btn1 = types.KeyboardButton(text = '🎮Перейти на сайт с акциями на игры🎮')
    markup.row(btn1)
    btn2 = types.KeyboardButton(text='🔎Начать поиск игр🔍')
    markup.row(btn2)
    bot.register_next_step_handler(message, on_click1)

def on_click1(message):
    if message.text == "🎮Перейти на сайт с акциями на игры🎮":
        bot.send_message(message.chat.id, 'Ссылка на сайт: ''https://www.playground.ru/news/freebies')
        maincopy(message)
    if message.text == '🔎Начать поиск игр🔍':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
        btn6 = types.KeyboardButton(text="🤔Головоломка🤔")
        markup.row(btn6)
        btn7 = types.KeyboardButton(text='🏎Гонки🏎')
        markup.row(btn7)
        btn10 = types.KeyboardButton(text="🤖Симуляторы🤖")
        markup.row(btn10)
        btn11 = types.KeyboardButton(text="⚽️Спортивные⚽")
        markup.row(btn11)
        btn12 = types.KeyboardButton(text="🌍Страгетия🌍")
        markup.row(btn12)
        btn13 = types.KeyboardButton(text="💣Шутер💣")
        markup.row(btn13)
        bot.send_message(message.chat.id, "Выберите <b>категорию</b> игры", parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, on_clickGameSelect)

def on_clickGameSelect(message):
    if message.text == "🤔Головоломка🤔":
        golovolomka = Golovolomka(bot)
        print("golovolomka")
        golovolomka.on_clickGolovolomka(message)
    if message.text == '🏎Гонки🏎':
        gonka = Gonka(bot)
        gonka.on_clickGonka(message)
        print("gonka")
    if message.text == "🤖Симуляторы🤖":
        simulator = Simulator(bot)
        simulator.on_clickSimulator()
        print("simulator")

###############################################################
if __name__=='__main__':
    bot.polling(none_stop=True)
