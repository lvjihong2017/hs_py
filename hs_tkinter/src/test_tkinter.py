import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("输入框示例")

# 创建标签
label1 = tk.Label(root, text="请输入文本:")
label1.pack()
label2 = tk.Label(root, text="")
label2.pack()

# 创建输入框
entry = tk.Entry(root)
entry.pack()


# 定义一个函数来获取输入框中的文本
def get_text():
    user_input = entry.get()
    label2.config(text=user_input)


# 创建一个按钮来获取文本框中的值
button = tk.Button(root, text="获取文本", command=get_text)
button.pack()

# 运行主循环
root.mainloop()
