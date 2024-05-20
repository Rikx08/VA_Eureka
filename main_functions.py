import keyboard
import config
import tts
import datetime
from num2words import num2words
import webbrowser
import sys
import g4f
from youtube_search import YoutubeSearch
import os
import subprocess
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume,ISimpleAudioVolume
from word2number import w2n
from translate import Translator
import win32com.client


def help():
    text = "Я умею: ..."
    text += "произносить время ..."
    text += "рассказывать анекдоты ..."
    text += "и открывать браузер"
    tts.va_speak(text)
    pass

def time():
    now = datetime.datetime.now()
    text = num2words(now.hour, lang='ru') + " " + num2words(now.minute, lang='ru')
    tts.va_speak(text)

def return_tab():

    keyboard.press_and_release('ctrl + shift + t')

def close_tab():
    keyboard.press_and_release('ctrl + w')

def AltF4():
    keyboard.press_and_release('alt + f4')

def search_google(voice2):
    query = voice2
    search_cmd_list = config.VA_CMD_LIST["search_google"]  # Получаем список тригерных слов
    if isinstance(search_cmd_list, tuple):  # Проверяем, является ли значение для "search_google" кортежем
        for search_cmd in search_cmd_list:
            if search_cmd in query:
                # Удаляем триггерные слова и все что было до них
                query = query.split(search_cmd)[-1].strip()
                break

    search_terms = "+".join(query.split())
    url = "https://google.com/search?q=" + search_terms
    webbrowser.open(url)

def search_prog():
    # Эмуляция нажатия клавиши Alt
    keyboard.press('alt')
    # Эмуляция нажатия клавиши Tab
    keyboard.press_and_release('tab')
    # Эмуляция отпускания клавиши Alt
    keyboard.release('alt')

def search_youtube(voice2):
    query = voice2
    search_cmd_list = config.VA_CMD_LIST["youtube"]  # Получаем список тригерных слов
    if isinstance(search_cmd_list, tuple):  # Проверяем, является ли значение для "youtube" кортежем
        for search_cmd in search_cmd_list:
            if search_cmd in query:
                # Удаляем триггерные слова и все что было до них
                query = query.split(search_cmd)[-1].strip()
                break

    # Выполнить поиск на YouTube
    results = YoutubeSearch(query, max_results=1).to_dict()

    if results:  # Убедиться, что найден хотя бы один результат
        video_id = results[0]['id']

        # Сформировать URL для открытия видео
        url = f"https://www.youtube.com/watch?v={video_id}"

        # Открыть URL в браузере
        webbrowser.open(url)
    else:
        print("Ничего не найдено на YouTube по вашему запросу.")

def gpt_model(messages: list):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    return response

def process_user_input(user_input):
    messages = [{"role": "user", "content": user_input}]
    assistant_response = gpt_model(messages=messages)
    return assistant_response

def main_gpt(voice2):
    query = voice2
    search_cmd_list = config.VA_CMD_LIST["gpt"]  # Получаем список тригерных слов
    if isinstance(search_cmd_list, tuple):  # Проверяем, является ли значение для "gpt" кортежем
        for search_cmd in search_cmd_list:
            if search_cmd in query:
                # Удаляем триггерные слова и все что было до них
                query = query.split(search_cmd)[-1].strip()
                break

    user_input = query
    assistant_response = process_user_input(user_input)
    print("Assistant:", assistant_response)

def music(voice2):
    query = voice2
    search_cmd_list = config.VA_CMD_LIST["music"]  # Получаем список тригерных слов
    if isinstance(search_cmd_list, tuple):  # Проверяем, является ли значение для "music" кортежем
        for search_cmd in search_cmd_list:
            if search_cmd in query:
                # Удаляем триггерные слова и все что было до них
                query = query.split(search_cmd)[-1].strip()
                break

    # Выполнить поиск на YouTube
    results = YoutubeSearch(query, max_results=1).to_dict()

    if results:  # Убедиться, что найден хотя бы один результат
        video_id = results[0]['id']

        # Сформировать URL для открытия видео
        url = f"https://music.youtube.com/watch?v={video_id}"

        # Открыть URL в браузере
        webbrowser.open(url)
    else:
        print("Ничего не найдено на YouTube по вашему запросу.")

def notes(voice2):
    query = voice2
    search_cmd_list = config.VA_CMD_LIST["notes"]  # Получаем список тригерных слов
    if isinstance(search_cmd_list, tuple):  # Проверяем, является ли значение для "search_google" кортежем
        for search_cmd in search_cmd_list:
            if search_cmd in query:
                # Удаляем триггерные слова и все что было до них
                query = query.split(search_cmd)[-1].strip()
                break

    # Путь к рабочему столу пользователя (для Windows)
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    file_name = "VAE_notes.txt"
    file_path = os.path.join(desktop_path, file_name) # Полный путь к файлу на рабочем столе
    text_to_write = query


    if os.path.exists(file_path):                # Определяем номер строки, который нужно записать в файл
        with open(file_path, 'r') as file:       # Если файл уже существует, определяем номер строки
            lines = file.readlines()
            line_number = len(lines) + 1

    else:                                        # Если файл не существует, начинаем с первой строки
        line_number = 1

    with open(file_path, 'a') as file:   # Запись текста в файл
        if line_number > 1:
                                                 # Если файл уже существует, добавляем перевод строки перед новой записью
            file.write('\n')
        file.write(f"{line_number}. {text_to_write}")

    print(f"Строка успешно добавлена в файл {file_name} на рабочем столе.")

