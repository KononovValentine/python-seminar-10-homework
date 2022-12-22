import telebot
from config import TOKEN
import random

bot = telebot.TeleBot(TOKEN)


def comrpes(message):
    str = message.text[0]
    bot.send_message(message.chat.id, str)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG9JtjpKIzzLbmWbOmvKEmZxGUWdNeKQACEwAD4jf5KfBy2PdTdYzALAQ')
    bot.send_message(message.chat.id, 'для повторного сжатия снова нажмите на кнопку "Сжать"')


def getNumber(message):
    number = str(random.randint(0, 10))
    if message.text == number:
        bot.send_message(message.chat.id, 'Угадал!')
    else:
        bot.send_message(message.chat.id, f'Не угадал! Я загадывал {number}')


def getZodiacInfo(data):
    with open('zodiacInfo.txt', 'r', encoding='utf-8') as file:
        zodiacInfo = list(map(str, file.read().split('; ')))
        return zodiacInfo[int(data) - 1]


def getSticker(message):
     bot.send_message(message.chat.id, 'Вот id твоего стикера!')
     bot.send_message(message.chat.id, f'{message.sticker.file_id}')
     bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBW2OkpWGLiZi3DiEHEXEfdwHBjJ5KAAIpAAPiN_kp9LGAEQRWbCcsBA')


"""Команда СТАРТ"""


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Рандомное число')
    item2 = telebot.types.KeyboardButton('Кинуть кость')
    item3 = telebot.types.KeyboardButton('Как дела?')
    item4 = telebot.types.KeyboardButton('Сжать')
    item5 = telebot.types.KeyboardButton('Загадай число')
    item6 = telebot.types.KeyboardButton('Знак зодиака')
    item7 = telebot.types.KeyboardButton('Покажи id стикера')

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)


def random_number(message):
    bot.send_message(message.chat.id, str(random.randint(1, 10)))


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет, как дела?')
    elif message.text == 'Рандомное число':
        random_number(message)
    elif message.text == 'Как дела?':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)

        item1 = telebot.types.InlineKeyboardButton('Не очень', callback_data='111')
        item2 = telebot.types.InlineKeyboardButton('Хорошо', callback_data='222')
        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Отлично, а у вас?', reply_markup=markup)
    elif message.text == 'Кинуть кость':
        bot.send_message(message.chat.id, f'Вам выпало {(random.randint(1, 6))}')
    elif message.text == 'Сжать':
        mesg = bot.send_message(message.chat.id, 'Введите строку которую хотите сжать')
        bot.register_next_step_handler(mesg, comrpes)
    elif message.text == 'Загадай число':
        mesg = bot.send_message(message.chat.id, 'Загадал')
        bot.register_next_step_handler(mesg, getNumber)
    elif message.text == 'Знак зодиака':
        markupZodiacSign = telebot.types.InlineKeyboardMarkup(row_width=3)

        itemZod1 = telebot.types.InlineKeyboardButton('Овен', callback_data='1')
        itemZod2 = telebot.types.InlineKeyboardButton('Телец', callback_data='2')
        itemZod3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data='3')
        itemZod4 = telebot.types.InlineKeyboardButton('Рак', callback_data='4')
        itemZod5 = telebot.types.InlineKeyboardButton('Лев', callback_data='5')
        itemZod6 = telebot.types.InlineKeyboardButton('Дева', callback_data='6')
        itemZod7 = telebot.types.InlineKeyboardButton('Весы', callback_data='7')
        itemZod8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='8')
        itemZod9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='9')
        itemZod10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='10')
        itemZod11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='11')
        itemZod12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='12')

        markupZodiacSign.add(itemZod1, itemZod2, itemZod3, itemZod4, itemZod5, itemZod6,
                             itemZod7, itemZod8, itemZod9, itemZod10, itemZod11, itemZod12)

        bot.send_message(message.chat.id, 'Выберите знак', reply_markup=markupZodiacSign)
    elif message.text == 'Покажи id стикера':
        mesg = bot.send_message(message.chat.id, 'Отправь мне стикер')
        bot.register_next_step_handler(mesg, getSticker)
    else:
        bot.send_message(message.chat.id, 'Данный функционал находится в разработке')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG9KtjpKLKiJySn0cxUtDhc8-9RLcp6AACFwAD4jf5KcGjsuWVf1eULAQ')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '111':
        bot.send_message(call.message.chat.id, 'Почему?')
    elif call.data == '222':
        bot.send_message(call.message.chat.id, 'Я рад!')
    elif call.data == '1':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')
    elif call.data == '2':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')
    elif call.data == '3':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')
    elif call.data == '4':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')
    elif call.data == '5':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')
    elif call.data == '6':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')
    elif call.data == '7':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')
    elif call.data == '8':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')
    elif call.data == '9':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')
    elif call.data == '10':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')
    elif call.data == '11':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')
    elif call.data == '12':
        bot.send_message(call.message.chat.id, f'{getZodiacInfo(call.data)}')


bot.polling(none_stop=True)
