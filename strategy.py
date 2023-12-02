import telebot
from telebot import types
import webbrowser

class Strategy:
    def __init__(self, bot):
        self.bot = bot
    def on_clickStrategy(self, message):
        if message.text == "🌍Страгетия🌍":
            print("Gonka handler. Text", message.text)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btnpla = types.KeyboardButton(text="💸Платная💸")
            markup.row(btnpla)
            btnbesp = types.KeyboardButton(text="🆓Бесплатная🆓")
            markup.row(btnbesp)
            self.bot.send_message(message.chat.id,
                                  "Вы бы хотели чтобы игра была <b>платной</b> или <b>бесплатной?</b>",
                                  parse_mode='html', reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickPriceStrategy)
    def on_clickPriceStrategy(self, message):
        if message.text == '💸Платная💸':
            print("platnaya")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btnfe = types.KeyboardButton(text='⚔️Средневековая⚔️')
            markup.row(btnfe)
            btnj = types.KeyboardButton(text='🌍По II мировой войне🌍')
            markup.row(btnj)
            self.bot.send_message(message.chat.id, 'Вы бы хотели поиграть в средневековую стратегию или в стратегию по II мировой войне?',
                                  reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickvidstr)
        if message.text == "🆓Бесплатная🆓":
            self.bot.send_message(message.chat.id, 'RISK: Global Domination - Захватите мир в игре RISK.'
                                                   ' Мировое господство — в'
                                                   ' культовой стратегической настольной игре. Ссылка на скачивание в Steam: https://store.steampowered.com/app/1128810/RISK_Global_Domination/')
    def on_clickvidstr(self, message):
        if message.text == '⚔️Средневековая⚔️':
            self.bot.send_message(message.chat.id, 'Crusader Kings III - Любовь, война, '
                                                   'интриги и величие. Определите наследие'
                                                   ' своего знатного рода в безграничной '
                                                   'глобальной стратегии Crusader Kings III. Ссылка на скачивание в Steam: https://store.steampowered.com/app/1158310/Crusader_Kings_III/')
        if message.text == '🌍По II мировой войне🌍':
            self.bot.send_message(message.chat.id, 'Hearts of Iron IV - это глобальная стратегическая игра,'
                                                   ' разработанная компанией Paradox Development Studio, '
                                                   'в которой игроки могут управлять одной из многих наций'
                                                   ' во время Второй мировой войны и вести ее к победе. Игроки'
                                                   ' могут играть за любую из доступных наций, включая'
                                                   ' Германию, СССР, США, Великобританию, Францию, Японию и другие. Ссылка'
                                                   ' на скачивание в Steam: https://store.steampowered.com/app/394360/Hearts_of_Iron_IV/')
