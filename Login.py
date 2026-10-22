from getpass import getpass

usuario = "admin"
contra = "gestor123"

print("bienvenido")

while True:
    user=input("Ingrese su usuario: ")
    pwd=getpass("ingrese la contraseña: ")

    if user == usuario and pwd == contra:
        print("Datos válidos")
        print("Bienvenido a Beauty Stock")

        break

    else:
        print("Datos Inválidos")

print("Entrando al sistema de inventario...")

#Nota:Solo es la logica, falta implementar los * cuando se escriba la contraseña