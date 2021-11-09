import telebot
from telebot import types
import random
import time


token = "2098827991:AAEyRFMfBvkSkfjLZnN6uOMCc1o-clk9W3o"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Меня зовут Нина и я '
                                      'консультант по здоровому питанию! Хотите, я помогу вам похудеть? Ответь да/нет')
    bot.send_photo(message.chat.id, open('photo9.jpg', 'rb'))


@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == 'да':
        time.sleep(2)
        msg = bot.reply_to(message, "Отлично! Но давайте сперва проверим, надо ли вам это?")
        time.sleep(2)
        bot.send_message(message.chat.id, 'Как вас зовут?')
        bot.register_next_step_handler(msg, send_name)

    elif message.text.lower() == 'нет':
        time.sleep(2)
        bot.send_message(message.chat.id, 'Я уверена, что у вас все в порядке с весом! Всего хорошего!')

    else:
        time.sleep(2)
        bot.send_message(message.chat.id, 'Извините, я не поняла вас')
        return


def send_name(message):
    global name
    name = message.text
    time.sleep(2)
    msg = bot.reply_to(message, f'Какой у вас рост, {name} ?')
    bot.register_next_step_handler(msg, send_height)


def send_height(message):
    global height
    height = message.text
    global yourHeight
    yourHeight = int(height)
    if not height.isdigit():
        msg = bot.reply_to(message, f'Вы уверены? Какой у вас рост, {name} ?')
        bot.register_next_step_handler(msg, send_height)
        return
    time.sleep(2)
    msg = bot.reply_to(message, f'Какой ваш вес, {name} ?')
    bot.register_next_step_handler(msg, send_weight)


def send_weight(message):
    global weight
    weight = message.text
    global yourWeight
    yourWeight = int(weight)
    if not weight.isdigit():
        msg = bot.reply_to(message, f'Вы уверены? Какой ваш вес, {name} ?')
        bot.register_next_step_handler(msg, send_weight)
        return
    time.sleep(2)
    msg = bot.reply_to(message, 'Одну минуту. Сейчас я рассчитаю, есть ли у вас лишний вес. ')
    time.sleep(3)
    bot.send_message(message.chat.id,  f'Готовы увидеть результат, {name}? Но сперва напишите мне, какой вес вы считаете идеальным.')
    time.sleep(5)
    bot.register_next_step_handler(msg,  offer)


def calculation_of_weight(weight, height):
    global normalWeight
    normalWeight= int(height - 100 - (height - 150)/2)
    global excessWeight
    excessWeight= normalWeight - weight
    global  group
    group = ''
    answer = ''
    if abs(excessWeight) <= 3:
        group = '1'
        answer = f"Ваш оптимальный вес, {name} - {normalWeight} кг. Отклонение - {excessWeight} кг. \nВы - Человек-Идеал. Вы в прекрасной форме. Занимайтесь спортом и не забывайте про здоровое питание"
    elif 3 < excessWeight <= 10:
        group = '2'
        answer = f"Ваш оптимальный вес, {name} - {normalWeight} кг. Отклонение - {excessWeight} кг.\nВы - Слишком Стройная Газель. Вам не надо беспокоиться по поводу веса, возможно вам стоит немного поправиться"
    elif excessWeight > 10:
        group = '3'
        answer = f"Ваш оптимальный вес, {name} - {normalWeight} кг. Отклонение - {excessWeight} кг. \nВы - Человек Кожа-и-Кости. Обратитесь к врачу."
    elif abs(-3) < abs(excessWeight) <= abs(-10):
        group = '4'
        answer = f"Ваш оптимальный вес, {name} - {normalWeight} кг. Отклонение - {excessWeight} кг. \nВы - Человек с Приятной Полнотой(пока еще). Стоит похудеть! "
    elif excessWeight < abs(-10):
        group = '5'
        answer = f"Ваш оптимальный вес, {name} - {normalWeight} кг. Отклонение - {excessWeight} кг. \nВы - Очень Пышная Особа. Вы обратились по адресу, но предстоит долгий путь!"
    return answer


def offer(message):
    msg = bot.reply_to(message, f'Вы здравомыслящий человек, {name}!')
    bot.send_message(message.chat.id, f'{calculation_of_weight(weight  = yourWeight, height = yourHeight)}')
    time.sleep(3)
    if group in '12':
        bot.send_message(message.chat.id, 'Вам не нужно худеть! Оставайтесь подписчиком моего канала и получайте каждый день рецепты полезных блюд и меню на день для поддержания веса')
        bot.send_photo(message.chat.id, open('photo10.jpg', 'rb'))
        while True:
            time.sleep(86400)
            bot.send_photo(message.chat.id, open('photo8.jpg', 'rb'))
            bot.send_message(message.chat.id, f'{menu()}')
            bot.send_message(message.chat.id, f'{recipies()}')
    elif group == '3':
        bot.send_message(message.chat.id, 'Будьте внимательны к своему здоровью! Помните: худоба не самоцель! Желаю удачи!!!')
        bot.send_photo(message.chat.id, open('photo3.jpg', 'rb'))
    elif group in '45':
        kb = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True,one_time_keyboard= True)
        button1 = types.KeyboardButton("Японская")
        button2 = types.KeyboardButton("Кремлевская")
        button3 = types.KeyboardButton("Гречневая")
        kb.add(button1,button2,button3)

        bot.send_message(message.chat.id, 'Предлагаю вам на выбор три лучшие диеты: японская (14 дней), гречневая(14 дней) и кремлевская (10 дней)',reply_markup=kb)

        bot.register_next_step_handler(msg, diets)
        bot.send_photo(message.chat.id, open('photo8.jpg', 'rb'))


