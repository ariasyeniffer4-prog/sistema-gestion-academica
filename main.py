"""Punto de entrada del Sistema de Gestión Académica."""

from src.modelos import (
    Administrativo,
    AsignaturaNoEncontradaError,
    Asignatura,
    CapacidadGrupoCompletaError,
    Docente,
    Estudiante,
    EstudianteNoMatriculadoError,
    EstudianteYaMatriculadoError,
    GrupoAcademico,
    ProgramaNoEncontradoError,
    ProgramaAcademico,
    buscar_asignatura,
    buscar_programa,
)


def main():
    print("Intento de crear Persona directamente:")
    try:
        # Persona es abstracta; este intento debe ser rechazado por Python.
        from src.modelos import Persona
        Persona("0", "Persona genérica", "persona@ejemplo.edu.co")
    except TypeError as error:
        print(f"No se puede instanciar Persona: {error}")

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

    programas = [programa]
    asignaturas = [asignatura]
    docente = personas[2]
    estudiante_uno, estudiante_dos = personas[0], personas[1]
    estudiante_tres = Estudiante(
        "1003", "Ana Pérez", "ana@ejemplo.edu.co", "E003", programa, 3, 4.2
    )
    grupo_uno = GrupoAcademico(
        "G-POO-01", asignatura, docente, 2,
        "Lunes", "08:00", "10:00", "B-201"
    )
    grupo_dos = GrupoAcademico(
        "G-POO-02", asignatura, personas[3], 3,
        "Miércoles", "10:00", "12:00", "B-202"
    )
    print("\nGrupos académicos creados:")
    print(grupo_uno.mostrar_informacion_grupo())
    print(grupo_dos.mostrar_informacion_grupo())

    # Cada error se captura donde se demuestra para que el flujo continúe.
    try:
        grupo_uno.matricular_estudiante(estudiante_uno)
        print("\nMatrícula válida realizada en G-POO-01.")
    except (EstudianteYaMatriculadoError, CapacidadGrupoCompletaError) as error:
        print(f"No fue posible matricular: {error}")

    try:
        grupo_uno.matricular_estudiante(estudiante_uno)
    except EstudianteYaMatriculadoError as error:
        print(f"\nMatrícula duplicada controlada: {error}")

    grupo_uno.matricular_estudiante(estudiante_dos)
    try:
        grupo_uno.matricular_estudiante(estudiante_tres)
    except CapacidadGrupoCompletaError as error:
        print(f"Capacidad máxima controlada: {error}")

    try:
        grupo_uno.retirar_estudiante(estudiante_dos.obtener_codigo_estudiantil())
        print("Retiro válido realizado.")
    except EstudianteNoMatriculadoError as error:
        print(f"No fue posible retirar: {error}")

    try:
        grupo_uno.retirar_estudiante("E-NO-EXISTE")
    except EstudianteNoMatriculadoError as error:
        print(f"Retiro de estudiante no matriculado controlado: {error}")

    try:
        buscar_asignatura(asignaturas, "NO-EXISTE")
    except AsignaturaNoEncontradaError as error:
        print(f"Búsqueda de asignatura controlada: {error}")

    try:
        buscar_programa(programas, "NO-EXISTE")
    except ProgramaNoEncontradoError as error:
        print(f"Búsqueda de programa controlada: {error}")

    print("\nEl programa continúa después de los casos excepcionales.")
    print("Estudiantes actuales en G-POO-01:")
    print(grupo_uno.mostrar_estudiantes())

    # Cambios válidos y valores inválidos rechazados por las validaciones.
    personas[1].cambiar_correo_electronico("luis.gomez@ejemplo.edu.co")
    personas[0].cambiar_correo_electronico("")
    programa.cambiar_numero_semestres(9)
    programa.cambiar_numero_semestres(0)
    asignatura.cambiar_creditos(4)
    asignatura.cambiar_creditos(0)
    personas[1].cambiar_semestre(0)
    personas[1].cambiar_promedio_acumulado(5.5)
    personas[2].cambiar_horas_semanales(0)

    # Un solo ciclo y las mismas llamadas para todos: el tipo real determina
    # qué implementación de cada método se ejecuta (polimorfismo).
    for persona in personas:
        print("\n" + "-" * 50)
        print(persona.mostrar_informacion())
        print(persona.realizar_actividad_principal())


if __name__ == "__main__":
    main()
