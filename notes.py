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

import threading
import time

def countdown():

    time.sleep(1)
    print("Time's up!")

# Запускаем таймер в отдельном потоке
timer_thread = threading.Thread(target=countdown)
timer_thread.start()

# Основной код, который будет выполняться параллельно с таймером
print("Основной код запущен...")
time.sleep(6)  # Пауза на 6 секунд для демонстрации
print("Основной код завершен.")

# Ожидаем завершения таймера
timer_thread.join()
print("Таймер завершил свою работу.")
