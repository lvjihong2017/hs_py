import ctypes
import psutil
import pygetwindow as gw
import time

time.sleep(10)

# 获取当前活动窗口的句柄
def get_foreground_window_handle():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    return hwnd


# 获取窗口句柄对应的进程ID
def get_process_id_from_handle(handle):
    process_id = ctypes.c_ulong()
    ctypes.windll.user32.GetWindowThreadProcessId(handle, ctypes.byref(process_id))
    return process_id.value  # 返回 PID


def get_foreground_window_info():
    # 获取当前活动窗口的句柄
    handle = get_foreground_window_handle()

    # 获取窗口标题
    window = gw.Window(handle)
    title = window.title

    # 获取窗口的进程ID
    pid = get_process_id_from_handle(handle)

    # 根据进程ID找到对应的进程信息
    process = psutil.Process(pid)
    process_name = process.name()
    process_path = process.exe()

    print(
        f"Active Window Title: {title}, Window Handle: {handle}, Process ID: {pid}, Process Name: {process_name}, Process Path: {process_path}")


if __name__ == "__main__":
    get_foreground_window_info()