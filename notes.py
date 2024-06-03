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
# # Пример использования: (Counter-Strike: Global Offensive)
# run_steam_game("730")
