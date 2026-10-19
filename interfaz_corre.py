
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk



# Paleta de colores


THEME_BG = "#FFF9F7"
THEME_FG = "#59434B"
THEME_ACCENT = "#D9A7B0"
THEME_ACCENT_FG = "#FFF9F7"
THEME_FIELD_BG = "#F3E1E4"
THEME_BORDER = "#E8D7C8"
THEME_DARK = "#785964"
THEME_FONT = ("Helvetica", 12)



# Configuración Visual


def apply_theme(root):
    root.configure(bg=THEME_BG)

    style = ttk.Style(root)

    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    style.configure(
        ".",
        background=THEME_BG,
        foreground=THEME_FG,
        font=THEME_FONT
    )

    style.configure(
        "Treeview",
        background="#FFFFFF",
        foreground=THEME_FG,
        fieldbackground="#FFFFFF",
        rowheight=35,
        font=("Helvetica", 11),
        borderwidth=1
    )

    style.configure(
        "Treeview.Heading",
        background="#E8C1CA",
        foreground=THEME_FG,
        font=("Helvetica", 11, "bold"),
        relief="flat",
        padding=8
    )

    style.map(
        "Treeview",
        background=[("selected", "#D9A7B0")],
        foreground=[("selected", "#59434B")]
    )


def crear_boton(parent, texto, comando, fondo, texto_color=THEME_FG,
                fuente=("Helvetica", 14), ancho=None, alto=None):

    boton = tk.Button(
        parent,
        text=texto,
        command=comando,
        bg=fondo,
        fg=texto_color,
        activebackground="#E8C1CA",
        activeforeground=THEME_FG,
        font=fuente,
        relief="flat",
        bd=0,
        highlightthickness=0,
        cursor="hand2"
    )

    return boton


def crear_entry(parent, readonly=False):
    opciones = {
        "bg": THEME_FIELD_BG,
        "fg": THEME_FG,
        "insertbackground": THEME_FG,
        "font": ("Helvetica", 12),
        "relief": "flat",
        "highlightthickness": 1,
        "highlightbackground": THEME_BORDER,
        "highlightcolor": THEME_ACCENT
    }

    if readonly:
        opciones["state"] = "readonly"
        opciones["readonlybackground"] = THEME_FIELD_BG

    return tk.Entry(parent, **opciones)


def crear_label(parent, texto, fuente=("Helvetica", 16),
                color=THEME_FG, fondo=THEME_BG):

    return tk.Label(
        parent,
        text=texto,
        font=fuente,
        fg=color,
        bg=fondo,
        anchor="w"
    )



# LOGIN


