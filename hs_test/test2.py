import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x400")  # 设置窗口初始大小

# 创建 Notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")  # Notebook 填满窗口

# 创建 Frame 并添加到 Notebook 中
frame = ttk.Frame(notebook)
frame.pack(expand=True, fill="both")  # Frame 填满 Notebook
notebook.add(frame, text="Tab 1")

# 在 Frame 中创建 Listbox，并设置自动填充
listbox = tk.Listbox(frame)
listbox.pack(expand=True, fill="both")  # Listbox 填满 Frame

# 添加一些示例内容
for i in range(20):
    listbox.insert("end", f"Item {i + 1}")

root.mainloop()
