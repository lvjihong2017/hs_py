import json5
import tkinter as tk
from hs_view import Panel1


class Auto(Panel1):
    db = None
    cfg = None

    def __init__(self, root):
        super().__init__(root)  # 调用父类的__init__方法来初始化父类属性
        self.init_cfg()

    # 初始化配置
    def init_cfg(self):
        with open('res/cfg.json', 'r') as f: self.cfg = json5.load(f)
        with open('res/db.json', 'r') as f: self.db = json5.load(f)

    # 运行，重写父方法
    def handle_run(self):
        self.v9 = self.db


def main():
    root = tk.Tk()
    app = Auto(root)
    root.mainloop()


if __name__ == "__main__":
    main()
