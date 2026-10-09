# Definición de la clase Estudiante
class Estudiante:
    # Constructor que inicializa el nombre y un diccionario para guardar las notas
    def __init__(self, nombre, nota_minima_aprobacion=60):
        self.nombre = nombre  # Nombre del estudiante
        self.nota_minima_aprobacion = nota_minima_aprobacion  # Puntaje mínimo para aprobar
        self.materias = {}  # Diccionario con clave: materia y valor: nota (0-100)

    # Método para registrar o actualizar la nota de una materia
    def registrar_nota(self, materia, nota):
        if 0 <= nota <= 100:  # Valida que la nota esté dentro del rango permitido
            self.materias[materia] = nota  # Asigna la nota en el diccionario
            print(f"Nota registrada: {materia} -> {nota}")
        else:
            print("[ERROR] La nota debe estar entre 0 y 100.")

    # Método para calcular el promedio de todas las notas cargadas
    def calcular_promedio(self):
        if not self.materias:  # Verifica si no hay materias cargadas
            return 0.0
        return sum(self.materias.values()) / len(self.materias)  # Retorna el promedio simple

    # Método para verificar si el estudiante está en condición de aprobado
    def esta_aprobado(self):
        return self.calcular_promedio() >= self.nota_minima_aprobacion  # Retorna un booleano

    # Método para imprimir el boletín de calificaciones completo
    def __str__(self):
        res = f"=== BOLETÍN ACADÉMICO: {self.nombre} ===\n"
        for materia, nota in self.materias.items():  # Recorre cada materia cargada
            res += f"  - {materia}: {nota} pts.\n"
        prom = self.calcular_promedio()  # Obtiene el promedio final
        condicion = "APROBADO" if self.esta_aprobado() else "REPROBADO"  # Evalúa la condición
        res += f"--------------------------------------\n"
        res += f"Promedio General: {prom:.2f} pts. | Condición: [{condicion}]"
        return res


# Bloque de ejecución principal
if __name__ == "__main__":
    # Instanciación del estudiante
    estudiante = Estudiante("María Celeste", nota_minima_aprobacion=60)

    # Registro de notas del semestre
    estudiante.registrar_nota("Programación Orientada a Objetos", 95)
    estudiante.registrar_nota("Sistemas Distribuidos", 88)
    estudiante.registrar_nota("Cálculo Integral", 70)

    # Muestra el boletín de notas procesado
    print("\n" + str(estudiante))