class Main:
    def __init__(self, root):
        self.root = root

        root.title("Beauty Stock - Iniciar sesión")
        root.geometry("625x650")
        root.resizable(False, False)

        apply_theme(root)

        root.update_idletasks()
        x = (root.winfo_screenwidth() - 625) // 2
        y = (root.winfo_screenheight() - 650) // 2
        root.geometry(f"625x650+{x}+{y}")

        # Imagen del login
        self.image1_image = ImageTk.PhotoImage(
            Image.open("img/2.png").resize((240, 650))
        )

        self.image1 = tk.Label(
            root,
            image=self.image1_image,
            bd=0
        )
        self.image1.place(x=0, y=0, width=240, height=650)

        # Título
        self.text1 = tk.Label(
            root,
            text="Beauty Stock",
            fg="#B77C8B",
            bg=THEME_BG,
            font=("Helvetica", 34, "bold italic")
        )
        self.text1.place(x=260, y=55, width=345, height=100)

        # Usuario
        self.usuario = crear_label(
            root, "Usuario:",
            fuente=("Helvetica", 17, "bold")
        )
        self.usuario.place(x=280, y=220, width=250, height=30)

        self.user = crear_entry(root)
        self.user.place(x=280, y=260, width=270, height=38)

        # Contraseña
        self.contrase = crear_label(
            root, "Contraseña:",
            fuente=("Helvetica", 17, "bold")
        )
        self.contrase.place(x=280, y=335, width=250, height=30)

        self.password = crear_entry(root)
        self.password.configure(show="*")
        self.password.place(x=280, y=375, width=270, height=38)

        # Botón
        self.btn_inicios = crear_boton(
            root,
            "Iniciar sesión",
            self.on_btn_inicios,
            fondo=THEME_DARK,
            texto_color="#785964",
            fuente=("Helvetica", 15, "bold")
        )
        self.btn_inicios.place(x=330, y=465, width=190, height=60)

        self.password.bind("<Return>", lambda event: self.on_btn_inicios())

    def open_menuprincipal(self):
        return Menuprincipal(self.root, self)

    def open_agregar(self):
        return Agregar(self.root)

    def open_buscar(self):
        return Buscar(self.root)

    def open_eliminar(self):
        return Eliminar(self.root)

    def on_btn_inicios(self):
        usuario = self.user.get().strip()
        contraseña = self.password.get()

        if not usuario and not contraseña:
            messagebox.showwarning(
                "Campos vacíos",
                "Ingresa tu usuario y contraseña.",
                parent=self.root
            )

        elif not usuario:
            messagebox.showwarning(
                "Falta el usuario",
                "Ingresa tu usuario.",
                parent=self.root
            )

        elif not contraseña:
            messagebox.showwarning(
                "Falta la contraseña",
                "Ingresa tu contraseña.",
                parent=self.root
            )

        elif usuario == "admin" and contraseña == "gestor123":
            self.open_menuprincipal()
            self.root.withdraw()

        else:
            messagebox.showerror(
                "Datos incorrectos",
                "El usuario o la contraseña son incorrectos.",
                parent=self.root
            )



# Menú Principla


