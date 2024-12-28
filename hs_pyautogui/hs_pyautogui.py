import pyautogui
import time
import win32process
import psutil


# -------------- 各种参数介绍
# image：要查找的图像文件的路径或图像对象。这是唯一必需的参数。
# region：指定在屏幕的哪个区域内搜索图像的元组，格式为 (左上角X坐标, 左上角Y坐标, 区域宽度, 区域高度)。默认情况下，将在整个屏幕上搜索。
# grayscale：一个布尔值，指定是否将图像转换为灰度图像进行匹配。默认为False。
# confidence：一个0到1之间的浮点数，用于设置匹配的最小置信度。如果不指定，默认为1.0，表示完全匹配。你可以降低这个值以允许更宽松的匹配。值越低，匹配越不严格，但也可能更容易出现误匹配。
# interval：指定连续搜索之间的时间间隔（秒），用于减轻CPU负载。默认为0.5秒。
# --------------- 找一个
def find_one(image, confidence=0.9, grayscale_bool=True, region=None):
    if region is None:
        width, height = pyautogui.size()
        region = (0, 0, width, height)

    png_center = pyautogui.locateCenterOnScreen(image=image,
                                                confidence=confidence,
                                                grayscale=grayscale_bool,
                                                region=region)
    return png_center


####################################
# 找到并且点击
####################################
def find_click(image, confidence=0.9, grayscale_bool=True, region=None, loop_num=1):
    png_center = None

    for i in range(loop_num):
        png_center = find_one(image, confidence, grayscale_bool, region)
        if png_center is not None:
            pyautogui.click(png_center)
            break

    return png_center


####################################
#  找所有
####################################
def find_all():
    for pos in pyautogui.locateAllOnScreen('../res/jiff.png', confidence=0.9):
        pyautogui.click(pos)
        time.sleep(0.1)


####################################
#  通过窗口找到进程ID，然后找到进程名字
####################################
def fun2():
    for window in pyautogui.getAllWindows():
        # 获取窗口的句柄
        hwnd = window._hWnd
        # 使用win32process模块获取窗口的进程ID
        _, process_id = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(process_id)
        # 获取进程的名称
        process_name = process.name()
        # print(f"process_id:{process_id}")
        print(f"title:{window.title},process_name:{process_name}")
        # if process_name == "msedge.exe":
        #     print(f"if_print_process_name:{process_name}")
