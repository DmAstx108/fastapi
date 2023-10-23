import telebot
import config
import client

# import pydantic_models
# import client
# import json


bot = telebot.TeleBot(config.bot_token)


@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    first_name = str(message.from_user.last_name)
    last_name = str(message.from_user.first_name)
    text = (f'👋Привет, {first_name} {last_name}.Я бот для проведения опросов!;'
            f'Ты здесь потому что хочешь пройти опрос?Тогда приступим!Нажми на кнопку "📝Пройти опрос" и начнем!')
    # создаем объект для работы с кнопками (row_width - определяет количество кнопок по ширине)
    markup = telebot.types.ReplyKeyboardMarkup(
        row_width=2, resize_keyboard=True)

    # создаем каждую кнопку таким образом
    btn1 = telebot.types.KeyboardButton('📝Пройти опрос')

    markup.add(btn1)

    # теперь добавляем объект с кнопками к отправляемому пользователю сообщению в аргумент "reply_markup"
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(regexp='📝Пройти опрос')
def choose_research(message):
    inline_markup = telebot.types.InlineKeyboardMarkup()
    text = f'✔️Пожалуйста, выбери желаемый опрос'

    btn1 = telebot.types.InlineKeyboardButton(
        text='Опрос 1', callback_data='research 1')
    btn2 = telebot.types.InlineKeyboardButton(
        text='Опрос 2', callback_data='research 2')
    btn3 = telebot.types.InlineKeyboardButton(
        text='Опрос 3', callback_data='research 3')

    inline_markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, text, reply_markup=inline_markup)

