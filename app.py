from flask import Flask, render_template, request
import requests, random, html
from decouple import config
from pprint import pprint


# import flask
# import
app = Flask(__name__)

#https://api.telegram.org/bot905758054:AAFHVuWpqPzlB69ynoIKIbfH1u2-tLbV68A/setWebhook?url=https://bdabb82e.ngrok.io/



#https://api.telegram.org/bot905758054:AAFHVuWpqPzlB69ynoIKIbfH1u2-tLbV68A/METHOD_NAME

#url = "https://api.telegram.org/bot905758054:AAFHVuWpqPzlB69ynoIKIbfH1u2-tLbV68A/getMe"

url = "https://api.telegram.org"
token = config("TELEGRAM_BOT_TOKEN")
chat_id = config("CHAT_ID")
key = config("GOOGLE_TOKEN")

google_url = "https://translation.googleapis.com/language/translate/v2"

# 사용자의 id 값 찾기 

# 나의 챗 아이디 (chat id)
# 709075583
# sendMessage
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/write')
def write():
    return render_template("write.html")

@app.route('/send')
def send():
    #1. 사용자가 입력한 데이터 받기
    data = request.args.get("message")
    print(data)
    #2. 텔레그램 api 메시지 전송 요청 보내기
    send_message = requests.get(f"{url}/bot{token}/sendMessage?chat_id={chat_id}&text={data}")

    return 'Msg sent!'

# flask 서버는 현재 로컬환경에서 개발용 서버로 작동. 그래서 텔레그램 측에 웹훅을 적용하기 위해 주솔ㄹ 알려주더라도 텔레그램 측에서 우리 서버 주소로 접근을 할 수 없다> (사내 인트라넷 글 올려놓고 부모님께 접속해보라고 링크 던져줌 과 마찬가지>?)
# 이를 해결하기 위해 로컬 서버 주소를 임시로 퍼블릭하게 열어주는 툴인 엔그록 (ngrok) 사용.

@app.route(f'/{token}', methods = ['POST'])
def telegram():
    # 1. 메아리 기능
    pprint(request.get_json())
    # 2. user id // msg 
    chat_id = request.get_json().get('message').get('from').get('id')
    message = request.get_json().get('message').get('text')
    # 3 . 텔릭램 api 요청해서 답장 보내주기
    # requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={message}')

    # 사용자가 로또 입력하면 로또 번호 6개 만ㄷㄹ기
    if message == '로또':
        
        result = [random.randint(1,40) for _ in range(6)]
        # for i in range(6):
        #     result = random.randint(1, 40)
        # requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={result}')
    elif message[:4] == '/번역 ':

        translate_data = {
            'q': message[4:],
            'source': 'ko',
            'target': 'en'
        }

        response = requests.post(f'{google_url}?key={key}', translate_data).json()
        
        # result = response.get('data').get('translations')[0].get('translatedText')

        result = html.unescape(response.get('data').get('translations')[0].get('translatedText'))

    else:
        result = message

        # requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={message}')
    
    requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={result}')
    return '', 200

# 반드시 파일 최하단에 위치시킬 것!
if __name__ == '__main__':
    # 파일실행 간편하게
    app.run(debug=True)