from bot import telegram_chatbot
from insult import insultGenerator
import update_gembox
import datetime
import re
from dbhelper import DBHelper
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
            user = item["message"]["from"]["first_name"] 
            epoch = item["message"]["date"]
            date = datetime.datetime.fromtimestamp(epoch).strftime('%m-%d-%Y')
            gemresponse = "{}'s quote has been added to the Gembox Vault".format(user)
            chat_id = item["message"]["chat"]["id"]
            from_ = item["message"]["from"]["id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = str(item["edited_message"]["text"])
            deletestr = '@GemboxMiboss_bot delete'
            ifsofacto = 'ifsofacto'
            ifso_space = 'ifso facto'
            ifso = 'ifso'
            ifspace = 'if so'
            '''
            response = thing[message]
            If response:
            send(response)
            '''
            if message == '/welcome@GemboxMiboss_bot':
                bot.send_message("""Thanks for choosing Gembox_bot.  For a list of commands, type /commands and press Enter""", chat_id)
            elif message == '@GemboxMiboss_bot view' or message == '@GemboxMiboss_bot /view':
                try:
                    reply = read_only(message)
                    bot.send_message(reply, chat_id)
                except:
                    message = None
            elif message == '@GemboxMiboss_bot' or message == '@GemboxMiboss_bot hi' or message == '@GemboxMiboss_bot hello' or message == '@GemboxMiboss_bot yo' or message == 'hi @GemboxMiboss_bot' or message == 'Hi @GemboxMiboss_bot':
                bot.send_message(("Hello there {}").format(user), chat_id)
            elif message == '@GemboxMiboss_bot fuck you':
                bot.send_message("Fuck you too, scrub", chat_id)
            elif message == '@GemboxMiboss_bot what\'s my name?' or message == '@GemboxMiboss_bot what\'s my name':
                bot.send_message(("Usually your name is {}").format(user), chat_id)
            elif message == '@GemboxMiboss_bot gembox' or message == 'gembox' or message == 'Gembox' or message == '/gembox' or message == '/Gembox':
                try:
                    try:
                        msg = item["message"]["reply_to_message"]["text"]
                        add_and_reply(msg, user, date, gemresponse, chat_id, from_)
                    except:
                        bot.send_message("You must QUOTE or REPLY a message to add it to the Gembox Vault", chat_id)
                except Exception as e: bot.send_message(e, chat_id)
            elif deletestr in message:
                num = message[24:]
                update_gembox.gembox_delete(num, chat_id)
                reply = update_gembox.gembox_view()
                bot.send_message(reply, chat_id)
            elif message == '/vivaldi':
                reply = 'https://goo.gl/jUJ7R1'
                bot.send_message(reply, chat_id)
            elif message == '/commands@GemboxMiboss_bot' or message == '@GemboxMiboss_bot commands':
                update_gembox.gembox_commands(chat_id)
            elif re.findall(r"\b" + ifso + r"\b", message) or re.findall(r"\b" + ifsofacto + r"\b", message) or re.findall(r"\b" + ifso_space + r"\b", message) or re.findall(r"\b" + ifspace + r"\b", message): 
                bot.send_message("You spelled 'ipso' wrong", chat_id)
                bot.send_message('https://en.wikipedia.org/wiki/Ipso_facto', chat_id)
            elif '@GemboxMiboss_bot' in message:
                replyinsult = insult.getInsult()
                bot.send_message("There was no command request, so here's a random insult", chat_id)
                bot.send_message(replyinsult, chat_id)
