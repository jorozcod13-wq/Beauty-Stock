from tkinter import messagebox
# Burbuja1_prueba

def ordenar_burbuja(productos):
    # Ordena la misma lista de mayor a menor precio.
    n = len(productos)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if productos[j]['precio'] < productos[j + 1]['precio']:
                temporal = productos[j]
                productos[j] = productos[j + 1]
                productos[j + 1] = temporal

    if n == 0:
        messagebox.showinfo('Ordenamiento', 'No hay productos para ordenar.')
        return

    texto = 'Productos ordenados del más caro al más barato:\n\n'
    for producto in productos:
        texto += f'{producto["nombre"]}: Q{producto["precio"]:.2f}\n'

    messagebox.showinfo('Ordenamiento burbuja', texto)
