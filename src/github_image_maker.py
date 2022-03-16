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
    import json
    import configparser as cfgp
except ModuleNotFoundError as NO_MODULE_ERROR:
    print(f"ModuleNotFoundError:{NO_MODULE_ERROR}")

class App(tk.Frame):
    def __init__(self, master, font_dot, color_data):
        super().__init__(master)
        self.pack()

        #メニューバー
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # 親メニュー
        self.file_menu = tk.Menu(master, tearoff=False)
        self.menu_bar.add_cascade(label="ファイル", menu=self.file_menu)

        self.config_menu = tk.Menu(master, tearoff=False)
        self.menu_bar.add_cascade(label="設定", menu=self.config_menu)

        # 子メニュー(ファイル)
        self.file_menu.add_command(label="新規作成")

        # キャンバス描画
        self.canvas = tk.Canvas(master, background="#ffffff", height=120, width=500)
        self.draw_canvas()

        # テキストボックス
        self.input_box = tk.Entry(width=40)
        self.input_box.place(x=30, y=250)

        # sendボタン
        self.send_string_button = tk.Button(master, text="OK", command=self.send_string).place(x=100, y=300)


    def rands(self):
        return random.randint(0, 100)

    def draw_canvas(self):
        self.canvas.delete("obj")
        # 図形描画
        self.canvas.create_polygon(self.rands(), self.rands(), self.rands(), self.rands(), self.rands(), self.rands(),fill="red", tags="obj")

        # 初期描画位置指定
        vertical = 10
        horizontal = 10

        # 空の要素を描画
        for i in range(48):
            horizontal = 10
            for j in range(7):
                self.canvas.create_rectangle(vertical, horizontal, vertical+10, horizontal+10, fill="#ebedf0", outline="#b0b4c0")
                horizontal += 15
            vertical += 15

        self.canvas.pack()
        self.after(1000, self.draw_canvas)

    def send_string(self):
        print(self.input_box.get())

# jsonファイル(フォントデータ)の読み込み
def read_json():
    with open("font_data.json", mode="r", encoding="UTF-8") as json_file:
        json_data = json.load(json_file)
    return json_data

# iniファイル(色定義ファイル)の読み込み
def read_ini():
    ini_data = cfgp.ConfigParser()
    ini_data.read("color_data.ini")
    return ini_data

def main():
    # フォントデータ読み込み(ドット)
    font_obj = read_json()
    # 色定義ファイルの読み込み(カラーコード)
    color_ini = read_ini()
    # App初期設定・実行
    widget = tk.Tk()
    widget.geometry("600x400")
    widget.title("GitHub Image Maker")
    app = App(master=widget, font_dot=font_obj, color_data=color_ini)
    app.mainloop()

if __name__ == "__main__":
    main()
