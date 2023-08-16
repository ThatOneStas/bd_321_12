import telebot

from telebot import types
import requests


bot = telebot.TeleBot("6433719050:AAE6tnR7jOSBza4uelfvAW5JTYmQW-GiAk8")

print('_____ START BOT _____')

counters = {
    "menu": 0,
    "admins": [6269605642],
    "admin": False
}
users = {}
#admins = [6269605642]

def total_price(cid):
    baseURL = "https://fakestoreapi.com"
    if __name__ == "__main__":
        response = requests.get(f"{baseURL}/products")
        data = response.json()
        total_price = 0
        for i in data:
            total_price += i['price']
        bot.send_message(cid, total_price, reply_markup=second_reply_menu())

### REPLY KEYBOARD

def main_reply_menu(cid):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton('💡Ask me'), types.KeyboardButton('💧Btn 2'), types.KeyboardButton('🔥Btn 3'))
    markup.row(types.KeyboardButton('InlineMenu'))
    markup.row(types.KeyboardButton('/start'), types.KeyboardButton('/update'))
    if cid in counters['admins']:
        markup.row(types.KeyboardButton('Admin'))
        counters["admin"] = True

        print(counters["admin"])

    return markup

def second_reply_menu():
    markup_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_2.row(types.KeyboardButton('Price'), types.KeyboardButton('Btn2'), types.KeyboardButton('Btn3'))
    markup_2.row(types.KeyboardButton('Btn4'), types.KeyboardButton('Btn5'))
    markup_2.row(types.KeyboardButton('back'), types.KeyboardButton('next'))
    return markup_2

def third_reply_menu():
    markup_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_3.row(types.KeyboardButton('Btn6'), types.KeyboardButton('Btn7'), types.KeyboardButton('Btn8'))
    markup_3.row(types.KeyboardButton('back'), types.KeyboardButton('main'), types.KeyboardButton('next'))
    return markup_3

def fourth_reply_menu():
    markup_4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_4.row(types.KeyboardButton('Btn9'), types.KeyboardButton('Btn10'))
    markup_4.row(types.KeyboardButton('back'), types.KeyboardButton('main'))
    return markup_4

### INLINE MENU

def get_user_name(msg):
    cid = msg.chat.id
    txt = msg.text
    users[f'{cid}'] = {}
    users[f'{cid}']['name'] = txt
    mess = bot.send_message(cid, 'Input your age: ')
    bot.register_next_step_handler(mess, get_user_age)

def get_user_age(msg):
    cid = msg.chat.id
    txt = msg.text
    users[f"{cid}"]["age"] = txt
    msg_text = f'Name: {users[f"{cid}"]["name"]} \n' \
               f'Age: {users[f"{cid}"]["age"]}'
    bot.send_message(cid, msg_text, reply_markup=main_reply_menu(cid))


@bot.message_handler(commands=['admin'])
def admins(msg):
    cid = msg.chat.id
    if cid in admins:
        bot.send_message(cid, "Hello admin!")
    else:
        bot.send_message(cid, "Not allowed")

@bot.message_handler(commands=['start'])
def send_welcome(msg):
    cid = msg.chat.id
    temp_text = '<u>Test</u>'
    bot.send_message(cid, temp_text, reply_markup=main_reply_menu(cid), parse_mode='html')
    print(msg.chat.id)

@bot.message_handler(commands=['update'])
def some_msg(msg):
    bot.reply_to(msg, "Update✅", reply_markup=main_reply_menu(cid), parse_mode='html')

@bot.message_handler(func=lambda message: True)
def echo_all(msg):
    cid = msg.chat.id

    if msg.text == '💧Btn 2' and counters['menu'] == 0:
        bot.send_message(cid, 'Done✅', reply_markup=second_reply_menu())
        counters['menu'] += 1
    elif msg.text == 'next' and counters['menu'] == 1:
        bot.send_message(cid, 'Done✅', reply_markup=third_reply_menu())
        counters['menu'] += 1
    elif msg.text == 'next' and counters['menu'] == 2:
        bot.send_message(cid, "Done✅", reply_markup=fourth_reply_menu())
        counters['menu'] += 1

    elif msg.text == 'main':
        bot.send_message(cid, "Returned to main✅", reply_markup=main_reply_menu(cid))
        counters['menu'] -= counters['menu']
    elif msg.text == 'back' and counters['menu'] == 1:
        bot.send_message(cid, "Returned back✅", reply_markup=main_reply_menu(cid))
        counters['menu'] -= counters['menu']
    elif msg.text == 'back' and counters['menu'] == 2:
        bot.send_message(cid, "Returned back✅", reply_markup=second_reply_menu())
        counters['menu'] -= 1
    elif msg.text == 'back' and counters['menu'] == 3:
        bot.send_message(cid, "Returned back✅", reply_markup=third_reply_menu())
        counters['menu'] -= 1
    elif msg.text == '💡Ask me':
        mess = bot.send_message(cid, 'Input your name: ')
        bot.register_next_step_handler(mess, get_user_name)
    elif msg.text == 'Price':
        total_price(cid)
    elif msg.text == 'Admin':
        if counters["admin"] == True:
            bot.send_message(cid, 'Welcome Admin!', reply_markup=main_reply_menu(cid))
        else:
            bot.send_message(cid, 'Error 418', reply_markup=main_reply_menu(cid))

bot.infinity_polling()