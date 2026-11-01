# Documento de Decisiones de Diseño

## Evolución del Sistema de Gestión Académica

**Universidad de Manizales**  
**Facultad de Ciencias e Ingenierías**  
**Actividad Colaborativa N.º 2**  
**Integrante registrado en el README:** Yeniffer Fernanda Arias Ordoñez  
**Proyecto:** sistema de gestión académica en Python

## Introducción

Este documento describe las decisiones aplicadas al sistema de gestión
académica que se inició en la Actividad Colaborativa 1. La evolución conserva
las entidades y el comportamiento polimórfico existentes, y amplía el modelo
para representar grupos, horarios y matrícula. También formaliza el uso de
`Persona` como clase abstracta y controla situaciones excepcionales con tipos
de error propios.

## Descripción general de la solución

El punto de entrada continúa siendo `main.py`, mientras que `src/modelos.py`
contiene las clases del dominio. `ProgramaAcademico` y `Asignatura` conservan
su relación previa. `Persona` reúne los datos compartidos; `Estudiante`,
`Docente` y `Administrativo` agregan sus atributos y comportamientos
especializados. La nueva clase `GrupoAcademico` organiza una asignatura
ofrecida por un docente, mantiene la lista de estudiantes matriculados y
contiene un horario propio.

## Desarrollo

### Generalización de personas y polimorfismo

Una instancia genérica de `Persona` no tendría una actividad principal que
describa una responsabilidad concreta. Por eso `Persona` hereda de `ABC` y
declara `realizar_actividad_principal()` con `@abstractmethod`. Python impide
crear directamente esa clase mientras el método abstracto no esté
implementado.

Las clases derivadas implementan el método según su papel: `Estudiante`
describe el programa y semestre que cursa; `Docente` informa la facultad en la
que orienta clases; y `Administrativo` describe su cargo y dependencia. En
`main.py`, la lista heterogénea `personas` se recorre invocando
`mostrar_informacion()` y `realizar_actividad_principal()` sin consultar el
tipo concreto. El despacho de cada implementación conserva el polimorfismo de
la Actividad 1.

### Oferta académica y composición del horario

`GrupoAcademico` recibe referencias a objetos ya construidos de `Asignatura` y
`Docente`, además del código y la capacidad máxima. La lista interna de
estudiantes guarda objetos `Estudiante`, lo que permite presentar sus códigos
y nombres y comprobar matrículas repetidas. Sus métodos
`mostrar_informacion_grupo()`, `matricular_estudiante(estudiante)`,
`retirar_estudiante(codigo_estudiantil)` y `mostrar_estudiantes()` expresan las
operaciones principales de la oferta.

El constructor de `GrupoAcademico` crea un objeto `Horario` con el día, la hora
de inicio, la hora de finalización y el salón. Así, el grupo contiene un
horario como parte de su estado y lo presenta desde
`mostrar_informacion_grupo()`. La relación es composición porque el horario
forma parte de la organización del grupo y el grupo lo crea y administra. No
es herencia: un horario no es una clase especializada de grupo y no comparte
la identidad ni el comportamiento de una oferta académica.

### Excepciones y búsquedas

Cada situación excepcional tiene una clase propia declarada en
`src/modelos.py`. `GrupoAcademico.matricular_estudiante()` lanza
`EstudianteYaMatriculadoError` si el código estudiantil ya está en la lista y
`CapacidadGrupoCompletaError` si no quedan cupos. El método
`retirar_estudiante()` lanza `EstudianteNoMatriculadoError` cuando no encuentra
el código solicitado.

Las funciones `buscar_asignatura()` y `buscar_programa()` recorren las
colecciones recibidas y devuelven el objeto coincidente. Si no hay coincidencia,
lanzan `AsignaturaNoEncontradaError` o `ProgramaNoEncontradoError`,
respectivamente. `main.py` captura cada error en el lugar donde demuestra el
caso, comunica el motivo y continúa con las demostraciones siguientes.

### Demostración en el programa principal

`main.py` intenta instanciar `Persona` y captura el `TypeError` esperado. Crea
programa, asignatura, docentes y estudiantes, y luego crea dos grupos con
horarios distintos. Demuestra una matrícula válida, una matrícula duplicada,
el límite de capacidad, un retiro válido, un retiro inválido y las dos
búsquedas fallidas. Al final informa que la ejecución continuó y muestra la
lista actual de estudiantes del primer grupo.

## Conclusiones

La evolución mantiene las clases principales de la Actividad 1 y extiende el
mismo punto de entrada y módulo de modelos. La abstracción expresa que toda
persona concreta debe definir su actividad principal; el polimorfismo permite
recorrer distintos tipos de persona con las mismas llamadas. `GrupoAcademico`
coordina los objetos que participan en una oferta y crea su `Horario` como
parte de ella. Las excepciones separan los errores de dominio de los mensajes
presentados por el programa principal.

Antes de entregar, los integrantes deben revisar el código y poder explicar
estas decisiones y su ejecución. El README registra únicamente a Yeniffer
Fernanda Arias Ordoñez; si participaron más integrantes, deben agregarse sus
nombres confirmados y cada integrante debe realizar su propio commit. Este
documento no afirma participación ni comprensión individual que no haya sido
confirmada.

## Declaración de uso de inteligencia artificial

Se utilizó inteligencia artificial como apoyo para comprender los
requerimientos, proponer cambios de código, revisar errores y redactar partes
de esta explicación. La herramienta no sustituye la revisión del equipo; los
integrantes deben comprender y justificar el código que presenten.
