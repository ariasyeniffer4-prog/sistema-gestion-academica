"""Modelos iniciales del Sistema de Gestión Académica."""


class Persona:
    """Información común de una persona vinculada con la universidad."""

    def __init__(self, identificacion, nombre, correo_electronico):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo_electronico = correo_electronico

    def obtener_identificacion(self):
        return self.__identificacion

    def obtener_nombre(self):
        return self.__nombre

    def obtener_correo_electronico(self):
        return self.__correo_electronico

    def cambiar_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def cambiar_identificacion(self, nueva_identificacion):
        self.__identificacion = nueva_identificacion

    def cambiar_correo_electronico(self, nuevo_correo):
        if not nuevo_correo or not nuevo_correo.strip():
            print("Error: el correo electrónico no puede estar vacío.")
            return False
        self.__correo_electronico = nuevo_correo
        return True

    def mostrar_informacion(self):
        return (
            f"Identificación: {self.__identificacion}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo electrónico: {self.__correo_electronico}"
        )

    def realizar_actividad_principal(self):
        return "La persona realiza sus actividades en la universidad."


class ProgramaAcademico:
    """Programa académico ofrecido por una facultad."""

    def __init__(self, codigo, nombre, facultad, numero_semestres):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__facultad = facultad
        self.__numero_semestres = None
        self.cambiar_numero_semestres(numero_semestres)

    def obtener_codigo(self):
        return self.__codigo

    def obtener_nombre(self):
        return self.__nombre

    def obtener_facultad(self):
        return self.__facultad

    def obtener_numero_semestres(self):
        return self.__numero_semestres

    def cambiar_numero_semestres(self, cantidad):
        if not isinstance(cantidad, int) or cantidad <= 0:
            print("Error: el número de semestres debe ser un entero mayor que cero.")
            return False
        self.__numero_semestres = cantidad
        return True

    def mostrar_informacion(self):
        return (
            f"Programa: {self.__nombre} ({self.__codigo})\n"
            f"Facultad: {self.__facultad}\n"
            f"Número de semestres: {self.__numero_semestres}"
        )


class Asignatura:
    """Asignatura asociada con un programa académico."""

    def __init__(self, codigo, nombre, creditos, programa_academico):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = None
        self.__programa_academico = programa_academico
        self.cambiar_creditos(creditos)

    def obtener_codigo(self):
        return self.__codigo

    def obtener_nombre(self):
        return self.__nombre

    def obtener_creditos(self):
        return self.__creditos

    def obtener_programa_academico(self):
        return self.__programa_academico

    def cambiar_creditos(self, cantidad):
        if not isinstance(cantidad, int) or cantidad <= 0:
            print("Error: el número de créditos debe ser un entero mayor que cero.")
            return False
        self.__creditos = cantidad
        return True

    def mostrar_informacion(self):
        return (
            f"Asignatura: {self.__nombre} ({self.__codigo})\n"
            f"Créditos: {self.__creditos}\n"
            f"Programa: {self.__programa_academico.obtener_nombre()}"
        )


class Estudiante(Persona):
    """Persona que cursa un programa académico."""

    def __init__(self, identificacion, nombre, correo_electronico,
                 codigo_estudiantil, programa_academico, semestre,
                 promedio_acumulado):
        super().__init__(identificacion, nombre, correo_electronico)
        self.__codigo_estudiantil = codigo_estudiantil
        self.__programa_academico = programa_academico
        self.__semestre = semestre
        self.__promedio_acumulado = promedio_acumulado

    def obtener_codigo_estudiantil(self):
        return self.__codigo_estudiantil

    def obtener_programa_academico(self):
        return self.__programa_academico

    def obtener_semestre(self):
        return self.__semestre

    def obtener_promedio_acumulado(self):
        return self.__promedio_acumulado

    def cambiar_semestre(self, semestre):
        if not isinstance(semestre, int) or semestre <= 0:
            print("Error: el semestre debe ser un entero mayor que cero.")
            return False
        self.__semestre = semestre
        return True

    def cambiar_promedio_acumulado(self, promedio):
        if not isinstance(promedio, (int, float)) or not 0 <= promedio <= 5:
            print("Error: el promedio debe estar entre 0 y 5.")
            return False
        self.__promedio_acumulado = promedio
        return True

    def mostrar_informacion(self):
        return (
            f"{super().mostrar_informacion()}\n"
            f"Código estudiantil: {self.__codigo_estudiantil}\n"
            f"Programa: {self.__programa_academico.obtener_nombre()}\n"
            f"Semestre: {self.__semestre}\n"
            f"Promedio acumulado: {self.__promedio_acumulado}"
        )

    def realizar_actividad_principal(self):
        return (
            f"Cursa {self.__programa_academico.obtener_nombre()} "
            f"en el semestre {self.__semestre}."
        )


class Docente(Persona):
    """Persona que orienta clases en una facultad."""

    def __init__(self, identificacion, nombre, correo_electronico,
                 numero_empleado, facultad, tipo_contratacion,
                 horas_semanales):
        super().__init__(identificacion, nombre, correo_electronico)
        self.__numero_empleado = numero_empleado
        self.__facultad = facultad
        self.__tipo_contratacion = tipo_contratacion
        self.__horas_semanales = horas_semanales

    def obtener_numero_empleado(self):
        return self.__numero_empleado

    def obtener_facultad(self):
        return self.__facultad

    def obtener_tipo_contratacion(self):
        return self.__tipo_contratacion

    def obtener_horas_semanales(self):
        return self.__horas_semanales

    def cambiar_horas_semanales(self, horas):
        if not isinstance(horas, (int, float)) or horas <= 0:
            print("Error: las horas semanales deben ser mayores que cero.")
            return False
        self.__horas_semanales = horas
        return True

    def mostrar_informacion(self):
        return (
            f"{super().mostrar_informacion()}\n"
            f"Número de empleado: {self.__numero_empleado}\n"
            f"Facultad: {self.__facultad}\n"
            f"Tipo de contratación: {self.__tipo_contratacion}\n"
            f"Horas semanales: {self.__horas_semanales}"
        )

    def realizar_actividad_principal(self):
        return f"Orienta clases en la facultad de {self.__facultad}."


class Administrativo(Persona):
    """Persona que cumple funciones administrativas."""

    def __init__(self, identificacion, nombre, correo_electronico,
                 numero_empleado, dependencia, cargo, jornada):
        super().__init__(identificacion, nombre, correo_electronico)
        self.__numero_empleado = numero_empleado
        self.__dependencia = dependencia
        self.__cargo = cargo
        self.__jornada = jornada

    def obtener_numero_empleado(self):
        return self.__numero_empleado

    def obtener_dependencia(self):
        return self.__dependencia

    def obtener_cargo(self):
        return self.__cargo

    def obtener_jornada(self):
        return self.__jornada

    def mostrar_informacion(self):
        return (
            f"{super().mostrar_informacion()}\n"
            f"Número de empleado: {self.__numero_empleado}\n"
            f"Dependencia: {self.__dependencia}\n"
            f"Cargo: {self.__cargo}\n"
            f"Jornada: {self.__jornada}"
        )

    def realizar_actividad_principal(self):
        return f"Desempeña el cargo de {self.__cargo} en {self.__dependencia}."
