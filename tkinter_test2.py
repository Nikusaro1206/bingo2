import tkinter as tk
import random

class Aplication(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=380,height=280,
                         borderwidth=4,relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):

        #結果表示部分
        Text_sp = tk.Label(self,text="結果",font = (20))
        Text_sp.pack()
        self.Text = tk.StringVar()
        self.Text.set ("-")
        self.label = tk.Label(self,textvariable = self.Text,font = ("Times",30,'bold'))
        self.label.pack()

        #抽選ボタン
        start_btn = tk.Button(self, text="抽選開始",command=self.button_click)#command=~でdef~に飛ぶ
        start_btn.pack()

        #履歴部分
        rireki_sp = tk.Label(self,text="履歴")
        rireki_sp.pack()
        self.Text2 = tk.StringVar()
        self.Text2.set("-")
        rireki1 = tk.Message(self,aspect=300,textvariable = self.Text2,width=200,)
        rireki1.pack()

        #回数カウント
        ct_sp = tk.Label(self,text="現在の抽選回数")
        ct_sp.pack()
        self.count_Text = tk.StringVar()
        self.count_Text.set(0)
        count = tk.Label(self,textvariable = self.count_Text)
        count.pack()

        #リセットボタン
        reset_btn = tk.Button(self, text="リセット",command =self.reset_click)#command=~でdef~に飛ぶ
        reset_btn.pack()


        #閉じるボタン
        quit_btn = tk.Button(self)
        quit_btn['text'] ='終了'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side = 'bottom')

    def button_click(self):
        kazu = len(hyouzi)
        #乱数生成
        kari=random.randint(1,75)
        print(kari)
        #重複回避
        while True:
            if kari in hyouzi:
                kari=random.randint(1,75)
            else:
                hyouzi.insert(0,kari)
                break

        print(hyouzi)#リスト内確認
        #print(kazu)
        #各表示の更新
        self.Text.set(hyouzi[0])
        if kazu >= 1:
            self.Text2.set(hyouzi[1:kazu+1])
        else:
            pass
        self.count_Text.set(kazu+1)

    def reset_click(self):
        hyouzi.clear()
        print(hyouzi)
        kazu = len(hyouzi)
        print(kazu)
        self.Text.set("-")
        self.Text2.set("-")
        self.count_Text.set(kazu)

root = tk.Tk()
hyouzi = []#空のリスト
root.title("bingo!!")#title
root.geometry("400x300")
app = Aplication(root=root)
app.mainloop()