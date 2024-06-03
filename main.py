import config
import main_functions
import stt
import tts
from fuzzywuzzy import fuzz
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime


def play_sound():
    try:
        morning_start = datetime.strptime('03:00', '%H:%M').time()
        morning_end = datetime.strptime('12:00', '%H:%M').time()

        current_time = datetime.now().time()

        if morning_start <= current_time <= morning_end:
            sound = AudioSegment.from_wav('saund/start/dobroe-utro.mp3')
        else:
            sound = AudioSegment.from_wav('saund/start/app_sound_jarvis-og_game_mode.mp3')
        play(sound)
    except Exception as e:
        print(f"Ошибка при воспроизведении звука: {e}")

def main():
    try:
        print(f"{config.VA_NAME} (v{config.VA_VER}) начала свою работу ...")
        voice2 = ""

        def contains_trigger_word(voice):
            for word in config.VA_ALIAS.split():
                if word in voice:
                    return True
            return False

        def va_respond(voice: str):
            print(voice)
            nonlocal voice2
            voice2 = voice

            if contains_trigger_word(voice):
                cmd = recognize_cmd(filter_cmd(voice))

                if cmd['cmd'] not in config.VA_CMD_LIST.keys():
                    tts.va_speak("Что?")
                else:
                    try:
                        execute_cmd(cmd['cmd'])
                    except Exception as e:
                        print(f"Ошибка при выполнении команды '{cmd['cmd']}': {e}")

        def filter_cmd(raw_voice: str):
            cmd = raw_voice

            for x in config.VA_ALIAS.split():
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
            try:
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
            except Exception as e:
                print(f"Ошибка при выполнении команды '{cmd}': {e}")

        stt.va_listen(va_respond)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    play_sound()
    main()