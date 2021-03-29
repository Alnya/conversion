import subprocess
import pyautogui
import time
import pyperclip
from settings import get_data_algorithm_path


def conversion(path):
    with open(path, encoding="UTF-8") as file:
        input_string = file.read()
        input_list = list(input_string.split("\n"))
        write_string = ""
        for i in range(len(input_list)):
            n = list(input_list[i])
            for j in range(2, len(n)):
                write_string += n[j]
            write_string += "\n"
            # write_string += "\n\nconversion completed."
    with open(path, mode="w", encoding="UTF-8") as file:
        file.write(write_string)
    subprocess.run(["start", "dir", "/w"], shell=True)
    time.sleep(1)
    pyperclip.copy(path)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")


if __name__ == '__main__':
    conversion(get_data_algorithm_path())
