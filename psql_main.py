import subprocess
import pyautogui
import time

subprocess.run(['start', 'dir', '/w'], shell=True)
time.sleep(0.1)
pyautogui.typewrite("python psql_on.py")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.typewrite("postgres")
pyautogui.press("enter")