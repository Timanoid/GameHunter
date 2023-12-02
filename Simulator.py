import telebot
from telebot import types
import webbrowser

class Simulator:
    def __init__(self, bot):
        self.bot = bot
    def on_clickSimulator(self, message):
        if message.text == "🏎Гонки🏎":
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
