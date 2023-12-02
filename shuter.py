import telebot
from telebot import types
import webbrowser

class Shuter:
    def __init__(self, bot):
        self.bot = bot
    def on_clickShuter(self, message):
        if message.text == "💣Шутер💣":
            print("Gonka handler. Text", message.text)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btnpla = types.KeyboardButton(text="💸Платная💸")
            markup.row(btnpla)
            btnbesp = types.KeyboardButton(text="🆓Бесплатная🆓")
            markup.row(btnbesp)
            self.bot.send_message(message.chat.id,
                                  "Вы бы хотели чтобы игра была <b>платной</b> или <b>бесплатной?</b>",
                                  parse_mode='html', reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickPriceShuter)
    def on_clickPriceShuter(self, message):
        if message.text == '💸Платная💸':
            print("platnaya")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btnon = types.KeyboardButton(text='🌐Онлайн шутер🌐')
            markup.row(btnon)
            btnsuj = types.KeyboardButton(text='🎬С сюжетом🎬')
            markup.row(btnsuj)
            self.bot.send_message(message.chat.id, 'Вы бы хотели поиграть в онлайн шутер или в шутер с сюжетом?',
                                  reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickvidshut)
        if message.text == "🆓Бесплатная🆓":
            self.bot.send_message(message.chat.id, 'Overwatch® 2 - бесплатная командная игра '
                                                   'в ярком мире будущего с постоянно растущим'
                                                   ' списком героев. Играйте вместе с друзьями уже '
                                                   'сегодня! Ссылка на скачивание в Steam: https://store.steampowered.com/app/2357570/Overwatch_2/')
    def on_clickvidshut(self, message):
        if message.text == '🌐Онлайн шутер🌐':
            self.bot.send_message(message.chat.id, 'Total Lockdown – королевская битва '
                                                   'на последних этажах огромного небоскреба.'
                                                   ' Динамичный шутер, где цель игры выжить,'
                                                   ' используя любое оружие, гаджеты и уловки. '
                                                   'Сражайтесь за деньги и славу в смертельной битве! Ссылка на скачивание в Steam: https://store.steampowered.com/app/1121710/Total_Lockdown/')
        if message.text == '🎬С сюжетом🎬':
            self.bot.send_message(message.chat.id, 'Deep Rock Galactic - первый научно-фантастический шутер с видом от'
                                                   ' первого лица для совместной игры, в котором '
                                                   'вас ждут крутые космические гномы, полностью разрушаемое '
                                                   'окружение, процедурно генерируемые системы пещер и бесконечные '
                                                   'волны инопланетных чудовищ. Ссылка на скачивание в Steam: https://store.steampowered.com/app/548430/Deep_Rock_Galactic/')