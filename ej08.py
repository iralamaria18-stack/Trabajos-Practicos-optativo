# Clase que representa una Canción individual
class Cancion:
    # Constructor que define título, artista y duración en segundos
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo  # Título de la canción
        self.artista = artista  # Intérprete o banda
        self.duracion_segundos = duracion_segundos  # Tiempo en segundos

    # Representación en formato legible de la canción
    def __str__(self):
        minutos = self.duracion_segundos // 60  # Obtiene la cantidad de minutos
        segundos = self.duracion_segundos % 60  # Obtiene el residuo en segundos
        return f"'{self.titulo}' - {self.artista} ({minutos}:{segundos:02d} min)"


# Clase que representa la Lista de Reproducción que agrupa varias canciones
class ListaReproduccion:
    # Constructor que inicializa la lista vacía de canciones
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la playlist
        self.canciones = []  # Colección interna de objetos de tipo Cancion

    # Método para agregar un objeto Cancion a la lista
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)  # Inserta el objeto al final de la lista
        print(f"Canción agregada a '{self.nombre}': {cancion.titulo}")

    # Método para calcular la duración total recorriendo la colección
    def calcular_duracion_total(self):
        total_segundos = sum(c.duracion_segundos for c in self.canciones)  # Suma las duraciones
        minutos = total_segundos // 60  # Convierte a minutos
        segundos = total_segundos % 60  # Residuos en segundos
        return f"{minutos}:{segundos:02d} min"

    # Método para listar todas las canciones y la duración global
    def __str__(self):
        res = f"=== LISTA DE REPRODUCCIÓN: {self.nombre} ===\n"  # Encabezado
        for i, cancion in enumerate(self.canciones, start=1):  # Recorre la colección
            res += f"{i}. {cancion}\n"  # Agrega cada canción numerada
        res += f"Duración Total: {self.calcular_duracion_total()}\n"  # Muestra el total
        return res


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de objetos Cancion
    c1 = Cancion("Question!", "System of a Down", 200)
    c2 = Cancion("Chop Suey!", "System of a Down", 210)
    c3 = Cancion("Toxicity", "System of a Down", 219)

    # Creación del objeto ListaReproduccion
    playlist = ListaReproduccion("Rock Favorito")

    # Agregado de las canciones a la lista
    playlist.agregar_cancion(c1)
    playlist.agregar_cancion(c2)
    playlist.agregar_cancion(c3)

    # Impresión completa de la lista de reproducción
    print("\n" + str(playlist))