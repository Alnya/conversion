import subprocess
import pyautogui
import time
import pyperclip


def conversion(path):
    with open(path, encoding="UTF-8") as file:
        input_string = file.read()
        input_list = list(input_string)
        write_string = ""
        for i in range(len(input_list)):
            if input_list[i] == "‐":
                input_list[i] = "-"
            if input_list[i] == "’" or input_list[i] == "‘":
                input_list[i] = "'"
            write_string += input_list[i]
        write_string += "\n\nconversion completed."
    with open(path, mode="w") as file:
        file.write(write_string)
    subprocess.run(["start", "dir", "/w"], shell=True)
    time.sleep(1)
    pyperclip.copy(path)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")


if __name__ == '__main__':
    conversion(r"C:\Alnya\tmp\conversion.txt")
