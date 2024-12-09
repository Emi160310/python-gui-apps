import tkinter as tk

# import random
from tkinter import messagebox
# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

player_1 = "罪"
player_2 = "罰"

current_player=player_1

buttons=[]

for i in range(9):
    button=tk.Button(
        window,text=""comand=lambda i=i: button_action(i),width=3,height=3
    )
    buttons.append(button)


buttons[0].place(x=200,y=100)
buttons[1].place(x=270,y=100)
buttons[2].place(x=340,y=100)
buttons[3].place(x=200,y=170)
buttons[4].place(x=270,y=170)
buttons[5].place(x=340,y=170)
buttons[6].place(x=200,y=240)
buttons[7].place(x=270,y=240)
buttons[8].place(x=340,y=240)



def button_action(index):
     global current_player




     if buttons[index]["text"]=="":
          buttons[index]["text"]=current_player
    
     if is_winner(current_player):
                   
        messagebox.showinfo("勝利",f"{current_player}の勝利です。おめでとうございます")
        widow.quit()

     elif all(button["text"] !=for button in buttons):
                messagebox.showinfo(
                    "引き分け","引き分けですね。"
                )
                window.puit()

     else:
               current_player=player_2 if current_player==player_1 else player_1
     else:
         messagebox.showarning("無効","そうマスはもう選べません。")

def is_winner(symbol):


    winning_combinations=[
        #横
        (0,1,2,),
        (3,4,5,),
        (6,7,8,),
        #縦
        (0.3,6),
        (1,4,7),
        (2,5,8),
        #斜め
        (0,4,8),
        (2,4,6),
    ]

    for combo in winning_combinations:
        if(
            buttons[combo[0]]["text"] ==symbol
            and buttons[combo[1]]["text"]==symbol
            and buttons[combo[2]]["text"]==symbol
        ):
            return True
        

    return False

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