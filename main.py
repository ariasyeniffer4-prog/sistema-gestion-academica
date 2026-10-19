"""Punto de entrada del Sistema de Gestión Académica."""

from src.modelos import (
    Administrativo,
    Asignatura,
    Docente,
    Estudiante,
    ProgramaAcademico,
)


def main():
    programa = ProgramaAcademico(
        "115988",
        "Ingeniería en Análisis de Datos",
        "Facultad de Ciencias e Ingenierías",
        9,
    )
    asignatura = Asignatura(
        "POO-101", "Programación Orientada a Objetos", 3, programa
    )
    print(programa.mostrar_informacion())
    print()
    print(asignatura.mostrar_informacion())

    personas = [
        Estudiante(
            "1060655290",
            "Yeniffer Fernanda Arias Ordoñez",
            "ariasyeniffer4@gmail.com",
            "104202618344",
            programa,
            2,
            4.78,
        ),
        Estudiante(
            "1002", "Luis Gómez", "luis@ejemplo.edu.co", "E002", programa, 5, 3.9
        ),
        Docente(
            "2001", "Marta Ruiz", "marta@ejemplo.edu.co", "D001",
            "Ciencias e Ingenierías", "Tiempo completo", 40
        ),
        Docente(
            "2002", "Carlos Díaz", "carlos@ejemplo.edu.co", "D002",
            "Ciencias e Ingenierías", "Cátedra", 12
        ),
        Administrativo(
            "3001", "Sofía León", "sofia@ejemplo.edu.co", "A001",
            "Registro Académico", "Coordinadora", "Diurna"
        ),
        Administrativo(
            "3002", "Julián Mora", "julian@ejemplo.edu.co", "A002",
            "Biblioteca", "Auxiliar", "Mixta"
        ),
    ]

    # Cambio válido y tres intentos inválidos exigidos como demostración.
    personas[1].cambiar_correo_electronico("luis.gomez@ejemplo.edu.co")
    personas[0].cambiar_correo_electronico("")
    programa.cambiar_numero_semestres(9)
    programa.cambiar_numero_semestres(0)
    asignatura.cambiar_creditos(4)
    asignatura.cambiar_creditos(0)

    # Un solo ciclo y las mismas llamadas para todos: el tipo real determina
    # qué implementación de cada método se ejecuta (polimorfismo).
    for persona in personas:
        print("\n" + "-" * 50)
        print(persona.mostrar_informacion())
        print(persona.realizar_actividad_principal())


if __name__ == "__main__":
    main()
