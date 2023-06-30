# Introducción

## ¿Conoces las diferencia entre **verificación** y **validación**?

![Diferencia entre verificación y validación](img/verificacion-validacion.jpg)

![Testing implica V&V](img/verificacion-validacion2.jpg)

## ¿Cuál es la **diferencia** entre **Calidad** y **Testing**?

* QA: Quality Assurance (aseguramiento de la calidad de software). Término del campo del área.
* Testing de software:
  * Es una técnica de Verificación y Validación.
  * Identificar diferencias entre el comportamiento real y esperado.
  * No garantiza la ausencia de errores, sólo puede detectar su presencia.

![Diferencia entre Calidad y Testing](img/diferencia-calidad-testing.jpg)

## ¿Cuáles son los tipos de testing?

* **Estático**: proceso de evaluar el objeto de prueba sin ejecutarlo. Ejemplo: revisiones o análisis estático de código.
* **Dinámico**: proceso de evaluar el objeto de prueba ejecutándolo. Ejemplo: pruebas unitarias sobre un componente.

## ¿Qué son los **atributos** de calidad?

![Atributos de Calidad](img/atributos-calidad.jpg)

![Atributos de Calidad](img/atributos-calidad2.JPG)

## ¿Sabes medir el **retorno de inversión** de **QA** en un proyecto?

![Retorno de Inversión](img/retorno-inversion.jpg)

## ¿Qué **tareas** se hacen en **QA** y cuales en **Testing**?

![Tareas en QA y en Testing](img/tareas-qa-testing.jpg)

## ¿Qué **beneficios** nos aporta un proceso de **calidad de software**?

![Beneficios que aporta un proceso de calidad de software](img/beneficios-calidad-software.jpg)

## ¿Qué aportan las **pruebas** en un producto de software?

![Aportes de las pruebas en un producto de software](img/aporte-pruebas.jpg)

## ¿Conoces las **verdades absolutas** (principios) del Testing?

![Verdades absolutas del Testing](img/verdades-absolutas.jpg)

![Siete principios de las pruebas](img/principios.jpg)

## ¿Qué dice la **paradoja del pesticida** sobre nuestras pruebas?

![Paradoja del pesticida](img/paradoja-pesticida.jpg)

## ¿Conoces estas **curiosidades del Testing**?

![Curiosidades del Testing](img/curiosidades.jpg)

## ¿Conoces la **historia del Testing**?

![Historia del Testing](img/historia.jpg)

## ¿Qué significa ISTQB?

* International Software Testing Qualifications Board
* Comité Internacional de Calificación en Pruebas de Software
* Es una organización de certificación de la calidad de software que opera y es reconocido internacionalmente por:
  * su visión constante de mantener una base de conocimientos.
  * fomentar la comunidad de pruebas de software internacional.
  * promover la investigación en el área.

## ¿Cuál es el ciclo de vida del desarrollo de software (Software Development Life Cicle - SDLC)?

1. Project Initiation / Ideation: se reunen las personas. Se planifica todo.
2. Requirements Definition: planificación de requerimientos. Features.
3. Design
4. Development / Construct
5. Testing
6. Deployment / Product Release
7. Maintenance / Post Implementation

## ¿Cuál es el ciclo de vida de pruebas de software (Software Testing Life Cicle - STLC)?

1. **Requirement Analysys (Análisis de requerimientos)**:
    * El equipo de prueba estudia los requisitos desde un punto de vista prueba para identificar requisitos comprobables (ciertos requisitos producen resultados alimentandose de datos de entrada)
    * El equipo de control de calidad puede interactuar con varias partes interesadas para comprender los requisitos en detalle.
    * Los requisitos pueden ser funcionales o no funcionales.
    * La viabilidad de la automatización para el proyecto de prueba tambien se realiza en esta etapa.
2. **Test Planning (Planificación de pruebas)**:
    * Es un documento o guía para gestionar la prueba. Insumo: Product Backlog.
    * Lo prepara el lider de pruebas.
    * Se determina la estrategia del plan de pruebas junto con los esfuerzos y las estimaciones de costos para el proyecto.
    * Se determinan los recursos, el entorno de prueba, las limitaciones (alcance) de las pruebas, tipos de prueba y el programa de pruebas.
3. **Test Design (Diseño y desarrollo de casos de prueba)**:
    * Implica la creación, verificación y reelaboración de casos de prueba y scripts de prueba una vez que el plan de prueba está listo. También se los prioriza (más comunes, cuales afectaria mas al producto)
    * Inicialmente, los datos de prueba se identifican, luego se crean y revisan y luego se vuelven a trabajar en función de las condiciones previas.
    * Luego, el equipo de control de calidad comienza el proceso de desarrollo de casos de prueba para unidades individuales.
4. **Environment Setup (Configuración del entorno de prueba)**:
    * Decide las condiciones de software y hardware en las que se prueba un producto de trabajo.
    * Se puede realizar en paralelo con la fase de desarrollo del caso de prueba.
    * Se requiere que el equipo de prueba realice una verificacion de preparación (prueba de humo) del entorno dado.
5. **Test Execution (Ejecución de pruebas)**:
    * La llevan a cabo los evaluadores/probadores.
    * El proceso consiste en la ejecución del script de prueba, el mantenimiento del script de prueba y la notificación de defectos.
    * Si se informan errores (comparar los resultados esperados con el resultado real), se devuelve al equipo de desarrollo para su corrección y se realizará una nueva prueba. Seguimiento de los defectos hasta el cierre.
6. **Test Closure (Cierre del ciclo de prueba)**:
    * Es la finalización de la ejecución de la prueba, que involucra varias actividades como informes de finalización de la prueba y resultados de la prueba.
    * Los miembros del equipo se reunen, discuten y analizan los artefactos de prueba para identificar estrategias que deben implementarse en el futuro.
    * Se analizan desviaciones de los valores estimados.
    * Se consideran las métricas de prueba, el cumplimiento de los objetivos y plazos.
