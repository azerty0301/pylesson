import csv
import tkinter as tk
from tkinter import messagebox

qs=[]
qpath="quizUTF.csv"
total_count=0
ok_count=0
with open(qpath, encoding = "utf-8") as f:
    qs  =list(csv.reader(f))
qindex=0
def click_bt():
    global qindex,ok_count,total_count
    total_count+=1
    user_ans=iv.get()
    isOk=user_ans==int(qs[qindex][5])
    if isOk:
        ok_count+=1
    res="正解!" if isOk else f'不正解...正解は「{qs[qindex][int(qs[qindex][5])]}」'
    if total_count==len(qs):
        res=res+f'\n全{len(qs)}中{ok_count}正解でした!'
    messagebox.showinfo('確認', res)
    if total_count==len(qs):
        return
    qindex+=1
    label['text']=qs[qindex][0]
    rb1['text']=qs[qindex][1]
    rb2['text']=qs[qindex][2]
    rb3['text']=qs[qindex][3]
    rb4['text']=qs[qindex][4]
    iv.set(0)

root=tk.Tk()
root.title("クイズ")
root.geometry("500x300")

label=tk.Label(text=qs[qindex][0])
label.pack()
iv=tk.IntVar()
rb1=tk.Radiobutton(text=qs[qindex][1],value=1,variable=iv)
rb1.pack()
rb2=tk.Radiobutton(text=qs[qindex][2],value=2,variable=iv)
rb2.pack()
rb3=tk.Radiobutton(text=qs[qindex][3],value=3,variable=iv)
rb3.pack()
rb4=tk.Radiobutton(text=qs[qindex][4],value=4,variable=iv)
rb4.pack()
bt=tk.Button(text="click",command=click_bt)
bt.pack()
root.mainloop()
