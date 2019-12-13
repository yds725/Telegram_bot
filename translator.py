from flask import Flask, render_template, request
import requests, random 
from decouple import config
from pprint import pprint

# "https://translation.googleapis.com/language/translate/v2"

url = "https://translation.googleapis.com/language/translate/v2"

key = config("GOOGLE_TOKEN")

data = {
    'q': '엄마 판다는 새끼가 있네',
    'source': 'ko',
    'target': 'en'
}

result = requests.post(f'{url}?key={key}', data) #post method


print(result.json())



# https://api.telegram.org/bot905758054:AAFHVuWpqPzlB69ynoIKIbfH1u2-tLbV68A/setWebhook?url=https://yds725.pythonanywhere.com/1030079990:AAHSKAY1cwk7D-3JrHm16BhR_vkxTznLqN0 https 

#http://yds725.pythonanywhere.com/