import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

name_list = []


def button_action1():
    user_input = entry1.get()
    name_out = ""
    name_list.append(user_input)
    for i in name_list:
        name_out += f"{i}\n"
    label1.config(text=name_out)


def button_action2():
    import random

    num = len(name_list)
    label2.config(text=name_list[random.randrange(num)])


entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)
# ボタンの作成
button1 = tk.Button(window, text="追加", command=button_action1)
button1.pack(pady=10)
button2 = tk.Button(window, text="ランダム", command=button_action2)
button2.pack(pady=10)
# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)
# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコー
