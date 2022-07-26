import tkinter as tk
from tkinter import messagebox
import random
import csv
import pandas as pd

quizQuantity = 40

root = tk.Tk()
root.title('Quiz')
root.geometry('600x400')
var = tk.IntVar()
var.set(0)
indexList = list(range(40))
random.shuffle(indexList)
quiz_index = 0
totalcount=40
correct=0
qLabel=None




df = pd.read_csv('quizU.csv', encoding = 'utf-8')
def selector():
    global quiz_index
    while True:
        quiz_index = random.randrange(totalcount)
        if len(indexChosen)==0:
            indexChosen.append(quiz_index)
        else:
            for i in indexChosen:
                if quiz_index in indexChosen:
                    quiz_index = random.randrange(totalcount)
                if quiz_index not in indexChosen:
                    indexChosen.append(quiz_index)
                    return

def clickBtn():
    global totalcount,indexChosen,quiz_index,correct,qLabel,button,indexList
    button['text']='OK'
    totalcount += 1 
    if not qLabel == None:    
        qLabel.pack_forget()
        button.place_forget()
    

    #print(quiz_index)
    qLabel = tk.Label(root, text = df.iloc[indexList[quiz_index],0])
    qLabel.pack()

    for i in range(4):
        radioButton = tk.Radiobutton(root, value=i+1, variable=var, text=df.iloc[indexList[quiz_index],i+1])
        radioButton.place(x=10, y=100+40*i)

    userAns = var.get()
    ans_index = df.iloc[indexList[quiz_index],5]
    quiz_index += 1
    print(userAns)
    print(ans_index)

    if button['text']=='OK':
        if userAns == ans_index:
            correct += 1
            messagebox.showinfo("結果", "正解です！！")
        else:
            
            answer = df.iloc[quiz_index, ans_index]
            messagebox.showerror("結果", "不正解です。\n"+ answer)
    print(correct)

button=startButton = tk.Button(
    text = 'START',
    command = clickBtn
    )
startButton.place(x=10, y=300)

root.mainloop()