from tkinter import *
from PIL import Image,ImageTk
import json
from difflib import get_close_matches

f=open("data.json")
data_load = json.load(f)

def search_word(word):
	if word in data_load:
		meaning_word.delete(1.0,END)
		meaning_word.config(fg='black')
		meaning_word.insert(END,data_load[word])

	elif len(get_close_matches(word,data_load.keys()))>0:
		meaning_word.config(fg='red')
		meaning_word.delete(1.0,END)
		meaning_word.insert(END,"Were you finding {} and meaning is:{}".format(get_close_matches(word,data_load.keys())[0],data_load[get_close_matches(word,data_load.keys())[0]]))
		final=get_close_matches(word,data_load.keys())

root=Tk()
root.title("Modern Dictionary")

image= Image.open('dict.png')
image_picture=ImageTk.PhotoImage(image)
dest_pic= Label(root,image=image_picture)
dest_pic.pack()

a=StringVar()
word_1=Entry(root,textvariable=a,background="blue",fg="white",font=('arial',40,"bold"))
word_1.place(relx=.185,rely=0.70,relwidth=.63,relheight=.08)

button_1=Button(root,text="Search The Word",command=lambda:search_word(a.get()),background='red',fg='white',font=('STENCIL',30,"bold"))
button_1.place(relx=0.25,rely=0.85,relwidth=.50,relheight=.052)

meaning_word=Text(root,background='white',font=('Comic Sans MS',20,"bold"))
meaning_word.place(relx=.20,rely=.05,relwidth=.63,relheight=.36)

root.mainloop()