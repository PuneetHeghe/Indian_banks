from tkinter import *
import bank_backend
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
def ifsc_command():
    list1.delete(0,END)
    for row in bank_backend.ifsc_get(ifsc_text.get()):
        list1.insert(END,row)
    
def city_command():
    list1.delete(0,END)
    for row in bank_backend.branch_city_get(bank_name_text.get(),city_text.get()):
        list1.insert(END,row)

window=Tk()

window.wm_title("Indian Banks")

l1=Label(window,text="IFSC")
l1.grid(row=0,column=0)

l2=Label(window,text="Bank Name")
l2.grid(row=0,column=2)

l3=Label(window,text="City")
l3.grid(row=1,column=2)

ifsc_text=StringVar()
e1=Entry(window,textvariable=ifsc_text)
e1.grid(row=0,column=1)

bank_name_text=StringVar()
e2=Entry(window,textvariable=bank_name_text)
e2.grid(row=0,column=3)

city_text=StringVar()
e3=Entry(window,textvariable=city_text)
e3.grid(row=1,column=3)

list1=Listbox(window, height=10,width=100)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=10)
sb2=Scrollbar(window,orient=HORIZONTAL)
sb2.grid(row=9,column=1,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="search by IFSC", width=25,command=ifsc_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search by City and Bank Name", width=25,command=city_command)
b2.grid(row=3,column=3)

b6=Button(window,text="Close", width=25,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
