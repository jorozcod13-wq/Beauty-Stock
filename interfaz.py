import tkinter as tk
from tkinter import ttk
# Requires Pillow:  pip install pillow
from PIL import Image, ImageTk
from tkinter import messagebox


THEME_BG = "#f9f7f6"
THEME_FG = "#716060"
THEME_ACCENT = "#8ba5c6"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#f4f2f0"
THEME_FONT = ("Georgia", 10)


def apply_theme(root):
    """Apply the project theme as defaults; per-widget options override these."""
    root.configure(bg=THEME_BG)
    root.option_add("*background", THEME_BG)
    root.option_add("*foreground", THEME_FG)
    root.option_add("*font", THEME_FONT)
    root.option_add("*Entry.background", THEME_FIELD_BG)
    root.option_add("*Text.background", THEME_FIELD_BG)
    root.option_add("*Listbox.background", THEME_FIELD_BG)
    root.option_add("*Button.background", THEME_ACCENT)
    root.option_add("*Button.foreground", THEME_ACCENT_FG)
    style = ttk.Style(root)
    try:
        style.theme_use("classic")
    except tk.TclError:
        pass
    style.configure(".", background=THEME_BG, foreground=THEME_FG, fieldbackground=THEME_FIELD_BG, font=THEME_FONT)


class Main:
    def __init__(self, root):
        self.root = root
        root.title("Main")
        root.geometry("625x650")
        root.update_idletasks()
        apply_theme(root)
        root.geometry(
            f"+{(root.winfo_screenwidth() - 625) // 2}"
            f"+{(root.winfo_screenheight() - 650) // 2}"
        )

        # Kept on self, or Python garbage-collects it and the image goes blank.
        self.image1_image = ImageTk.PhotoImage(Image.open("img/2.png").resize((240, 650)))
        self.image1 = tk.Label(root, image=self.image1_image)
        self.image1.place(x=0, y=0, width=240, height=650)

        self.btn_inicios = tk.Button(root, text="Iniciar Sesión", command=self.on_btn_inicios, bg="#654A54", font=("Helvetica", 15))
        self.btn_inicios.place(x=330, y=470, width=170, height=70)

        self.user = tk.Entry(root)
        self.user.place(x=280, y=270, width=250, height=30)

        self.password = tk.Entry(root)
        self.password.place(x=280, y=390, width=250, height=30)

        self.usuario = tk.Label(root, text="Usuario:", font=("Helvetica", 20))
        self.usuario.place(x=280, y=230, width=110, height=30)

        self.contrase = tk.Label(root, text="Contraseña:", font=("Helvetica", 20))
        self.contrase.place(x=280, y=350, width=160, height=30)

        self.text1 = tk.Label(root, text="Beauty Stock", fg="#B77C8B", font=("Helvetica", 45, "bold italic"))
        self.text1.place(x=280, y=40, width=310, height=150)

    def open_menuprincipal(self):
        return Menuprincipal(self.root)

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
            "Ingresa tu usuario y contraseña."
        )

        elif not usuario:
            messagebox.showwarning(
            "Falta el usuario",
            "Ingresa tu usuario."
        )

        elif not contraseña:
            messagebox.showwarning(
            "Falta la contraseña",
            "Ingresa tu contraseña."
        )

        elif usuario == "admin" and contraseña == "gestor123":
            print("Credenciales correctas")
            self.open_menuprincipal()

        else:
            messagebox.showerror(
            "Datos incorrectos",
            "El usuario o la contraseña son incorrectos."
        )


