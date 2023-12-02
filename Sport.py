import telebot
from telebot import types
import webbrowser

class Sport:
    def __init__(self, bot):
        self.bot = bot
    def on_clickSport(self, message):
        if message.text == "⚽️Спортивные⚽":
            print("Gonka handler. Text", message.text)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btnplatn = types.KeyboardButton(text="💸Платная💸")
            markup.row(btnplatn)
            btnbesplatn = types.KeyboardButton(text="🆓Бесплатная🆓")
            markup.row(btnbesplatn)
            self.bot.send_message(message.chat.id,
                                  "Вы бы хотели чтобы игра была <b>платной</b> или <b>бесплатной?</b>",
                                  parse_mode='html', reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickPriceSport)
    def on_clickPriceSport(self, message):
        if message.text == '💸Платная💸':
            print("platnaya")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btnfu = types.KeyboardButton(text='⚽️Футбол⚽️')
            markup.row(btnfu)
            btnho = types.KeyboardButton(text='🏒Хоккей🏒')
            markup.row(btnho)
            btnbas = types.KeyboardButton(text='🏀Баскетбол🏀')
            markup.row(btnbas)
            self.bot.send_message(message.chat.id, 'Вы бы хотели поиграть в игру про футбол, хоккей или баскетбол?',
                                  reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickvidsport)
        if message.text == "🆓Бесплатная🆓":
            self.bot.send_message(message.chat.id, 'eFootball™ 2024 - Классический футбольный симулятор '
                                                   'с актуальными данными! Наслаждайтесь атмосферой реалистичного'
                                                   'футбола в eFootball™ 2024! Ссылка на скачивание в Steam: https://store.steampowered.com/app/1665460/eFootball_2024/')
    def on_clickvidsport(self, message):
        if message.text == '⚽️Футбол⚽️':
            self.bot.send_message(message.chat.id, 'Заряжено футболом. EA SPORTS™ FIFA 22 приближает игру к '
                                                   'реальности с фундаментальными улучшениями игрового процесса и '
                                                   'инновациями во всех режимах. Ссылка на скачивание в Steam: https://store.steampowered.com/app/1506830/FIFA_22/')
        if message.text == '🏒Хоккей🏒':
            self.bot.send_message(message.chat.id, 'Super Blood Hockey — это простенькая с виду и по игровому процессу,'
                                                   ' но глубоко проработанная хоккейная аркада в мире кровавого спорта. '
                                                   'Станьте тренером хоккейной команды, набирайте игроков среди заключённых,'
                                                   ' настраивайте их тренировки и рацион. Ссылка на скачивание в Steam: https://store.steampowered.com/app/532190/Super_Blood_Hockey/')
        if message.text == '🏀Баскетбол🏀':
            self.bot.send_message(message.chat.id,'Regular Human Basketball – мультиплеерная игра, где твоя команда борется с контролем гигантских механических машин смерти. Выкрикивай приказы, нажимай переключатели, бросай мяч в кольца'
                                                  ' в пост-апокалиптическом баскетбольном матче. '
                                                  'Работай совместно, чтобы контролировать человека. Играй в '
                                                  'матче 1 на 1 или бери с собой на помощь друзей. Ссылка на скачивание в Steam: https://store.steampowered.com/app/661940/Regular_Human_Basketball/')

