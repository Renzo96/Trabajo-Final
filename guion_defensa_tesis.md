# Guion — Defensa de Tesis en Video (10 min)
**Título:** Implementación de IA Agéntica para la Creación de Rúbricas — Un caso de estudio aplicado a la materia Organización Empresarial
**Integrantes:** Renzo Sosa · Emmanuel Avellaneda
**Director/Profesor:** Alberto Cortez

*Nota: los tiempos son orientativos. Practiquen leyéndolo en voz alta al menos
una vez para ajustar el ritmo real antes de grabar.*

---

## [0:00–0:45] Apertura e identificación
**RENZO:**
"Buenos días. Somos Renzo Sosa y Emmanuel Avellaneda, y presentamos nuestro
trabajo final de tesis titulado *'Implementación de IA Agéntica para la
Creación de Rúbricas: un caso de estudio aplicado a la materia Organización
Empresarial'*, desarrollado bajo la dirección del profesor Alberto Cortez."

**EMMANUEL:**
"En los próximos diez minutos vamos a recorrer el problema que motivó esta
investigación, los objetivos, el marco teórico, la metodología aplicada, los
resultados obtenidos y las conclusiones."

---

## [0:45–2:00] Problema y motivación
**RENZO:**
"Hoy es común usar inteligencia artificial para corregir entregas de
alumnos, pero la calidad de esa corrección automática depende de un elemento
que casi nunca se discute con el mismo rigor: la rúbrica. Una rúbrica mal
diseñada para ser leída por una IA genera notas inconsistentes, criterios
ambiguos, o directamente entregas que el corrector no puede evaluar porque
piden algo que la IA no puede procesar, como una captura de pantalla o un
link externo."

**EMMANUEL:**
"Esto afecta directamente a docentes que necesitan escalar la corrección en
cursadas numerosas, y a los alumnos, que reciben feedback poco confiable si
la rúbrica no fue pensada para ese corrector específico. Detectamos que no
existe una metodología documentada para construir rúbricas compatibles con
las limitaciones reales de un corrector por IA. Y para eso es esta tesis:
para dejar un método probado, replicable y con evidencia empírica de que
funciona."

---

## [2:00–3:00] Pregunta de investigación y objetivos
**RENZO:**
"La pregunta que guía este trabajo es: ¿cómo se construye una rúbrica de
evaluación que un agente de inteligencia artificial pueda aplicar de forma
consistente, confiable y verificable, respetando las limitaciones técnicas
reales del corrector?"

**EMMANUEL:**
"El objetivo general fue documentar y validar empíricamente un flujo de
trabajo para crear ese tipo de rúbricas usando una IA agéntica. Como
objetivos específicos: primero, identificar los límites técnicos concretos
de un corrector automático y traducirlos en criterios de normalización de la
consigna y de la entrega. Segundo, aplicar ese flujo —creación, auditoría,
validación y testeo— sobre un caso real: los siete trabajos prácticos de la
materia Organización Empresarial. Y tercero, testear cada rúbrica con
entregas sintéticas diseñadas a propósito para fallar, y verificar que la
nota resultante discrimine correctamente."

---

## [3:00–4:30] Marco teórico / antecedentes
**RENZO:**
"Nos apoyamos en tres conceptos centrales. Primero, la definición de rúbrica
de evaluación como conjunto de criterios ponderados, con subcriterios y
evidencias verificables, donde el puntaje siempre vive en el criterio y no
en el subcriterio. Segundo, el concepto de IA agéntica: un modelo capaz de
usar herramientas y ejecutar un flujo de trabajo de varios pasos, no solo
responder una pregunta aislada. En nuestro caso, Claude Code de Anthropic."

**EMMANUEL:**
"Tercero, el concepto de 'skill': un paquete de instrucciones y scripts que
le da a la IA agéntica un procedimiento reproducible para una tarea
específica. Usamos como caso de estudio la skill *rubrica-builder*,
desarrollada por Juan Cruz Robledo bajo licencia Apache 2.0, a quien
reconocemos toda la autoría de su diseño; nuestro aporte es documentar y
validar su aplicación real sobre un caso de uso universitario. También
consultamos la documentación oficial de GitHub sobre la estructura interna
de un repositorio Git, que fue clave para una de las decisiones
metodológicas que vamos a mostrar en los resultados."

---

