import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Beauty Stock: tema visual
THEME_BG = "#FFF9F7"
THEME_FG = "#59434B"
THEME_ACCENT = "#D9A7B0"
THEME_FIELD_BG = "#F3E1E4"
THEME_BORDER = "#E8D7C8"
THEME_DARK = "#785964"
THEME_PINK = "#E8C1CA"
THEME_MAUVE = "#B77C8B"
THEME_FONT = ("Helvetica", 12)


def apply_theme(root):
    root.configure(bg=THEME_BG)
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass
    style.configure(".", background=THEME_BG, foreground=THEME_FG, font=THEME_FONT)
    style.configure("Treeview", background="#FFFFFF", foreground=THEME_FG,
                    fieldbackground="#FFFFFF", rowheight=35,
                    font=("Helvetica", 11), borderwidth=1)
    style.configure("Treeview.Heading", background=THEME_PINK,
                    foreground=THEME_FG, font=("Helvetica", 11, "bold"),
                    relief="flat", padding=8)
    style.map("Treeview", background=[("selected", THEME_ACCENT)],
              foreground=[("selected", THEME_FG)])


def crear_boton(parent, texto, comando, fondo, texto_color=THEME_FG,
                fuente=("Helvetica", 14), ancho=None, alto=None):
    # Label estilizado para que el color se respete en macOS.
    boton = tk.Label(parent, text=texto, bg=fondo, fg=texto_color,
                     font=fuente, relief="flat", bd=0,
                     cursor="hand2", anchor="center")
    original = fondo
    boton.bind("<Button-1>", lambda event: comando() if comando else None)
    boton.bind("<Enter>", lambda event: boton.configure(bg=THEME_PINK))
    boton.bind("<Leave>", lambda event: boton.configure(bg=original))
    return boton


def crear_entry(parent, readonly=False):
    opciones = dict(bg=THEME_FIELD_BG, fg=THEME_FG,
                    insertbackground=THEME_FG, font=("Helvetica", 12),
                    relief="flat", highlightthickness=1,
                    highlightbackground=THEME_BORDER,
                    highlightcolor=THEME_ACCENT)
    if readonly:
        opciones.update(state="readonly", readonlybackground=THEME_FIELD_BG)
    return tk.Entry(parent, **opciones)


def crear_label(parent, texto, fuente=("Helvetica", 16),
                color=THEME_FG, fondo=THEME_BG):
    return tk.Label(parent, text=texto, font=fuente, fg=color, bg=fondo, anchor="w")


def poner_texto_entry(entry, texto):
    anterior = entry.cget("state")
    if anterior == "readonly":
        entry.configure(state="normal")
    entry.delete(0, tk.END)
    entry.insert(0, str(texto))
    if anterior == "readonly":
        entry.configure(state="readonly")


