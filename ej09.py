# Clase que representa un Turno médico
class Turno:
    # Constructor del turno con paciente, hora y estado inicial "pendiente"
    def __init__(self, paciente, hora):
        self.paciente = paciente  # Nombre del paciente
        self.hora = hora  # Hora fijada para la cita (ej. "09:00")
        self.atendido = False  # Estado del turno (False = Pendiente, True = Atendido)

    # Método para marcar el turno como atendido
    def marcar_como_atendido(self):
        self.atendido = True  # Modifica el estado interno a True

    # Representación en texto del turno
    def __str__(self):
        estado_str = "Atendido" if self.atendido else "Pendiente"
        return f"Hora: {self.hora} | Paciente: {self.paciente} | Estado: [{estado_str}]"


# Clase Agenda que gestiona el conjunto de turnos del día
class Agenda:
    # Constructor que inicializa una lista de turnos vacía
    def __init__(self, fecha):
        self.fecha = fecha  # Fecha de la jornada del consultorio
        self.turnos = []  # Lista que contendrá objetos de tipo Turno

    # Método para agendar un nuevo turno
    def agendar_turno(self, turno):
        self.turnos.append(turno)  # Agrega el turno a la agenda
        print(f"Turno agendado para {turno.paciente} a las {turno.hora}")

    # Método para listar solamente los turnos que están pendientes
    def listar_pendientes(self):
        print(f"\n--- TURNOS PENDIENTES PARA EL {self.fecha} ---")
        pendientes = [t for t in self.turnos if not t.atendido]  # Filtra los no atendidos
        if not pendientes:  # Verifica si la lista filtrada está vacía
            print("No quedan turnos pendientes para el día.")
        else:
            for t in pendientes:  # Muestra cada turno pendiente
                print(t)

    # Muestra el estado completo de la agenda
    def __str__(self):
        res = f"=== AGENDA DEL DÍA {self.fecha} ===\n"
        for t in self.turnos:
            res += str(t) + "\n"
        return res


# Bloque de ejecución principal
if __name__ == "__main__":
    # Creación de la agenda del día
    agenda = Agenda("09/10/2026")

    # Instanciación de turnos
    t1 = Turno("María Celeste", "08:30")
    t2 = Turno("Facundo Campuzano", "09:15")
    t3 = Turno("Ana Rodríguez", "10:00")

    # Agendado de turnos
    agenda.agendar_turno(t1)
    agenda.agendar_turno(t2)
    agenda.agendar_turno(t3)

    # Se atiende al primer paciente
    t1.marcar_como_atendido()
    print(f"\n[ATENCIÓN] Se atendió la cita de las {t1.hora}")

    # Se muestran los turnos que continúan pendientes
    agenda.listar_pendientes()