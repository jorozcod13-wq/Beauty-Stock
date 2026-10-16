productos= []


 #Agregar Producto
def agregar ():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: Q. "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    categoria = input("Ingrese la categoría del producto: ")

    producto= {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
}
    
    productos.append(producto)


#Mostrar Producto

def mostrar ():
    if not productos:
        print("No hay productos registrados")

        return

    for producto in productos:
        print("Código:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Precio:", producto["precio"])
        print("Cantidad:", producto["cantidad"])
        print("Categoría:", producto["categoria"])


#Eliminar Producto
def eliminar ():
    codigo_eliminar=input("Ingresa el código del producto que deseas eliminar: ")
    for producto in productos:
        if producto["codigo"] == codigo_eliminar:
            productos.remove(producto)
            print("Producto eliminado correctamente")

            break
        else:
            print("No se encontro algún producto con ese código")


#Buscar Producto 
def buscar ():
    buscar_codigo=input("Ingresa el código del producto que deseas buscar: ")
    for producto in productos:
        if producto["codigo"] == buscar_codigo:
            print("Nombre:", producto["nombre"])

            break
    else:
        print("No se encontró el producto.")
    

agregar()
mostrar()
agregar()
eliminar()
mostrar()
buscar()