class Main:
    def __init__(self, root):
        self.root = root
        self.menu = None
        root.title("Beauty Stock - Iniciar sesión")
        root.geometry("625x650")
        root.resizable(False, False)
        apply_theme(root)
        root.update_idletasks()
        x = (root.winfo_screenwidth() - 625) // 2
        y = (root.winfo_screenheight() - 650) // 2
        root.geometry(f"625x650+{x}+{y}")

        try:
            self.image1_image = ImageTk.PhotoImage(
                Image.open("img/login2.jpg").resize((240, 650)))
            tk.Label(root, image=self.image1_image, bd=0).place(
                x=0, y=0, width=240, height=650)
        except (FileNotFoundError, OSError):
            tk.Frame(root, bg=THEME_PINK).place(x=0, y=0, width=240, height=650)
            tk.Label(root, text="♡", font=("Helvetica", 90),
                     bg=THEME_PINK, fg=THEME_BG).place(
                         x=55, y=240, width=130, height=150)

        tk.Label(root, text="Beauty Stock", fg=THEME_MAUVE, bg=THEME_BG,
                 font=("Helvetica", 34, "bold italic")).place(
                     x=260, y=55, width=345, height=100)
        crear_label(root, "Usuario:", fuente=("Helvetica", 17, "bold")).place(
            x=280, y=220, width=250, height=30)
        self.user = crear_entry(root)
        self.user.place(x=280, y=260, width=270, height=38)
        crear_label(root, "Contraseña:", fuente=("Helvetica", 17, "bold")).place(
            x=280, y=335, width=250, height=30)
        self.password = crear_entry(root)
        self.password.configure(show="*")
        self.password.place(x=280, y=375, width=270, height=38)
        crear_boton(root, "Iniciar sesión", self.on_btn_inicios, THEME_DARK,
                    "#FFFFFF", ("Helvetica", 15, "bold")).place(
                        x=330, y=465, width=190, height=60)
        self.password.bind("<Return>", lambda event: self.on_btn_inicios())
        self.user.bind("<Return>", lambda event: self.password.focus_set())

    def open_menuprincipal(self):
        if self.menu is not None:
            try:
                if self.menu.root.winfo_exists():
                    self.menu.root.lift()
                    return self.menu
            except tk.TclError:
                pass
        self.menu = Menuprincipal(self.root, self)
        return self.menu

    def open_agregar(self):
        if self.menu:
            self.menu.on_agregar_btn()

    def open_buscar(self):
        if self.menu:
            self.menu.on_buscar_btn()

    def open_eliminar(self):
        if self.menu:
            self.menu.on_eliminar_btn()

    def on_btn_inicios(self):
        usuario, contrasena = self.user.get().strip(), self.password.get()
        if not usuario or not contrasena:
            mensaje = "Ingresa tu usuario y contraseña." if not usuario and not contrasena else (
                "Ingresa tu usuario." if not usuario else "Ingresa tu contraseña.")
            messagebox.showwarning("Campos incompletos", mensaje, parent=self.root)
        elif usuario == "admin" and contrasena == "gestor123":
            self.open_menuprincipal()
            self.root.withdraw()
        else:
            messagebox.showerror("Datos incorrectos",
                                 "El usuario o la contraseña son incorrectos.",
                                 parent=self.root)


class Menuprincipal:
    def __init__(self, master, aplicacion):
        self.aplicacion = aplicacion
        self.productos = []
        self.ventana_activa = None
        self.ventana_agregar = self.ventana_buscar = self.ventana_eliminar = None
        self.root = tk.Toplevel(master)
        root = self.root
        root.title("Beauty Stock - Menú principal")
        root.geometry("950x900")
        root.minsize(950, 900)
        apply_theme(root)

        self.encabezado = tk.Frame(root, bg=THEME_ACCENT, bd=0)
        self.encabezado.place(x=0, y=0, width=950, height=170)

        try:
            self.logo_image = ImageTk.PhotoImage(
                Image.open("img/logotipo.png").resize((125, 100))
            )
            tk.Label(
                self.encabezado,
                image=self.logo_image,
                bg=THEME_ACCENT,
                bd=0
            ).place(x=45, y=40, width=125, height=100)

        except (FileNotFoundError, OSError):
            tk.Label(
                self.encabezado,
                text="♡",
                font=("Helvetica", 65, "bold"),
                bg=THEME_ACCENT,
                fg=THEME_BG
            ).place(x=55, y=35, width=100, height=110)


        tk.Label(
            self.encabezado,
            text="BEAUTY JyD STOCK",
            fg=THEME_BG,
            bg=THEME_ACCENT,
            font=("Helvetica", 43, "bold")
        ).place(x=205, y=35, width=680, height=70)

        tk.Label(
                self.encabezado,
                text="Gestión de inventario",
                fg=THEME_BG,
                bg=THEME_ACCENT,
                font=("Helvetica", 18, "italic")
            ).place(x=210, y=105, width=400, height=35)

        crear_boton(root, "Buscar", self.on_buscar_btn, THEME_MAUVE,
                    "#FFFFFF").place(x=90, y=190, width=200, height=60)
        crear_boton(root, "Agregar", self.on_agregar_btn, THEME_FIELD_BG,
                    THEME_MAUVE).place(x=375, y=190, width=200, height=60)
        crear_boton(root, "Eliminar", self.on_eliminar_btn, THEME_MAUVE,
                    "#FFFFFF").place(x=660, y=190, width=200, height=60)


        self.tabla_product = ttk.Treeview(
            root, columns=("col1", "col2", "col3", "col4", "col5"),
            show="headings")
        encabezados = {
            "col1": ("Código", 100, "center"),
            "col2": ("Nombre", 220, "w"),
            "col3": ("Precio Q", 120, "center"),
            "col4": ("Cantidad", 120, "center"),
            "col5": ("Categoría", 220, "w")}
        for columna, (titulo, ancho, alineacion) in encabezados.items():
            self.tabla_product.heading(columna, text=titulo)
            self.tabla_product.column(columna, width=ancho, minwidth=70,
                                      anchor=alineacion)
        self.tabla_product.place(x=50, y=300, width=850, height=470)
        crear_boton(root, "Cálculos", self.on_calculo_btn, THEME_BORDER,
                    THEME_DARK).place(x=50, y=810, width=140, height=60)
        crear_boton(root, "Ordenar", self.on_ordenar_btn, THEME_ACCENT,
                    "#FFFFFF").place(x=250, y=810, width=140, height=60)
        crear_boton(root, "Cerrar sesión", self.on_logout_btn, THEME_DARK,
                    "#FFFFFF", ("Helvetica", 13)).place(
                        x=760, y=810, width=140, height=60)
        root.protocol("WM_DELETE_WINDOW", self.on_logout_btn)

    def abrir_ventana(self, atributo, clase):
        ventana = getattr(self, atributo)
        if ventana is not None:
            try:
                if ventana.root.winfo_exists():
                    ventana.root.lift()
                    ventana.root.focus_force()
                    return
            except tk.TclError:
                pass
            setattr(self, atributo, None)
        if self.ventana_activa is not None:
            try:
                if self.ventana_activa.winfo_exists():
                    self.ventana_activa.lift()
                    self.ventana_activa.focus_force()
                    return
            except tk.TclError:
                pass
            self.ventana_activa = None

        ventana = clase(self.root, self)
        setattr(self, atributo, ventana)
        self.ventana_activa = ventana.root
        ventana.root.transient(self.root)
        ventana.root.grab_set()

        def cerrar():
            try:
                if ventana.root.winfo_exists():
                    try:
                        ventana.root.grab_release()
                    except tk.TclError:
                        pass
                    ventana.root.destroy()
            except tk.TclError:
                pass
            setattr(self, atributo, None)
            if self.ventana_activa is ventana.root:
                self.ventana_activa = None

        ventana.cerrar = cerrar
        ventana.root.protocol("WM_DELETE_WINDOW", cerrar)

    def on_buscar_btn(self):
        self.abrir_ventana("ventana_buscar", Buscar)

    def on_agregar_btn(self):
        self.abrir_ventana("ventana_agregar", Agregar)

    def on_eliminar_btn(self):
        self.abrir_ventana("ventana_eliminar", Eliminar)

