import telebot

import firstFeature
import secondFeature
import thirdFeature


ERROR_MSG = """Воспользуйтесь следующими командами:
               1 или /text <Ваша строка> - преобразовать текст в консольную графику
               2 или /calculate <Ваше выражение> - калькулятор математических выражений с неограниченной вложенностью скобок
               3 или /weather <Название города> - отображение погоды в запрошенном городе"""

bot = telebot.TeleBot('1851423450:AAFLMOobcFsuar0ZiPqYd8xlyqPhVMdBalw')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        command, text = message.text[:message.text.index(" ")],message.text[message.text.index(" ")+1:]
    except Exception:
        bot.send_message(message.from_user.id, ERROR_MSG)
        return
    if command in ["1", "/text"]:
        for msg in firstFeature.transformLongString(text):
            bot.send_message(message.from_user.id, msg)
    elif command in ["2", "/calculate"]:
        msg = secondFeature.calculate(text)
        bot.send_message(message.from_user.id, msg)
    elif command in ["3", "/weather"]:
        msg = thirdFeature.getWeatherStr(text)
        bot.send_message(message.from_user.id, msg)
    else:
        bot.send_message(message.from_user.id, ERROR_MSG)




bot.polling(none_stop=True, interval=0)