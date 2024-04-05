# from pytube import YouTube

# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download()
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
# Download(link)
from datetime import timedelta
from telebot import TeleBot
from telebot import *
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup


from pytube import YouTube
import requests
from bs4 import BeautifulSoup

video = YouTube('https://www.youtu.be/k3CLd-Zc3r0?si=dzeQcGGsgcC5DtXy')

bot = TeleBot(token = 'token')

first_markup = InlineKeyboardMarkup(row_width=2)
button1 = InlineKeyboardButton(text='240',callback_data='q-240')
button2 = InlineKeyboardButton(text='320',callback_data='q-320')
button3 = InlineKeyboardButton(text='480',callback_data='q-480')
button4 = InlineKeyboardButton(text='720',callback_data='q-720')
button5 = InlineKeyboardButton(text='1080',callback_data='q-1080')
first_markup.add(button1,button2,button3,button4,button5)


@bot.message_handler(commands=['start'])
def starting(message):
    bot.send_message(message.chat.id,"Hi send me youtube link !")


@bot.message_handler()
def keyboard(message):
    if 'https' in message.text:
        #recieve link
        bot.send_message(message.chat.id,"Choose your quality",reply_markup=first_markup)         
    else:
        bot.send_message(message.chat.id,"It's not a link") 





@bot.callback_query_handler(func = lambda call: call.data=='q-240')
def download_240(call):
    video.streams.filter(res='240').first().download()



# try:
#     print('Title: ',video.title)
#     print('Author: ',video.author)
#     video_length = video.length
#     print('Lenght: ',(str(timedelta(seconds=video_length))))

# except:
#     print('ummm')

