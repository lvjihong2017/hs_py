####################################
#
####################################
import tkinter as tk
import pyautogui
import time


####################################
# 主方法
####################################
def main_run():
    all_windows = pyautogui.getAllWindows()
    for window in all_windows:
        if "Edge" in window.title:
            window.maximize()
            label_title.config(text=window.title)
            print(window.title)
            if not window.isActive:
                print("not_active")
                window.restore()
                window.activate()

            label_state_k_1.config(text="判断是否播放页面")
            if "正在播放" in window.title:
                label_state_v_1.config(text="是播放页面")
                label_state_k_2.config(text="判断是否播放完毕")
                label_state_v_2.config(text="播放完毕判断代码待补充......")
            else:
                label_state_v_1.config(text="不是播放页面")
                label_state_k_2.config(text="判断是否选课页面")
                label_state_v_2.config(text="判断代码待补充")
            # 处理完之后，最小化
            time.sleep(2)
            window.minimize()
    root.after(2000, main_run)


####################################
# 提交按钮执行方法
####################################
def on_submit():
    label_curr_title.config(text="当前运行中：你点了提交按钮")


####################################
# 创建窗体
####################################
root = tk.Tk()
root.title("自动学习")
# 指定
root.attributes('-topmost', True)

# 调整窗口的宽度和高度
window_width = 500
window_height = 500
frame_padx = 20
frame_pady = 1
root.geometry(f"{window_width}x{window_height}")

####################################
# 当前运行中
####################################
label_curr_title = tk.Label(root, text="当前运行中：")
label_curr_title.pack()
label_name = tk.Label(root, text="")
label_name.pack()
label_area = tk.Label(root, text="")
label_area.pack()
label_title = tk.Label(root, text="")
label_title.pack()
label_state_k_1 = tk.Label(root, text="")
label_state_k_1.pack()
label_state_v_1 = tk.Label(root, text="")
label_state_v_1.pack()
label_state_k_2 = tk.Label(root, text="")
label_state_k_2.pack()
label_state_v_2 = tk.Label(root, text="")
label_state_v_2.pack()

####################################
# 添加提交按钮
####################################
submit_button = tk.Button(root, text="提交", command=on_submit)
submit_button.pack()

####################################
#
####################################
# 定时执行
root.after(1000, main_run)
# mainloop
root.mainloop()
