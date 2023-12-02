import telebot
from telebot import types
import webbrowser
#bot = telebot.TeleBot('6425757827:AAFom6wJs2H-AFdj6kJMqc1fDXboK99i89o')
#def golovolomka(message):
    #bot.send_message(message.chat.id, ("В головоломке"
class Golovolomka:
    def __init__(self, bot):
        self.bot = bot

    def on_clickGolovolomka(self, message):
        # это коммент на русском
        res = ""
        if message.text == "🤔Головоломка🤔":
            print("Golovolomka handler. Text", message.text)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btn15 = types.KeyboardButton(text="💸Платная💸")
            markup.row(btn15)
            btn16 = types.KeyboardButton(text="🆓Бесплатная🆓")
            markup.row(btn16)
            self.bot.send_message(message.chat.id, "Вы бы хотели чтобы игра была <b>платной</b> или <b>бесплатной?</b>",
                             parse_mode='html', reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickPrice)
        else:
            print("golovolomka Error. Invalid message: ", message.text)
        print("on_clickGolovolomka done")

    def on_clickPrice(self, message):
        if message.text == '💸Платная💸':
            print("platnaya")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
            btn17 = types.KeyboardButton(text="⛱Песочница⛱")
            markup.row(btn17)
            btn18 = types.KeyboardButton(text="🌆С глубоким сюжетом🌆")
            markup.row(btn18)
            btn19 = types.KeyboardButton(text="💀Хоррор-головоломка💀")
            markup.row(btn19)
            self.bot.send_message(message.chat.id, "Вы бы поиграли в головоломку <b>песочницу</b> или "
                                                   "головоломку <b>с глубоким сюжетом?</b> или же в "
                                                   "<b>Хоррор-головоломку?</b>", parse_mode='html',
                                  reply_markup=markup)
            self.bot.register_next_step_handler(message, self.on_clickpes)
        if message.text == "🆓Бесплатная🆓":
            wwh = open(r"C:\Users\user\Pictures\header (2).jpg", 'rb')
            print("on click price. Message: ", message.text)
            print("besplatnaya")
            self.bot.send_photo(message.chat.id, wwh, 'We were here - По сюжету игры два человека оказываются в некоем заброшенном замке в'
                                        ' Антарктиде, при этом они могут общаться по рации. Первый заперт, а второму нужно '
                                        'его найти. Идея состоит в совместном прохождении, '
                                        'используя только голос и описание. Ссылка на скачивание в Steam: https://store.steampowered.com/app/582500/We_Were_Here/')
            self.bot.send_message(message.chat.id, 'Вот одна игра, подходящая описанию!')
    def on_clickpes(self, message):
        print("on_click5")
        if message.text == "⛱Песочница⛱":
            markup = types.InlineKeyboardMarkup()
            hff = open(r"C:\Users\user\Pictures\s728031.jpg", 'rb')
            self.bot.send_photo(message.chat.id, hff,
                                'Human: Fall Flat — головоломка с упором на реалистичную физику, '
                                'где игрок управляет персонажем по имени Боб. Вся игра — серия снов Боба. '
                                'Каждый сон нужно пройти до конца, решая головоломки и преодолевая препятствия.'
                                ' В арсенале у Боба есть только он сам: его тело и руки. '
                                'Руки у Боба не из слабых. В руках игроков Боб напоминает пластилинового '
                                'человечка — он может выгибаться почти под любым углом. Ссылка на скачивание '
                                'в Steam: https://store.steampowered.com/app/477160/Human_Fall_Flat/',
                                reply_markup=markup)
        if message.text == "🌆С глубоким сюжетом🌆":
            markup = types.InlineKeyboardMarkup()
            sledigra = types.InlineKeyboardButton(text='Следующая игра', callback_data='sled')
            markup.add(sledigra)
            self.bot.send_message(message.chat.id,
                                    'Portal 2 - логическая платформенная головоломка от 1-го лица, продолжение оригинальной игры Portal. '
                                    'Игроку вновь предстоит проходить сложные комнаты с использованием портальной пушки'
                                    ' и своей логики. В новой части появились новые элементы для взаимодействия с игроком, '
                                    'добавляющие интересные механики, например проталкивающий, отталкивающий и преобразующий гели, '
                                    'транспортные воронки, мосты плотного света и другие. Ссылка на скачивание в Steam: https://store.'
                                    'steampowered.com/category/puzzle_matching/', reply_markup=markup)
            self.bot.send_message(message.chat.id, 'Вот две игры, подходящих описанию!')
            @self.bot.callback_query_handler(func=lambda callback: callback.data)
            def callback_messagesuj(callback):
                if callback.data == 'sled':
                    self.bot.send_message(message.chat.id,  'We Were Here Together — кооперативное приключение с'
                                                           ' головоломками и видом от первого лица в серии игр We Were'
                                                           ' Here. Игра расскажет историю двух авантюристов, которые оказались '
                                                           'запертыми в таинственной цитадели вместе с чудаковатым психом-шутом. '
                                                           'Только слаженные действия героев помогут выбраться из этого мрачного места. '
                                                           'У каждого персонажа присутствует свой уникальный набор умений, который поможет '
                                                           'справиться с загадками свихнувшегося клоуна.'
                                                           'Cсылка на скачивание в Steam: https://store.steampowered.com/app/865360/We_Were_Here_Together/')
        if message.text == "💀Хоррор-головоломка💀":
            markup = types.InlineKeyboardMarkup()
            sleduigra = types.InlineKeyboardButton(text='Следующая игра', callback_data='sledu')
            markup.add(sleduigra)
            self.bot.send_message(message.chat.id, 'Phasmophobia — кооперативный хоррор, в котором вы'
                                                   ' вместе с тремя товарищами или случайными знакомыми'
                                                   ' охотитесь за доказательствами существования привидений.'
                                                   ' Ваша задача — не поймать или уничтожить призрака, а просто'
                                                   ' собрать доказательства его существования и определить тип.'
                                                   ' И чем больше будет этих доказательств,'
                                                   ' тем больше денег вам заплатят. Ссылка на скачивание в Steam: https://store.steampowered.com/app/739630/Phasmophobia/')
            self.bot.send_message(message.chat.id, 'Вот одна игра, подходящая описанию!')














