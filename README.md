# Sistema de Gestión Académica

## Integrantes

- Yeniffer Fernanda Arias Ordoñez

## Descripción

Evolución del sistema académico de la Actividad Colaborativa 1. Representa
programas, asignaturas y personas vinculadas a la universidad, y agrega grupos
académicos con matrícula y horario propio.

## Archivos

- `main.py`: punto de entrada y demostración inicial.
- `src/modelos.py`: clases `Persona`, `ProgramaAcademico`, `Asignatura`,
  `Estudiante`, `Docente`, `Administrativo`, `Horario` y `GrupoAcademico`, además
  de las excepciones y funciones de búsqueda.
- `src/__init__.py`: inicialización del paquete de modelos.

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

## Conceptos de programación orientada a objetos

`Persona` concentra los datos comunes y es abstracta. `Estudiante`, `Docente` y
`Administrativo` heredan de ella e implementan `realizar_actividad_principal()`
según su responsabilidad. `main.py` recorre una lista heterogénea y llama a
los mismos métodos sin identificar previamente el tipo, conservando el
polimorfismo de la Actividad 1.

`GrupoAcademico` recibe objetos `Asignatura` y `Docente`, mantiene a los
estudiantes matriculados y construye un `Horario` propio con día, hora de
inicio, hora de finalización y salón. Esta es composición: el grupo contiene y
administra el horario que forma parte de la oferta del grupo. `Horario` no es
una clase base de `GrupoAcademico`; ambos representan conceptos distintos y el
grupo usa el horario como parte de su estado.

Las excepciones de matrícula y búsqueda se definen como clases propias en
`src/modelos.py`, se lanzan al detectar la situación y se capturan en `main.py`
con mensajes para que la demostración continúe.

## Verificación manual

Al ejecutar `python main.py`, se presentan los objetos académicos y las
personas, dos grupos, una matrícula válida y los casos excepcionales requeridos
por la actividad. No se requieren dependencias externas.

## Uso de inteligencia artificial

Se utilizó inteligencia artificial como apoyo para comprender los
requerimientos, proponer cambios, revisar errores y redactar explicaciones.
El equipo debe revisar y poder justificar el código y las decisiones antes de
la entrega.

## Repositorio y versión de entrega

Repositorio: [sistema-gestion-academica](https://github.com/ariasyeniffer4-prog/sistema-gestion-academica).

La versión de la Actividad 1 permanece identificable en la etiqueta
`actividad-1-entrega`. La etiqueta requerida `Entrega_AC2` y los commits de
participación de todos los integrantes deben registrarse para la entrega final;
no se han creado en esta actualización local.
