#testing the bot api
import telegram
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

def check_spam(response):
    pass           #model goes here



def start(bot,update):    #start message
    try:
        chat_id = update.message.chat_id
        username=update.message.from_user.first_name
        bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
        bot.send_message(chat_id=chat_id, text="Hai.. "+username+"\n\n I'm a Spam Detection bot. Send me any text and I will verify it for spam.")
    except Exception as e:
        print("Error!: ",str(e))    


def not_command(bot,update):   
    chat_id =update.message.chat_id
    response=update.message.text
    print(response)
    res=check_spam(response)
    print(res)
    bot.send_message(chat_id=chat_id,text=res)


def main():
    TOKEN = "" #unique id
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    text_message_handler=MessageHandler(Filters.text,not_command)
    dp.add_handler(text_message_handler)
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('name',name))
  
    updater.start_polling(clean=True)
    updater.idle()

if __name__ == '__main__':
    main()
