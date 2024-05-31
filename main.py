import config
import main_functions
import stt
import tts
from fuzzywuzzy import fuzz


print(f"{config.VA_NAME} (v{config.VA_VER}) начала свою работу ...")
voice2 = ""


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
    elif cmd == 'youtube':
        main_functions.search_youtube(voice2)
    elif cmd == "gpt":
        main_functions.main_gpt(voice2)
    elif cmd == "music":
        main_functions.music_player.search_music(voice2)
    elif cmd == "next_track":
        main_functions.music_player.next_track()
    elif cmd == "previous_track":
        main_functions.music_player.previous_track()
    elif cmd == "notes":
        main_functions.notes(voice2)
    elif cmd == "conductor":
        main_functions.conductor()
    elif cmd == "open_Pycharm":
        main_functions.open_Pycharm()
    elif cmd == "steam":
        main_functions.open_Steam()
    elif cmd == "volume_max":
        main_functions.volume_max()
    elif cmd == "volume_min":
        main_functions.volume_min()
    elif cmd == "Mega_volume":
        main_functions.Mega_volume(voice2)
    elif cmd == "volume_on":
        main_functions.volume_on()
    elif cmd == "volume_off":
        main_functions.volume_off()
    elif cmd == "set_audio_columns":
        main_functions.set_audio_columns("PHL 223V7")
    elif cmd == "timer":
        main_functions.start_timer(voice2)
    elif cmd == "set_alarm":
        main_functions.set_alarm(voice2)
    elif cmd == "Off_Eureka":
        main_functions.Off_Eureka()


stt.va_listen(va_respond)



