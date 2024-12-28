import pyautogui
import time
import win32process
import psutil


def active_window(process_name):
    for window in pyautogui.getAllWindows():
        # 获取窗口的句柄
        hwnd = window._hWnd
        # 使用win32process模块获取窗口的进程ID
        _, process_id = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(process_id)
        # print(f"process_id:{process_id}")
        # print(f"if_print_process_name:{process.name(), window.title}")
        # 获取进程的名称
        if process.name() == process_name and window.title != '':
            window.activate()
            window.maximize()


def find_and_click(res):
    png_center = pyautogui.locateCenterOnScreen(res, confidence=0.95, grayscale=True)
    if png_center is not None:
        pyautogui.click(png_center)
        time.sleep(0.2)
        pyautogui.moveTo(0, 0)


active_window("BCompare.exe")
screen_size = pyautogui.size()
pyautogui.click(button='right', x=0, y=screen_size.height / 2)
time.sleep(0.2)
find_and_click('../res/vedpqrbu.png')
