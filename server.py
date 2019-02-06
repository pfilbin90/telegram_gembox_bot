from bot import telegram_chatbot
import update_gembox
import datetime
bot = telegram_chatbot("config.cfg")
from dbhelper import DBHelper

db = DBHelper()

def add_and_reply(msg, user, date, gemresponse, chat_id, from_):
    reply = None
    if msg is not None:
        reply = update_gembox.gembox_add(msg, user, date, gemresponse, chat_id, from_)
    return reply

def read_only(message):
    reply = None
    if message is not None:
        reply = update_gembox.gembox_read_vault(message)
    return reply

update_id = None
while True:
    db.setup()
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            user = item["message"]["from"]["first_name"]
            epoch = item["message"]["date"]
            date = datetime.datetime.fromtimestamp(epoch).strftime('%m-%d-%Y %H:%M')
            gemresponse = "{}'s quote has been added to the Gembox Vault".format(user)
            chat_id = item["message"]["chat"]["id"]
            from_ = item["message"]["from"]["id"]
            message = str(item["message"]["text"])
            if message == '/view@GemboxMiboss_bot':
                try:
                    reply = read_only(message)
                    bot.send_message(reply, chat_id)
                except:
                    message = None
            if message == '/gembox@GemboxMiboss_bot':
                msg = item["message"]["reply_to_message"]["text"]
                try:
                    add_and_reply(msg, user, date, gemresponse, chat_id, from_)
                except:
                    print("add and reply failed")
            
                

            

"""
def make_reply(msg, quoted_message, user, date, gemresponse, groupid, from_):
    reply = None
    if msg is not None:
        update_gembox.gembox_bot(msg, quoted_message, user, date, gemresponse, groupid, from_)
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
                message = str(item["message"]["text"])
                quoted_message = str(item["message"]["reply_to_message"]["text"])
            except:
                raise KeyError
            user = item["message"]["from"]["first_name"]
            epoch = item["message"]["date"]
            date = datetime.datetime.fromtimestamp(epoch).strftime('%c')
            gemresponse = "{}'s quote has been added to the Gembox Vault".format(user)
            groupid = item["message"]["chat"]["id"]
            from_ = item["message"]["from"]["id"]

            reply = make_reply(message, quoted_message, user, date, gemresponse, groupid, from_) """