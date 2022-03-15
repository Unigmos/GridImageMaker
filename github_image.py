#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shaneron
#
# Created:     15/03/2022
# Copyright:   (c) Shaneron 2022
#-------------------------------------------------------------------------------

import tkinter as tk
import random

class App(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        # キャンバス描画
        self.canvas = tk.Canvas(master, background="white", height=300, width=300)

        master.after(10, self.draw_canvas)

    def rands(self):
        x = random.randint(50, 300)
        return x

    def draw_canvas(self):
        self.canvas.delete("obj")
        # 図形描画
        self.canvas.create_polygon(self.rands(), self.rands(), self.rands(), self.rands(), self.rands(), self.rands(),fill="red", tags="obj")

        self.canvas.pack()
        self.after(50, self.draw_canvas)

def main():
    widget = tk.Tk()
    widget.geometry("600x400")
    widget.title("Random Shape")
    app = App(master=widget)
    app.mainloop()

if __name__ == "__main__":
    main()