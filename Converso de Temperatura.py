from tkinter import *

# Função para calcular a conversão da temperatura
# C = (F - 32) * 5/9

def calcular():
    F = float(textbox1.get())
    C = (F-32) * 5/6
    final.set(str(round(C,1)) + " graus Celsius")

# Interface Gráfica
root = Tk()
root.title("Conversor de Temperatura")
final = StringVar()

# Cálculos e Informações da conversão da temperatura
label1=Label(root,text="Graus Fahrenheit: ")
textbox1=Entry(root)
button1=Button(root,text="Calcular", command=calcular)
label_resultado=Label(root, textvariable=final)

#layout
label1.grid()
textbox1.grid()
button1.grid()
label_resultado.grid()

root.mainloop()
