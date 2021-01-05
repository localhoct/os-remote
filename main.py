import telebot
from telebot import types
import os
import random
from PIL import ImageGrab
from winsound import Beep
import requests
import platform
import psutil
import time

# proxy = 'http://192.168.88.170:8888'
# os.environ['http_proxy'] = proxy
# os.environ['HTTP_PROXY'] = proxy
# os.environ['https_proxy'] = proxy
# os.environ['HTTPS_PROXY'] = proxy

start_time = time.time()
os.system("cls")

token = 'Your Token Here ;) ' #str
bot = telebot.TeleBot(token)
admin = 440904809 # here Enter Your Telegram UserId (int)

bot.send_message(admin, 'سیستم روشن شد!')


def getfile(filename):
    myfile = open(filename, "r+", encoding='utf-8')
    return myfile.read()


def putfile(filename, filedata):
    myfile = open(filename, "w+", encoding='utf-8')
    myfile.write(filedata)
    myfile.close()


def startcm(user):
    chat_id = user.from_user.id
    btns = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('ScreenShot📸')
    btn2 = types.KeyboardButton('Power Option ⚠️')
    btn3 = types.KeyboardButton('Sound🔉')
    btn4 = types.KeyboardButton('File Manager🗄')
    btn5 = types.KeyboardButton('System Info💻')
    btn6 = types.KeyboardButton('Open Web🌍')
    btns.add(btn1, btn2, btn3, btn4, btn5, btn6)
    message = '''
    سلام خوش آمدید.😄

لیست دستورات برای فقط شماست😜
    '''
    bot.send_message(chat_id, message, reply_markup=btns)
    # print(id)


def savedb(user):
    chat_id = user.from_user.id
    text = user.text
    con_text = text.replace('/save ', '')
    # con_text = con_text.encode("utf-8")
    mesid = random.randint(1111, 9999)
    message = f'پیام شما: \n {con_text} \n شناسه پیام : {mesid}'
    bot.send_message(chat_id, message)
    putfile(f'database/data_{mesid}.txt', str(con_text))
    # print(con_text, mesid)


def savedb_lsit(user):
    chat_id = user.from_user.id
    list_file = ''
    for r, d, f in os.walk('database'):
        for file in f:
            list_file = list_file + '\n' + str(file)
    bot.send_message(chat_id, 'پیام های شما: \n' + str(list_file))


def power(user):
    chat_id = user.from_user.id
    # text = user.text
    btns = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton('ShoutDown | خاموش کردن')
    btn2 = types.KeyboardButton('ریستارت | Restart')
    btn3 = types.KeyboardButton('بازگشت')
    btns.add(btn1, btn2, btn3, )
    bot.send_message(chat_id, 'شما به بخش power option وارد شدید.لیست دستورات: \n', reply_markup=btns)


def home(user):
    chat_id = user.from_user.id
    btns = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('ScreenShot📸')
    btn2 = types.KeyboardButton('Power Option ⚠️')
    btn3 = types.KeyboardButton('Sound🔉')
    btn4 = types.KeyboardButton('File Manager🗄')
    btn5 = types.KeyboardButton('System Info💻')
    btn6 = types.KeyboardButton('Open Web🌍')
    btns.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(chat_id, '🏛صفحه اصلی: ', reply_markup=btns)


def playmusic_btn(user):
    chat_id = user.from_user.id
    btns = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Music 🎧')
    btn2 = types.KeyboardButton('Beep')
    btn3 = types.KeyboardButton('بازگشت')
    btns.add(btn1, btn2, btn3)
    message = '''
    🤔لطفا نوع صدا را انتخاب کنید
    '''
    bot.send_message(chat_id, message, reply_markup=btns)


def bep(user):
    chat_id = user.from_user.id
    bot.send_message(chat_id, 'بوق پخش شد😉')
    for x in range(1, 6):
        Beep(1000 * x, 200)
        Beep(1000 * x, 200 - (x * 50))


def music(user):
    chat_id = user.from_user.id
    message = '''
    لطفا آهنگ خود را بفرستید تا برایتان پخش کنم!😊

    یا از دستور زیر استفاده کنید👇:

    /music [File_id]

    برای دریافت آیدی ها دستور زیر را بزنید👇:

    /music_list
    '''
    bot.send_message(chat_id, message)


def music_id(user):
    chat_id = user.from_user.id
    list_file = ''
    music_count = 0
    for r, d, f in os.walk('music'):
        for file in f:
            if 'mp3' in file:
                music_count += 1
                list_file = list_file + '\n' + str(file)
            else:
                pass
    message = f'''
    تعداد آهنگ ها:{music_count}
لیست آهنگ های ذخیره شده:
    {list_file}
    '''
    bot.send_message(chat_id, message)


