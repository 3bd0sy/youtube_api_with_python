from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
import config
from youtubeAPI import Search


def main():
    key = config.key
    key_word = box1.get()
    n = boxn.get()
    ord = comboi1.get()
    typ = comboi.get()

    result_list = Search(key, key_word, n, ord, typ)
    var = ""
    for result in result_list:
        var += f"name:{result['name']}\n"
        var += f"URL={result['url']}\n\n"
    box2.delete('1.0', END)
    box2.insert(END, var)


root = Tk()
root.title('Youtube API')
root.geometry('500x500')
root['bg'] = '#26F066'
lbl = Label(root, text='enter the keywords :'.title())
lbl.place(x=50, y=50)
lbl['bg'] = '#DE71E6'
box1 = Entry(root, width=20)
box1.place(x=190, y=50)
box1.insert(0, "syria")

lbla = Label(root, text='enter the number of result you wont : '.title())
lbla.place(x=50, y=80)
lbla['bg'] = '#DE71E6'
boxn = Entry(root, width=5, )
boxn.place(x=280, y=80)
boxn.insert(0, "3")

lblcom = Label(root, text='filters : '.title())
lblcom.place(x=50, y=120)
lblcom['bg'] = '#E87F1A'

comboi = ttk.Combobox(root, width=10)
comboi['values'] = ('video', 'channel', 'playlist',)
comboi.current(0)  # defines the selected item
comboi.place(x=100, y=120)

comboi1 = ttk.Combobox(root, width=10)
comboi1['values'] = ('date', 'rating', 'relevance', 'title', 'videoCount')
comboi1.current(0)  # defines the selected item
comboi1.place(x=200, y=120)

but = Button(root, text='search in youtube'.title(), fg='white')
but.place(x=200, y=200)
but['bg'] = '#259BE6'
lbl2 = Label(root, text='the results :'.title())
lbl2.place(x=200, y=250)
lbl2['bg'] = '#DE71E6'
box2 = scrolledtext.ScrolledText(root, undo=True, width=50, height=12)
box2.place(x=50, y=275)

but.config(command=main)
root.mainloop()
