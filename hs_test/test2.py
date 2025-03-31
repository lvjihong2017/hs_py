
import tkinter as tk

root = tk.Tk()
root.title("Listbox 自动调整大小")

# 创建 Listbox
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)  # 核心参数

# 添加示例数据
for i in range(1, 20):
    listbox.insert(tk.END, f"项目项目项目项目项目项目项目项目项目项目项目项目项目项目项目项目项目项目项目项目项目项目项目项目项目 {i}")

root.mainloop()