# import telebot
# import turtle
#
# token="2098827991:AAEyRFMfBvkSkfjLZnN6uOMCc1o-clk9W3o"
#
# bot = telebot.TeleBot(token)
#
# user_dict = {}
#
#
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.weight = None
#         self.height = None
#         self.normalWeight = None
#         self.excessWeight = None
#
#
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id, 'Здравствуйте! Меня зовут Нина и я '
#                                       'консультант по здоровому питанию! Хотите, я помогу вам похудеть? Ответь да/нет')
#
#
# @bot.message_handler(content_types=["text"])
# def send_text(message):
#     if message.text.lower() == 'да':
#         msg = bot.reply_to(message, "Отлично! Но давай сперва проверим, надо ли вам это?")
#         bot.send_message(message.chat.id, 'Как вас зовут?')
#         bot.register_next_step_handler(msg, send_name)
#
#     elif message.text.lower() == 'нет':
#         bot.send_message(message.chat.id, 'Я уверена, что у вас все в порядке с весом! Прощайте, дружок!')
#
#
# def send_name(message):
#     chat_id = message.chat.id
#     name = message.text
#     user = User(name)
#     user_dict[chat_id] = user
#     msg = bot.reply_to(message, f'Какой у вас рост, {name} ?')
#     bot.register_next_step_handler(msg, send_height)
#
#
# def send_height(message):
#     chat_id = message.chat.id
#     height = message.text
#     if not height.isdigit():
#         msg = bot.reply_to(message, f'Вы уверены? Какой у вас рост?')
#         bot.register_next_step_handler(msg, send_height)
#         return
#     user = user_dict[chat_id]
#     self.height = height
#     msg = bot.reply_to(message, 'Какой ваш вес?')
#     bot.register_next_step_handler(msg, send_weight)
#
#
# def send_weight(message):
#     chat_id = message.chat.id
#     weight = message.text
#     if not weight.isdigit():
#         msg = bot.reply_to(message, 'Вы уверены? Какой ваш вес?')
#         bot.register_next_step_handler(msg, send_weight)
#         return
#     user = user_dict[chat_id]
#     self.weight = weight
#     bot.send_message(message.chat.id, 'Одну минуту. Сейчас я рассчитаю, есть ли у вас лишний вес. ')
#     bot.register_next_step_handler(msg, offer)
#
#
# # def calculation_of_weight(self, weight, height):
# #      self.normalWeight = self.height - 100 - (self.height - 150)/2
# #      self.excessWeight = self.normalWeight - self.weight
# #      group = 0
# #      answer = ''
# #      if self.excessWeight >= abs(3):
# #          group = 1
# #          answer = "Вы - Человек-Идеал. Вы в прекрасной форме. Занимайтесь спортом и не забывайте про здоровое питание"
# #      elif self.excessWeight <= 10:
# #          group = 2
# #          answer = "Вы - Слишком Стройная Газель. вам не надо беспокоиться по поводу веса, возможно вам стоит немного поправиться"
# #      elif self.excessWeight > 10:
# #          group = 3
# #          answer = "Вы - Человек Кожа-и-Кости. Обратитесь к врачу."
# #      elif self.excessWeight <= 10:
# #          group = 4
# #          answer = "Вы - Человек с Приятной Полнотой(пока еще). Стоит похудеть! "
# #      elif self.excessWeight <= 10:
# #          group = 5
# #          answer = "Вы - Очень Пышная Особа. Вы обратились по адресу, но предстоит долгий путь! "
# #      return answer
#
# def offer(message):
#     pass
#
# #     chat_id = message.chat.id
# #     weight = message.text
# #     if not weight.isdigit():
# #         msg = bot.reply_to(message, 'Вы уверены. Какой ваш вес?')
# #         bot.register_next_step_handler(msg, height_name)
# #         return
# #     user = user_dict[chat_id]
# #     user.weight = weight
# #     bot.send_message(message.chat.id, 'Одну минуту. Сейчас я рассчитаю, есть ли у вас лишний вес. ')
# #     bot.register_next_step_handler(msg, process_sex_step)
#
# bot.polling(none_stop=True)