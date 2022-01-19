import os
import time  
import telebot  
from telebot import types 
import random

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY, parse_mode="Markdown")

markupSTART = types.ReplyKeyboardMarkup(row_width=3)
btn1 = types.KeyboardButton('Flip a Coin')
btn2 = types.KeyboardButton('Roll D-6')
btn3 = types.KeyboardButton('Roll D-10')
btn4 = types.KeyboardButton('Roll D-20')
btn5 = types.KeyboardButton('Roll D-n')
markupSTART.add(btn1, btn2, btn3, btn4, btn5)

markupRESTART = types.ReplyKeyboardMarkup()
butt1 = types.KeyboardButton('/restart')
markupRESTART.add(butt1)

markupCOIN = types.ReplyKeyboardMarkup(row_width = 2)
butt1 = types.KeyboardButton('Flip Again')
butt2 = types.KeyboardButton('/restart')
markupCOIN.add(butt1, butt2)

@bot.message_handler(func=lambda message: message.text.lower() == 'roll d-n' or message.text.lower() == 'roll d-n again')
def command_search(m):
    cid = m.chat.id
    bot.send_message(cid, "To roll: please send\n\n'Roll D-\[_number_]'", reply_markup=markupRESTART)

@bot.message_handler(func=lambda message: len(message.text) > 7 and message.text[:7].lower() == 'roll d-')
def command_search(m):
    cid = m.chat.id
    n = m.text[7:].strip()
    if n.isdigit() and int(n):
      n = int(n)
      markup = types.ReplyKeyboardMarkup(row_width = 2)
      button1 = types.KeyboardButton(f'Roll D-{n}')
      button2 = types.KeyboardButton('/restart')
      markup.add(button1, button2)
      bot.send_message(cid, f"The die has come up... *{random.randint(1,n)}*!", reply_markup=markup)
    else:
      bot.send_message(cid, "Invalid input!", reply_markup=markupRESTART)

@bot.message_handler(func=lambda message: message.text.lower() == 'flip a coin' or message.text.lower() == 'flip again')
def command_search(m):
    cid = m.chat.id
    result = random.randint(0,1)
    if result == 0:
      bot.send_message(cid, "It has been decided, *HEADS*", reply_markup=markupCOIN)
    else:
      bot.send_message(cid, "It has been decided, *TAILS*", reply_markup=markupCOIN)



@bot.message_handler(commands=['start', 'restart'])
def command_start(m):
    cid = m.chat.id
    bot.send_message(cid, "Let me make that decision for you", reply_markup=markupSTART)



bot.polling(none_stop=True)
while True: 
    time.sleep(300)