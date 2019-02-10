from bot import telegram_chatbot
from dbhelper import DBHelper

db = DBHelper()
bot = telegram_chatbot("config.cfg")

def gembox_add(msg, user, date, gemresponse, chat_id, from_):
    db_entry = user + " on " + date + ": " + '"{}"'.format(msg)
    try:
        db.add_item(db_entry)
        items = db.get_items()
        counter_list = list(enumerate(items, 1))
        output = '\n'.join([str(i) for i in counter_list])
        msg = output.replace('(', '').replace(')', '').replace("'", '')
        bot.send_message(gemresponse, chat_id)
        bot.send_message(msg, chat_id)
    except Exception as e: return(e)
    return msg

def gembox_view():
    try:
        items = db.get_items()
        counter_list = list(enumerate(items, 1))
        output = '\n'.join([str(i) for i in counter_list])
        msg = output.replace('(', '').replace(')', '').replace("'", '')

    except Exception as e: return(e)
    return msg

def gembox_delete(num, chat_id):
    reply = gembox_view()
    try:
        for line in reply.split("\n"):
            if line[0].isdigit():
                if str(num) == line[0]:
                    db.delete_item(line[0])
    except Exception as e: print(e)
    