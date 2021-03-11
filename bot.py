import telebot
import vk_api #импорт основного модуля
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType #импорт longpoll и типа ивента
import threading
bott = telebot.TeleBot('1578726351:AAGnwYTAUfiPZapoBJSsXaq83nipzSzrIlI')

vk = vk_api.VkApi(token = '2d92a30dc044df0e72f7ad298ef7b4b6097e765ff2b37866508d8e6c62e3c0fceb72d35585c28d5100b5b') #токен группы
session = vk.get_api()
longpoll = VkBotLongPoll(vk, group_id='203184619')

def sender(text):
    vk.method('messages.send', {'peer_id': 2000000001, 'message': text, 'random_id': 0})

@bott.message_handler(content_types=['text'])
def get_text_messages(message):
    msg = message.text
    aut = str(message.from_user.first_name)
    print(f'{aut}: {msg}')
    sender(f'{aut}: {msg}')

bott.polling(none_stop=True)