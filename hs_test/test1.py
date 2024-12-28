import subprocess

# 定义要启动的程序列表
programs = [
    "C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe",
    "C:\\Program Files\\FxSound LLC\\FxSound\\FxSound.exe",
]
# programs = [
#     "C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe",
#     "C:\\Program Files\\JetBrains\\IntelliJ IDEA 2021.3.3\\bin\\idea64.exe",
#     "D:\\Program Files (x86)\\Tencent\\QQMusic\\QQMusic2005.14.05.40\\QQMusic.exe",
#     "D:\\ProgramData\\Everything-1.4.1.1026.x64\\everything.exe",
#     "C:\\Program Files (x86)\\DingDing\\DingtalkLauncher.exe",
#     "C:\\Program Files\\FxSound LLC\\FxSound\\FxSound.exe",
#     "C:\\Program Files\\Unity Hub\\Unity Hub.exe"
# ]

# 遍历列表并启动每个程序
processes = []
for program in programs:
    print(program)
    process = subprocess.Popen([program], creationflags=subprocess.CREATE_NEW_CONSOLE)
    processes.append(process)

# 等待所有程序完成（如果需要）
for process in processes:
    process.wait()