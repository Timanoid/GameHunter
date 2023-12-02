import telebot
from telebot import types
import webbrowser

class Gonka:
    def __init__(self, bot):
        self.bot = bot
    def on_clickGonka(self, message):
        if message.text == "🏎Гонки🏎":
            print("Gonka handler. Text", message.text)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btn15 = types.KeyboardButton(text="💸Платная💸")
            markup.row(btn15)
            btn16 = types.KeyboardButton(text="🆓Бесплатная🆓")
            markup.row(btn16)
            self.bot.send_message(message.chat.id,
                                  "Вы бы хотели чтобы игра была <b>платной</b> или <b>бесплатной?</b>",
                                  parse_mode='html', reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickPricegonka)
    def on_clickPricegonka(self, message):
        if message.text == '💸Платная💸':
            print("platnaya")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btndr = types.KeyboardButton(text = '🛣Дрифт🛣')
            markup.row(btndr)
            btngon = types.KeyboardButton(text = '🚘Гонки🚘')
            markup.row(btngon)
            self.bot.send_message(message.chat.id, 'Вы бы хотели дрифт по городу или же спортивные гонки?', reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickvid)
        if message.text == "🆓Бесплатная🆓":
            self.bot.send_message(message.chat.id, 'Вместо привычной практики выбора автомобиля и '
                                                   'трассы для гонки, TrackMania позволяет играть на '
                                                   'своих собственных трассах, созданных с использованием '
                                                   'конструкций блоков в духе игры Stunts. '
                                                   'Ссылка на скачивание в Steam: https://store.steampowered.com/app/2225070/Trackmania/')
    def on_clickvid(self, message):
        if message.text == '🛣Дрифт🛣':
            self.bot.send_message(message.chat.id, 'CarX Drift Racing дает вам шанс окунуться в истинный мир дрифта. '
                                                   'Объединяйтесь с друзьями, настраивайте свой автомобиль'
                                                   ' и жгите резину!, Ссылка на скачивание в Steam: https://store.steampowered.com/app/635260/CarX_Drift_Racing_Online/')
        if message.text == '🚘Гонки🚘':
            self.bot.send_message(message.chat.id, 'Forza Horizon 5 - это гоночная видеоигра, действие которой разворачивается в'
                                                   ' открытом мире, основанном на вымышленном представлении'
                                                   ' Мексики. В игре самая большая карта во всей серии Forza Horizon.'
                                                   ' Ссылка на скачивание в Xbox Store: https://www.microsoft.com/store/productId/9NNX1VVR3KNQ')




