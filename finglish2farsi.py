import telepot
from telepot.loop import MessageLoop
from config import TOKEN
from time import sleep
from finglish import f2p

def f2f(text) :
    std_text = ''
    for char in text:
        if(not char.isalpha()):
            std_text += ' %c '%char
        else:
            std_text += char

    farsi_text = ''
    for word in std_text.split():
        farsi_text += ' ' + f2p(word)

    return farsi_text


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_type == u'private':
        if content_type == 'text' :
            if msg['text'] == '/start' :
                bot.sendMessage(chat_id, '*WELCOME* 🙂\nI translate Finglish to Farsi', parse_mode='Markdown')
            else:
                bot.sendMessage(chat_id, f2f(msg['text']))


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

# Keep the program running ...
while 1:
    sleep(10)
