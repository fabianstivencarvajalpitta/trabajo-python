from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter

class Producto:

    def __init__(self, window):
        self.window = window
        self.window.title('Productos')

        
        self.window.configure(bg='white')

        frame = LabelFrame(self.window, text='Registrar producto')
        frame.grid(row=0, column=0, columnspan=3, pady=20) 
        
        
        Label(frame, text='Nombre:', bg='white').grid(row=1, column=0)
        self.nombre = Entry(frame)
        self.nombre.grid(row=1, column=1)

        Label(frame, text='Precio:', bg='white').grid(row=2, column=0)
        self.precio = Entry(frame)
        self.precio.grid(row=2, column=1)



if __name__ == '__main__':
    window = Tk()

    
    window.geometry('400x300')

    application = Producto(window)
    window.mainloop()