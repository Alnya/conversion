import subprocess
import pyautogui
import time
from settings import get_psql_main_password


def main():
    # コマンドプロンプトを開き、キーボードから
    # psql_onを起動するように命令
    # パスワードをキーボードから入力してログイン
    subprocess.run(['start', 'dir', '/w'], shell=True)
    time.sleep(0.1)
    pyautogui.typewrite("python psql_on.py")
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.typewrite(get_psql_main_password())
    pyautogui.press("enter")


if __name__ == '__main__':
    main()
