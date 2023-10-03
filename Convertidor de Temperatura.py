import tkinter as tk

def borrar():
    entry1.delete(0,tk.END)
    entry1.insert(0, 0.0)
    entry2.delete(0,tk.END)
    entry2.insert(0, 0.0)

def Convertir_a_Celcius():
    Farenheit = float(entry1.get())
    Celsius = (Farenheit - 32)*5.0/9.0
    entry2.delete(0, tk.END)
    entry2.insert(0,str(Celsius))
    
def Convertir_a_Farenheit():
    Celcius = float(entry2.get())
    Farenheit = (Celcius*9/5)+32
    entry1.delete(0, tk.END)
    entry1.insert(0,str(Farenheit))

app = tk.Tk()
app.title("Conversor de Temperatura")

label1 = tk.Label(app, text ="Farenheit:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)

button1 = tk.Button(app, text = "Convertir a Celsius" , command = Convertir_a_Celcius)
button1.grid(row=0, column=2)

label2 = tk.Label(app, text = "Celcius:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(app)
entry2.grid(row=1 , column=1)

button2 = tk.Button(app, text = "Convertir a Farenheit:",command=Convertir_a_Farenheit)
button2.grid(row=1, column=2)

button3 = tk.Button(app, text = "Borrar" , command = borrar)
button3.grid(row=2, column=1)

app.mainloop()