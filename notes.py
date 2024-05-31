# import subprocess
#
# def run_steam_game(app_id):
#     try:
#         # Формируем URL для запуска игры в Steam
#         steam_url = "steam://run/{}".format(app_id)
#         # Открываем URL с помощью стандартной команды операционной системы
#         subprocess.Popen(["start", steam_url], shell=True)
#         return True
#     except Exception as e:
#         print("Ошибка при попытке запустить игру в Steam:", e)
#         return False
#
# # Пример использования: запустить игру с идентификатором 730 (Counter-Strike: Global Offensive)
# run_steam_game("730")
# import customtkinter as ctk
# import tkinter as tk  # Импорт стандартного tkinter для работы с переменными
# import main_functions
#
# # Инициализация библиотеки customtkinter
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")
#
# # Функция для показа фрейма главного окна
# def show_main_frame():
#     settings_frame.pack_forget()
#     main_frame.pack(fill="both", expand=True)
#
# # Функция для показа фрейма с настройками
# def show_settings_frame():
#     main_frame.pack_forget()
#     settings_frame.pack(fill="both", expand=True)
#
# # Создание главного окна
# root = ctk.CTk()
# root.title("Приложение")
# root.geometry("550x800")
#
# # Создание фрейма главного окна
# main_frame = ctk.CTkFrame(root)
# main_frame.pack(fill="both", expand=True)
#
# main_label = ctk.CTkLabel(main_frame, text="Главное окно", font=("Arial", 24))
# main_label.pack(pady=20)
#
# button_exit = ctk.CTkButton(main_frame, text="Завершить работу", command=main_functions.Off_Eureka)
# button_exit.pack(pady=20)
# button_exit.pack(side="bottom", pady=150)
#
# settings_button = ctk.CTkButton(main_frame, text="Настройки", command=show_settings_frame)
# settings_button.pack(side="bottom", pady=20)
#
# # Создание фрейма настроек
# settings_frame = ctk.CTkFrame(root)
#
# settings_label = ctk.CTkLabel(settings_frame, text="Настройки", font=("Arial", 24))
# settings_label.pack(pady=20)
#
# back_button = ctk.CTkButton(settings_frame, text="Назад", command=show_main_frame)
# back_button.pack(pady=20)
#
# # Переменная для радиокнопок
# selected_voice = tk.StringVar(value="")
#
# # Создание радиокнопок для выбора голоса
# option1_switch = ctk.CTkRadioButton(settings_frame, text="Голос kseniya", variable=selected_voice, value="kseniya")
# option1_switch.pack(pady=10)
#
# option2_switch = ctk.CTkRadioButton(settings_frame, text="Голос baya", variable=selected_voice, value="baya")
# option2_switch.pack(pady=10)
#
# option3_switch = ctk.CTkRadioButton(settings_frame, text="Голос xenia", variable=selected_voice, value="xenia")
# option3_switch.pack(pady=10)
#
# button_speak1 = ctk.CTkButton(settings_frame, text="Тест голоса",command=tts.va_speak("Привет"))
# button_speak1.pack(pady=20)
#
# option2_label = ctk.CTkLabel(settings_frame, text="Опция 2")
# option2_label.pack(pady=10)
#
# option2_entry = ctk.CTkEntry(settings_frame)
# option2_entry.pack(pady=10)



# def start_voice_assistant():
#     stt.va_listen(va_respond)
#
# # Запуск голосового ассистента в отдельном потоке
# voice_thread = threading.Thread(target=start_voice_assistant)
# voice_thread.daemon = True  # Позволяет завершить поток при закрытии основного окна
# voice_thread.start()
#
# # Запуск основного цикла обработки событий
# root.mainloop()
import re

import webbrowser
from youtube_search import YoutubeSearch

import config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from youtube_search import YoutubeSearch

class MusicPlayer:
    def __init__(self, driver_path):
        self.tracks = []
        self.current_index = 0

        # Настройка Selenium
        options = Options()
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")  # Отключите, если хотите видеть браузер
        self.driver = webdriver.Chrome(service=Service(driver_path), options=options)

    def search_music(self, query):
        search_cmd_list = config.VA_CMD_LIST["music"]
        if isinstance(search_cmd_list, tuple):
            for search_cmd in search_cmd_list:
                if search_cmd in query:
                    query = query.split(search_cmd)[-1].strip()
                    break

        results = YoutubeSearch(query, max_results=5).to_dict()

        if results:
            self.tracks = [{'title': result['title'], 'video_id': result['id']} for result in results]
            self.current_index = 0
            self.play_current_track()
        else:
            print("Ничего не найдено на YouTube по вашему запросу.")

    def play_current_track(self):
        if self.tracks:
            video_id = self.tracks[self.current_index]['video_id']
            url = f"https://music.youtube.com/watch?v={video_id}"
            self.driver.get(url)
            time.sleep(5)  # Дать время для загрузки страницы
            print(f"Сейчас играет: {self.tracks[self.current_index]['title']}")
        else:
            print("Нет треков для воспроизведения.")

    def next_track(self):
        if self.tracks:
            self.current_index = (self.current_index + 1) % len(self.tracks)
            self.play_current_track()
        else:
            print("Нет треков для переключения.")

    def previous_track(self):
        if self.tracks:
            self.current_index = (self.current_index - 1) % len(self.tracks)
            self.play_current_track()
        else:
            print("Нет треков для переключения.")

    def pause(self):
        if self.driver:
            self.driver.find_element(By.CSS_SELECTOR, 'button[title="Pause"]').click()

    def play(self):
        if self.driver:
            self.driver.find_element(By.CSS_SELECTOR, 'button[title="Play"]').click()

    def close(self):
        if self.driver:
            self.driver.quit()

# Пример использования
music_player = MusicPlayer(driver_path='/path/to/chromedriver')

# Для поиска и воспроизведения музыки
music_player.search_music("ваш запрос")

# Для переключения на следующий трек
music_player.next_track()

# Для переключения на предыдущий трек
music_player.previous_track()

# Для паузы воспроизведения
music_player.pause()

# Для продолжения воспроизведения
music_player.play()

# Закрыть браузер
music_player.close()
