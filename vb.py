#!/usr/bin/python3.6
import telebot
import requests
import json



api = '1728080936:AAEudp9G6J0ZCkAUensva_MML9erHI18IV4'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def action_start(message):
  first_name = message.chat.first_name
  last_name = message.chat.last_name
  bot.reply_to(message, 'Hi, apa kabar {} {}?'.format(first_name,last_name))

@bot.message_handler(commands=['covid'])
def covid(message):
   texts = message.text
   provinsi = texts[7:]
   page = requests.get('https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
   page_json = page.json()
   features = page_json['features']
   for i in features: 
      prov = i['attributes']['Provinsi'] 
      pos =  i['attributes']['Kasus_Posi'] 
      sem = i['attributes']['Kasus_Semb'] 
      men = i['attributes']['Kasus_Meni'] 
      dirawat = int(pos)-int(sem)-int(men) 
      data = ('''
Provinsi = {}
Positif = {}
Sembuh = {}
Meninggal= {}
Dirawat = {}
'''.format(prov, pos, sem, men, dirawat))
      if provinsi.upper() in prov.upper():
         bot.reply_to(message, data)
      else:
         pass

@bot.message_handler(regexp='halo')
def text(message):
  bot.reply_to(message,'halo apa kabar?')
  
@bot.message_handler(regexp='ngentot')
def text(message):
  bot.reply_to(message,'gas kak')


@bot.message_handler(regexp='tidur')
def text(message):
  bot.reply_to(message,'oke kak aku tidur')

@bot.message_handler(regexp='brb')
def text(message):
  bot.reply_to(message,'selamat tinggal {}')

@bot.message_handler(regexp='fambest')
def text(message):
  bot.reply_to(message,'maaf ini cuma bot')

@bot.message_handler(regexp='cp')
def text(message):
  bot.reply_to(message,'cpan dosa kak ^^')


@bot.message_handler(regexp='tolol')
def text(message):
  bot.reply_to(message,'siapa yang tolol kak?')

@bot.message_handler(regexp='yo')
def text(message):
  bot.reply_to(message,'Yo')
  
@bot.message_handler(regexp='hai bot')
def text(message):
  bot.reply_to(message,'halo aku adalah bot untuk bersenang senang')
  
@bot.message_handler(regexp='sange')
def text(message):
  bot.reply_to(message,'tobat kak')


@bot.message_handler(regexp='hai')
def text(message):
  bot.reply_to(message,'hai juga')
  

@bot.message_handler(regexp='i love you')
def text(message):
  bot.reply_to(message,'too baby')
  

@bot.message_handler(regexp='makan')
def text(message):
  bot.reply_to(message,'aku udah makan')

@bot.message_handler(commands=['support'])
def action_support(message):
  first_name = message.chat.first_name
  last_name = message.chat.last_name
  bot.reply_to(message, '{} {} untuk support bisa ke @vohaunion'.format(first_name,last_name))
  
@bot.message_handler(commands=['afk'])
def action_afk(message):
  first_name = message.chat.first_name
  last_name = message.chat.last_name
  bot.reply_to(message, 'selamat tinggal {} {}'.format(first_name,last_name))

@bot.message_handler(commands=['unafk'])
def action_afk(message):
  first_name = message.chat.first_name
  last_name = message.chat.last_name
  bot.reply_to(message, 'selamat datang {} {}'.format(first_name,last_name))

@bot.message_handler(commands=['profile'])
def action_profile(message):
  first_name = message.chat.first_name
  last_name = message.chat.last_name
  bot.reply_to(message, '''
Hi {} {}, ini list command yaa
/usn -> melihat username kamu (masih tahap pembuatan)
/id -> Cek id Kamu
'''.format(first_name,last_name))


@bot.message_handler(commands=['id'])
def action_id(message):
  first_name = message.chat.first_name
  last_name = message.chat.last_name
  id_telegram = message.chat.id
  bot.reply_to(message, '''
Hi, ini ID Telegram kamu
Nama = {} {}
ID = {}
'''.format(first_name,last_name, id_telegram))

@bot.message_handler(commands=['usn'])
def action_username(message):
  first_name = message.chat.first_name
  last_name = message.chat.last_name
  username_telegram = message.chat.username
  bot.reply_to(message, '''
Hi, ini usn Telegram kamu
Nama = {} {}
usn = {}
'''.format(first_name,last_name, username_telegram))



@bot.message_handler(commands=['help'])
def action_help(message):
  first_name = message.chat.first_name
  last_name = message.chat.last_name
  bot.reply_to(message, '''
Hi {} {}, ini list command yaa
/start -> Sapa Bot dulu kak
/profile -> Cek profil Kamu
/help -> List Command Bot
/covid  ->  untuk melihat data covid (untuk sekarang masih soon)
'''.format(first_name,last_name))


print('bot running')
bot.polling()