class Menuprincipal:
    def __init__(self, master):
        root = tk.Toplevel(master)
        self.root = root
        root.title("menuprincipal")
        root.geometry("950x900")
        apply_theme(root)

        self.encabezado = tk.Frame(root, bg="#D9A7B0", relief="groove", bd=2)
        self.encabezado.place(x=0, y=0, width=1000, height=170)

        # Kept on self, or Python garbage-collects it and the image goes blank.
        self.logo_image = ImageTk.PhotoImage(Image.open("img/logo.webp").resize((110, 80)))
        self.logo = tk.Label(self.encabezado, image=self.logo_image)
        self.logo.place(x=40, y=25, width=110, height=80)

        self.text2 = tk.Label(self.encabezado, text="Beauty Stock", fg="#D9A7B0", font=("Helvetica", 45))
        self.text2.place(x=310, y=15, width=350, height=140)

        self.name1 = tk.Label(self.encabezado, text="Diana Barrios", fg="#D9A7B0", font=("Helvetica", 15))
        self.name1.place(x=790, y=25, width=160, height=40)

        self.name2 = tk.Label(self.encabezado, text="Janeth Orozco", fg="#D9A7B0", font=("Helvetica", 15))
        self.name2.place(x=790, y=85, width=150, height=40)

        self.carne1 = tk.Label(self.encabezado, text="0903-26-", fg="#E8D7C8", font=("Helvetica", 15))
        self.carne1.place(x=785, y=50, width=160, height=40)

        self.carne2 = tk.Label(self.encabezado, text="0903-26-5297", fg="#E8D7C8", font=("Helvetica", 15))
        self.carne2.place(x=780, y=115, width=160, height=40)

        self.tabla_product = ttk.Treeview(root, columns=("col1", "col2", "col3", "col4", "col5"), show="headings")
        self.tabla_product.heading("col1", text="Código")
        self.tabla_product.heading("col2", text="Nombre")
        self.tabla_product.heading("col3", text="Precio Q")
        self.tabla_product.heading("col4", text="Cantidad")
        self.tabla_product.heading("col5", text="Categoría")
        self.tabla_product.place(x=50, y=300, width=840, height=470)

        self.buscar_btn = tk.Button(root, text="Buscar", command=self.on_buscar_btn, fg="#F3E1E4", bg="#B77C8B", font=("Helvetica", 15))
        self.buscar_btn.place(x=50, y=190, width=140, height=60)

        self.agregar_btn = tk.Button(root, text="Agregar", command=self.on_agregar_btn, fg=" #B77C8B", bg="#F3E1E4", font=("Helvetica", 15))
        self.agregar_btn.place(x=290, y=190, width=140, height=60)

        self.eliminar_btn = tk.Button(root, text="Eliminar", command=self.on_eliminar_btn, fg="#F3E1E4", bg="#B77C8B", font=("Helvetica", 15))
        self.eliminar_btn.place(x=530, y=190, width=140, height=60)

        self.mostrar_btn = tk.Button(root, text="Mostrar", command=self.on_mostrar_btn, fg="#B77C8B", bg="#F3E1E4", font=("Helvetica", 15))
        self.mostrar_btn.place(x=760, y=190, width=140, height=60)

        self.calculo_btn = tk.Button(root, text="Calculos", command=self.on_calculo_btn, fg="#785964", bg="#E8D7C8", font=("Helvetica", 15))
        self.calculo_btn.place(x=50, y=810, width=140, height=60)

        self.ordenar_btn = tk.Button(root, text="Ordernar", command=self.on_ordenar_btn, fg="#F3E1E4", bg="#D9A7B0", font=("Helvetica", 15))
        self.ordenar_btn.place(x=250, y=810, width=140, height=60)

        self.logout_btn = tk.Button(root, text="cerrar sesión", command=self.on_logout_btn, bg="#785964", font=("Helvetica", 15))
        self.logout_btn.place(x=760, y=810, width=140, height=60)

    def on_buscar_btn(self):
        pass

    def on_agregar_btn(self):
        pass

    def on_eliminar_btn(self):
        pass

    def on_mostrar_btn(self):
        pass

    def on_calculo_btn(self):
        pass

    def on_ordenar_btn(self):
        pass

    def on_logout_btn(self):
        pass

    def load_tabla_product(self, rows):
        """Populate the table — pass any iterable of row tuples/lists."""
        self.tabla_product.delete(*self.tabla_product.get_children())
        for values in rows:
            self.tabla_product.insert("", "end", values=values)


