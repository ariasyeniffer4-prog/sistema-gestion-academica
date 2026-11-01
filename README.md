# Sistema de Gestión Académica

## Integrante

- Yeniffer Fernanda Arias Ordoñez (trabajo individual)

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
- `Documento_Decisiones_Diseno.md`: justificación de las decisiones de diseño.

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

En Windows también puede ejecutarse con el lanzador de Python:

```powershell
py main.py
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

La autora ejecutó `py main.py` en Windows. La salida confirmó que `Persona` no
se puede instanciar directamente, se crean dos grupos y se demuestran la
matrícula válida, el duplicado, el límite de capacidad, ambos retiros y las dos
búsquedas fallidas. El programa continuó hasta mostrar las actividades
principales polimórficas. Esta verificación es una demostración manual en el
archivo principal; no se presenta como una suite automatizada. No se requieren
dependencias externas.

## Uso de inteligencia artificial

Se utilizó inteligencia artificial como apoyo para comprender los
requerimientos, proponer cambios, revisar errores y redactar explicaciones. La
autora debe revisar y poder justificar el código y las decisiones presentadas.

## Repositorio y versión de entrega

Repositorio: [sistema-gestion-academica](https://github.com/ariasyeniffer4-prog/sistema-gestion-academica).

La versión de la Actividad 1 permanece identificable en la etiqueta
[`actividad-1-entrega`](https://github.com/ariasyeniffer4-prog/sistema-gestion-academica/tree/actividad-1-entrega).
La entrega de la Actividad 2 está identificada por
[`Entrega_AC2`](https://github.com/ariasyeniffer4-prog/sistema-gestion-academica/tree/Entrega_AC2),
que identifica la versión corregida de la entrega. El proyecto fue desarrollado
individualmente por Yeniffer Fernanda Arias Ordoñez, y el historial de `main`
registra su contribución.
