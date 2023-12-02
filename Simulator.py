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
            self.bot.send_message(message.chat.id, 'Вы бы хотели поиграть в симулятор жизни или симулятор фермы?',
                                  reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickvidsim)
        if message.text == "🆓Бесплатная🆓":
            self.bot.send_message(message.chat.id, 'Russian Fishing 4 - это рыболовный симулятор с'
                                           ' элементами RPG, игровой процесс которого основан на '
                                           'концепции открытого мира и полной свободе '
                                           'действий игрока. Ссылка на скачивание в Steam: https://store.steampowered.com/app/766570/Russian_Fishing_4/')
    def on_clickvidsim(self, message):
        if message.text == '🚜Симулятор фермы🚜':
            self.bot.send_message(message.chat.id, 'Stardew Valley - Вам досталась старая дедушкина ферма в долине'
                                           ' Стардью. С горстью монет в кармане и старыми инструментами'
                                           ' в руках вы начинаете новую жизнь. Сможете '
                                           'ли вы превратить пустырь в цветущий сад? Ссылка на скачивание в Steam: https://store.steampowered.com/app/413150/Stardew_Valley/')
        if message.text == '❤️Симулятор жизни❤️':
            self.bot.send_message(message.chat.id, 'Estate Agent Simulator позволит вам окунуться'
                                           ' в захватывающий мир рынка недвижимости.Вы можете'
                                           ' покупать, декорировать, осуществлять рекламу,'
                                           ' сдавать в аренду или продавать дома.Вы можете '
                                           'покупать свободные участки земли и строить дома. Ссылка на скачивание в Steam: https://store.steampowered.com/app/2553050/Estate_Agent_Simulator/')

