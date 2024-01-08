from tkinter import * #for accessing all classes
from tkinter import ttk #for using themed widget set
import requests
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q"+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(data["main"]["temp"]-273.15))
    pre_label1.config(text=data["main"]["pressure"])





win = Tk()
#"win" is the main window of the tkinter application
win.title("Weather Condition")
win.config(bg="red")
win.geometry("500x700")
name_label = Label(win, text="Weather Condition", font=("Time New Roman",30,"bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name= StringVar()
state_name =["Dhaka","Delhi","Colombo","Islamabad","Male","Kathmandu","Beijing","Kabul","Riyadh","Tehran","Doha"]
com = ttk.Combobox(win, text="Weather Condition", values=state_name,font=("Time New Roman",15,"bold"),textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_label = Label(win, text="Weather Climate", font=("Time New Roman",20))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text=" ", font=("Time New Roman",20))
w_label1.place(x=250, y=260, height=50, width=210)

wd_label = Label(win, text="Weather Description", font=("Time New Roman",15))
wd_label.place(x=25, y=330, height=50, width=210)
wd_label1 = Label(win, text=" ", font=("Time New Roman",20))
wd_label1.place(x=250, y=330, height=50, width=210)


temp_label = Label(win, text="Temperature", font=("Time New Roman",20))
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text=" ", font=("Time New Roman",20))
temp_label1.place(x=250, y=400, height=50, width=210)

pre_label = Label(win, text="Pressure", font=("Time New Roman",20))
pre_label.place(x=25, y=470, height=50, width=210)
pre_label1 = Label(win, text=" ", font=("Time New Roman",20))
pre_label1.place(x=250, y=470, height=50, width=210)

Button = Button(win, text="Done", font=("Time New Roman",20,"bold"),command=data_get)
Button.place(y=190, height=50,width=100,x=200)

win.mainloop()
