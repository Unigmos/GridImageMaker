#-------------------------------------------------------------------------------
# Name:         GitHubImageMaker
# Purpose:      GitHubのグリッド風の画像生成プログラムです
#
# Author:       Shaneron
#
# Created:      15/03/2022
# Copyright:    (c) Shaneron 2022
#-------------------------------------------------------------------------------

# ライブラリのimport
try:
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import filedialog
    import random
    import json
    import configparser as cfgp
except ModuleNotFoundError as NO_MODULE_ERROR:
    print(f"ModuleNotFoundError:{NO_MODULE_ERROR}")

class App(tk.Frame):
    def __init__(self, master, font_dot, definition_data):
        super().__init__(master)
        self.pack()

        # ×ボタンでの終了
        master.protocol("WM_DELETE_WINDOW", self.close_app)

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
        self.file_menu.add_command(label="名前を付けて保存", command=self.ask_save)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="閉じる", command=self.close_app)

        # 子メニュー(設定)
        self.config_menu.add_command(label="サイズ変更", command=self.change_size)
        #self.config_menu.add_command(label="描画設定", command=self.change_style)

        # キャンバス描画
        self.canvas = tk.Canvas(master, background="#ffffff", width=500, height=120)
        self.draw_canvas()

        # テキストボックス(描画文字用)
        self.input_box = tk.Entry(width=30, font=("", 20))
        self.input_box.place(x=30, y=250)

        # 反映ボタン(draw_strings:引数はfont_data.jsonの中身)
        tk.Button(master, text="OK", relief="groove", command=lambda:self.draw_strings(font_dot_json=font_dot, colors=definition_data)).place(x=100, y=300)

    def rands(self):
        return random.randint(0, 100)

    def draw_canvas(self, row=7, column=30):
        # 再描画時、過去に描画したオブジェクトの削除
        self.canvas.delete("obj")

        # 初期描画位置指定
        vertical = 10
        horizontal = 10

        # 空の要素を描画
        for i in range(column):
            vertical = 10
            for j in range(row):
                # 四角形描画、引数(x始点, y始点, x終点, y終点, fill:塗りつぶし, outline:枠線, tags:タグ)
                self.canvas.create_rectangle(horizontal, vertical, horizontal+10, vertical+10, fill="#ebedf0", outline="#b0b4c0", tags="obj")
                vertical += 15
            horizontal += 15

        self.canvas.pack()

    # 記入された文字列を描画
    def draw_strings(self, font_dot_json, colors):
        print(self.input_box.get())
        print(font_dot_json)

        # 過去に描画した文字列の削除
        self.canvas.delete("font")

        # 初期描画位置指定
        vertical = 10
        horizontal = -95
        new_pos = 10

        # 文字列をlist分け・1文字ずつ判定
        list_str = list(self.input_box.get())
        for strs in list_str:
            try:
                print(font_dot_json[strs])
                # 2次元配列ドットデータ(font_dot_json)から1つずつ抽出
                for row_dots in font_dot_json[strs]:
                    horizontal = new_pos
                    for dot in row_dots:
                        print(dot)
                        if dot == 1:
                            self.canvas.create_rectangle(horizontal, vertical, horizontal+10, vertical+10, fill=colors["LIGHTMODE"]["high_green"], outline=colors["LIGHTMODE"]["high_green_frame"], tags="font")
                            horizontal += 15
                        elif dot == 0:
                            horizontal += 15
                        else:
                            messagebox.showerror(title="Data Error!!", message="font_data.jsonのデータが不正です。\nデータに「0」もしくは「1」以外の数値、文字列が含まれています。")
                    vertical += 15
                vertical = 10
                new_pos += 120
            except KeyError:
                messagebox.showerror(title="Key Error!!", message="未対応の文字列を入力している可能性があります。\n現在対応済みの文字列は大文字英語と「 」(スペース)です。")

    # 名前を付けて保存
    def ask_save(self):
        file_data = filedialog.asksaveasfilename(title="名前を付けて保存", filetype=[("postscript", ".ps")])
        self.canvas.update()
        self.canvas.postscript(file=f"{file_data}.ps", colormode="color")

    # アプリケーションの終了
    def close_app(self):
        self.close_ans = messagebox.askyesno(title="確認", message="ウィンドウを閉じますか？")
        # はい(yes)選択時のみ終了する
        if self.close_ans:
            self.master.destroy()

    # Canvasサイズ変更ダイアログ
    def change_size(self):
        change_size_window = tk.Toplevel()
        change_size_window.geometry("250x200")
        change_size_window.title("サイズ変更")
        change_size_window.resizable(width=False, height=False)

        # 横サイズLabel・Entry
        x_size_label = tk.Label(change_size_window, text="横サイズ")
        x_size_label.place(x=20, y=20)
        self.x_size_box = tk.Entry(change_size_window, width=20)
        self.x_size_box.insert(tk.END, 500)
        self.x_size_box.place(x=100, y=20)

        # 縦サイズLabel・Entry
        y_size_label = tk.Label(change_size_window, text="縦サイズ")
        y_size_label.place(x=20, y=50)
        self.y_size_box = tk.Entry(change_size_window, width=20)
        self.y_size_box.insert(tk.END, 120)
        self.y_size_box.place(x=100, y=50)

        # 行数Label・Entry
        row_size_label = tk.Label(change_size_window, text="行の数")
        row_size_label.place(x=20, y=100)
        self.row_size_box = tk.Entry(change_size_window, width=20)
        self.row_size_box.insert(tk.END, 7)
        self.row_size_box.place(x=100, y=100)

        # 列数Label・Entry
        column_size_label = tk.Label(change_size_window, text="列の数")
        column_size_label.place(x=20, y=130)
        self.column_size_box = tk.Entry(change_size_window, width=20)
        self.column_size_box.insert(tk.END, 30)
        self.column_size_box.place(x=100, y=130)

        # 反映ボタン
        tk.Button(change_size_window, text="OK", relief="groove", command=self.re_create_canvas).place(x=200, y=160)

    def re_create_canvas(self):
        # キャンバス再描画
        self.canvas.pack_forget()
        self.canvas = tk.Canvas(self.master, background="#333333", width=600, height=120)
        self.draw_canvas()

# jsonファイル(フォントデータ)の読み込み
def read_json():
    with open("font_data.json", mode="r", encoding="UTF-8") as json_file:
        json_data = json.load(json_file)
    return json_data

# iniファイル(色定義ファイル)の読み込み
def read_ini():
    ini_data = cfgp.ConfigParser()
    ini_data.read("definition_data.ini")
    return ini_data

def main():
    # フォントデータ読み込み(ドット)
    font_data = read_json()
    # 色定義ファイルの読み込み(カラーコード)
    definition_ini = read_ini()
    # App初期設定・実行
    widget = tk.Tk()
    widget.geometry("600x400")
    widget.title("Image Maker")
    app = App(master=widget, font_dot=font_data, definition_data=definition_ini)
    app.mainloop()

if __name__ == "__main__":
    main()
