import telebot

bot = telebot.TeleBot('6052351009:AAFpg6J7Jmiq2fSfA5xxwjEgXN-3beVn7AY')


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот. Введите /help для списка команд.')


@bot.message_handler(commands=['piu'])
def handle_piu(message):
    bot.send_message(message.chat.id, '~~~Тут тоже могло бы быть сообщение, но, опять нет~~~', parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def handle_link(message):
    bot.send_message(message.chat.id, 'На vds для маленьких бездомных ботов [ссылка](https://qiwi.com/n/IZ0RB)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, 'Список команд:\n'
                                      '/start - Начать\n'
                                      '/piu - Пиу-Пиу\n'
                                      '/link - Получить ссылку\n'
                                      '/help - Справка')


@bot.message_handler(commands=['info'])
def handle_info(message):
    bot.send_message(message.chat.id, 'Этот бот создан для демонстрации обработки команд. Веселитесь!')


bot.infinity_polling()