#Seccion de Diana

    # ESTADISTICAS DEL INVENTARIO

    def on_calculo_btn(self):
        productos = self.productos

        if len(productos) == 0:
            messagebox.showinfo(
                "Estadísticas",
                "Todavía no hay productos registrados.",
                parent=self.root
            )
            return

        total_productos = len(productos)
        total_unidades = 0
        valor_inventario = 0
        suma_precios = 0

        mas_caro = productos[0]
        mas_barato = productos[0]

        for producto in productos:
            total_unidades += producto["cantidad"]

            valor_inventario += (
                producto["precio"] * producto["cantidad"]
            )

            suma_precios += producto["precio"]

            if producto["precio"] > mas_caro["precio"]:
                mas_caro = producto

            if producto["precio"] < mas_barato["precio"]:
                mas_barato = producto

        promedio = suma_precios / total_productos

        mensaje = (
            f"Productos diferentes: {total_productos}\n"
            f"Unidades disponibles: {total_unidades}\n"
            f"Valor del inventario: Q{valor_inventario:.2f}\n"
            f"Precio promedio: Q{promedio:.2f}\n"
            f"Más caro: {mas_caro['nombre']} "
            f"(Q{mas_caro['precio']:.2f})\n"
            f"Más barato: {mas_barato['nombre']} "
            f"(Q{mas_barato['precio']:.2f})"
        )

        messagebox.showinfo(
            "Estadísticas de Beauty Stock",
            mensaje,
            parent=self.root
        )
        

    # ORDENAMIENTO BURBUJA

    def on_ordenar_btn(self):
        productos = self.productos
        n = len(productos)

        if n == 0:
            messagebox.showinfo(
                "Ordenamiento",
                "No hay productos para ordenar.",
                parent=self.root
            )
            return

        # Ordenar de mayor a menor precio
        for i in range(n - 1):
            for j in range(n - 1 - i):

                if productos[j]["precio"] < productos[j + 1]["precio"]:
                    temporal = productos[j]

                    productos[j] = productos[j + 1]

                    productos[j + 1] = temporal

        # Actualizar la tabla del inventario
        self.actualizar_tabla()

        texto = "Productos ordenados del más caro al más barato:\n\n"

        for producto in productos:
            texto += (
                f"{producto['nombre']}: "
                f"Q{producto['precio']:.2f}\n"
            )

        messagebox.showinfo(
            "Ordenamiento burbuja",
            texto,
            parent=self.root
        )



    def actualizar_tabla(self):
        self.tabla_product.delete(*self.tabla_product.get_children())
        for p in self.productos:
            self.tabla_product.insert("", "end", values=(
                p["codigo"], p["nombre"], f'{p["precio"]:.2f}',
                p["cantidad"], p["categoria"]))

    def buscar_producto(self, codigo):
        for p in self.productos:
            if p["codigo"].lower() == codigo.strip().lower():
                return p
        return None

    def load_tabla_product(self, rows):
        self.tabla_product.delete(*self.tabla_product.get_children())
        for values in rows:
            self.tabla_product.insert("", "end", values=values)

    def on_logout_btn(self):
        if not messagebox.askyesno("Cerrar sesión", "¿Deseas cerrar sesión?",
                                   parent=self.root):
            return
        if self.ventana_activa is not None:
            try:
                if self.ventana_activa.winfo_exists():
                    self.ventana_activa.destroy()
            except tk.TclError:
                pass
        self.root.destroy()
        self.aplicacion.menu = None
        self.aplicacion.root.deiconify()
        self.aplicacion.user.delete(0, tk.END)
        self.aplicacion.password.delete(0, tk.END)


