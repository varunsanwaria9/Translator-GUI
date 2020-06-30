from googletrans import Translator,LANGUAGES
from tkinter import StringVar,Tk,OptionMenu,Entry,Button,Label

root = Tk()
root.geometry("600x400")
root.title("Translator")
tr = Translator()

def T():
    t = tr.translate(sentence.get(),dest=varq.get().split("-")[0])
    Label(root,text=f"{sentence.get()} -> {t.text}",font="Corier 20 italic").pack(pady=10) 

lang = []
for l in LANGUAGES:
    lang.append(f"{l}- {LANGUAGES[l]}")
varq = StringVar(root)
varq.set(lang[3])
lang_menu = OptionMenu(root,varq,*lang)
lang_menu.pack(pady=20)
sentence = Entry(root,width=40)
sentence.pack(pady=10)
Button(root,text="Translate",command=T).pack(pady=10)
root.mainloop()