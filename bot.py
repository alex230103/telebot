import telebot
from decouple import config
import requests
from telebot import types
import os

path = os.getcwd()


TELEGRAM_API_KEY = config('TELEGRAM_API_KEY')


bot = telebot.TeleBot(TELEGRAM_API_KEY)




@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 

    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Создать папку')
    markup.add(itembtn1)
    msg = bot.reply_to(message, 'Выберите действие', reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)



def process_step (message):
    chat_id = message.chat.id
    if message.text=='Создать папку':
         msg = bot.reply_to(message, 'Узажите имя папки')
         bot.register_next_step_handler(msg, create_folder)
    else:
        print (2)


def create_folder (message):
    import os
    directory = path + '/img/' + message.text
    if not os.path.exists(directory):
        os.makedirs(directory)
    


@bot.message_handler(content_types=['photo'])
def get_img(message):
    bot.send_message(message.from_user.id, "вот это да... ты отправил мне картинку =/ ")
        
    fileID = message.photo[-1].file_id
    
    file_info = bot.get_file(fileID)
    
    downloaded_file = bot.download_file(file_info.file_path)

    with open("img/ "+ fileID +".jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    s = requests.Session()
    s.get('https://api.telegram.org/bot{0}/deletemessage?message_id={1}&chat_id={2}'.format(TELEGRAM_API_KEY, message.message_id, message.chat.id))


@bot.message_handler(content_types=['document'])
def get_img(message):
    

    
    
    
    fileID = message.document.file_id
    
    file_info = bot.get_file(fileID)
    
    downloaded_file = bot.download_file(file_info.file_path)

    with open("img/ "+ fileID +".jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    #bot.send_message(message.from_user.id, "вот это да... ты отправил мне документ =/ ")

    s = requests.Session()
    s.get('https://api.telegram.org/bot{0}/deletemessage?message_id={1}&chat_id={2}'.format(TELEGRAM_API_KEY, message.message_id, message.chat.id))


bot.polling(none_stop=True, interval=0)
