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
en la actividad. También se valida que el semestre del estudiante y las horas
semanales sean mayores que cero, y que el promedio esté entre 0 y 5. Estas
tres reglas adicionales se incluyen como validaciones razonables para los
datos académicos.

## Verificación manual

Al ejecutar `python main.py`, se presentan un programa académico, una
asignatura, seis personas (dos de cada tipo), sus actividades principales,
cambios válidos y mensajes para seis intentos inválidos. No se requieren
dependencias externas.

## Uso de inteligencia artificial

Se utilizó inteligencia artificial como apoyo para comprender los
requerimientos, proponer la estructura inicial y explicar decisiones de
diseño. Los integrantes deben revisar, comprender, adaptar y poder justificar
todo el código entregado, de acuerdo con la actividad.

## Repositorio y versión de entrega

Repositorio: [sistema-gestion-academica](https://github.com/ariasyeniffer4-prog/sistema-gestion-academica).

La versión marcada para la actividad está en la etiqueta `actividad-1-entrega`.
Las mejoras posteriores se encuentran en la rama `main`.