# @bot.message_handler(func=lambda message: message.from_user.id == config.tg_admin_id and message.text == "Все юзеры")
# def all_users(message):
#     text = f'Юзеры:'
#     users = client.get_users()
#     # создаем объект с инлайн-разметкой
#     inline_markup = telebot.types.InlineKeyboardMarkup()
#     for user in users:  # в цикле создаем 3 кнопки и добавляем их поочередно в нашу разметку
#         inline_markup.add(telebot.types.InlineKeyboardButton(text=f'Юзер: {user["tg_ID"]}',
#                                                              callback_data=f"user_{user['tg_ID']}"))
#         # в коллбеке у нас будет текст, который содержит айди юзеров
#     bot.send_message(message.chat.id, text,
#                      reply_markup=inline_markup)  # прикрепляем нашу разметку к ответному сообщению


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    questions = client.get_question_one()
    inline_markup = telebot.types.InlineKeyboardMarkup()
    if call.data == 'research 1':
        # call.message.answer('Вы выбрали Опрос №1!')
        for question in questions:
            text_message = f"Вопрос №1. {question['title']}"
            inline_markup.add(telebot.types.InlineKeyboardButton(text=f"1. {question['answer1']}", callback_data='question2'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"2. {question['answer2']}", callback_data='question2'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"3. {question['answer3']}", callback_data='question2'),
                              telebot.types.InlineKeyboardButton(text=f"4. {question['answer4']}", callback_data='question2'))

            bot.send_message(chat_id=call.from_user.id,
                             text=text_message, reply_markup=inline_markup)
            break

    elif call.data == 'question2':
        questions = client.get_question_two()
        inline_markup = telebot.types.InlineKeyboardMarkup()
        for question in questions:
            text_message = f"Вопрос №2. {question['title']}"
            inline_markup.add(telebot.types.InlineKeyboardButton(text=f"1. {question['answer1']}", callback_data='question3'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"2. {question['answer2']}", callback_data='question3'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"3. {question['answer3']}", callback_data='question3'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"4. {question['answer4']}", callback_data='question3'),
                              telebot.types.InlineKeyboardButton(text=f"5. {question['answer5']}", callback_data='question3'))

            bot.send_message(chat_id=call.from_user.id,
                             text=text_message, reply_markup=inline_markup)

            break

    elif call.data == 'question3':
        questions = client.get_question_three()
        inline_markup = telebot.types.InlineKeyboardMarkup()
        for question in questions:
            text_message = f"Вопрос №3. {question['title']}"
            inline_markup.add(telebot.types.InlineKeyboardButton(text=f"{question['answer1']}", callback_data='question4'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"{question['answer2']}", callback_data='question4'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"{question['answer3']}", callback_data='question4'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"{question['answer4']}", callback_data='question4'),
                              telebot.types.InlineKeyboardButton(text=f"{question['answer5']}", callback_data='question4'))

            bot.send_message(chat_id=call.from_user.id,
                             text=text_message, reply_markup=inline_markup)

            break

    elif call.data == 'question4':
        questions = client.get_question_four()
        inline_markup = telebot.types.InlineKeyboardMarkup()
        for question in questions:
            text_message = f"Вопрос №4. {question['title']}"
            inline_markup.add(telebot.types.InlineKeyboardButton(text=f"1. {question['answer1']}", callback_data='question5'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"1. {question['answer2']}", callback_data='question5'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"2. {question['answer3']}", callback_data='question5'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"3. {question['answer4']}", callback_data='question5'),
                              telebot.types.InlineKeyboardButton(text=f"4. {question['answer5']}", callback_data='question5'))

            bot.send_message(chat_id=call.from_user.id,
                             text=text_message, reply_markup=inline_markup)

            break

    elif call.data == 'question5':
        questions = client.get_question_five()
        inline_markup = telebot.types.InlineKeyboardMarkup()
        for question in questions:
            text_message = f"Вопрос №5. {question['title']}"
            inline_markup.add(telebot.types.InlineKeyboardButton(text=f"1. {question['answer1']}", callback_data='question6'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"2. {question['answer2']}", callback_data='question6'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"3. {question['answer3']}", callback_data='question6'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"4. {question['answer4']}", callback_data='question6'))

            bot.send_message(chat_id=call.from_user.id,
                             text=text_message, reply_markup=inline_markup)

            break

    elif call.data == 'question6':
        questions = client.get_question_six()
        inline_markup = telebot.types.InlineKeyboardMarkup()
        for question in questions:
            text_message = f"Вопрос №6. {question['title']}"
            inline_markup.add(telebot.types.InlineKeyboardButton(text=f"1. {question['answer1']}", callback_data='question7'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"2. {question['answer2']}", callback_data='question7'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"3. {question['answer3']}", callback_data='question7'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"4. {question['answer4']}", callback_data='question7'))

            bot.send_message(chat_id=call.from_user.id,
                             text=text_message, reply_markup=inline_markup)

            break

    elif call.data == 'question7':
        questions = client.get_question_seven()
        inline_markup = telebot.types.InlineKeyboardMarkup()
        for question in questions:
            text_message = f"Вопрос №7. {question['title']}"
            inline_markup.add(telebot.types.InlineKeyboardButton(text=f"1. {question['answer1']}", callback_data='question8'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"2. {question['answer2']}", callback_data='question8'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"3. {question['answer3']}", callback_data='question8'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"4. {question['answer4']}", callback_data='question8'))

            bot.send_message(chat_id=call.from_user.id,
                             text=text_message, reply_markup=inline_markup)

            break

    elif call.data == 'question8':
        questions = client.get_question_eight()
        inline_markup = telebot.types.InlineKeyboardMarkup()
        for question in questions:
            text_message = f"Вопрос №8. {question['title']}"
            inline_markup.add(telebot.types.InlineKeyboardButton(text=f"1. {question['answer1']}", callback_data='finish'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"2. {question['answer2']}", callback_data='finish'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"3. {question['answer3']}", callback_data='finish'),
                              telebot.types.InlineKeyboardButton(
                                  text=f"4. {question['answer4']}", callback_data='finish'),
                              telebot.types.InlineKeyboardButton(text=f"5. {question['answer5']}", callback_data='finish'))

            bot.send_message(chat_id=call.from_user.id,
                             text=text_message, reply_markup=inline_markup)

            break

    elif call.data == 'finish':
        inline_markup = telebot.types.InlineKeyboardMarkup()
        text_message = f"Опрос окончен!Спасибо за участие!"
        inline_markup.add(telebot.types.InlineKeyboardButton(
            text=f"Завершить опрос", callback_data='done'))

        bot.send_message(chat_id=call.from_user.id,
                         text=text_message, reply_markup=inline_markup)

    elif call.data == 'done':
        print(call)
        inline_markup = telebot.types.InlineKeyboardMarkup()
        text_message = f'✔️Пожалуйста, выбери желаемый опрос'

        btn1 = telebot.types.InlineKeyboardButton(
            text='Опрос 1', callback_data='research 1')
        btn2 = telebot.types.InlineKeyboardButton(
            text='Опрос 2', callback_data='research 2')
        btn3 = telebot.types.InlineKeyboardButton(
            text='Опрос 3', callback_data='research 3')

        inline_markup.add(btn1, btn2, btn3)

        bot.send_message(chat_id=call.from_user.id,
                         text=text_message, reply_markup=inline_markup)
# хендлер принимает объект Call

    # запускаем бота этой командой:
bot.infinity_polling(none_stop=True)
