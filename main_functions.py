import keyboard
import pyautogui
import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from num2words import num2words
import webbrowser
import random
import sys
import g4f


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
    search_cmd_list = config.VA_CMD_LIST["search_youtube"]  # Получаем список тригерных слов
    if isinstance(search_cmd_list, tuple):  # Проверяем, является ли значение для "search_youtube" кортежем
        for search_cmd in search_cmd_list:
            if search_cmd in query:
                # Удаляем триггерные слова и все что было до них
                query = query.split(search_cmd)[-1].strip()
                break

    search_terms = "+".join(query.split())
    url = "https://www.youtube.com/results?search_query=" + search_terms
    webbrowser.open(url)
    # Ютуб не работает доделать!!!!!!!!

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
    if isinstance(search_cmd_list, tuple):  # Проверяем, является ли значение для "search_google" кортежем
        for search_cmd in search_cmd_list:
            if search_cmd in query:
                # Удаляем триггерные слова и все что было до них
                query = query.split(search_cmd)[-1].strip()
                break

    user_input = query
    assistant_response = process_user_input(user_input)
    print("Assistant:", assistant_response)
    tts.va_speak(assistant_response)


def Off_Eureka():
    sys.exit()  # Остановить выполнение программы
