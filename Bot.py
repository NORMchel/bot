import telebot
from telebot import types

bot = telebot.TeleBot(token='5409683463:AAGEoKBR3HTKEqDFaxttf1rQgZZRXzDJQ4o')

@bot.message_handler(commands=['start'])
def wellcome(message):
  markup = types.InlineKeyboardMarkup()
  button = types.InlineKeyboardButton(text='Поделиться', switch_inline_query='Текст, которым хочешь поделиться')
  markup.add(button)
  bot.send_message(message.chat.id, text='Кнопка поделиться', reply_markup=markup)

bot.polling()
