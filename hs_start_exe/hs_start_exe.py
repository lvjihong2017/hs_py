import time
import tkinter as tk
from tkinter import filedialog, messagebox, Menu, ttk, simpledialog
import subprocess
import sys
import json
import os


# 检查或创建配置文件
def check_or_create_config():
    if not os.path.exists('res/cfg.json'):
        # 创建一个包含路径和标题的结构
        with open('res/cfg.json', 'w') as f:
            json.dump({"tabs": [
                {"title": "Tab 1", "paths": []},
                {"title": "Tab 2", "paths": []},
                {"title": "Tab 3", "paths": []},
                {"title": "Tab 4", "paths": []},
                {"title": "Tab 5", "paths": []},
            ]}, f)


# 读取配置文件
def read_config():
    try:
        with open('res/cfg.json', 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        messagebox.showerror("Error", f"Failed to read config file: {e}")
        return {"tabs": [{"title": f"Tab {i + 1}", "paths": []} for i in range(5)]}  # 返回默认结构


# 保存配置文件
def save_config(config):
    try:
        with open('res/cfg.json', 'w') as f:
            json.dump(config, f)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save config file: {e}")


def rm_config():
    if os.path.exists('res/cfg.json'):
        os.remove('res/cfg.json')


# 打开应用程序
def open_applications(paths):
    for path in paths:
        try:
            subprocess.Popen(path)
            time.sleep(0.5)
        except Exception as e:
            if "740" in str(e):  # 检查错误信息中是否包含 740
                os.popen(path)
            else:
                messagebox.showerror("Error", f"打开失败: {path}\n{e}")


# 添加文件并更新列表
def add_file(tab_index):
    file_path = filedialog.askopenfilename()
    if file_path:
        config = read_config()
        config["tabs"][tab_index]["paths"].append(file_path)  # 修改路径位置
        save_config(config)
        update_listbox(tab_index, config["tabs"][tab_index]["paths"])


# 删除选中的文件
def delete_selected(tab_index):
    try:
        selection = listboxes[tab_index].curselection()
        if not selection:  # 没有选择项时显示警告
            messagebox.showwarning("Warning", "No item selected.")
            return

        # 获取选中项的索引
        selected_index = selection[0]

        # 获取当前配置文件
        config = read_config()

        # 删除选中的路径
        config["tabs"][tab_index]["paths"].pop(selected_index)

        # 保存更新后的配置
        save_config(config)

        # 更新列表框
        update_listbox(tab_index, config["tabs"][tab_index]["paths"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete item: {e}")


# 删除当前页签所有
def delete_all(tab_index):
    try:
        # 获取当前配置文件
        config = read_config()
        # 删除选中的路径
        config["tabs"][tab_index]["paths"] = []
        # 保存更新后的配置
        save_config(config)
        # 更新列表框
        update_listbox(tab_index, config["tabs"][tab_index]["paths"])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete item: {e}")


# 更新列表框
def update_listbox(tab_index, paths):
    listboxes[tab_index].delete(0, tk.END)
    for path in paths:
        listboxes[tab_index].insert(tk.END, path)


# 创建右键菜单（仅显示Delete）
def create_right_click_menu(tab_index):
    right_click_menu = Menu(root, tearoff=0)
    right_click_menu.add_command(label="Delete", command=lambda: delete_selected(tab_index))
    return right_click_menu


# 修改页签标题（重命名）——直接在页签标题位置编辑
def rename_tab(tab_index):
    config = read_config()
    new_name = simpledialog.askstring("修改标题", "输入新标题:", parent=notebook)
    if new_name:
        config["tabs"][tab_index]["title"] = new_name
        save_config(config)
        notebook.tab(tab_index, text=new_name)


# 更新配置文件中的页签标题
def update_tab_title_in_config(tab_index, new_title):
    config = read_config()
    config["tabs"][tab_index]["title"] = new_title  # 修改页签标题
    save_config(config)


# 设置GUI布局
def setup_gui():
    global root, listboxes, notebook
    root = tk.Tk()
    root.title("二师兄")
    # 置顶
    root.attributes('-topmost', True)
    # 默认大小
    root.geometry(f"{900}x{500}")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both")

    # 创建5个页签
    listboxes = []
    for i in range(5):
        frame = ttk.Frame(notebook)
        frame.pack(expand=True, fill="both")
        notebook.add(frame, text=f"Tab {i + 1}")
        listbox = tk.Listbox(frame)
        listbox.pack(expand=True, side=tk.LEFT, fill="both")
        listboxes.append(listbox)
        # 运行按钮
        btn_run = tk.Button(frame, text="启动", width=10, height=2,
                            command=lambda i=i: open_applications(read_config()["tabs"][i]["paths"]))
        btn_run.pack(pady=1, padx=10)
        # 添加按钮
        btn_add = tk.Button(frame, text="添加程序", width=10, height=2, command=lambda i=i: add_file(i))
        btn_add.pack(pady=1, padx=10)
        # 删除按钮
        btn_del = tk.Button(frame, text="删除程序", width=10, height=2, command=lambda i=i: delete_selected(i))
        btn_del.pack(pady=1, padx=10)
        # 删除按钮
        btn_del_all = tk.Button(frame, text="全部删除", width=10, height=2, command=lambda i=i: delete_all(i))
        btn_del_all.pack(pady=1, padx=10)
        # 重命名
        btn_rename = tk.Button(frame, text="修改标题", width=10, height=2,
                               command=lambda i=i: rename_tab(i))
        btn_rename.pack(pady=1, padx=10)

    check_or_create_config()
    config = read_config()

    try:
        for i, tab in enumerate(config["tabs"]):
            update_listbox(i, tab["paths"])
            notebook.tab(i, text=tab["title"])  # 设置标题
    except Exception as e:
        messagebox.showerror("Error", f"文件格式错误，删除res目录下cfg.json，自动恢复初始状态")

    root.mainloop()


if __name__ == "__main__":
    setup_gui()