def diets(message):
    if message.text.lower() == 'японская':
        bot.send_message(message.chat.id,'Отлично! Сейчас я пришлю меню на каждый день! Изучите его.')
        time.sleep(3)
        bot.send_message(message.chat.id, f'Купите необходимые продукты и начинайте путь к красоте и здоровью! У вас все получится {name}!')
        time.sleep(2)
        bot.send_message(message.chat.id, f'Желаю удачи, {name}!')
        bot.send_photo(message.chat.id, open('photo7.jpg', 'rb'))
        bot.send_message(message.chat.id, f'{diet_yap()}')
        i = 0
        while i <= 85:
            time.sleep(14400)
            bot.send_photo(message.chat.id, open('photo4.jpg', 'rb'))
            bot.send_message(message.chat.id, f'{warnings()}')
            i += 1

        bot.send_message(message.chat.id, f'Молодец, {name}! Вы справились!')
        bot.send_message(message.chat.id, f'А теперь давайте проверим результаты.')
        time.sleep(2)
        msg = bot.send_message(message.chat.id, f'Какой ваш новый вес, {name}? ')
        bot.register_next_step_handler(msg, send_weight)



    elif message.text.lower() == 'кремлевская':
        bot.send_message(message.chat.id,'Отлично! Сейчас я пришлю меню на каждый день! Изучите его.')
        bot.send_message(message.chat.id,f'Купите необходимые продукты и начинайте путь к красоте и здоровью! У вас все получится {name}!')
        bot.send_message(message.chat.id,f'Желаю удачи, {name}!')
        bot.send_photo(message.chat.id, open('photo7.jpg', 'rb'))
        bot.send_message(message.chat.id, f'{diet_kr()}')
        i = 0
        while i <= 60:
            time.sleep(14400)
            bot.send_photo(message.chat.id, open('photo4.jpg', 'rb'))
            bot.send_message(message.chat.id, f'{warnings()}')
            i += 1

        bot.send_message(message.chat.id, f'Молодец, {name}! Вы справились!')
        bot.send_message(message.chat.id, f'А теперь давайте проверим результаты.')
        time.sleep(2)
        msg = bot.send_message(message.chat.id, f'Какой ваш новый вес, {name}? ')
        bot.register_next_step_handler(msg, send_weight)

    elif message.text.lower() == 'гречневая':
        bot.send_message(message.chat.id,'Отлично! Сейчас я пришлю меню на каждый день! Изучите его.')
        bot.send_message(message.chat.id,f'Купите необходимые продукты и начинайте путь к красоте и здоровью! У вас все получится {name}!')
        bot.send_message(message.chat.id,f'Желаю удачи, {name}!')
        bot.send_photo(message.chat.id, open('photo7.jpg', 'rb'))
        bot.send_message(message.chat.id, f'{diet_gr()}')
        i = 0
        while i <= 85:
            time.sleep(14400)
            bot.send_photo(message.chat.id, open('photo4.jpg', 'rb'))
            bot.send_message(message.chat.id, f'{warnings()}')
            i += 1

        bot.send_message(message.chat.id, f'Молодец, {name}! Вы справились!')
        bot.send_message(message.chat.id, f'А теперь давайте проверим результаты.')
        time.sleep(2)
        msg = bot.send_message(message.chat.id, f'Какой ваш новый вес, {name}? ')
        bot.register_next_step_handler(msg, send_weight)
    else:
        bot.send_message(message.chat.id,'Извините, я вас не поняла. Уточните, какую диету вы выбрали.')
        return


def menu():
    with open('menu.txt', encoding='utf-8') as f:
        result = random.choice(f.readlines()).split('|')
        global strResult
        strResult = ''
        for i in result:
            strResult += i + '\n'
        return strResult


def warnings():
    global warning
    with open('warnings.txt', 'r', encoding='utf-8') as f:
        warning = random.choice(f.readlines())
        return warning


def recipies():
    global recipe       
    with open('recipies.txt', 'r', encoding='utf-8') as f:
        result = random.choice(f.readlines()).split('|')
        recipe = ''
        for i in result:
            recipe += i + '\n'
        return recipe


def diet_yap():
    global Diet_Yap
    Diet_Yap = ''
    with open('diet_yap.txt', encoding='utf-8') as f:
        content = f.readlines()
        for i in content:
            result = i.split('|')
            for y in result:
                Diet_Yap += y + '\n'
        return Diet_Yap


def diet_kr():
    global Diet_Kr
    Diet_Kr = ''
    with open('diet_kr.txt', encoding='utf-8') as f:
        content = f.readlines()
        for i in content:
            result = i.split('|')
            for y in result:
                Diet_Kr += y + '\n'
        return Diet_Kr


def diet_gr():
    global Diet_Gr
    Diet_Gr = ''
    with open('diet_gr.txt', encoding='utf-8') as f:
        content = f.readlines()
        for i in content:
            result = i.split('|')
            for y in result:
                Diet_Gr += y + '\n'
        return Diet_Gr


bot.polling(none_stop=True)