import requests
from decouple import config 


url = "https://api.telegram.org"
token = config("TELEGRAM_BOT_TOKEN")
chat_id = config("CHAT_ID")

#token_api = "905758054:AAFHVuWpqPzlB69ynoIKIbfH1u2-tLbV68A"
#chat_id = "709075583"

#chat_id = requests.get(f"{url}/bot{token_api}/getUpdates").json()["result"][""]

text = input("메세지 입력: ")

send_message = requests.get(f"{url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}")

print(send_message.text)


