import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
import json

class GestorFinanzas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Finanzas")
        self.geometry("900x800")
        self.configure(bg='white')
        
        self.cargar_datos()
        
        # Frame principal
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Descripción
        ttk.Label(main_frame, text="Descripción:", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="W")
        self.entrada_descripcion = ttk.Entry(main_frame, font=("Arial", 12), width=30)
        self.entrada_descripcion.grid(row=0, column=1, pady=5, sticky="WE")

        # Cantidad
        ttk.Label(main_frame, text="Cantidad:", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="W")
        self.entrada_cantidad = ttk.Entry(main_frame, font=("Arial", 12), width=30)
        self.entrada_cantidad.grid(row=1, column=1, pady=5, sticky="WE")

        # Tipo
        ttk.Label(main_frame, text="Tipo:", font=("Arial", 12)).grid(row=2, column=0, pady=5, sticky="W")
        self.opcion_tipo = tk.StringVar(value="Gastos")
        ttk.OptionMenu(main_frame, self.opcion_tipo, "Gastos", "Gastos", "Ingresos").grid(row=2, column=1, pady=5, sticky="WE")

        # Fecha
        ttk.Label(main_frame, text="Fecha:", font=("Arial", 12)).grid(row=3, column=0, pady=5, sticky="W")
        self.fecha_calendario = DateEntry(main_frame, width=12, font=("Arial", 12), date_pattern="yyyy-mm-dd", maxdate=datetime.today(), showweeknumbers=False)
        self.fecha_calendario.grid(row=3, column=1, pady=5, sticky="WE")

        # Botón para agregar
        ttk.Button(main_frame, text="Agregar Registro", command=self.agregar_registro).grid(row=4, column=0, columnspan=2, pady=10)

        # Botón para eliminar y editar
        ttk.Button(main_frame, text="Eliminar Registro", command=self.eliminar_registro).grid(row=5, column=0, pady=10)
        ttk.Button(main_frame, text="Editar Registro", command=self.editar_registro).grid(row=5, column=1, pady=10)

        # Botón para borrar todo
        ttk.Button(main_frame, text="Borrar Todo", command=self.borrar_todo).grid(row=6, column=0, columnspan=2, pady=10)

        # Tabla de Registros
        self.tree = ttk.Treeview(main_frame, columns=("tipo", "descripcion", "cantidad", "fecha"), show="headings", height=10)
        self.tree.grid(row=7, column=0, columnspan=2, pady=10, sticky="WE")
        self.tree.heading("tipo", text="Tipo")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.heading("cantidad", text="Cantidad")
        self.tree.heading("fecha", text="Fecha")

        # Estadísticas
        self.label_estadisticas = ttk.Label(main_frame, text="", font=("Arial", 12, "bold"))
        self.label_estadisticas.grid(row=8, column=0, columnspan=2, pady=10)

        self.mostrar_registros()
        self.actualizar_estadisticas()

    def cargar_datos(self):
        try:
            with open('datos.json', 'r') as f:
                self.registros = json.load(f)
        except FileNotFoundError:
            self.registros = {"Gastos": [], "Ingresos": []}

    def guardar_datos(self):
        with open('datos.json', 'w') as f:
            json.dump(self.registros, f)

    def agregar_registro(self):
        descripcion = self.entrada_descripcion.get()
        cantidad = self.entrada_cantidad.get()
        tipo = self.opcion_tipo.get()
        fecha = self.fecha_calendario.get_date().strftime("%Y-%m-%d")
        
        if not descripcion or not cantidad:
            messagebox.showwarning("Error", "Ingrese una descripción y una cantidad válida")
            return
        
        try:
            cantidad = float(cantidad)
        except ValueError:
            messagebox.showwarning("Error", "La cantidad debe ser un número")
            return
        
        self.registros[tipo].append({"Descripción": descripcion, "Cantidad": cantidad, "Fecha": fecha})
        self.mostrar_registros()
        self.actualizar_estadisticas()
        self.guardar_datos()
        messagebox.showinfo("Éxito", "Registro agregado correctamente")

    def eliminar_registro(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            tipo, descripcion, cantidad, fecha = item["values"]
            registro_a_eliminar = next((r for r in self.registros[tipo] if r["Descripción"] == descripcion and r["Cantidad"] == float(cantidad) and r["Fecha"] == fecha), None)
            if registro_a_eliminar:
                self.registros[tipo].remove(registro_a_eliminar)
                self.mostrar_registros()
                self.actualizar_estadisticas()
                self.guardar_datos()
                messagebox.showinfo("Éxito", "Registro eliminado correctamente")
        else:
            messagebox.showwarning("Error", "Seleccione un registro para eliminar")

    def editar_registro(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            tipo, descripcion, cantidad, fecha = item["values"]
            registro_a_editar = next((r for r in self.registros[tipo] if r["Descripción"] == descripcion and r["Cantidad"] == float(cantidad) and r["Fecha"] == fecha), None)
            if registro_a_editar:
                self.entrada_descripcion.delete(0, tk.END)
                self.entrada_descripcion.insert(0, descripcion)
                self.entrada_cantidad.delete(0, tk.END)
                self.entrada_cantidad.insert(0, str(cantidad))
                self.opcion_tipo.set(tipo)
                self.fecha_calendario.set_date(datetime.strptime(fecha, "%Y-%m-%d"))
                self.registros[tipo].remove(registro_a_editar)
                self.mostrar_registros()
                self.actualizar_estadisticas()
                self.guardar_datos()
                messagebox.showinfo("Listo", "Edite los datos y presione Agregar para actualizar el registro")
        else:
            messagebox.showwarning("Error", "Seleccione un registro para editar")

    def borrar_todo(self):
        confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro que desea borrar todos los registros?")
        if confirmacion:
            self.registros = {"Gastos": [], "Ingresos": []}
            self.mostrar_registros()
            self.actualizar_estadisticas()
            self.guardar_datos()
            messagebox.showinfo("Éxito", "Todos los registros han sido borrados correctamente")

    def mostrar_registros(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for tipo, lista in self.registros.items():
            lista_ordenada = sorted(lista, key=lambda x: datetime.strptime(x['Fecha'], "%Y-%m-%d"))
            for registro in lista_ordenada:
                self.tree.insert("", tk.END, values=(tipo, registro["Descripción"], registro["Cantidad"], registro["Fecha"]))

    def actualizar_estadisticas(self):
        total_gastos = sum(r['Cantidad'] for r in self.registros['Gastos'])
        total_ingresos = sum(r['Cantidad'] for r in self.registros['Ingresos'])
        neto = total_ingresos - total_gastos
        self.label_estadisticas.config(text=f"Total Gastos: ${total_gastos:.2f} - Total Ingresos: ${total_ingresos:.2f} - Neto: ${neto:.2f}")

if __name__ == "__main__":
    app = GestorFinanzas()
    app.mainloop()
