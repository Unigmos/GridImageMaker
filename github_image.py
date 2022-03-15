#-------------------------------------------------------------------------------
# Name:         GitHubImageMaker
# Purpose:      GitHubのグリッド風の画像生成プログラムです
#
# Author:       Shaneron
#
# Created:      15/03/2022
# Copyright:    (c) Shaneron 2022
#-------------------------------------------------------------------------------

try:
    import tkinter as tk
    import random
except ModuleNotFoundError as NO_MODULE_ERROR:
    print(f"ModuleNotFoundError:{NO_MODULE_ERROR}")

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        #メニューバー
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # 親メニュー
        self.menus = tk.Menu(master)
        self.menu_bar.add_cascade(label="ファイル", menu=self.menus)

        # 子メニュー
        self.menus.add_command(label="新規作成")

        # キャンバス描画
        self.canvas = tk.Canvas(master, background="#ffffff", height=300, width=300)

        master.after(10, self.draw_canvas)


    def rands(self):
        x = random.randint(50, 300)
        return x

    def draw_canvas(self):
        self.canvas.delete("obj")
        # 図形描画
        self.canvas.create_polygon(self.rands(), self.rands(), self.rands(), self.rands(), self.rands(), self.rands(),fill="red", tags="obj")
        self.canvas.create_rectangle(100, 100, 200, 200, fill="#ebedf0", outline="#b0b4c0")

        self.canvas.pack()
        self.after(50, self.draw_canvas)

def main():
    widget = tk.Tk()
    widget.geometry("600x400")
    widget.title("GitHub Image Maker")
    app = App(master=widget)
    app.mainloop()

if __name__ == "__main__":
    main()
