import tkinter as tk
from tkinter import ttk


def add_item(tab_index):
    item = "abc"
    listboxes[tab_index].insert(tk.END, item)


def delete_item(tab_index):
    selected = listboxes[tab_index].curselection()
    if selected:
        listboxes[tab_index].delete(selected)


def setup_gui():
    global listboxes

    root = tk.Tk()
    root.title("Notebook with Listbox Example")

    # 创建 Notebook
    notebook = ttk.Notebook(root)
    notebook.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    # 创建 3 个页面
    listboxes = []
    for i in range(3):  # 假设我们有3个页签
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=f"Tab {i + 1}")

        # 在每个页面中创建 Listbox
        listbox = tk.Listbox(frame)
        listbox.pack(expand=True, fill=tk.BOTH)
        listboxes.append(listbox)

        # 向 Listbox 添加初始内容
        listbox.insert(tk.END, f"Item 1 for Tab {i + 1}")
        listbox.insert(tk.END, f"Item 2 for Tab {i + 1}")
        listbox.insert(tk.END, f"Item 3 for Tab {i + 1}")

        # 创建添加和删除按钮
        btn_add = tk.Button(frame, text="Add Item", command=lambda i=i: add_item(i))
        btn_add.pack(side=tk.LEFT, padx=5, pady=5)

        btn_delete = tk.Button(frame, text="Delete Item", command=lambda i=i: delete_item(i))
        btn_delete.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    setup_gui()
