import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action1():  # 関数の定義 ※ボタンが押されたときの動き # 入力値を取得
    seireki = int(num.get())
    if seireki <= 1912:
        genngo = "明治"
        wareki = seireki - 1867 + 1
    elif seireki < 1926:
        genngo = "大正"
        wareki = seireki - 1912 + 1
    elif seireki < 1926:
        genngo = "昭和"
        wareki = seireki - 1926 + 1
    elif seireki < 2019:
        genngo = "平成"
        wareki = seireki - 1989 + 1
    else:
        seireki > 2019
        genngo = "令和"
        wareki = seireki - 2019 + 1

    if num == 1:
        label1.config(text=f"西暦{seireki}年は{genngo}元年です")
    else:
        label1.config(text=f"西暦{seireki}年は{genngo}{wareki}年です")


num = tk.Entry(window, bg=fg_color, fg=bg_color)
num.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="Submit", command=button_action1)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
