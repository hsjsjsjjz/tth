import requests
from telebot import types
import telebot
from time import sleep
from user_agent import generate_user_agent
token = ('1953118731:AAHRSqFjumgs6Y8z1FCThBZsyy3Za_bHgAM')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text=f"Hi {first},Send Email To rest 💡\n\nBy TTH",parse_mode="markdown")
@bot.message_handler(func=lambda m: True)
def Get(message):
    try:
        msg = message.text
        bot.send_message(message.chat.id, text="Wait Pro",)
        sleep(2)
        url = 'https://www.instagram.com/accounts/account_recovery_send_ajax/' 
 
        head = { 
            'accept':'*/*', 
            'accept-encoding':'gzip,deflate,br', 
            'accept-language':'en-US,en;q=0.9,ar;q=0.8', 
            'content-length':'269', 
            'content-type':'application/x-www-form-urlencoded', 
            'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-', 
            'origin':'https://www.instagram.com', 
            'referer':'https://www.instagram.com/', 
            'sec-fetch-dest':'empty', 
            'sec-fetch-mode':'cors', 
            'sec-fetch-site':'same-origin', 
            'user-agent': generate_user_agent(), 
            'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8', 
            'x-ig-app-id':'936619743392459', 
            'x-ig-www-claim':'0', 
            'x-instagram-ajax':'8a8118fa7d40', 
            'x-requested-with':'XMLHttpRequest', 
        } 
        
        data = { 
            'email_or_username': msg, 
            'recaptcha_challenge_field': '', 
            'flow': '', 
            'app_id': '', 
            'source_account_id': '', 
        } 
        
        
        rest = requests.post(url,headers=head,data=data).text 
        if '"Email Sent",' in rest: 
            bot.send_message(message.chat.id, text=f"*Done Sent Rest To! {msg}*",parse_mode="markdown")
        else:
            bot.send_message(message.chat.id, text=f"*done Sent Rest To! {msg}*",parse_mode="markdown")
    except:
        pass
bot.polling(True)
