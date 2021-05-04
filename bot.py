import telebot
from decouple import config

TELEGRAM_API_KEY = config('TELEGRAM_API_KEY')


bot = telebot.TeleBot(TELEGRAM_API_KEY)


@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
    if message.text == "Привет": 
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.") 
    elif message.text == "/help": 
        bot.send_message(message.from_user.id, "Напиши Привет") 
    else: 
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.message_handler(content_types=['document', 'audio', 'photo'])
def get_img(message):
    bot.send_message(message.from_user.id, "вот это да... ты отправил мне картинку =/ ")
    
    fileID = message.photo[-1].file_id
    
    file_info = bot.get_file(fileID)
    
    downloaded_file = bot.download_file(file_info.file_path)

    with open("img/ "+ fileID +".jpg", 'wb') as new_file:
        new_file.write(downloaded_file)


bot.polling(none_stop=True, interval=0)
