import time
import win32gui
import win32con
import pyautogui


def active_show():
    print("active_show:置顶切保持激活状态")
    hwnd = win32gui.FindWindow(None, "遮天世界")  # 将 "窗口标题" 替换为实际的窗口标题
    if hwnd != 0:
        while True:
            # 将窗口置于顶层
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                                  win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
            # 激活窗口
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(0.1)  # 等待一段时间
    else:
        print("active_show:未找到窗口")


def set_window(type):
    all_windows = pyautogui.getAllWindows()
    for window in all_windows:
        if "" != window.title:
            if "遮天世界" == window.title:
                print("restore")
                window.restore()
                time.sleep(1)
                print("resizeTo")
                if type == "2":
                    window.resizeTo(240, 135)
                elif type == "3":
                    window.resizeTo(960, 540)
                elif type == "4":
                    window.maximize()
                else:
                    print("type_error")


print("1置顶")
print("2窗口化-240*135")
print("3窗口化-960*540")
print("4全屏")
while True:
    print("请输入：")
    type = input()
    print(f"输入值：{type}")
    if type == "1":
        try:
            active_show()
        except:
            print("...")
    else:
        set_window(type)
