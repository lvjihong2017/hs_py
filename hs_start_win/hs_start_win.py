import logging
import subprocess
import json5
import time
import pyautogui
from datetime import datetime

logging.basicConfig(filename='error.log', level=logging.ERROR)

# 读取配置文件
with open('res/cfg.json', 'r', encoding='utf-8') as f:
    cfg = json5.load(f)

for program in cfg["exe_path"]:
    print(program)
    try:
        # 遍历列表并启动每个程序
        subprocess.Popen([program], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except Exception:
        # 在这里记录堆栈信息和变量
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.error('%s,program=%s', current_time, program, exc_info=True)

time.sleep(2)
pyautogui.hotkey('win', 'd')
