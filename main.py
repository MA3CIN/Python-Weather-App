# Press Shift+F10 to execute it or replace it with your code.
import tkinter as tk
from tkinter import *
import requests
import time

def getWeatherInfo(canvas):
    city = textfield.get()
    api = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=5fbf71bcc5acba7b0882d42f75e27f88'
    dane_json = requests.get(api).json()
    stats = dane_json['weather'][0]['main']
    temp = int(dane_json['main']['temp'] - 273.15)  #Konwertuje na C
    hum = dane_json['main']['humidity']


    calosc = stats + '\n' + 'Temperatura :' + str(temp) + '\n' + 'Wilgotnosc :' + str(hum)
    label1.config(text = calosc)
    label2.config(text = '')

canvas = tk.Tk()
# ToDo Case statement background zaleznie od weather main (stats)
#ToDo Error Handling
backgroundZdjecie = PhotoImage(file = "E:\Python Projekty\Pogoda\Chmury.png")
background_label = Label(canvas, image=backgroundZdjecie)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.geometry('600x500')
canvas.title('Pogoda app')
f = ('poppins', 15, 'bold')
t = ('poppins', 35, 'bold')
# @params yyy

textfield = tk.Entry(canvas, font = f)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeatherInfo)
# labele kolejne

label1 = tk.Label(canvas, font = t)
label1.pack()
# canvas.wm_attributes("-alpha",0.5)  #Alpha, ale na cale okno
label2 = tk.Label(canvas, font = f)
label2.pack()
canvas.mainloop()