class Menuprincipal:
    def __init__(self, master, aplicacion):
        self.aplicacion = aplicacion

        self.root = tk.Toplevel(master)
        root = self.root

        root.title("Beauty Stock - Menú principal")
        root.geometry("950x900")
        root.minsize(950, 900)

        apply_theme(root)

        # Encabezado
        self.encabezado = tk.Frame(
            root,
            bg="#D9A7B0",
            bd=0
        )
        self.encabezado.place(x=0, y=0, width=950, height=170)

        self.logo_image = ImageTk.PhotoImage(
            Image.open("img/logo.webp").resize((110, 80))
        )

        self.logo = tk.Label(
            self.encabezado,
            image=self.logo_image,
            bg="#D9A7B0",
            bd=0
        )
        self.logo.place(x=35, y=35, width=110, height=80)

        self.text2 = tk.Label(
            self.encabezado,
            text="Beauty Stock",
            fg="#FFF9F7",
            bg="#D9A7B0",
            font=("Helvetica", 36, "bold")
        )
        self.text2.place(x=220, y=30, width=420, height=80)

        self.name1 = tk.Label(
            self.encabezado,
            text="Diana Barrios",
            fg="#FFF9F7",
            bg="#D9A7B0",
            font=("Helvetica", 12)
        )
        self.name1.place(x=755, y=25, width=170, height=30)

        self.carne1 = tk.Label(
            self.encabezado,
            text="0903-26-",
            fg="#59434B",
            bg="#D9A7B0",
            font=("Helvetica", 11)
        )
        self.carne1.place(x=755, y=50, width=170, height=25)

        self.name2 = tk.Label(
            self.encabezado,
            text="Janeth Orozco",
            fg="#FFF9F7",
            bg="#D9A7B0",
            font=("Helvetica", 12)
        )
        self.name2.place(x=755, y=85, width=170, height=30)

        self.carne2 = tk.Label(
            self.encabezado,
            text="0903-26-5297",
            fg="#59434B",
            bg="#D9A7B0",
            font=("Helvetica", 11)
        )
        self.carne2.place(x=755, y=110, width=170, height=25)

        # Botones superiores
        self.buscar_btn = crear_boton(
            root, "Buscar", self.on_buscar_btn,
            "#B77C8B", "#F3E1E4"
        )
        self.buscar_btn.place(x=50, y=190, width=140, height=60)

        self.agregar_btn = crear_boton(
            root, "Agregar", self.on_agregar_btn,
            "#F3E1E4", "#B77C8B"
        )
        self.agregar_btn.place(x=290, y=190, width=140, height=60)

        self.eliminar_btn = crear_boton(
            root, "Eliminar", self.on_eliminar_btn,
            "#B77C8B", "#F3E1E4"
        )
        self.eliminar_btn.place(x=530, y=190, width=140, height=60)

        self.mostrar_btn = crear_boton(
            root, "Mostrar", self.on_mostrar_btn,
            "#F3E1E4", "#B77C8B"
        )
        self.mostrar_btn.place(x=760, y=190, width=140, height=60)

        # Tabla
        self.tabla_product = ttk.Treeview(
            root,
            columns=("col1", "col2", "col3", "col4", "col5"),
            show="headings"
        )

        encabezados = {
            "col1": ("Código", 100, "center"),
            "col2": ("Nombre", 220, "w"),
            "col3": ("Precio Q", 120, "center"),
            "col4": ("Cantidad", 120, "center"),
            "col5": ("Categoría", 220, "w")
        }

        for columna, (titulo, ancho, alineacion) in encabezados.items():
            self.tabla_product.heading(columna, text=titulo)
            self.tabla_product.column(
                columna,
                width=ancho,
                minwidth=70,
                anchor=alineacion
            )

        self.tabla_product.place(
            x=50, y=300, width=850, height=470
        )

        # Botones inferiores
        self.calculo_btn = crear_boton(
            root, "Cálculos", self.on_calculo_btn,
            "#E8D7C8", "#785964"
        )
        self.calculo_btn.place(x=50, y=810, width=140, height=60)

        self.ordenar_btn = crear_boton(
            root, "Ordenar", self.on_ordenar_btn,
            "#D9A7B0", "#FFFFFF"
        )
        self.ordenar_btn.place(x=250, y=810, width=140, height=60)

        self.logout_btn = crear_boton(
            root, "Cerrar sesión", self.on_logout_btn,
            "#785964", "#FFFFFF",
            fuente=("Helvetica", 13)
        )
        self.logout_btn.place(x=760, y=810, width=140, height=60)

        root.protocol("WM_DELETE_WINDOW", self.on_logout_btn)

    def on_buscar_btn(self):
        self.aplicacion.open_buscar()

    def on_agregar_btn(self):
        self.aplicacion.open_agregar()

    def on_eliminar_btn(self):
        self.aplicacion.open_eliminar()

    def on_mostrar_btn(self):
        pass

    def on_calculo_btn(self):
        pass

    def on_ordenar_btn(self):
        pass

    def on_logout_btn(self):
        if messagebox.askyesno(
            "Cerrar sesión",
            "¿Deseas cerrar sesión?",
            parent=self.root
        ):
            self.root.destroy()
            self.aplicacion.root.deiconify()
            self.aplicacion.user.delete(0, tk.END)
            self.aplicacion.password.delete(0, tk.END)

    def load_tabla_product(self, rows):
        self.tabla_product.delete(
            *self.tabla_product.get_children()
        )

        for values in rows:
            self.tabla_product.insert("", "end", values=values)



# Ventana agregar producto