def conductor():
    keyboard.press_and_release('win + e')

def open_Pycharm():

    try:
        subprocess.Popen(["C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.2.1\\bin\\pycharm64.exe"])
        return True
    except Exception as e:
        print("Ошибка при попытке открыть pycharm:", e)
        return False

def open_Steam():

    try:
        subprocess.Popen(["C:\\Program Files (x86)\\Steam\\steam.exe"])
        return True
    except Exception as e:
        print("Ошибка при попытке открыть Steam:", e)
        return False

def volume_max():
    # Получение объекта для управления звуком текущего устройства воспроизведения
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Получение текущей громкости
    current_volume = volume.GetMasterVolumeLevelScalar()

    # Установка новой громкости ( увеличиваем на 10%)
    new_volume = min(1.0, current_volume + 0.1)
    volume.SetMasterVolumeLevelScalar(new_volume, None)

def volume_min():
    # Получение объекта для управления звуком текущего устройства воспроизведения
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Получение текущей громкости
    current_volume = volume.GetMasterVolumeLevelScalar()

    # Установка новой громкости ( уменьшаем  на 10%)
    new_volume = max(0.0, current_volume - 0.1)
    volume.SetMasterVolumeLevelScalar(new_volume, None)

def translate_word(word, source_lang, target_lang):
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    translation = translator.translate(word)
    return translation

def Mega_volume(voice2):
    query = voice2
    search_cmd_list = config.VA_CMD_LIST["Mega_volume"]  # Получаем список тригерных слов
    if isinstance(search_cmd_list, tuple):  # Проверяем, является ли значение для "Mega_volume" кортежем
        for search_cmd in search_cmd_list:
            if search_cmd in query:
                # Удаляем триггерные слова и все что было до них
                query = query.split(search_cmd)[-1].strip()
                break

    russian_word =query
    english_translation = translate_word(russian_word, "ru", "en")
    oll = w2n.word_to_num(english_translation)

    # Получение объекта для управления звуком текущего устройства воспроизведения
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Получение текущей громкости
    current_volume = volume.GetMasterVolumeLevelScalar()

    # Установка новой громкости (в примере увеличиваем на 10%)
    new_volume = oll/100
    volume.SetMasterVolumeLevelScalar(new_volume, None)

def volume_on():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = cast(session._ctl.QueryInterface(ISimpleAudioVolume), POINTER(ISimpleAudioVolume))
        volume.SetMute(0, None)

def volume_off():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = cast(session._ctl.QueryInterface(ISimpleAudioVolume), POINTER(ISimpleAudioVolume))
        volume.SetMute(1, None)

def set_audio_columns(device_name):
    None

def set_alarm(voice2):
    query = voice2
    search_cmd_list = config.VA_CMD_LIST["set_alarm"]  # Получаем список тригерных слов
    if isinstance(search_cmd_list, tuple):  # Проверяем, является ли значение для "set_alarm" кортежем
        for search_cmd in search_cmd_list:
            if search_cmd in query:
                # Удаляем триггерные слова и все что было до них
                query = query.split(search_cmd)[-1].strip()
                break
    russian_word = query

    english_translation = translate_word(russian_word, "ru", "en")
    sp = english_translation.split()


    hour = str(w2n.word_to_num(sp[0]))  # Преобразуйте часы в строку
    minute = str(w2n.word_to_num(sp[1]))


    try:
        # Создаем экземпляр объекта WScript.Shell
        shell = win32com.client.Dispatch("WScript.Shell")
        # Запускаем приложение "Часы"
        shell.Run("ms-clock:")
        # Подтверждаем активацию окна "Часы"
        shell.AppActivate("Часы")
        # Закрываем предыдущее окно будильников, если оно открыто
        shell.SendKeys("%{F4}")
        # Открываем вкладку с будильниками
        shell.SendKeys("^{2}")
        # Добавляем новый будильник
        shell.SendKeys("%{a}")
        # Переходим к полю ввода часов
        shell.SendKeys("%(h)")
        # Вводим часы
        shell.SendKeys(hour)  # Предполагается, что переменная `hour` уже определена
        # Переходим к полю ввода минут
        shell.SendKeys("{TAB}")
        # Вводим минуты
        shell.SendKeys(minute)  # Предполагается, что переменная `minute` уже определена
        # Нажимаем Enter для сохранения будильника
        shell.SendKeys("{ENTER}")
    except Exception as e:
        print("Ошибка:", e)


def timer(voice2):
    None

def Off_Eureka():
    sys.exit()  # Остановить выполнение программы
