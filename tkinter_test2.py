import tkinter as tk
import tkinter.messagebox as tkmg
import random

class Aplication(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=380,height=480,
                         borderwidth=4,relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):

        #結果表示部分
        Text_sp = tk.Label(self,text="結果",font = (20))
        self.Text = tk.StringVar()#別のdefで参照する変数はself.~にする
        self.Text.set ("-")
        label = tk.Label(self,textvariable = self.Text,font = ("Times",30,'bold'))

        #抽選ボタン
        start_btn = tk.Button(self, text="抽選開始",command=self.button_click)#command=~でdef~に飛ぶ

        #履歴部分
        self.rireki_sp = tk.LabelFrame(self,text="履歴",padx=10,pady=10)
        self.Text2 = tk.StringVar()
        self.Text2.set("-")
        rireki1 = tk.Message(self.rireki_sp,textvariable = self.Text2,width=100,anchor="nw")

        #回数カウント
        ct_sp = tk.Label(self,text="現在の抽選回数")
        self.count_Text = tk.StringVar()
        self.count_Text.set(0)
        count = tk.Label(self,textvariable = self.count_Text)

        #リセットボタン
        reset_btn = tk.Button(self, text="リセット",command =self.reset_click)#command=~でdef~に飛ぶ


        #閉じるボタン
        quit_btn = tk.Button(self)
        quit_btn['text'] ='終了'
        quit_btn['command'] = self.root.destroy

        #Widgetの配置
        Text_sp.grid(row=0,column=1)
        label.grid(row=1,column=1)
        start_btn.grid(row=4,column=1)
        self.rireki_sp.grid(row=5,column=0,columnspan=3,rowspan=2)
        rireki1.grid(in_=self.rireki_sp,row=0,column=0)
        ct_sp.grid(row=10,column=0,columnspan=3)
        count.grid(row=11,column=1)
        reset_btn.grid(row=13,column=0)
        quit_btn.grid(row=13,column=2)

    def button_click(self):
        kazu = len(hyouzi)
        #乱数生成
        kari=random.randint(1,75)
        print(kari)
        #重複回避
        while True:
            if not kari in hyouzi:
                hyouzi.insert(0,kari)
                break
            else:
                #75個以上のときの実装
                if kazu < 75: 
                    kari=random.randint(1,75)
                else:
                    tkmg.showinfo("テスト","リセットしてください")
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
        #print(hyouzi)
        kazu = len(hyouzi)
        #print(kazu)
        self.Text.set("-")
        self.Text2.set("-")
        self.count_Text.set(kazu)

root = tk.Tk()
hyouzi = []#空のリスト
#hyouzi.clear()
root.title("bingo!!")#title
root.geometry("400x500")
app = Aplication(root=root)
app.mainloop()