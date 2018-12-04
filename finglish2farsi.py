import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
from config import TOKEN
from time import sleep
from finglish import f2p

def f2f(text):
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
        if content_type == 'text':
            if msg['text'] == '/start':
                bot.sendMessage(chat_id, '*WELCOME* 🙂\nI translate Finglish to Farsi', 'Markdown')
            else:
                bot.sendMessage(chat_id, f2f(msg['text']))

    elif chat_type in [u'group', u'supergroup']:
        if content_type == 'text':
            if msg['text'].lower() == '/f2f':
                try:
                    bot.sendMessage(chat_id, f2f(msg['reply_to_message']['text']))
                except KeyError:
                    bot.sendMessage(chat_id, '`/f2f` should reply to a message that you want to translate it', 'Markdown')


def on_inline_query(msg):
    query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
    articles = [InlineQueryResultArticle(
        id='f2f',
        title='Finglish 2 Farsi',
        input_message_content=InputTextMessageContent(
            message_text=f2f(query_string)
        )
    )]
    bot.answerInlineQuery(query_id, articles)


bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': handle,
                  'inline_query': on_inline_query}).run_as_thread()

# Keep the program running ...
while 1:
    sleep(10)
