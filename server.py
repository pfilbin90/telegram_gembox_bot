from bot import telegram_chatbot
from insult import insultGenerator
import update_gembox
import datetime
import re
from dbhelper import DBHelper
from big_dict import hello_dict

bot = telegram_chatbot("config.cfg")
insult = insultGenerator()


db = DBHelper()

def add_and_reply(msg, user, date, gemresponse, chat_id, from_):
    reply = None
    if msg is not None:
        reply = update_gembox.gembox_add(msg, user, date, gemresponse, chat_id, from_)
    return reply

def read_only(message):
    reply = None
    if message is not None:
        reply = update_gembox.gembox_view()
    return reply

update_id = None
while True:
    db.setup()
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:    
                user = item["message"]["from"]["first_name"]
            except:
                continue
            try: 
                message = str(item["message"]["text"])
            except:
                message = str(item['edited_message']['text'])
            epoch = item["message"]["date"]
            date = datetime.datetime.fromtimestamp(epoch).strftime('%m-%d-%Y')
            gemresponse = "{}'s quote has been added to the Gembox Vault".format(user)
            chat_id = item["message"]["chat"]["id"]
            try:
                quote_user= item["message"]["reply_to_message"]["from"]["first_name"]
            except:
                continue
            for key in hello_dict:
                if message.lower() == key.lower():
                    print(hello_dict[key])