def music_play(user):
    chat_id = user.from_user.id
    text = user.text
    music_name = text.replace('/music ', '')
    os.system(f'start music/{str(music_name)}.mp3')
    musiv = open(f'music/{str(music_name)}.mp3', 'rb')

    message = f'''
    آهنگ با کد اختصاصی زیر درحال پخش:🎶
    {str(music_name)}
    '''
    bot.send_message(chat_id, message)
    bot.send_chat_action(chat_id, 'upload_document')
    bot.send_audio(chat_id, musiv, caption='آهنگ درحال پخش😐')


def screenshot(user):
    chat_id = user.from_user.id
    message = 'گرفتن اسکرین...'
    bot.send_message(chat_id, message)
    photo = ImageGrab.grab()
    photo.save('screen.png')
    message = 'اسکرین شات گرفته شد!😋'

    bot.send_message(chat_id, message)
    photo = open('screen.png', 'rb')
    bot.send_photo(chat_id, photo)
    photo.close()

    photo = open('screen.png', 'rb')
    bot.send_document(chat_id, photo, caption='اسکرین گرفته شده  نسخه با کیفیت 🙄')
    photo.close()

    os.remove('screen.png')
    # print(chat_id)


def systeminfo(user):
    chat_id = user.from_user.id
    uname = platform.uname()
    runtime = time.time() - start_time
    if runtime < 60:
        runtime = f'{int(runtime)} Second'
    else:
        runtime = runtime / 60
        runtime = f'{int(runtime)} Minutes'
    message = f'''
    🔰 System: {uname.system} {uname.release}

👥 Node Name: {uname.node}

🔺 CPU Usage  {psutil.cpu_percent()} Percent

🔺 RAM Usage: {psutil.virtual_memory()[2]} Percent

📝 Machine Architecture: {uname.machine}

⏱ Bot Run Time: {runtime}
    '''
    bot.send_message(chat_id, message)


def shutdown_btn(user):
    chat_id = user.from_user.id
    btns = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('آره مطمئنم میخوام خاموش بشه!!')
    btn2 = types.KeyboardButton('نه دستم خورد !!')
    btns.add(btn1, btn2, )
    message = '''
        آیا مطمئن هستید که سیستم خاموش شود؟🤨
        '''
    bot.send_message(chat_id, message, reply_markup=btns)


def restart_btn(user):
    chat_id = user.from_user.id
    btns = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('آره مطمئنم میخوام ریستارت بشه!!')
    btn2 = types.KeyboardButton('نه دستم خورد !!')
    btns.add(btn1, btn2)
    message = '''
            آیا مطمئن هستید که سیستم ریستارت شود؟🤨
            '''
    bot.send_message(chat_id, message, reply_markup=btns)


def download_btn(user):
    chat_id = user.from_user.id
    text = user.text
    btns = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Download File From System📥')
    btn2 = types.KeyboardButton('File List📂')
    btn3 = types.KeyboardButton('بازگشت')
    btns.add(btn1, btn2, btn3)
    bot.send_message(chat_id, 'به فایل منجر خوش آمدید😅', reply_markup=btns)


def downlaod_message(user):
    chat_id = user.from_user.id
    # text = user.text
    bot.send_message(chat_id, 'نحوه استفاده \n /download [file name or file address]')


def download_file(user):
    chat_id = user.from_user.id
    text = user.text
    filename_or_address = text.replace('/download ', '')
    if os.path.isdir(filename_or_address):
        bot.send_message(chat_id, 'این یک فولدر هست و قابل دانلود نیست😑')
    else:
        if os.path.isfile(filename_or_address):
            file = open(filename_or_address, 'rb')
            bot.send_message(chat_id, 'درحال آپلود کردن فایل درخواستی شما...')
            bot.send_document(chat_id, file, caption='این فایل درخواستی شماست 😁')
        else:
            bot.send_message(chat_id, 'فایل یا فولدری با این نام پیدا نشد.🤐')


def web_btn(user):
    chat_id = user.from_user.id
    text = user.text
    bot.send_message(chat_id, 'نحوه استفاده \n /web [URL]')


