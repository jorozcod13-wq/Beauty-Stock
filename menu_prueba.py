
# Menú principal
def menu():
    while True:
        print("\n================================")
        print("       BEAUTYSTOCK JyD")
        print("  INVENTARIO DE MAQUILLAJE")
        print("================================")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Estadísticas del inventario")
        print("6. Ordenar productos por precio")
        print("7. Salir")
        print("================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar()

        elif opcion == "2":
            mostrar()

        elif opcion == "3":
            buscar()

        elif opcion == "4":
            eliminar()

        elif opcion == "5":
            estadisticas()

        elif opcion == "6":
            ordenar_productos()

        elif opcion == "7":
            print("Gracias por utilizar BeautyStock JyD.")
            break

        else:
            print("Opción incorrecta. Intente de nuevo.")
