import tkinter
import tkinter.messagebox
#import numpy as np
import random

window = tkinter.Tk()

hyouzi = []#空のリスト
#kaisuu = 0
window.title("bingo!!")#title


#ボタン押下時処理
def button_click():
    kazu = len(hyouzi)
#乱数生成
    kari=random.randint(1,75)
    print(kari)
#    kaisuu += 1
#    if len(hyouzi) == 1:
#       hyouzi.insert(1,kari)
#    else:
#重複回避
    while True:
        if kari in hyouzi:
            kari=random.randint(1,75)
        else:
            hyouzi.insert(0,kari)
            break

    print(hyouzi)#リスト内確認
#    print(kazu)
#各表示の更新
    Text.set(hyouzi[0])

    if kazu >= 1:
        Text2.set(hyouzi[1:kazu+1])
    else:
        pass

    count_Text.set(kazu+1)

def reset_click():
    hyouzi.clear()
    print(hyouzi)
    kazu = len(hyouzi)
    print(kazu)
    Text.set("-")
    Text2.set("-")
    count_Text.set(kazu)

    
#結果表示部分
Text_sp = tkinter.Label(window,text="結果",font = (20))
Text = tkinter.StringVar()
Text.set ("-")
label = tkinter.Label(window,textvariable = Text,font = ("Times",30,'bold'))

#ボタン部分
btn1 = tkinter.Button(window, text=f"抽選開始",command=button_click)#command=~でdef~に飛ぶ

#履歴部分
rireki_sp = tkinter.Label(window,text="履歴")
Text2 = tkinter.StringVar()
Text2.set("-")
rireki1 = tkinter.Message(window,aspect=300,textvariable = Text2,width=200,)

#回数カウント
ct_sp = tkinter.Label(window,text="現在の抽選回数")
count_Text = tkinter.StringVar()
count_Text.set(0)
count = tkinter.Label(window,textvariable = count_Text)

#リセットボタン
reset_btn = tkinter.Button(window, text=f"リセット",command = reset_click)#command=~でdef~に飛ぶ

#packで表示
Text_sp.pack()
label.pack()
btn1.pack()
rireki_sp.pack()
rireki1.pack()
ct_sp.pack()
count.pack()
reset_btn.pack()

window.geometry("400x300")
window.mainloop()