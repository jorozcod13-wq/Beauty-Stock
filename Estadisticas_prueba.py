
#Pendiente que se una para quitar esta variable
productos = []

# Estadisticas Inventario Fer
def estadisticas():
    if not productos:
        print("No hay productos registrados.")
        return

    total_productos = len(productos)
    total_unidades = 0
    valor_inventario = 0
    suma_precios = 0


    producto_caro = productos[0]
    producto_barato = productos[0]

    for producto in productos:
        total_unidades += producto["cantidad"]
        valor_inventario += producto["precio"] * producto["cantidad"]
        suma_precios += producto["precio"]

        if producto["precio"] > producto_caro["precio"]:
            producto_caro = producto

        if producto["precio"] < producto_barato["precio"]:
            producto_barato = producto

    promedio = suma_precios / total_productos

    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    print("Productos registrados:", total_productos)
    print("Unidades disponibles:", total_unidades)
    print("Valor total: Q", round(valor_inventario, 2))
    print("Precio promedio: Q", round(promedio, 2))
    print("Producto más caro:", producto_caro["nombre"])
    print("Precio: Q", producto_caro["precio"])
    print("Producto más barato:", producto_barato["nombre"])
    print("Precio: Q", producto_barato["precio"]) 
