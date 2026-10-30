import tkinter as tk
from tkinter import messagebox
from estadisticas import mostrar_estadisticas
from burbuja import ordenar_burbuja

# Esta lista comienza vacía. Se compartirá con las funciones de inventario.
productos = []


def funcion_pendiente():
    messagebox.showinfo('Beauty Stock', 'Aquí se conectará la función de inventario.')


def abrir_menu():
    ventana = tk.Tk()
    ventana.title('Beauty Stock JyD')
    ventana.geometry('440x540')
    ventana.configure(bg='#FFF9F7')

    titulo = tk.Label(
        ventana, text='BEAUTY STOCK JyD', font=('Arial', 20, 'bold'),
        bg='#FFF9F7', fg='#785964'
    )
    titulo.pack(pady=25)

    subtitulo = tk.Label(
        ventana, text='Sistema de inventario de maquillaje',
        font=('Arial', 11), bg='#FFF9F7', fg='#59434B'
    )
    subtitulo.pack(pady=5)

    opciones = [
        ('Agregar producto', funcion_pendiente),
        ('Mostrar productos', funcion_pendiente),
        ('Buscar producto', funcion_pendiente),
        ('Eliminar producto', funcion_pendiente),
        ('Ver estadísticas', lambda: mostrar_estadisticas(productos)),
        ('Ordenar por precio (burbuja)', lambda: ordenar_burbuja(productos)),
        ('Salir', ventana.destroy)
    ]

    for nombre, funcion in opciones:
        boton = tk.Button(
            ventana, text=nombre, command=funcion,
            font=('Arial', 11), bg='#D9A7B0', fg='#59434B',
            width=29, height=1
        )
        boton.pack(pady=7)

    ventana.mainloop()


if __name__ == '__main__':
    abrir_menu()
