"""Pruebas automatizadas del modelo académico de la Actividad 2."""

import unittest

from src.modelos import (
    Administrativo,
    Asignatura,
    AsignaturaNoEncontradaError,
    CapacidadGrupoCompletaError,
    Docente,
    Estudiante,
    EstudianteNoMatriculadoError,
    EstudianteYaMatriculadoError,
    GrupoAcademico,
    Persona,
    ProgramaAcademico,
    ProgramaNoEncontradoError,
    buscar_asignatura,
    buscar_programa,
)


class SistemaAcademicoTests(unittest.TestCase):
    def setUp(self):
        self.programa = ProgramaAcademico("P1", "Ingeniería", "Facultad", 8)
        self.asignatura = Asignatura("A1", "Programación", 3, self.programa)
        self.docente = Docente(
            "D1", "Marta", "marta@example.edu", "E1", "Facultad",
            "Tiempo completo", 40
        )
        self.estudiante = Estudiante(
            "ID1", "Ana", "ana@example.edu", "S1", self.programa, 2, 4.5
        )
        self.otro_estudiante = Estudiante(
            "ID2", "Luis", "luis@example.edu", "S2", self.programa, 3, 4.0
        )
        self.grupo = GrupoAcademico(
            "G1", self.asignatura, self.docente, 1,
            "Lunes", "08:00", "10:00", "B-201"
        )

    def test_persona_es_abstracta_y_subclases_sobrescriben_actividad(self):
        with self.assertRaises(TypeError):
            Persona("ID", "Persona", "persona@example.edu")

        administrativo = Administrativo(
            "ID3", "Sofía", "sofia@example.edu", "E2",
            "Registro", "Coordinadora", "Diurna"
        )
        self.assertIn("Cursa", self.estudiante.realizar_actividad_principal())
        self.assertIn("Orienta clases", self.docente.realizar_actividad_principal())
        self.assertIn(
            "Desempeña el cargo", administrativo.realizar_actividad_principal()
        )

    def test_grupo_muestra_asignatura_docente_y_horario(self):
        informacion = self.grupo.mostrar_informacion_grupo()
        self.assertIn("Programación", informacion)
        self.assertIn("Marta", informacion)
        self.assertIn("Lunes, 08:00 a 10:00", informacion)
        self.assertIn("B-201", informacion)

    def test_matricula_valida_y_rechaza_duplicado_y_sobrecupo(self):
        self.grupo.matricular_estudiante(self.estudiante)
        self.assertIn("S1 - Ana", self.grupo.mostrar_estudiantes())
        with self.assertRaises(EstudianteYaMatriculadoError):
            self.grupo.matricular_estudiante(self.estudiante)
        with self.assertRaises(CapacidadGrupoCompletaError):
            self.grupo.matricular_estudiante(self.otro_estudiante)
        self.assertEqual("S1 - Ana", self.grupo.mostrar_estudiantes())

    def test_retiro_valido_y_rechazo_de_estudiante_ausente(self):
        self.grupo.matricular_estudiante(self.estudiante)
        self.grupo.retirar_estudiante("S1")
        self.assertEqual("No hay estudiantes matriculados.", self.grupo.mostrar_estudiantes())
        with self.assertRaises(EstudianteNoMatriculadoError):
            self.grupo.retirar_estudiante("S-NO-EXISTE")
        self.assertEqual("No hay estudiantes matriculados.", self.grupo.mostrar_estudiantes())

    def test_busquedas_devuelven_objetos_y_lanzan_error_si_no_existen(self):
        self.assertIs(self.asignatura, buscar_asignatura([self.asignatura], "A1"))
        self.assertIs(self.programa, buscar_programa([self.programa], "P1"))
        with self.assertRaises(AsignaturaNoEncontradaError):
            buscar_asignatura([self.asignatura], "NO-EXISTE")
        with self.assertRaises(ProgramaNoEncontradoError):
            buscar_programa([self.programa], "NO-EXISTE")


if __name__ == "__main__":
    unittest.main()
