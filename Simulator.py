import telebot
from telebot import types
import webbrowser

class Simulator:
    def __init__(self, bot):
        self.bot = bot
    def on_clickSimulator(self, message):
        if message.text == "🤖Симуляторы🤖":
            print("Gonka handler. Text", message.text)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btnpla = types.KeyboardButton(text="💸Платная💸")
            markup.row(btnpla)
            btnbesp = types.KeyboardButton(text="🆓Бесплатная🆓")
            markup.row(btnbesp)
            self.bot.send_message(message.chat.id,
                                  "Вы бы хотели чтобы игра была <b>платной</b> или <b>бесплатной?</b>",
                                  parse_mode='html', reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickPriceSimulator)
    def on_clickPriceSimulator(self, message):
        if message.text == '💸Платная💸':
            print("platnaya")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btnfe = types.KeyboardButton(text='🚜Симулятор фермы🚜')
            markup.row(btnfe)
            btnj = types.KeyboardButton(text='❤️Симулятор жизни❤️')
            markup.row(btnj)
            self.bot.send_message(message.chat.id, 'Вы бы хотели поиграть в симулятор жизни или симулятор феомы?',
                                  reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickvidsim)
        if message.text == "🆓Бесплатная🆓":
            self.bot.send_message(message, 'Russian Fishing 4 - это рыболовный симулятор с'
                                           ' элементами RPG, игровой процесс которого основан на '
                                           'концепции открытого мира и полной свободе '
                                           'действий игрока. Ссылка на скачивание в Steam: https://store.steampowered.com/app/766570/Russian_Fishing_4/')
