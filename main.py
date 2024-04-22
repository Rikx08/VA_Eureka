import keyboard

import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from num2words import num2words
import webbrowser
import random
from selenium import webdriver

import pyautogui
import time
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup


print(f"{config.VA_NAME} (v{config.VA_VER}) начала свою работу ...")
voice2 = ""
# def contains_trigger_word(voice):
#     for word in config.VA_ALIAS:
#         if word in voice:
#             return True
#     return False
#
# def va_respond(voice: str):
#     print(voice)
#     global voice2
#     voice2 = voice
#
#     if contains_trigger_word(voice):
#         cmd = recognize_cmd(filter_cmd(voice))
#
#         if cmd['cmd'] not in config.VA_CMD_LIST.keys():
#             tts.va_speak("Что?")
#         else:
#             execute_cmd(cmd['cmd'])
#     # if voice.startswith(config.VA_ALIAS):
#     #     # обращаются к ассистенту
#     #     cmd = recognize_cmd(filter_cmd(voice))
#     #
#     #     if cmd['cmd'] not in config.VA_CMD_LIST.keys():
#     #         tts.va_speak("Что?")
#     #     else:
#     #         execute_cmd(cmd['cmd'])
#
#
# def filter_cmd(raw_voice: str):
#     cmd = raw_voice
#
#     for x in config.VA_ALIAS:
#         cmd = cmd.replace(x, "").strip()
#
#     for x in config.VA_TBR:
#         cmd = cmd.replace(x, "").strip()
#
#     return cmd
#
#
# def recognize_cmd(cmd: str):
#     rc = {'cmd': '', 'percent': 0}
#     for c, v in config.VA_CMD_LIST.items():
#
#         for x in v:
#             vrt = fuzz.ratio(cmd, x)
#             if vrt > rc['percent']:
#                 rc['cmd'] = c
#                 rc['percent'] = vrt
#
#     return rc
def contains_trigger_word(voice):
    for word in config.VA_ALIAS.split():  # Разделяем триггерное слово на отдельные слова
        if word in voice:
            return True
    return False

def va_respond(voice: str):
    print(voice)
    global voice2
    voice2 = voice

    if contains_trigger_word(voice):
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd'])

def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS.split():  # Разделяем триггерное слово на отдельные слова
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd

def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc

def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        text += "и открывать браузер"
        tts.va_speak(text)
        pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = num2words(now.hour, lang='ru') + " " + num2words(now.minute, lang='ru')
        tts.va_speak(text)

    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                 'Программист это машина для преобразования кофе в код']

        tts.va_speak(random.choice(jokes))

    elif cmd == 'return_tab':
        keyboard.press_and_release('ctrl + shift + t')


    elif cmd == 'close_tab':
        keyboard.press_and_release('ctrl + w')


    elif cmd == 'search':
        query = voice2
        search_cmd_list = config.VA_CMD_LIST["search"]  # Получаем список тригерных слов
        if isinstance(search_cmd_list, tuple):  # Проверяем, является ли значение для "search2" кортежем
            for search_cmd in search_cmd_list:
                if search_cmd in query:
                    # Удаляем триггерные слова и все что было до них
                    query = query.split(search_cmd)[-1].strip()
                    break

        search_terms = "+".join(query.split())
        url = "https://google.com/search?q=" + search_terms
        webbrowser.open(url)

        # query = voice2
        # search_cmd_list = config.VA_CMD_LIST["search"] # Получаем список тригерных слов
        # if isinstance(search_cmd_list, tuple):  # Проверяем, является ли значение для "search2" кортежем
        #     for search_cmd in search_cmd_list:
        #         if search_cmd in query:
        #             query = query.replace("эврика","")
        #             query = query.replace(search_cmd, "", 1)  # Удаляем только первое вхождение триггерного слова
        #             break
        # search_terms = "+".join(query.split())
        # url = "https://google.com/search?q=" + search_terms
        # webbrowser.open(url)


# начать прослушивание команд
stt.va_listen(va_respond)