def filemanagerlist(user):
    userchatid = user.chat.id
    usertext = user.text

    directory = usertext.replace("/filemanager ", "")

    if (os.path.isdir(directory)):
        bot.send_message(userchatid, "🔎 درحال اسکن کردن فولدر ...")

        foldercount = 0
        folderlist = ""

        filecount = 0
        filelist = ""

        for r, d, f in os.walk(directory):
            for folder in d:
                if (foldercount > 30 or foldercount == 30):
                    break
                else:
                    if ("\\" in r):
                        pass
                    else:
                        foldercount += 1
                        folderlist = folderlist + "\n" + "📁 " + r + "/" + folder
            for file in f:
                if (filecount > 30 or filecount == 30):
                    break
                else:
                    filecount += 1
                    filelist = filelist + "\n" + "🧾 " + r + "/" + file
        bot.send_message(userchatid, "🗂 30 First Folders In " + directory + " : \n\n" + str(folderlist))
        bot.send_message(userchatid, "🗃 30 First File In " + directory + " : \n\n" + str(filelist))
    else:
        bot.send_message(userchatid, "چیزی پیدا نکردم 😐")


def justfilelist(user):
    userchatid = user.chat.id
    bot.send_message(userchatid, "نحوه استفاده:\n/filemanager [dir]")


@bot.message_handler(content_types=['text'])
def main(user):
    chat_id = user.from_user.id
    text = user.text
    # print(chat_id)
    if chat_id == admin:
        if text == '/start':
            startcm(user)

        if text == '/save':
            bot.send_message(chat_id, 'لطفا بعد از دستور پیام خود را اضافه کنید\n به این صورت : \n /save [message] ')

        if text.startswith('/save '):
            savedb(user)

        if text == '/message':
            savedb_lsit(user)

        if text == 'Power Option ⚠️':
            power(user)

        if text == 'ShoutDown | خاموش کردن':
            shutdown_btn(user)

        if text == 'ریستارت | Restart':
            restart_btn(user)

        if text == 'آره مطمئنم میخوام خاموش بشه!!':
            bot.send_message(chat_id, 'سیستم شما خاموش شد!😐')
            os.system('shutdown /s /t 1')
            home(user)

        if text == 'آره مطمئنم میخوام ریستارت بشه!!':
            bot.send_message(chat_id, 'سیستم شما ریستارت شد!😐')
            os.system('shutdown /r /t 1')
            home(user)

        if text == 'بازگشت':
            home(user)

        if text == 'نه دستم خورد !!':
            bot.send_message(chat_id, 'کنترل دستت هم نداری بدبخت 😂')
            home(user)

        if text == 'ScreenShot📸':
            screenshot(user)

        if text == 'Sound🔉':
            playmusic_btn(user)
        if text == 'Beep':
            bep(user)

        if text == 'Music 🎧':
            music(user)

        if text == 'System Info💻':
            systeminfo(user)

        if text == 'File Manager🗄':
            download_btn(user)

        if text == 'Download File From System📥':
            downlaod_message(user)

        if text.startswith('/download '):
            download_file(user)

        if text == '/download':
            downlaod_message(user)

        if text == 'Open Web🌍':
            web_btn(user)

        if text.startswith('/web '):
            url = text.replace('/web ', '')
            bot.send_message(chat_id, f'گوگل کروم با آدرس شما[{url}] باز شد🥳')
            os.system(f"start chrome {url}")

        if text == '/web':
            web_btn(user)

        if (text == "File List📂" or text == "/filemanager"):
            justfilelist(user)

        if (text.startswith("/filemanager ")):
            filemanagerlist(user)

        if text.startswith('/music '):
            music_play(user)
        if text == '/music':
            music(user)
        if text == '/music_list':
            music_id(user)
    else:
        bot.send_message(chat_id, 'شما ادمین نیستید 😐')


@bot.message_handler(content_types=['audio'])
def audio(message):
    chat_id = message.from_user.id
    # print(message.audio)
    raw = message.audio.file_id
    # file_name = message.audio.file_unique_id
    title = message.audio.title
    title = title.strip()
    title = title.replace(' ', '_')
    performer = message.audio.performer
    performer = performer.strip()
    performer = performer.replace(' ', '_')
    file_size = message.audio.file_size

    if file_size > 20971520:
        bot.send_message(chat_id, 'محدودیت های تلگرام حجم فایل بیش از 20مگابایت هست 🤐')

    else:
        try:
            file_info = bot.get_file(raw)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(f'music/{str(performer)}-{str(title).strip()}.mp3', 'wb') as new_file:
                new_file.write(downloaded_file)
            os.system(f'start music/{str(performer)}-{str(title).strip()}.mp3')
            bot.send_message(chat_id, 'درحال پخش آهنگ شما...😯')
            bot.send_message(chat_id, 'کد اختصاصی این آهنگ👇')
            bot.send_message(chat_id, f'``` /music {str(performer)}-{str(title).strip()}```', parse_mode='markdown')
        except:
            bot.send_message(chat_id, 'این آهنگ درحال پخش است😒')


try:
    bot.polling(True)
except:
    print(' I Got Error :( ')
