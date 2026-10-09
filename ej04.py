# Definición de la clase Libro para el catálogo de una biblioteca
class Libro:
    # Constructor con título, autor y estado de disponibilidad (True o False)
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo  # Asigna el título del libro
        self.autor = autor  # Asigna el autor del libro
        self.disponible = disponible  # Guarda el estado (True = Disponible, False = Prestado)

    # Método especial que devuelve la ficha descriptiva del libro
    def __str__(self):
        # Evalúa el booleano y asigna el texto 'Disponible' o 'Prestado'
        estado_texto = "Disponible" if self.disponible else "Prestado"
        return f"Libro: '{self.titulo}' | Autor: {self.autor} | Estado: [{estado_texto}]"


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de un libro en estado Disponible
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", disponible=True)
    # Creación de un libro en estado Prestado
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", disponible=False)

    # Impresión de las fichas de los dos libros
    print(libro1)
    print(libro2)