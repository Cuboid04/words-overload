from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Random Words")
import random
list1=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
print(list1)

label=Label(root)
label.place(relx=0.5, rely=0.7, anchor=CENTER)
def random_name():
    random_no = random.randint(0, 25)
    print(random_no)
    name1=list1[random_no]
    random_no2= random.randint(0, 25)
    name2=list1[random_no2]
    random_no3= random.randint(0, 25)
    name3=list1[random_no3]
    random_no4= random.randint(0, 25)
    name4=list1[random_no4]
    random_no5= random.randint(0, 25)
    name5=list1[random_no5]
    word=name1 + name2 + name3 + name4 + name5
    label["text"] = str(word)
btn=Button(root, text="Generate A Word", command=random_name)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()