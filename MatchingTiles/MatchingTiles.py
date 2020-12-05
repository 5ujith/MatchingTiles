from tkinter import *
import random
from tkinter import messagebox
root=Tk()
root.title('MatchingTiles')
root.geometry("500x400")
root.iconbitmap('C:/Users/Sujith/Documents/MatchingTiles/matchingtiles.ico')
root.resizable(False,False)
bgimage=PhotoImage(file='C:/Users/Sujith/Documents/MatchingTiles/matchingtiles2.png')
photolabel=Label(root,image=bgimage)
photolabel.place(relx=0,rely=0,relheight=1,relwidth=1)

#matches
matches=[0,0,1,1,2,2,3,3,4,4,5,5]
#shuffle
random.shuffle(matches)
#frame
frame=Frame(root)
frame.pack()
bottomframe=Frame(root)
bottomframe.pack(side='bottom')
#function
count=0
match_list=[]
match_dic={}
def buttonclick(b,no):
    global count,match_list,match_dic
    if b['text']=='' and count<2:
        b['text']=matches[no]
        match_list.append(no)
        match_dic[b]=matches[no]
        count+=1
        print(match_list)
    if len(match_list)==2:
        if matches[match_list[0]]==matches[match_list[1]]:
            matchlabel.config(text='MATCH')
            for key in match_dic:
                key['state']='disabled'
            count=0
            match_list=[]
            match_dic={}
        else:
            matchlabel.config(text='OOPS!')
            match_list=[]
            count=0
            messagebox.showinfo('Incorrect!','Incorrect!')
            for key in match_dic:
                key['text']=''
            match_dic={}

#buttons
b0=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b0,0))
b1=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b1,1))
b2=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b2,2))
b3=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b3,3))
b4=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b4,4))
b5=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b5,5))
b6=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b6,6))
b7=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b7,7))
b8=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b8,8))
b9=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b9,9))
b10=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b10,10))
b11=Button(frame,text='',font=('Helvetica',20),bg='#ffcc33',height=3,width=6,command=lambda:buttonclick(b11,11))


b0.grid(row=1,column=0)
b1.grid(row=1,column=1)
b2.grid(row=1,column=2)
b3.grid(row=1,column=3)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=2,column=3)

b8.grid(row=3,column=0)
b9.grid(row=3,column=1)
b10.grid(row=3,column=2)
b11.grid(row=3,column=3)

#matchlabel
matchlabel=Label(root,text='')
matchlabel.pack()

root.mainloop()
