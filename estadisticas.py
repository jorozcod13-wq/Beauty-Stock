import tkinter as tk
from tkinter import messagebox

# estadisticas1_prueba

def mostrar_estadisticas(productos):
    if len(productos) == 0:
        messagebox.showinfo('Estadísticas', 'Todavía no hay productos registrados.')
        return

    total_productos = len(productos)
    total_unidades = 0
    valor_inventario = 0
    suma_precios = 0
    mas_caro = productos[0]
    mas_barato = productos[0]

    for producto in productos:
        total_unidades += producto['cantidad']
        valor_inventario += producto['precio'] * producto['cantidad']
        suma_precios += producto['precio']

        if producto['precio'] > mas_caro['precio']:
            mas_caro = producto
        if producto['precio'] < mas_barato['precio']:
            mas_barato = producto

    promedio = suma_precios / total_productos

    mensaje = (
        f'Productos diferentes: {total_productos}\n'
        f'Unidades disponibles: {total_unidades}\n'
        f'Valor del inventario: Q{valor_inventario:.2f}\n'
        f'Precio promedio: Q{promedio:.2f}\n'
        f'Más caro: {mas_caro["nombre"]} (Q{mas_caro["precio"]:.2f})\n'
        f'Más barato: {mas_barato["nombre"]} (Q{mas_barato["precio"]:.2f})'
    )
    messagebox.showinfo('Estadísticas de Beauty Stock', mensaje)
