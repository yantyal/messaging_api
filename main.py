import json
import random

from linebot import LineBotApi
from linebot.models import TextSendMessage

info = dict()
with open('info.json', 'r') as file:
    info = json.load(file)
CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


def main():
    USER_ID = info['USER_ID']
    data = dict()
    with open('english.json', mode='rt', encoding='utf-8') as file:
        data = json.load(file)
    item = random.choice(data['items'])
    messages = TextSendMessage(text= item['sentence'])
    line_bot_api.push_message(USER_ID, messages=messages)

if __name__ == "__main__":
    main()
