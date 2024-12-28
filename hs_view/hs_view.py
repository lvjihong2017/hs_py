import tkinter as tk
import time
import threading


class Panel1:
    def __init__(self, root):
        # 创建窗口
        self.root = root
        self.root.title("二师兄")
        # 置顶
        self.root.attributes('-topmost', True)

        # 调整窗口的宽度和高度
        self.window_width = 800
        self.window_height = 500
        self.root.geometry(f"{self.window_width}x{self.window_height}")

        self.RunBool = False  # 是否运行中
        self.RefreshBool = False  # 是否在刷新
        # 界面布局
        self.LabelPadx1 = 5
        self.LabelWidth1 = 15
        self.LabelWidth2 = 70
        self.ButtonWidth1 = 10

        # 显示格子的数据
        self.v1 = ""
        self.v2 = ""
        self.v3 = ""
        self.v4 = ""
        self.v5 = ""
        self.v6 = ""
        self.v7 = ""
        self.v8 = ""
        self.v9 = 0

        ####################################
        # 界面设置
        ####################################
        self.label_k1 = tk.Label(self.root, anchor="e", width=self.LabelWidth1, text="当前查找图片：")
        self.label_k2 = tk.Label(self.root, anchor="e", width=self.LabelWidth1, text="错误信息：")
        self.label_k3 = tk.Label(self.root, anchor="e", width=self.LabelWidth1, text="")
        self.label_k4 = tk.Label(self.root, anchor="e", width=self.LabelWidth1, text="")
        self.label_k5 = tk.Label(self.root, anchor="e", width=self.LabelWidth1, text="")
        self.label_k6 = tk.Label(self.root, anchor="e", width=self.LabelWidth1, text="")
        self.label_k7 = tk.Label(self.root, anchor="e", width=self.LabelWidth1, text="")
        self.label_k8 = tk.Label(self.root, anchor="e", width=self.LabelWidth1, text="")
        self.label_k9 = tk.Label(self.root, anchor="e", width=self.LabelWidth1, text="运行次数：")

        self.label_v1 = tk.Label(self.root, anchor="w", width=self.LabelWidth2, text="")
        self.label_v2 = tk.Label(self.root, anchor="w", width=self.LabelWidth2, text="")
        self.label_v3 = tk.Label(self.root, anchor="w", width=self.LabelWidth2, text="")
        self.label_v4 = tk.Label(self.root, anchor="w", width=self.LabelWidth2, text="")
        self.label_v5 = tk.Label(self.root, anchor="w", width=self.LabelWidth2, text="")
        self.label_v6 = tk.Label(self.root, anchor="w", width=self.LabelWidth2, text="")
        self.label_v7 = tk.Label(self.root, anchor="w", width=self.LabelWidth2, text="")
        self.label_v8 = tk.Label(self.root, anchor="w", width=self.LabelWidth2, text="")
        self.label_v9 = tk.Label(self.root, anchor="w", width=self.LabelWidth2, text="")

        self.button1 = tk.Button(self.root, width=self.ButtonWidth1, text="开始", command=self.button1_fun)
        self.button2 = tk.Button(self.root, width=self.ButtonWidth1, text="按钮2", command=self.button2_fun)
        self.button3 = tk.Button(self.root, width=self.ButtonWidth1, text="")
        self.button4 = tk.Button(self.root, width=self.ButtonWidth1, text="")
        self.button5 = tk.Button(self.root, width=self.ButtonWidth1, text="")
        self.button6 = tk.Button(self.root, width=self.ButtonWidth1, text="")
        self.button7 = tk.Button(self.root, width=self.ButtonWidth1, text="")
        self.button8 = tk.Button(self.root, width=self.ButtonWidth1, text="")
        self.button9 = tk.Button(self.root, width=self.ButtonWidth1, text="")

        self.label_k1.grid(row=0, column=0, padx=self.LabelPadx1, pady=5)
        self.label_k2.grid(row=1, column=0, padx=self.LabelPadx1, pady=5)
        self.label_k3.grid(row=2, column=0, padx=self.LabelPadx1, pady=5)
        self.label_k4.grid(row=3, column=0, padx=self.LabelPadx1, pady=5)
        self.label_k5.grid(row=4, column=0, padx=self.LabelPadx1, pady=5)
        self.label_k6.grid(row=5, column=0, padx=self.LabelPadx1, pady=5)
        self.label_k7.grid(row=6, column=0, padx=self.LabelPadx1, pady=5)
        self.label_k8.grid(row=7, column=0, padx=self.LabelPadx1, pady=5)
        self.label_k9.grid(row=8, column=0, padx=self.LabelPadx1, pady=5)

        self.label_v1.grid(row=0, column=1, padx=self.LabelPadx1, pady=5)
        self.label_v2.grid(row=1, column=1, padx=self.LabelPadx1, pady=5)
        self.label_v3.grid(row=2, column=1, padx=self.LabelPadx1, pady=5)
        self.label_v4.grid(row=3, column=1, padx=self.LabelPadx1, pady=5)
        self.label_v5.grid(row=4, column=1, padx=self.LabelPadx1, pady=5)
        self.label_v6.grid(row=5, column=1, padx=self.LabelPadx1, pady=5)
        self.label_v7.grid(row=6, column=1, padx=self.LabelPadx1, pady=5)
        self.label_v8.grid(row=7, column=1, padx=self.LabelPadx1, pady=5)
        self.label_v9.grid(row=8, column=1, padx=self.LabelPadx1, pady=5)

        self.button1.grid(row=0, column=2, padx=10, pady=5)
        self.button2.grid(row=1, column=2, padx=10, pady=5)
        self.button3.grid(row=2, column=2, padx=10, pady=5)
        self.button4.grid(row=3, column=2, padx=10, pady=5)
        self.button5.grid(row=4, column=2, padx=10, pady=5)
        self.button6.grid(row=5, column=2, padx=10, pady=5)
        self.button7.grid(row=6, column=2, padx=10, pady=5)
        self.button8.grid(row=7, column=2, padx=10, pady=5)
        self.button9.grid(row=8, column=2, padx=10, pady=5)

    ####################################
    # 开始之后的方法
    ####################################
    def handle_run(self):
        self.v9 = self.v9 + 1
        self.label_v9.config(text="{}".format(self.v9))

    ####################################
    # 点击 按钮1
    ####################################
    def button1_fun(self):
        # refresh只运行要传
        if not self.RefreshBool:
            self.RefreshBool = True
            self.refresh()

        if self.RunBool:
            # 停止
            self.RunBool = False
            self.button1.config(text="开始")
        else:
            # 开始
            self.RunBool = True
            self.button1.config(text="停止")
            # 启动一个线程执行长时间运行的任务
            thread = threading.Thread(target=self.run)
            thread.start()

    ####################################
    # 点击 按钮2
    ####################################
    def button2_fun(self):
        pass

    ####################################
    # 开始之后的方法
    ####################################
    def run(self):
        while self.RunBool:
            self.handle_run()
            time.sleep(0.1)

    ####################################
    # 刷新
    ####################################
    def refresh(self):
        self.label_v1.config(text="{}".format(self.v1))
        self.label_v2.config(text="{}".format(self.v2))
        self.label_v3.config(text="{}".format(self.v3))
        self.label_v4.config(text="{}".format(self.v4))
        self.label_v5.config(text="{}".format(self.v5))
        self.label_v6.config(text="{}".format(self.v6))
        self.label_v7.config(text="{}".format(self.v7))
        self.label_v8.config(text="{}".format(self.v8))
        self.label_v9.config(text="{}".format(self.v9))
        self.root.after(200, self.refresh)


def main():
    root = tk.Tk()
    app = Panel1(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# ####################################
# # 更新value
# ####################################
# def handle_update_value(k, v):
#     match k:
#         case 1:
#             global v1
#             v1 = v
#         case 2:
#             global v2
#             v2 = v
#         case 3:
#             global v3
#             v3 = v
#         case 4:
#             global v4
#             v4 = v
#         case 5:
#             global v5
#             v5 = v
#         case 6:
#             global v6
#             v6 = v
#         case 7:
#             global v7
#             v7 = v
#         case 8:
#             global v8
#             v8 = v
#         case 9:
#             global v9
#             v9 = v
