from pytubefix import YouTube
from datetime import timedelta
from telebot import TeleBot
from telebot import *
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup


bot = TeleBot(token = 'your token')

first_markup = InlineKeyboardMarkup(row_width=3)
button1 = InlineKeyboardButton(text='240',callback_data='q-360')
button2 = InlineKeyboardButton(text='320',callback_data='720')
button3 = InlineKeyboardButton(text='480',callback_data='1080')
first_markup.add(button1,button2,button3)


@bot.message_handler(commands=['start'])
def starting(message):
    bot.send_message(message.chat.id,"Hi there.. send me any youtube link !")



@bot.message_handler(func = lambda message : True)
def handler_text(message):

    global usr_link
    usr_link = YouTube(message.text)    
    v_title  = usr_link.title
    v_author = usr_link.author
    v_length = usr_link.length
    v_length = (str(timedelta(seconds = v_length)))
    # v_des = usr_link.description
    v_tumb = usr_link.thumbnail_url
    bot.send_message(message.chat.id,"Your Link Information:\n\n|Title| --> {0}\n|Author| --> {1}\n|Length| --> {2}\n|Tumbnail| --> {3}".format(v_title,v_author,v_length,v_tumb),reply_markup=first_markup)



@bot.callback_query_handler(func = lambda call:call.data=="q-360")
def download_360(call):

    usr_video = usr_link.streams.filter(res="360p").first()
    usr_video.download('toto-utube-downloader-master/videos')


@bot.callback_query_handler(func = lambda call:call.data=="q-720")
def download_720(call):

    usr_video = usr_link.streams.filter(res="720p").first()
    usr_video.download('toto-utube-downloader-master/videos')


@bot.callback_query_handler(func = lambda call:call.data=="q-1080")
def download_1080(call):

    usr_video = usr_link.streams.filter(res="1080p").first()
    usr_video.download('toto-utube-downloader-master/videos')



bot.infinity_polling()
