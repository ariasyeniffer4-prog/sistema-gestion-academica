# Sistema de Gestión Académica

## Integrantes

- Yeniffer Fernanda Arias Ordoñez

## Descripción

Primera versión de un sistema académico en Python que representa programas,
asignaturas y personas vinculadas a la universidad. Estudiantes, docentes y
administrativos comparten la información de `Persona` y agregan sus datos y
actividades particulares.

## Archivos

- `main.py`: punto de entrada y demostración inicial.
- `src/modelos.py`: clases `Persona`, `ProgramaAcademico`, `Asignatura`,
  `Estudiante`, `Docente` y `Administrativo`.
- `src/__init__.py`: inicialización del paquete de modelos.

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

## Conceptos de programación orientada a objetos

`Persona` concentra los datos comunes. `Estudiante`, `Docente` y
`Administrativo` heredan de ella y sobreescriben `mostrar_informacion()` y
`realizar_actividad_principal()`. `main.py` recorre una sola lista heterogénea
con un único ciclo y llama a ambos métodos sin identificar previamente el tipo.
Los datos se encapsulan y se consultan mediante métodos. Las actualizaciones
del correo, número de semestres y créditos aplican las validaciones descritas
en la actividad. El programa principal muestra modificaciones válidas e
intentos de asignar valores inválidos.

## Verificación manual

Al ejecutar `python main.py`, se presentan un programa académico, una
asignatura, seis personas (dos de cada tipo), sus actividades principales y
mensajes para tres intentos inválidos. No se requieren dependencias externas.

## Uso de inteligencia artificial

Se utilizó inteligencia artificial como apoyo para comprender los
requerimientos, proponer la estructura inicial y explicar decisiones de
diseño. Los integrantes deben revisar, comprender, adaptar y poder justificar
todo el código entregado, de acuerdo con la actividad.

## Antes de entregar

- Completar los nombres reales de los integrantes.
- Confirmar con el docente las reglas adicionales usadas para promedio,
  semestre del estudiante y horas semanales, ya que la actividad no fija sus
  rangos.
- Subir el proyecto a GitHub y comprobar que cada integrante tenga al menos
  un commit sustantivo. Agregar el enlace real del repositorio al entregar.