class Agregar:
    def __init__(self, master):
        root = tk.Toplevel(master)
        self.root = root
        root.title("agregar")
        root.geometry("520x750")
        apply_theme(root)

        self.frame1 = tk.Frame(root, bg="#eed3d9", relief="groove", bd=2)
        self.frame1.place(x=0, y=0, width=520, height=140)

        self.save_btn = tk.Button(root, text="Guardar Producto", command=self.on_save_btn, fg="#fbf4f5", bg="#D9A7B0", font=("Helvetica", 16))
        self.save_btn.place(x=30, y=620, width=220, height=80)

        self.codigo = tk.Entry(root)
        self.codigo.place(x=30, y=210, width=450, height=30)

        self.nombreprod = tk.Entry(root)
        self.nombreprod.place(x=30, y=320, width=450, height=30)

        self.categoria = tk.Entry(root)
        self.categoria.place(x=30, y=540, width=450, height=30)

        self.precio = tk.Entry(root)
        self.precio.place(x=30, y=430, width=210, height=30)

        self.cantidad = tk.Entry(root)
        self.cantidad.place(x=270, y=430, width=210, height=30)

        self.codi = tk.Label(root, text="Código", font=("Helvetica", 20))
        self.codi.place(x=30, y=170, width=110, height=40)

        self.nameprod = tk.Label(root, text="Nombre del Producto", font=("Helvetica", 20))
        self.nameprod.place(x=30, y=280, width=270, height=40)

        self.price = tk.Label(root, text="Precio (Q)", font=("Helvetica", 20))
        self.price.place(x=30, y=390, width=140, height=40)

        self.cant = tk.Label(root, text="Cantidad", font=("Helvetica", 20))
        self.cant.place(x=270, y=400, width=120, height=30)

        self.cate = tk.Label(root, text="Categoría", font=("Helvetica", 20))
        self.cate.place(x=30, y=500, width=170, height=40)

        self.agregar = tk.Label(self.frame1, text="𑣲 Agregar producto", font=("Helvetica", 30))
        self.agregar.place(x=10, y=10, width=360, height=70)

        self.text3 = tk.Label(self.frame1, text="Registra un producto nuevo  en beauty stock", font=("Helvetica", 14))
        self.text3.place(x=30, y=70, width=370, height=50)

        self.cancel_btna = tk.Button(root, text="Cancelar", command=self.on_cancel_btna, fg="#785964", bg="#F3E1E4", font=("Helvetica", 18))
        self.cancel_btna.place(x=270, y=620, width=220, height=80)

    def on_save_btn(self):
        pass

    def on_cancel_btna(self):
        pass


class Buscar:
    def __init__(self, master):
        root = tk.Toplevel(master)
        self.root = root
        root.title("buscar")
        root.geometry("520x750")
        apply_theme(root)

        self.frame1 = tk.Frame(root, bg="#eed3d9", relief="groove", bd=2)
        self.frame1.place(x=0, y=0, width=520, height=140)

        self.buscar = tk.Label(self.frame1, text=" Buscar producto", font=("Helvetica", 30))
        self.buscar.place(x=10, y=10, width=360, height=70)

        self.text4 = tk.Label(self.frame1, text="Ingresa el código del producto que quieres buscar", font=("Helvetica", 14))
        self.text4.place(x=20, y=70, width=450, height=50)

        self.code_B = tk.Label(root, text="Código", font=("Helvetica", 20))
        self.code_B.place(x=46, y=186, width=110, height=40)

        self.code_btn_buscar = tk.Entry(root)
        self.code_btn_buscar.place(x=35, y=226, width=450, height=30)

        self.label4 = tk.Label(root, text="Nombre del Producto", font=("Helvetica", 20))
        self.label4.place(x=46, y=296, width=270, height=40)

        self.entry2 = tk.Entry(root, state="readonly")
        self.entry2.place(x=35, y=336, width=450, height=30)

        self.label5 = tk.Label(root, text="Precio (Q)", font=("Helvetica", 20))
        self.label5.place(x=46, y=406, width=140, height=40)

        self.entry3 = tk.Entry(root, state="readonly")
        self.entry3.place(x=35, y=446, width=210, height=30)

        self.label6 = tk.Label(root, text="Cantidad", font=("Helvetica", 20))
        self.label6.place(x=286, y=416, width=120, height=30)

        self.entry4 = tk.Entry(root, state="readonly")
        self.entry4.place(x=275, y=446, width=210, height=30)

        self.label7 = tk.Label(root, text="Categoría", font=("Helvetica", 20))
        self.label7.place(x=46, y=516, width=170, height=40)

        self.entry5 = tk.Entry(root, state="readonly")
        self.entry5.place(x=35, y=556, width=450, height=30)

        self.buscar_btnB = tk.Button(root, text="Buscar Producto", command=self.on_buscar_btnB, fg="#fbf4f5", bg="#D9A7B0", font=("Helvetica", 16))
        self.buscar_btnB.place(x=25, y=636, width=220, height=80)

        self.cancel_btnB = tk.Button(root, text="Cancelar", command=self.on_cancel_btnB, fg="#785964", bg="#F3E1E4", font=("Helvetica", 18))
        self.cancel_btnB.place(x=275, y=636, width=220, height=80)

    def on_buscar_btnB(self):
        pass

    def on_cancel_btnB(self):
        pass