class Agregar:
    def __init__(self, master, menu):
        self.menu = menu
        self.root = tk.Toplevel(master)
        root = self.root
        root.title("Beauty Stock - Agregar producto")
        root.geometry("520x750")
        root.resizable(False, False)
        apply_theme(root)
        self.encabezado(root, "♡ Agregar producto",
                        "Registra un producto nuevo en Beauty Stock")
        crear_label(root, "Código").place(x=30, y=170, width=200, height=35)
        self.codigo = crear_entry(root)
        self.codigo.place(x=30, y=210, width=450, height=35)
        crear_label(root, "Nombre del producto").place(x=30, y=275, width=300, height=35)
        self.nombreprod = crear_entry(root)
        self.nombreprod.place(x=30, y=315, width=450, height=35)
        crear_label(root, "Precio (Q)").place(x=30, y=385, width=200, height=35)
        crear_label(root, "Cantidad").place(x=270, y=385, width=200, height=35)
        self.precio = crear_entry(root)
        self.precio.place(x=30, y=425, width=210, height=35)
        self.cantidad = crear_entry(root)
        self.cantidad.place(x=270, y=425, width=210, height=35)
        crear_label(root, "Categoría").place(x=30, y=495, width=200, height=35)
        self.categoria = crear_entry(root)
        self.categoria.place(x=30, y=535, width=450, height=35)
        crear_boton(root, "Guardar producto", self.on_save_btn, THEME_ACCENT,
                    "#FFFFFF", ("Helvetica", 13, "bold")).place(
                        x=30, y=635, width=220, height=65)
        crear_boton(root, "Cancelar", self.on_cancel_btna, THEME_FIELD_BG,
                    THEME_DARK, ("Helvetica", 13)).place(
                        x=270, y=635, width=220, height=65)

    def encabezado(self, root, titulo, subtitulo):
        self.frame1 = tk.Frame(root, bg=THEME_PINK, bd=0)
        self.frame1.place(x=0, y=0, width=520, height=140)
        tk.Label(self.frame1, text=titulo, font=("Helvetica", 25, "bold"),
                 bg=THEME_PINK, fg=THEME_FG).place(x=15, y=10, width=470, height=60)
        tk.Label(self.frame1, text=subtitulo, font=("Helvetica", 11),
                 bg=THEME_PINK, fg=THEME_FG).place(x=20, y=75, width=480, height=35)

    def on_save_btn(self):
        codigo, nombre = self.codigo.get().strip(), self.nombreprod.get().strip()
        precio_txt, cantidad_txt = self.precio.get().strip(), self.cantidad.get().strip()
        categoria = self.categoria.get().strip()
        if not all((codigo, nombre, precio_txt, cantidad_txt, categoria)):
            messagebox.showwarning("Campos incompletos", "Completa todos los campos.",
                                   parent=self.root)
            return
        if self.menu.buscar_producto(codigo):
            messagebox.showwarning("Código duplicado",
                                   "Ya existe un producto con ese código.",
                                   parent=self.root)
            return
        try:
            precio = float(precio_txt.replace(",", "."))
            cantidad = int(cantidad_txt)
            if precio < 0 or cantidad < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Datos inválidos",
                                 "El precio debe ser positivo y la cantidad un entero positivo.",
                                 parent=self.root)
            return
        self.menu.productos.append({
            "codigo": codigo, "nombre": nombre, "precio": precio,
            "cantidad": cantidad, "categoria": categoria})
        self.menu.actualizar_tabla()
        messagebox.showinfo("Producto guardado", f"Se agregó «{nombre}» al inventario.",
                            parent=self.root)
        self.cerrar()

    def on_cancel_btna(self):
        self.cerrar() if hasattr(self, "cerrar") else self.root.destroy()


