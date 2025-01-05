import sys
from cx_Freeze import setup, Executable

# 排除不需要的 DLL 文件
excludes = []

# 基础设置
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # 如果是 Windows GUI 程序

# 可执行文件的设置
executables = [
    Executable(
        './hs_start_exe/hs_start_exe.py',  # 主脚本文件
        base=base,
        target_name='hs_start_app',  # 可执行文件名称
        icon="my_icon.ico"
    )
]

# 打包设置
setup(
    name='hs_start_app',
    version='1.0',
    description='一键启动多个应用程序',
    executables=executables,
    options={
        'build_exe': {
            'excludes': excludes,  # 排除不需要的文件
            'include_files': [],  # 包含需要的文件
            'packages': [],
            # 包含需要的包,打包完的exe运行时报错缺少哪个包就添加在这里，重新打包
            'include_msvcr': True,  # 包含 Microsoft Visual C++ 运行时库
            # 'silent': False,  # 启用调试模式
        }
    }
)
