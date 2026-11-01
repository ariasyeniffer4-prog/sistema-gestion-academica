"""Modelos iniciales del Sistema de Gestión Académica."""

from abc import ABC, abstractmethod


class EstudianteYaMatriculadoError(Exception):
    """Se intenta inscribir en el mismo grupo a un estudiante matriculado."""


class CapacidadGrupoCompletaError(Exception):
    """El grupo no tiene cupos disponibles."""


class EstudianteNoMatriculadoError(Exception):
    """Se intenta retirar a un estudiante que no pertenece al grupo."""


class AsignaturaNoEncontradaError(Exception):
    """No existe la asignatura solicitada."""


class ProgramaNoEncontradoError(Exception):
    """No existe el programa académico solicitado."""


class Persona(ABC):
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

    @abstractmethod
    def realizar_actividad_principal(self):
        """Describe la actividad propia de cada tipo de persona."""
        raise NotImplementedError


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


class Horario:
    """Horario de reunión de un grupo académico."""

    def __init__(self, dia, hora_inicio, hora_finalizacion, salon):
        self.__dia = dia
        self.__hora_inicio = hora_inicio
        self.__hora_finalizacion = hora_finalizacion
        self.__salon = salon

    def mostrar_informacion(self):
        return (
            f"{self.__dia}, {self.__hora_inicio} a {self.__hora_finalizacion}"
            f" - Salón {self.__salon}"
        )


class GrupoAcademico:
    """Oferta de una asignatura con docente, estudiantes y horario propio."""

    def __init__(self, codigo, asignatura, docente, capacidad_maxima,
                 dia, hora_inicio, hora_finalizacion, salon):
        if capacidad_maxima <= 0:
            raise ValueError("La capacidad máxima debe ser mayor que cero.")
        self.__codigo = codigo
        self.__asignatura = asignatura
        self.__docente = docente
        self.__capacidad_maxima = capacidad_maxima
        self.__estudiantes = []
        # El grupo crea y administra su horario como parte de su propia oferta.
        self.__horario = Horario(dia, hora_inicio, hora_finalizacion, salon)

    def mostrar_informacion_grupo(self):
        return (
            f"Grupo: {self.__codigo}\n"
            f"{self.__asignatura.mostrar_informacion()}\n"
            f"Docente: {self.__docente.obtener_nombre()}\n"
            f"Cupo: {len(self.__estudiantes)}/{self.__capacidad_maxima}\n"
            f"Horario: {self.__horario.mostrar_informacion()}"
        )

    def matricular_estudiante(self, estudiante):
        codigo = estudiante.obtener_codigo_estudiantil()
        if any(e.obtener_codigo_estudiantil() == codigo for e in self.__estudiantes):
            raise EstudianteYaMatriculadoError(
                f"El estudiante {codigo} ya está matriculado en el grupo {self.__codigo}."
            )
        if len(self.__estudiantes) >= self.__capacidad_maxima:
            raise CapacidadGrupoCompletaError(
                f"El grupo {self.__codigo} alcanzó su capacidad máxima."
            )
        self.__estudiantes.append(estudiante)

    def retirar_estudiante(self, codigo_estudiantil):
        for estudiante in self.__estudiantes:
            if estudiante.obtener_codigo_estudiantil() == codigo_estudiantil:
                self.__estudiantes.remove(estudiante)
                return
        raise EstudianteNoMatriculadoError(
            f"El estudiante {codigo_estudiantil} no está matriculado en el grupo {self.__codigo}."
        )

    def mostrar_estudiantes(self):
        if not self.__estudiantes:
            return "No hay estudiantes matriculados."
        return "\n".join(
            f"{e.obtener_codigo_estudiantil()} - {e.obtener_nombre()}"
            for e in self.__estudiantes
        )


def buscar_asignatura(asignaturas, codigo):
    """Devuelve una asignatura por código o lanza una excepción de dominio."""
    for asignatura in asignaturas:
        if asignatura.obtener_codigo() == codigo:
            return asignatura
    raise AsignaturaNoEncontradaError(
        f"No existe una asignatura con código {codigo}."
    )


def buscar_programa(programas, codigo):
    """Devuelve un programa por código o lanza una excepción de dominio."""
    for programa in programas:
        if programa.obtener_codigo() == codigo:
            return programa
    raise ProgramaNoEncontradoError(
        f"No existe un programa académico con código {codigo}."
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
