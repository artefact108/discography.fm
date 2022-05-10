import telebot
import schedule
import requests
import googlesearch
from googlesearch import search
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import wikipedia
import random


bot = telebot.TeleBot('5340972805:AAHVEwLpSx94NTWoipYl3n3ZRdVLkfF994U')

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, меломан! Введите команду \lyrics [названиен песни и исполнителя], чтобы получить текст песни, \clips, чтобы получить ссылку на лучшие клипы исполнителя')



def find_discography(req):
  albums = []
  #url = wikipedia.page(req).url
  lang = 'ru'
  for url in search(req + ' группа клипы',1):
    albums.append(url)
    break

  return albums

@bot.message_handler(commands = ['clips'])
def ans(message):
    albums = find_discography(message.text)
    s = ''
    print(albums)
    j = 0
    for i in range (len(albums)):
        s = s + albums[i]
        s = s + '\n'
    print(s)
    bot.send_message(message.chat.id, s)

@bot.message_handler(commands = ['lyrics'])
def lyrics(message):
    albums = []
    for url in search(message.text + ' текст песни', 1):
        albums.append(url)
        break
    s = albums[0]
    bot.send_message(message.chat.id, s)



bot.polling()