class Agregar:
    def __init__(self, master):
        self.root = tk.Toplevel(master)
        root = self.root

        root.title("Beauty Stock - Agregar producto")
        root.geometry("520x750")
        root.resizable(False, False)

        apply_theme(root)

        self.frame1 = tk.Frame(root, bg="#E8C1CA", bd=0)
        self.frame1.place(x=0, y=0, width=520, height=140)

        self.agregar = tk.Label(
            self.frame1,
            text="♡ Agregar producto",
            font=("Helvetica", 25, "bold"),
            bg="#E8C1CA",
            fg=THEME_FG
        )
        self.agregar.place(x=15, y=10, width=380, height=60)

        self.text3 = tk.Label(
            self.frame1,
            text="Registra un producto nuevo en Beauty Stock",
            font=("Helvetica", 11),
            bg="#E8C1CA",
            fg=THEME_FG
        )
        self.text3.place(x=20, y=75, width=450, height=35)

        self.codi = crear_label(root, "Código")
        self.codi.place(x=30, y=170, width=200, height=35)

        self.codigo = crear_entry(root)
        self.codigo.place(x=30, y=210, width=450, height=35)

        self.nameprod = crear_label(root, "Nombre del producto")
        self.nameprod.place(x=30, y=275, width=300, height=35)

        self.nombreprod = crear_entry(root)
        self.nombreprod.place(x=30, y=315, width=450, height=35)

        self.price = crear_label(root, "Precio (Q)")
        self.price.place(x=30, y=385, width=200, height=35)

        self.cant = crear_label(root, "Cantidad")
        self.cant.place(x=270, y=385, width=200, height=35)

        self.precio = crear_entry(root)
        self.precio.place(x=30, y=425, width=210, height=35)

        self.cantidad = crear_entry(root)
        self.cantidad.place(x=270, y=425, width=210, height=35)

        self.cate = crear_label(root, "Categoría")
        self.cate.place(x=30, y=495, width=200, height=35)

        self.categoria = crear_entry(root)
        self.categoria.place(x=30, y=535, width=450, height=35)

        self.save_btn = crear_boton(
            root, "Guardar producto", self.on_save_btn,
            "#D9A7B0", "#FFFFFF",
            fuente=("Helvetica", 13, "bold")
        )
        self.save_btn.place(x=30, y=635, width=220, height=65)

        self.cancel_btna = crear_boton(
            root, "Cancelar", self.on_cancel_btna,
            "#F3E1E4", "#785964",
            fuente=("Helvetica", 13)
        )
        self.cancel_btna.place(x=270, y=635, width=220, height=65)

    def on_save_btn(self):
        pass

    def on_cancel_btna(self):
        self.root.destroy()



# Ventana buscar


class Buscar:
    def __init__(self, master):
        self.root = tk.Toplevel(master)
        root = self.root

        root.title("Beauty Stock - Buscar producto")
        root.geometry("520x750")
        root.resizable(False, False)

        apply_theme(root)

        self.frame1 = tk.Frame(root, bg="#E8C1CA", bd=0)
        self.frame1.place(x=0, y=0, width=520, height=140)

        self.buscar = tk.Label(
            self.frame1,
            text="♡ Buscar producto",
            font=("Helvetica", 25, "bold"),
            bg="#E8C1CA",
            fg=THEME_FG
        )
        self.buscar.place(x=15, y=10, width=380, height=60)

        self.text4 = tk.Label(
            self.frame1,
            text="Ingresa el código del producto que quieres buscar",
            font=("Helvetica", 11),
            bg="#E8C1CA",
            fg=THEME_FG
        )
        self.text4.place(x=20, y=75, width=470, height=35)

        self.code_B = crear_label(root, "Código")
        self.code_B.place(x=35, y=175, width=200, height=35)

        self.code_btn_buscar = crear_entry(root)
        self.code_btn_buscar.place(x=35, y=215, width=450, height=35)

        self.label4 = crear_label(root, "Nombre del producto")
        self.label4.place(x=35, y=285, width=300, height=35)

        self.entry2 = crear_entry(root, readonly=True)
        self.entry2.place(x=35, y=325, width=450, height=35)

        self.label5 = crear_label(root, "Precio (Q)")
        self.label5.place(x=35, y=395, width=200, height=35)

        self.label6 = crear_label(root, "Cantidad")
        self.label6.place(x=275, y=395, width=200, height=35)

        self.entry3 = crear_entry(root, readonly=True)
        self.entry3.place(x=35, y=435, width=210, height=35)

        self.entry4 = crear_entry(root, readonly=True)
        self.entry4.place(x=275, y=435, width=210, height=35)

        self.label7 = crear_label(root, "Categoría")
        self.label7.place(x=35, y=505, width=200, height=35)

        self.entry5 = crear_entry(root, readonly=True)
        self.entry5.place(x=35, y=545, width=450, height=35)

        self.buscar_btnB = crear_boton(
            root, "Buscar producto", self.on_buscar_btnB,
            "#D9A7B0", "#FFFFFF",
            fuente=("Helvetica", 13, "bold")
        )
        self.buscar_btnB.place(x=25, y=635, width=220, height=65)

        self.cancel_btnB = crear_boton(
            root, "Cancelar", self.on_cancel_btnB,
            "#F3E1E4", "#785964",
            fuente=("Helvetica", 13)
        )
        self.cancel_btnB.place(x=275, y=635, width=220, height=65)

    def on_buscar_btnB(self):
        pass

    def on_cancel_btnB(self):
        self.root.destroy()

