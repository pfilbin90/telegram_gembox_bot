from bot import telegram_chatbot
from dbhelper import DBHelper

db = DBHelper()
bot = telegram_chatbot("config.cfg")

def add_to_gembox(message, quoted_message, user, date, gemresponse, groupid, from_):
    db_entry = user + " on " + date + ": " + '"{}"'.format(quoted_message))
    items = db.get_items()
    try:
        db.add_items(db_entry)
        items = db.get_items()
        msg = "\n".join(items)
        bot.send_message(gemresponse, groupid)
        bot.send_message(msg, groupid)
    except KeyError:
        pass



""" def add_to_gembox(message, quoted_message, user, date, gemresponse, groupid, from_):
    file = "/Users/peter.filbin/Desktop/quotes.txt"
    with open(file, "a+") as f:
        f.write("\n" + user + " on " + date + ": " + '"{}"'.format(quoted_message))
    bot.send_message(gemresponse, groupid)
    response = ("To view all gemboxes, type /gembox read")
    bot.send_message(response, groupid)
    return response
    
def read_from_gembox(message, quoted_message, user, date, gemresponse, groupid, from_):
    file = "/Users/peter.filbin/Desktop/quotes.txt"
    with open(file, "rt") as f:
        read_data = f.read()
    bot.send_message(read_data, groupid)
    return read_data """