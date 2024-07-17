import tkinter as tk

# import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

player_1 = "◯"
player_2 = "x"
table = [["◯", "", ""], ["", "", ""], ["", "", ""]]
word_1 = "win"


def action(x, y):
    # 自分のマークをつける
    table[x][y] = player_1
    # 自分の勝利判定
    if table[x][y] == player_1 and table[x][y] == player_1 and table[x][y] == player_1:
        label1.config(table=word_1)
    # 相手のマークを開いているところにつける

    # 相手の勝利判定


def button_action1():
    button1.config(text=player_1)
    action(0, 0)


def button_action2():
    button2.config(text=player_1)
    action(0, 1)


def button_action3():
    button3.config(text=player_1)
    action(0, 2)


def button_action4():
    button4.config(text=player_1)
    action(1, 0)


def button_action5():
    button5.config(text=player_1)
    action(1, 1)


def button_action6():
    button6.config(text=player_1)
    action(1, 2)


def button_action7():
    button7.config(text=player_1)
    action(2, 0)


def button_action8():
    button8.config(text=player_1)
    action(2, 1)


def button_action9():
    button9.config(text=player_1)
    action(2, 2)


button1 = tk.Button(window, text="", command=button_action1, width=3, height=3)
button1.pack(pady=10)
button1.place(x=200, y=100)

button2 = tk.Button(window, text="", command=button_action2, width=3, height=3)
button2.pack(pady=10)
button2.place(x=270, y=100)

button3 = tk.Button(window, text="", command=button_action3, width=3, height=3)
button3.pack(pady=10)
button3.place(x=340, y=100)

button4 = tk.Button(window, text="", command=button_action4, width=3, height=3)
button4.pack(pady=10)
button4.place(x=200, y=170)

button5 = tk.Button(window, text="", command=button_action5, width=3, height=3)
button5.pack(pady=10)
button5.place(x=270, y=170)

button6 = tk.Button(window, text="", command=button_action6, width=3, height=3)
button6.pack(pady=10)
button6.place(x=340, y=170)

button7 = tk.Button(window, text="", command=button_action7, width=3, height=3)
button7.pack(pady=10)
button7.place(x=200, y=240)

button8 = tk.Button(window, text="", command=button_action8, width=3, height=3)
button8.pack(pady=10)
button8.place(x=270, y=240)

button9 = tk.Button(window, text="", command=button_action9, width=3, height=3)
button9.pack(pady=10)
button9.place(x=340, y=240)


# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