class Buscar:
    def __init__(self, master, menu):
        self.menu = menu
        self.root = tk.Toplevel(master)
        root = self.root
        root.title("Beauty Stock - Buscar producto")
        root.geometry("520x750")
        root.resizable(False, False)
        apply_theme(root)
        Agregar.encabezado(self, root, "♡ Buscar producto",
                           "Ingresa el código del producto que quieres buscar")
        crear_label(root, "Código").place(x=35, y=175, width=200, height=35)
        self.code_btn_buscar = crear_entry(root)
        self.code_btn_buscar.place(x=35, y=215, width=450, height=35)
        crear_label(root, "Nombre del producto").place(x=35, y=285, width=300, height=35)
        self.entry2 = crear_entry(root, readonly=True)
        self.entry2.place(x=35, y=325, width=450, height=35)
        crear_label(root, "Precio (Q)").place(x=35, y=395, width=200, height=35)
        crear_label(root, "Cantidad").place(x=275, y=395, width=200, height=35)
        self.entry3 = crear_entry(root, readonly=True)
        self.entry3.place(x=35, y=435, width=210, height=35)
        self.entry4 = crear_entry(root, readonly=True)
        self.entry4.place(x=275, y=435, width=210, height=35)
        crear_label(root, "Categoría").place(x=35, y=505, width=200, height=35)
        self.entry5 = crear_entry(root, readonly=True)
        self.entry5.place(x=35, y=545, width=450, height=35)
        crear_boton(root, "Buscar producto", self.on_buscar_btnB, THEME_ACCENT,
                    "#FFFFFF", ("Helvetica", 13, "bold")).place(
                        x=25, y=635, width=220, height=65)
        crear_boton(root, "Cancelar", self.on_cancel_btnB, THEME_FIELD_BG,
                    THEME_DARK, ("Helvetica", 13)).place(
                        x=275, y=635, width=220, height=65)
        self.code_btn_buscar.bind("<Return>", lambda event: self.on_buscar_btnB())

    def on_buscar_btnB(self):
        codigo = self.code_btn_buscar.get().strip()
        if not codigo:
            messagebox.showwarning("Código requerido", "Ingresa el código del producto.",
                                   parent=self.root)
            return
        p = self.menu.buscar_producto(codigo)
        if not p:
            self.limpiar_resultados()
            messagebox.showinfo("Sin resultados", "No se encontró ese código.",
                                parent=self.root)
            return
        for entry, valor in ((self.entry2, p["nombre"]),
                             (self.entry3, f'{p["precio"]:.2f}'),
                             (self.entry4, p["cantidad"]),
                             (self.entry5, p["categoria"])):
            poner_texto_entry(entry, valor)

    def limpiar_resultados(self):
        for entry in (self.entry2, self.entry3, self.entry4, self.entry5):
            poner_texto_entry(entry, "")

    def on_cancel_btnB(self):
        self.cerrar() if hasattr(self, "cerrar") else self.root.destroy()