## [4:30–6:30] Metodología
**RENZO:**
"El enfoque es un estudio de caso aplicado, de carácter cualitativo, con
componentes de validación cuantitativa. La 'muestra' fueron los siete
trabajos prácticos reales de la cursada de Organización Empresarial: Git,
Ingeniería de Prompts, Metodologías Ágiles, Ecosistema Startup, Live Coding,
Automatización con n8n, y el Trabajo Integrador."

**EMMANUEL:**
"El procedimiento tiene cinco etapas. Primero, normalización: antes de
escribir un solo criterio, analizamos cada consigna contra los límites reales
del corrector —no navega links externos, filtra imágenes según el modo de
corrección, es un flujo único de código o PDF, y no ejecuta nada— y
decidimos qué tecnología y qué formato de entrega iban a usar todos los
alumnos por igual."

**RENZO:**
"Segundo, creación de la rúbrica con la IA agéntica. Tercero, auditoría:
buscar contradicciones, omisiones o criterios diluidos. Cuarto, validación
estructural, verificando que los pesos sumen cien puntos y que el esquema
sea válido. Y quinto, testeo: generamos entregas sintéticas —una perfecta y
varias diseñadas para fallar en un único criterio a la vez— y comparamos la
nota obtenida contra la esperada, como si fuera un test unitario aplicado a
la rúbrica."

---

## [6:30–8:00] Resultados
**EMMANUEL:**
"Sobre las siete rúbricas, confirmamos que los pesos de los criterios suman
exactamente cien puntos en todos los casos, sin excepción. Pero el resultado
más ilustrativo es un caso concreto: el trabajo práctico sobre control de
versiones con Git."

**RENZO:**
"Ahí decidimos que, en lugar de pedir capturas de pantalla de la terminal
—que la IA no puede auditar de forma confiable—, la entrega debía incluir la
carpeta oculta `.git`, que contiene el historial real de commits y ramas
generado por el propio sistema. Es evidencia que no depende de lo que el
alumno afirme haber hecho."

**EMMANUEL:**
"Al testear esa rúbrica con una entrega sintética perfecta, obtuvimos 100 de
100. Con una entrega que omitía una sola pregunta teórica, la nota bajó a 90,
un descuento aislado y correcto. Pero con una entrega que no incluía la
carpeta `.git`, la nota cayó a 30, porque se activa una condición de
desaprobación que impone ese techo cuando falta la evidencia práctica
central. Ese mismo patrón se repitió, de forma consistente, en la rúbrica de
n8n cuando faltaba el archivo del flujo exportado."

---

## [8:00–9:00] Discusión y conclusiones
**RENZO:**
"Estos resultados responden directamente nuestra pregunta de investigación:
la rúbrica discrimina correctamente cuando fue diseñada respetando las
limitaciones del corrector desde el principio, y no como un ajuste
posterior. La contribución original de esta tesis es justamente ese
orden: normalizar la consigna y la tecnología antes de escribir un
criterio, no después."

**EMMANUEL:**
"Esto dialoga con lo que planteamos en el marco teórico: no alcanza con
tener un buen modelo de IA corrigiendo; si la rúbrica no fue pensada para
las limitaciones reales de ese corrector, el resultado va a ser
inconsistente sin importar qué tan avanzado sea el modelo. Nuestro trabajo
amplía esa idea con evidencia empírica concreta, caso por caso, sobre una
cursada real."

---

## [9:00–10:00] Limitaciones, trabajo futuro y cierre
**RENZO:**
"Como limitación principal, el testeo lo corrimos con el CLI de Claude en
un entorno local, y no con el flujo real de producción, que usa n8n y
Gemini. Es un dato a tener en cuenta: un modelo distinto podría comportarse
de forma distinta ante la misma rúbrica. Tampoco comparamos todavía la nota
de la IA contra la corrección de un docente humano sobre una entrega real."

**EMMANUEL:**
"Como líneas de trabajo futuro, proponemos correr este mismo testeo contra
el corrector de producción, y comparar el acuerdo entre la IA y un docente
humano sobre casos reales, para medir con más precisión la confiabilidad
del método."

**RENZO:**
"Para cerrar: esta tesis deja un método documentado y con evidencia
empírica de que es posible construir rúbricas confiables para corrección
por IA, siempre que la normalización sea el primer paso y no el último."

**EMMANUEL:**
"Muchas gracias al profesor Alberto Cortez por la dirección de este
trabajo, y al tribunal por su tiempo y atención."
