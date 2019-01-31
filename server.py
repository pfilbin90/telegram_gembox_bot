from bot import telegram_chatbot
import update_gembox
import datetime
bot = telegram_chatbot("config.cfg")
from dbhelper import DBHelper

db = DBHelper()

def make_reply(msg, quoted_message, user, date, gemresponse, groupid, from_):
    reply = None
    if msg is not None and "/gembox add" in msg:
        reply = update_gembox.add_to_gembox(msg, quoted_message, user, date, gemresponse, groupid, from_)
    elif msg is not None and "/gembox read" in msg:
        reply = print("WHY ISNT WORKING")
        #reply = update_gembox.read_from_gembox(msg, quoted_message, user, date, gemresponse, groupid, from_)

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
                message = None
                quoted_message = None
            user = item["message"]["from"]["first_name"]
            epoch = item["message"]["date"]
            date = datetime.datetime.fromtimestamp(epoch).strftime('%c')
            gemresponse = "{}'s quote has been added to the Gembox Vault".format(user)
            groupid = item["message"]["chat"]["id"]
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message, quoted_message, user, date, gemresponse, groupid, from_)