class Eliminar:
    def __init__(self, master, menu):
        self.menu = menu
        self.root = tk.Toplevel(master)
        root = self.root
        root.title("Beauty Stock - Eliminar producto")
        root.geometry("520x750")
        root.resizable(False, False)
        apply_theme(root)
        Agregar.encabezado(self, root, "♡ Eliminar producto",
                           "Ingresa el código del producto que deseas eliminar")
        crear_label(root, "Código").place(x=35, y=165, width=200, height=35)
        self.code_btn_eliminar = crear_entry(root)
        self.code_btn_eliminar.place(x=35, y=205, width=450, height=35)
        crear_label(root, "Nombre del producto").place(x=35, y=270, width=300, height=35)
        self.entry5 = crear_entry(root, readonly=True)
        self.entry5.place(x=35, y=310, width=450, height=35)
        crear_label(root, "Precio (Q)").place(x=35, y=380, width=200, height=35)
        crear_label(root, "Cantidad").place(x=275, y=380, width=200, height=35)
        self.entry2 = crear_entry(root, readonly=True)
        self.entry2.place(x=35, y=420, width=210, height=35)
        self.entry3 = crear_entry(root, readonly=True)
        self.entry3.place(x=275, y=420, width=210, height=35)
        crear_label(root, "Categoría").place(x=35, y=490, width=200, height=35)
        self.entry4 = crear_entry(root, readonly=True)
        self.entry4.place(x=35, y=530, width=450, height=35)
        crear_boton(root, "Eliminar producto", self.on_delete_btn, THEME_ACCENT,
                    "#FFFFFF", ("Helvetica", 13, "bold")).place(
                        x=30, y=630, width=220, height=65)
        crear_boton(root, "Cancelar", self.on_cancel_btn2, THEME_FIELD_BG,
                    THEME_DARK, ("Helvetica", 13)).place(
                        x=270, y=630, width=220, height=65)
        self.code_btn_eliminar.bind("<Return>", lambda event: self.mostrar_producto())

    def mostrar_producto(self):
        codigo = self.code_btn_eliminar.get().strip()
        if not codigo:
            messagebox.showwarning("Código requerido", "Ingresa el código del producto.",
                                   parent=self.root)
            return None
        p = self.menu.buscar_producto(codigo)
        if not p:
            self.limpiar_resultados()
            messagebox.showinfo("Sin resultados", "No se encontró ese código.",
                                parent=self.root)
            return None
        for entry, valor in ((self.entry5, p["nombre"]),
                             (self.entry2, f'{p["precio"]:.2f}'),
                             (self.entry3, p["cantidad"]),
                             (self.entry4, p["categoria"])):
            poner_texto_entry(entry, valor)
        return p

    def on_delete_btn(self):
        p = self.mostrar_producto()
        if p is None:
            return
        if not messagebox.askyesno("Confirmar eliminación",
                                   f'¿Seguro que deseas eliminar «{p["nombre"]}»?',
                                   parent=self.root):
            return
        self.menu.productos.remove(p)
        self.menu.actualizar_tabla()
        messagebox.showinfo("Producto eliminado",
                            "El producto se eliminó del inventario.",
                            parent=self.root)
        self.cerrar()

    def limpiar_resultados(self):
        for entry in (self.entry5, self.entry2, self.entry3, self.entry4):
            poner_texto_entry(entry, "")

    def on_cancel_btn2(self):
        self.cerrar() if hasattr(self, "cerrar") else self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()


#Los botones se cambiaron por labels con eventos de clic para que se respetaran los colores originales del wireframe, se agrego un hover para que cuando se pasara el mouse cambie de color el "boton", se cambiaron colores para que contrastaran mejor 
#Modificación más importante: controlar las ventanas emergentes abiertas (no permitir que otra ventana este abierta mientras ya lo este otra)Si se abre Agregar y se vuelve a pulsar Agregar, no se abrirá otra ventana encima. Y mientras se tenga una ventana secundaria abierta, no se podrá abrir otra desde el menú
#Cambios en login (nuevas validaciones): distiguir si hay campos vacios o credenciales incorrectas, se añadio la tecla enter para iniciar sesion desde el campo de contraseña (no es necesario tocar el boton)
#Mejoras en las funciones; agregar: ya valida los campos, evita que hayan codigos duplicados (P001 no puede existir dos veces); Buscar: cuando se agrega un codigo YA MUESTRA los datos de ese producto; Eliminar: solicita confirmar; Mostrar: actualiza los datos pero es algo inservible (puede que no se quede para la version final)
#Al cerrar sesion en el menú, devuelve al login
#Faltan Mejoras e incorporar las funciones de Diana fecha 22/10/2026
#Se incorporo el trabajo de Diana 30/10/2026 se hicieron los ultimos cambios 