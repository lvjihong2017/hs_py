import tkinter as tk
from tkinter import ttk
import win32gui
import win32con


class WindowTopMostTool:
    def __init__(self, root):
        self.root = root
        self.root.title("窗口工具")
        self.windows = []  # 存储窗口句柄和标题

        # 创建界面组件
        self.listbox = tk.Listbox(root, width=150, height=30)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        # 按钮框架
        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=5)

        # 刷新按钮
        refresh_btn = ttk.Button(btn_frame, text="刷新列表", command=self.refresh_windows)
        refresh_btn.pack(side=tk.LEFT, padx=5)

        # 置顶按钮
        topmost_btn = ttk.Button(btn_frame, text="设为置顶", command=self.set_topmost)
        topmost_btn.pack(side=tk.LEFT, padx=5)
        # 取消置顶按钮
        untopmost_btn = ttk.Button(btn_frame, text="取消置顶", command=self.unset_topmost)
        untopmost_btn.pack(side=tk.LEFT, padx=5)

        # 初始刷新窗口列表
        self.refresh_windows()

    def refresh_windows(self):
        """刷新当前窗口列表"""
        self.listbox.delete(0, tk.END)
        self.windows.clear()

        def enum_handler(hwnd, _):
            if win32gui.IsWindowVisible(hwnd):  # 仅处理可见窗口
                title = win32gui.GetWindowText(hwnd)
                if title.strip():  # 过滤空标题
                    self.windows.append((hwnd, title))

        win32gui.EnumWindows(enum_handler, None)
        for hwnd, title in self.windows:
            self.listbox.insert(tk.END, title)

    def set_topmost(self):
        """设置选中窗口为置顶"""
        selection = self.listbox.curselection()
        if not selection:
            return
        for index in selection:
            hwnd, title = self.windows[index]
            window_topmost(hwnd, True)

    def unset_topmost(self):
        selection = self.listbox.curselection()
        if not selection:
            return
        for index in selection:
            hwnd, title = self.windows[index]
            window_topmost(hwnd, False)


# 设置是否置顶
def window_topmost(hwnd, is_topmost):
    flag = win32con.HWND_TOPMOST if is_topmost else win32con.HWND_NOTOPMOST
    win32gui.SetWindowPos(
        hwnd,
        flag,
        0, 0, 0, 0,
        win32con.SWP_NOSIZE | win32con.SWP_NOMOVE | win32con.SWP_SHOWWINDOW
    )
    win32gui.SetForegroundWindow(hwnd)


if __name__ == "__main__":
    root = tk.Tk()
    app = WindowTopMostTool(root)
    root.mainloop()