class Eliminar:
    def __init__(self, master):
        root = tk.Toplevel(master)
        self.root = root
        root.title("eliminar")
        root.geometry("520x750")
        apply_theme(root)

        self.frame1 = tk.Frame(root, bg="#eed3d9", relief="groove", bd=2)
        self.frame1.place(x=0, y=0, width=520, height=140)

        self.eliminar = tk.Label(self.frame1, text="Eliminar producto", font=("Helvetica", 30))
        self.eliminar.place(x=10, y=10, width=360, height=70)

        self.text5 = tk.Label(self.frame1, text="Ingresa el código del producto que desees eliminar", font=("Helvetica", 14))
        self.text5.place(x=20, y=70, width=450, height=50)

        self.code_B = tk.Label(root, text="Código", font=("Helvetica", 20))
        self.code_B.place(x=35, y=170, width=110, height=40)

        self.code_btn_eliminar = tk.Entry(root)
        self.code_btn_eliminar.place(x=35, y=220, width=450, height=30)

        self.label4 = tk.Label(root, text="Nombre del Producto", font=("Helvetica", 20))
        self.label4.place(x=35, y=280, width=270, height=40)

        self.label5 = tk.Label(root, text="Precio (Q)", font=("Helvetica", 20))
        self.label5.place(x=37, y=407, width=140, height=40)

        self.label6 = tk.Label(root, text="Cantidad", font=("Helvetica", 20))
        self.label6.place(x=275, y=417, width=120, height=30)

        self.entry2 = tk.Entry(root, state="readonly")
        self.entry2.place(x=35, y=455, width=210, height=30)

        self.entry3 = tk.Entry(root, state="readonly")
        self.entry3.place(x=275, y=455, width=210, height=30)

        self.label7 = tk.Label(root, text="Categoría", font=("Helvetica", 20))
        self.label7.place(x=35, y=510, width=170, height=40)

        self.entry4 = tk.Entry(root, state="readonly")
        self.entry4.place(x=37, y=550, width=450, height=30)

        self.delete_btn = tk.Button(root, text="Eliminar Producto", command=self.on_delete_btn, fg="#fbf4f5", bg="#D9A7B0", font=("Helvetica", 16))
        self.delete_btn.place(x=30, y=630, width=220, height=80)

        self.cancel_btn2 = tk.Button(root, text="Cancelar", command=self.on_cancel_btn2, fg="#785964", bg="#F3E1E4", font=("Helvetica", 18))
        self.cancel_btn2.place(x=270, y=630, width=220, height=80)

        self.entry5 = tk.Entry(root, state="readonly")
        self.entry5.place(x=35, y=345, width=450, height=30)

    def on_delete_btn(self):
        pass

    def on_cancel_btn2(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()



    #def on_button1(self):
        #usuario = self.entry1.get()
        #contraseña = self.entry2.get()

        #if usuario == "admin" and contraseña == "gestor123":
           # messagebox.showinfo(
            #"Beauty Stock",
            #"¡Inicio de sesión correcto!"
           # )
        #else:
         #   messagebox.showerror(
         #       "Error",
          #      "Usuario o contraseña incorrectos."
          #  )
