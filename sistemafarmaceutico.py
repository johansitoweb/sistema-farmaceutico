import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class Farmacia:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Farmacia")
        self.root.geometry("800x600")

        # Inicialización de datos
        self.productos = {}
        self.proveedores = {}
        self.clientes = {}
        self.recetas = {}
        self.ventas = []

        # Tabs
        self.tab_control = ttk.Notebook(root)
        self.tab_productos = ttk.Frame(self.tab_control)
        self.tab_proveedores = ttk.Frame(self.tab_control)
        self.tab_clientes = ttk.Frame(self.tab_control)
        self.tab_recetas = ttk.Frame(self.tab_control)
        self.tab_ventas = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_productos, text="Productos")
        self.tab_control.add(self.tab_proveedores, text="Proveedores")
        self.tab_control.add(self.tab_clientes, text="Clientes")
        self.tab_control.add(self.tab_recetas, text="Recetas")
        self.tab_control.add(self.tab_ventas, text="Ventas")
        self.tab_control.pack(expand=1, fill="both")

        # Configuración de cada pestaña
        self.configurar_tab_productos()
        self.configurar_tab_proveedores()
        self.configurar_tab_clientes()
        self.configurar_tab_recetas()
        self.configurar_tab_ventas()

    def configurar_tab_productos(self):
        # Entradas de productos
        self.label_nombre = tk.Label(self.tab_productos, text="Nombre del Producto:")
        self.label_nombre.grid(row=0, column=0)
        self.entry_nombre = tk.Entry(self.tab_productos)
        self.entry_nombre.grid(row=0, column=1)

        self.label_precio = tk.Label(self.tab_productos, text="Precio:")
        self.label_precio.grid(row=1, column=0)
        self.entry_precio = tk.Entry(self.tab_productos)
        self.entry_precio.grid(row=1, column=1)

        self.label_categoria = tk.Label(self.tab_productos, text="Categoría:")
        self.label_categoria.grid(row=2, column=0)
        self.entry_categoria = tk.Entry(self.tab_productos)
        self.entry_categoria.grid(row=2, column=1)

        self.label_cantidad = tk.Label(self.tab_productos, text="Cantidad:")
        self.label_cantidad.grid(row=3, column=0)
        self.entry_cantidad = tk.Entry(self.tab_productos)
        self.entry_cantidad.grid(row=3, column=1)

        self.label_fecha_caducidad = tk.Label(self.tab_productos, text="Fecha de Caducidad:")
        self.label_fecha_caducidad.grid(row=4, column=0)
        self.entry_fecha_caducidad = tk.Entry(self.tab_productos)
        self.entry_fecha_caducidad.grid(row=4, column=1)

        self.btn_agregar_producto = tk.Button(self.tab_productos, text="Agregar Producto", command=self.agregar_producto)
        self.btn_agregar_producto.grid(row=5, columnspan=2, pady=10)

        self.btn_mostrar_productos = tk.Button(self.tab_productos, text="Mostrar Productos", command=self.mostrar_productos)
        self.btn_mostrar_productos.grid(row=6, columnspan=2, pady=10)

        # Tabla para mostrar productos
        self.tree = ttk.Treeview(self.tab_productos, columns=("Nombre", "Precio", "Categoría", "Cantidad", "Fecha de Caducidad"), show='headings')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Fecha de Caducidad", text="Fecha de Caducidad")
        self.tree.column("Nombre", width=150)
        self.tree.column("Precio", width=100)
        self.tree.column("Categoría", width=100)
        self.tree.column("Cantidad", width=100)
        self.tree.column("Fecha de Caducidad", width=150)
        self.tree.grid(row=7, columnspan=2, pady=10)

    def agregar_producto(self):
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        categoria = self.entry_categoria.get()
        cantidad = self.entry_cantidad.get()
        fecha_caducidad = self.entry_fecha_caducidad.get()

        if nombre and precio.replace('.', '', 1).isdigit() and categoria and cantidad.isdigit() and fecha_caducidad:
            precio = float(precio)
            cantidad = int(cantidad)
            self.productos[nombre] = {
                'precio': precio,
                'categoria': categoria,
                'cantidad': cantidad,
                'fecha_caducidad': fecha_caducidad
            }
            messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado.")
            self.limpiar_campos_productos()
        else:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")

    def limpiar_campos_productos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_fecha_caducidad.delete(0, tk.END)

    def mostrar_productos(self):
        # Limpiar la tabla antes de mostrar los productos
        for item in self.tree.get_children():
            self.tree.delete(item)

        for nombre, info in self.productos.items():
            self.tree.insert("", "end", values=(nombre, info['precio'], info['categoria'], info['cantidad'], info['fecha_caducidad']))

    # Resto del código permanece igual...

    def configurar_tab_proveedores(self):
        # Entradas de proveedores
        self.label_proveedor = tk.Label(self.tab_proveedores, text="Nombre del Proveedor:")
        self.label_proveedor.grid(row=0, column=0)
        self.entry_proveedor = tk.Entry(self.tab_proveedores)
        self.entry_proveedor.grid(row=0, column=1)

        self.label_contacto = tk.Label(self.tab_proveedores, text="Contacto:")
        self.label_contacto.grid(row=1, column=0)
        self.entry_contacto = tk.Entry(self.tab_proveedores)
        self.entry_contacto.grid(row=1, column=1)

        self.btn_agregar_proveedor = tk.Button(self.tab_proveedores, text="Agregar Proveedor", command=self.agregar_proveedor)
        self.btn_agregar_proveedor.grid(row=2, columnspan=2, pady=10)

        self.btn_mostrar_proveedores = tk.Button(self.tab_proveedores, text="Mostrar Proveedores", command=self.mostrar_proveedores)
        self.btn_mostrar_proveedores.grid(row=3, columnspan=2, pady=10)

    def agregar_proveedor(self):
        nombre = self.entry_proveedor.get()
        contacto = self.entry_contacto.get()

        if nombre and contacto:
            self.proveedores[nombre] = contacto
            messagebox.showinfo("Éxito", f"Proveedor '{nombre}' agregado.")
            self.entry_proveedor.delete(0, tk.END)
            self.entry_contacto.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")

    def mostrar_proveedores(self):
        proveedores_list = "\n".join([f"{nombre}: {contacto}" for nombre, contacto in self.proveedores.items()])
        if not proveedores_list:
            proveedores_list = "No hay proveedores registrados."
        messagebox.showinfo("Proveedores", proveedores_list)

    def configurar_tab_clientes(self):
        # Entradas de clientes
        self.label_cliente = tk.Label(self.tab_clientes, text="Nombre del Cliente:")
        self.label_cliente.grid(row=0, column=0)
        self.entry_cliente = tk.Entry(self.tab_clientes)
        self.entry_cliente.grid(row=0, column=1)

        self.label_direccion = tk.Label(self.tab_clientes, text="Dirección:")
        self.label_direccion.grid(row=1, column=0)
        self.entry_direccion = tk.Entry(self.tab_clientes)
        self.entry_direccion.grid(row=1, column=1)

        self.btn_agregar_cliente = tk.Button(self.tab_clientes, text="Agregar Cliente", command=self.agregar_cliente)
        self.btn_agregar_cliente.grid(row=2, columnspan=2, pady=10)

        self.btn_mostrar_clientes = tk.Button(self.tab_clientes, text="Mostrar Clientes", command=self.mostrar_clientes)
        self.btn_mostrar_clientes.grid(row=3, columnspan=2, pady=10)

    def agregar_cliente(self):
        nombre = self.entry_cliente.get()
        direccion = self.entry_direccion.get()

        if nombre and direccion:
            self.clientes[nombre] = direccion
            messagebox.showinfo("Éxito", f"Cliente '{nombre}' agregado.")
            self.entry_cliente.delete(0, tk.END)
            self.entry_direccion.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")

    def mostrar_clientes(self):
        clientes_list = "\n".join([f"{nombre}: {direccion}" for nombre, direccion in self.clientes.items()])
        if not clientes_list:
            clientes_list = "No hay clientes registrados."
        messagebox.showinfo("Clientes", clientes_list)

    def configurar_tab_recetas(self):
        # Entradas de recetas
        self.label_receta = tk.Label(self.tab_recetas, text="Nombre del Paciente:")
        self.label_receta.grid(row=0, column=0)
        self.entry_receta = tk.Entry(self.tab_recetas)
        self.entry_receta.grid(row=0, column=1)

        self.label_medicamento = tk.Label(self.tab_recetas, text="Medicamento:")
        self.label_medicamento.grid(row=1, column=0)
        self.entry_medicamento = tk.Entry(self.tab_recetas)
        self.entry_medicamento.grid(row=1, column=1)

        self.btn_agregar_receta = tk.Button(self.tab_recetas, text="Agregar Receta", command=self.agregar_receta)
        self.btn_agregar_receta.grid(row=2, columnspan=2, pady=10)

        self.btn_mostrar_recetas = tk.Button(self.tab_recetas, text="Mostrar Recetas", command=self.mostrar_recetas)
        self.btn_mostrar_recetas.grid(row=3, columnspan=2, pady=10)

    def agregar_receta(self):
        paciente = self.entry_receta.get()
        medicamento = self.entry_medicamento.get()

        if paciente and medicamento:
            self.recetas[paciente] = medicamento
            messagebox.showinfo("Éxito", f"Receta para '{paciente}' agregada.")
            self.entry_receta.delete(0, tk.END)
            self.entry_medicamento.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")

    def mostrar_recetas(self):
        recetas_list = "\n".join([f"{paciente}: {medicamento}" for paciente, medicamento in self.recetas.items()])
        if not recetas_list:
            recetas_list = "No hay recetas registradas."
        messagebox.showinfo("Recetas", recetas_list)

    def configurar_tab_ventas(self):
        # Entradas de ventas
        self.label_cliente_venta = tk.Label(self.tab_ventas, text="Nombre del Cliente:")
        self.label_cliente_venta.grid(row=0, column=0)
        self.entry_cliente_venta = tk.Entry(self.tab_ventas)
        self.entry_cliente_venta.grid(row=0, column=1)

        self.label_medicamento_venta = tk.Label(self.tab_ventas, text="Medicamento:")
        self.label_medicamento_venta.grid(row=1, column=0)
        self.entry_medicamento_venta = tk.Entry(self.tab_ventas)
        self.entry_medicamento_venta.grid(row=1, column=1)

        self.label_cantidad_venta = tk.Label(self.tab_ventas, text="Cantidad:")
        self.label_cantidad_venta.grid(row=2, column=0)
        self.entry_cantidad_venta = tk.Entry(self.tab_ventas)
        self.entry_cantidad_venta.grid(row=2, column=1)

        self.btn_agregar_venta = tk.Button(self.tab_ventas, text="Registrar Venta", command=self.registrar_venta)
        self.btn_agregar_venta.grid(row=3, columnspan=2, pady=10)

        self.btn_mostrar_ventas = tk.Button(self.tab_ventas, text="Mostrar Ventas", command=self.mostrar_ventas)
        self.btn_mostrar_ventas.grid(row=4, columnspan=2, pady=10)

    def registrar_venta(self):
        cliente = self.entry_cliente_venta.get()
        medicamento = self.entry_medicamento_venta.get()
        cantidad = self.entry_cantidad_venta.get()

        if cliente in self.clientes and medicamento in self.productos and cantidad.isdigit():
            cantidad = int(cantidad)
            if self.productos[medicamento]['cantidad'] >= cantidad:
                self.productos[medicamento]['cantidad'] -= cantidad
                self.ventas.append((cliente, medicamento, cantidad, datetime.now()))
                messagebox.showinfo("Éxito", f"Venta registrada: {cantidad} de '{medicamento}' a '{cliente}'.")
                self.entry_cliente_venta.delete(0, tk.END)
                self.entry_medicamento_venta.delete(0, tk.END)
                self.entry_cantidad_venta.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "No hay suficiente stock.")
        else:
            messagebox.showerror("Error", "Datos de cliente o medicamento inválidos.")

    def mostrar_ventas(self):
        ventas_list = "\n".join([f"Cliente: {cliente}, Medicamento: {medicamento}, Cantidad: {cantidad}, Fecha: {fecha.strftime('%Y-%m-%d %H:%M:%S')}" for cliente, medicamento, cantidad, fecha in self.ventas])
        if not ventas_list:
            ventas_list = "No hay ventas registradas."
        messagebox.showinfo("Ventas", ventas_list)

if __name__ == "__main__":
    root = tk.Tk()
    app = Farmacia(root)
    root.mainloop()