# Ventana eliminar


class Eliminar:
    def __init__(self, master):
        self.root = tk.Toplevel(master)
        root = self.root

        root.title("Beauty Stock - Eliminar producto")
        root.geometry("520x750")
        root.resizable(False, False)

        apply_theme(root)

        self.frame1 = tk.Frame(root, bg="#E8C1CA", bd=0)
        self.frame1.place(x=0, y=0, width=520, height=140)

        self.eliminar = tk.Label(
            self.frame1,
            text="♡ Eliminar producto",
            font=("Helvetica", 25, "bold"),
            bg="#E8C1CA",
            fg=THEME_FG
        )
        self.eliminar.place(x=15, y=10, width=380, height=60)

        self.text5 = tk.Label(
            self.frame1,
            text="Ingresa el código del producto que deseas eliminar",
            font=("Helvetica", 11),
            bg="#E8C1CA",
            fg=THEME_FG
        )
        self.text5.place(x=20, y=75, width=470, height=35)

        self.code_B = crear_label(root, "Código")
        self.code_B.place(x=35, y=165, width=200, height=35)

        self.code_btn_eliminar = crear_entry(root)
        self.code_btn_eliminar.place(x=35, y=205, width=450, height=35)

        self.label4 = crear_label(root, "Nombre del producto")
        self.label4.place(x=35, y=270, width=300, height=35)

        self.entry5 = crear_entry(root, readonly=True)
        self.entry5.place(x=35, y=310, width=450, height=35)

        self.label5 = crear_label(root, "Precio (Q)")
        self.label5.place(x=35, y=380, width=200, height=35)

        self.label6 = crear_label(root, "Cantidad")
        self.label6.place(x=275, y=380, width=200, height=35)

        self.entry2 = crear_entry(root, readonly=True)
        self.entry2.place(x=35, y=420, width=210, height=35)

        self.entry3 = crear_entry(root, readonly=True)
        self.entry3.place(x=275, y=420, width=210, height=35)

        self.label7 = crear_label(root, "Categoría")
        self.label7.place(x=35, y=490, width=200, height=35)

        self.entry4 = crear_entry(root, readonly=True)
        self.entry4.place(x=35, y=530, width=450, height=35)

        self.delete_btn = crear_boton(
            root, "Eliminar producto", self.on_delete_btn,
            "#D9A7B0", "#FFFFFF",
            fuente=("Helvetica", 13, "bold")
        )
        self.delete_btn.place(x=30, y=630, width=220, height=65)

        self.cancel_btn2 = crear_boton(
            root, "Cancelar", self.on_cancel_btn2,
            "#F3E1E4", "#785964",
            fuente=("Helvetica", 13)
        )
        self.cancel_btn2.place(x=270, y=630, width=220, height=65)

    def on_delete_btn(self):
        pass

    def on_cancel_btn2(self):
        self.root.destroy()


# =========================
# INICIAR APLICACIÓN
# =========================

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
