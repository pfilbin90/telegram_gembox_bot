from bot import telegram_chatbot
from dbhelper import DBHelper

db = DBHelper()
bot = telegram_chatbot("config.cfg")

def gembox_add(msg, user, date, gemresponse, chat_id, from_):
    db_entry = user + " on " + date + ": " + '"{}"'.format(msg)
    try:
        db.add_item(db_entry)
        items = db.get_items()
        quoted_message = "\n".join(items)
        bot.send_message(gemresponse, chat_id)
        bot.send_message(quoted_message, chat_id)
    except Exception as e: return(e)
    return quoted_message

def gembox_read_vault(message):
    try:
        # print("message: " + message) #print these lines for debugging
        # print("user: " + user)
        # print("date: " + date)
        # print("chat_id: " + str(chat_id))
        # print("from_: " + str(from_))

        items = db.get_items()
        counter_list = list(enumerate(items, 1))
        msg = '\n'.join([str(i) for i in counter_list])

    except Exception as e: return(e)
    return msg

def grab_description(num, chat_id):
    gembox_read_vault(message)
    