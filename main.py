import keyboard
import pyautogui
import config
import main_functions
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from num2words import num2words
import webbrowser
import random
import sys
import pygetwindow as gw
from pytube import YouTube
import ctypes
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
        main_functions.help()
    elif cmd == 'ctime':
        main_functions.time()
    elif cmd == 'return_tab':
        main_functions.return_tab()
    elif cmd == 'close_tab':
        main_functions.close_tab()
    elif cmd == "Alt+F4":
        main_functions.AltF4()
    elif cmd == 'search_google':
        main_functions.search_google(voice2)
    elif cmd == "search_prog":
        main_functions.search_prog()
    elif cmd == 'search_youtube':
        main_functions.search_youtube(voice2)
    elif cmd == "Off_Eureka":
        main_functions.Off_Eureka()
    elif cmd == "gpt":
        main_functions.main_gpt(voice2)
# начать прослушивание команд
stt.va_listen(va_respond)
