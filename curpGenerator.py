import random
import string

class CurpGenerator:
    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado):
        self.nombre = nombre.upper()
        self.apellido_paterno = apellido_paterno.upper()
        self.apellido_materno = apellido_materno.upper() if apellido_materno else "X"
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo[0].upper()
        self.estado = estado.upper()
        self.entidades = {
            'AS': 'AGUASCALIENTES', 'BC': 'BAJA CALIFORNIA', 'BS': 'BAJA CALIFORNIA SUR', 'CC': 'CAMPECHE',
            'CL': 'COAHUILA', 'CM': 'COLIMA', 'CS': 'CHIAPAS', 'CH': 'CHIHUAHUA', 'DF': 'CIUDAD DE MEXICO',
            'DG': 'DURANGO', 'GT': 'GUANAJUATO', 'GR': 'GUERRERO', 'HG': 'HIDALGO', 'JC': 'JALISCO', 'MC': 'MEXICO',
            'MN': 'MICHOACAN', 'MS': 'MORELOS', 'NT': 'NAYARIT', 'NL': 'NUEVO LEON', 'OC': 'OAXACA', 'PL': 'PUEBLA',
            'QT': 'QUERETARO', 'QR': 'QUINTANA ROO', 'SP': 'SAN LUIS POTOSI', 'SL': 'SINALOA', 'SR': 'SONORA',
            'TC': 'TABASCO', 'TS': 'TAMAULIPAS', 'TL': 'TLAXCALA', 'VZ': 'VERACRUZ', 'YN': 'YUCATAN', 'ZS': 'ZACATECAS'
        }

    def obtener_codigo_estado(self):
        return next((key for key, value in self.entidades.items() if value == self.estado), "NE")

    def obtener_letra_nombre(self):
        nombres_excepciones = ["MARIA", "JOSE"]
        nombre_principal = self.nombre.split()[0]
        if nombre_principal in nombres_excepciones and len(self.nombre.split()) > 1:
            nombre_principal = self.nombre.split()[1]
        return nombre_principal[0]

    def obtener_vocal_interna(self, palabra):
        return next((char for char in palabra[1:] if char in "AEIOU"), "X")

    def obtener_consonante_interna(self, palabra):
        return next((char for char in palabra[1:] if char not in "AEIOU"), "X")
    
    def generar_caracter_aleatorio(self):
        opciones = list(string.digits) + list(string.ascii_uppercase)
        return random.choice(opciones)

    def generar_curp(self):
        primera_letra_apellido = self.apellido_paterno[0]
        primera_vocal_apellido = self.obtener_vocal_interna(self.apellido_paterno)
        primera_letra_materno = self.apellido_materno[0]
        primera_letra_nombre = self.obtener_letra_nombre()
        
        año = self.fecha_nacimiento[:4]
        mes = self.fecha_nacimiento[5:7]
        dia = self.fecha_nacimiento[8:10]
        fecha_curp = año[2:] + mes + dia
        
        letra_sexo = self.sexo
        codigo_estado = self.obtener_codigo_estado()
        
        consonante_apellido_paterno = self.obtener_consonante_interna(self.apellido_paterno)
        consonante_apellido_materno = self.obtener_consonante_interna(self.apellido_materno)
        consonante_nombre = self.obtener_consonante_interna(self.nombre)
        
        homoclave = self.generar_caracter_aleatorio() + str(random.randint(0, 9))
        
        curp = (primera_letra_apellido + primera_vocal_apellido + primera_letra_materno +
                primera_letra_nombre + fecha_curp + letra_sexo + codigo_estado +
                consonante_apellido_paterno + consonante_apellido_materno + consonante_nombre + homoclave)
        
        return curp.upper()
