usuario = "admin"
contra = "gestor123"

print("bienvenido")

while True:
    user=input("Ingrese su usuario: ")
    pwd=input("ingrese la contraseña: ")

    if user == usuario and pwd== contra:
        print("Datos Válidos")
        print("Bienvenido Beauty Stock")

        break

    else:
        print("Datos Inválidos")

print("Entrando al sistema de inventario...")