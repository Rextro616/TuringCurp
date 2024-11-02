# curp_app.py

import tkinter as tk
from tkinter import messagebox
from curpGenerator import CurpGenerator

class CurpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de CURP")
        self.root.geometry("400x350")
        
        self.estados = {
            'AGUASCALIENTES': 'AS', 'BAJA CALIFORNIA': 'BC', 'BAJA CALIFORNIA SUR': 'BS', 'CAMPECHE': 'CC',
            'COAHUILA': 'CL', 'COLIMA': 'CM', 'CHIAPAS': 'CS', 'CHIHUAHUA': 'CH', 'CIUDAD DE MEXICO': 'DF',
            'DURANGO': 'DG', 'GUANAJUATO': 'GT', 'GUERRERO': 'GR', 'HIDALGO': 'HG', 'JALISCO': 'JC', 'MEXICO': 'MC',
            'MICHOACAN': 'MN', 'MORELOS': 'MS', 'NAYARIT': 'NT', 'NUEVO LEON': 'NL', 'OAXACA': 'OC', 'PUEBLA': 'PL',
            'QUERETARO': 'QT', 'QUINTANA ROO': 'QR', 'SAN LUIS POTOSI': 'SP', 'SINALOA': 'SL', 'SONORA': 'SR',
            'TABASCO': 'TC', 'TAMAULIPAS': 'TS', 'TLAXCALA': 'TL', 'VERACRUZ': 'VZ', 'YUCATAN': 'YN', 'ZACATECAS': 'ZS'
        }
        
        tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Apellido Paterno:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Apellido Materno:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(root, text="Fecha de Nacimiento (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(root, text="Sexo:").grid(row=4, column=0, padx=10, pady=5)
        tk.Label(root, text="Estado:").grid(row=5, column=0, padx=10, pady=5)

        self.entry_nombre = tk.Entry(root)
        self.entry_apellido_paterno = tk.Entry(root)
        self.entry_apellido_materno = tk.Entry(root)
        self.entry_fecha_nacimiento = tk.Entry(root)
        
        self.entry_nombre.grid(row=0, column=1, pady=5)
        self.entry_apellido_paterno.grid(row=1, column=1, pady=5)
        self.entry_apellido_materno.grid(row=2, column=1, pady=5)
        self.entry_fecha_nacimiento.grid(row=3, column=1, pady=5)
        
        self.sexo_var = tk.StringVar()
        self.sexo_var.set("H")  # Valor por defecto: Hombre
        tk.OptionMenu(root, self.sexo_var, "H", "M").grid(row=4, column=1, pady=5)
        
        self.estado_var = tk.StringVar()
        self.estado_var.set("AGUASCALIENTES")  # Valor por defecto
        tk.OptionMenu(root, self.estado_var, *self.estados.keys()).grid(row=5, column=1, pady=5)
        
        tk.Button(root, text="Generar CURP", command=self.generar_curp).grid(row=6, columnspan=2, pady=10)
        
        self.curp_label = tk.Label(root, text="", fg="white")
        self.curp_label.grid(row=7, columnspan=2, pady=10)

    def generar_curp(self):
        nombre = self.entry_nombre.get()
        apellido_paterno = self.entry_apellido_paterno.get()
        apellido_materno = self.entry_apellido_materno.get()
        fecha_nacimiento = self.entry_fecha_nacimiento.get()
        sexo = "Hombre" if self.sexo_var.get() == "H" else "Mujer"
        estado = self.estado_var.get()
        
        if not all([nombre, apellido_paterno, apellido_materno, fecha_nacimiento]):
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            return
        
        try:
            curp_gen = CurpGenerator(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado)
            curp = curp_gen.generar_curp()
            self.curp_label.config(text=f"CURP Generada: {curp}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar CURP: {e}")
