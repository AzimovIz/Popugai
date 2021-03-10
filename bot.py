import telebot
bot = telebot.TeleBot('TOKEN')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    msg = message.text()
    aut = message.author()


bot.polling(none_stop=True)