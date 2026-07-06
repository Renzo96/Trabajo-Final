# Informe de Correcciones — TP3: Fundamentos de Metodologías Ágiles

**Materia:** Organización Empresarial | **Carrera:** Tecnicatura Universitaria en Programación | **UTN - Facultad Regional Mendoza**
**Rúbrica aplicada:** `rubrica-tp3-metodologias-agiles.json` | **Puntaje máximo:** 100 puntos

Las entregas evaluadas son textos de respuestas teóricas sobre metodologías ágiles (Waterfall vs. Ágil, roles de Scrum, Kanban/WIP Limit, Pair Programming, Historias de Usuario). No contienen nombres de alumnos ni metadatos de identidad embebidos en el contenido — a diferencia del TP1, aquí cada entrega se referencia únicamente por su identificador de archivo.

---

## Resumen General

| Entrega | Testea | Nota Final | Estado |
|---|---|---|---|
| `s0_perfecta.txt` | Rúbrica completa (caso ideal) | **100 / 100** | ✅ Aprobado |
| `s1_falla_c1.txt` | C1 discrimina (Waterfall vs ágil) | **90 / 100** | ✅ Aprobado |
| `s2_falla_c2.txt` | C2 discrimina (Roles de Scrum) | **80 / 100** | ✅ Aprobado |
| `s3_falla_c3.txt` | C3 discrimina (Kanban y WIP Limit) | **85 / 100** | ✅ Aprobado |
| `s4_falla_c4.txt` | C4 discrimina (Pair Programming) | **80 / 100** | ✅ Aprobado |
| `s5_falla_c5.txt` | C5 discrimina (Historias de Usuario) | **80 / 100** | ✅ Aprobado |
| `s6_parcial_c1.txt` | C1 parcial | **— (sin corrección disponible)** | ⚠️ Sin datos |
| `s7_parcial_c2.txt` | C2 parcial | **100 / 100** | ⚠️ Aprobado (ver hallazgo) |

En ninguna de las 7 entregas corregidas se activó la condición de desaprobación `CD1` (imágenes en el PDF) ni penalizaciones adicionales: en todos los `_correccion.json` disponibles, `condicion_desaprobacion_aplicada` es `null` y `penalizaciones_aplicadas` es `[]`. Los descuentos observados provienen exclusivamente del puntaje propio de cada criterio.

---

---

## Entrega: `s0_perfecta.txt`

### Nota Final: 100 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Waterfall vs mentalidad ágil | 20 | 20 | ✅ Completo |
| C2 | Roles de Scrum | 20 | 20 | ✅ Completo |
| C3 | Kanban y WIP Limit | 20 | 20 | ✅ Completo |
| C4 | Pair Programming | 20 | 20 | ✅ Completo |
| C5 | Historias de Usuario y Criterios de Aceptación | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Waterfall vs mentalidad ágil (20/20)**
La corrección destaca que la respuesta explica de forma completa y articulada ambas partes: por qué el cambio de requisitos en Cascada es un desastre (fases secuenciales, efecto dominó de retrabajo, costo altísimo, plan rígido firmado) y cómo la mentalidad ágil lo resuelve (iteraciones cortas, entregas incrementales, feedback frecuente, adaptación barata), con conexión lógica clara y vocabulario propio.

**C2 — Roles de Scrum (20/20)**
Ambos roles identificados correctamente: Product Owner para la priorización por valor de negocio (gestiona el Product Backlog) y Scrum Master para proteger al equipo de interferencias externas (facilitador/escudo). Sin confusión de responsabilidades.

**C3 — Kanban y WIP Limit (20/20)**
Identifica con claridad la multitarea/cambio de contexto como desperdicio Lean y explica cómo el WIP Limit obliga a terminar antes de empezar, reduciendo la fricción del cambio de contexto y mejorando el throughput. Conexión problema-solución bien desarrollada.

**C4 — Pair Programming (20/20)**
Defiende la práctica con dos beneficios sólidos y diferenciados: revisión de código en tiempo real (menos defectos) y transferencia de conocimiento (reduce bus factor, aprendizaje mutuo), ambos argumentados y conectados al código final y al equipo.

**C5 — Historias de Usuario y Criterios de Aceptación (20/20)**
La Historia de Usuario sigue la fórmula estándar completa (rol, acción, beneficio) coherente con el contexto Netflix/Mi Lista. Presenta tres criterios de aceptación en formato Given/When/Then, superando el mínimo de dos, todos verificables y pertinentes.

### Observación General
Según el `comentario_general` de la corrección: *"Trabajo excepcional. Todas las respuestas demuestran comprensión profunda de los conceptos, van más allá de definiciones memorizadas y conectan teoría con práctica de forma coherente y con vocabulario propio. La entrega cumple con creces cada criterio de evaluación sin observaciones negativas."* Las recomendaciones registradas son todas de profundización opcional (mencionar artefactos/eventos adicionales de Scrum, los 7 desperdicios Lean, las 3 C's de Historias de Usuario, la curva de Boehm), no correcciones de errores.

---

---

## Entrega: `s1_falla_c1.txt`

### Nota Final: 90 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Waterfall vs mentalidad ágil | 20 | **10** | ⚠️ Parcial |
| C2 | Roles de Scrum | 20 | 20 | ✅ Completo |
| C3 | Kanban y WIP Limit | 20 | 20 | ✅ Completo |
| C4 | Pair Programming | 20 | 20 | ✅ Completo |
| C5 | Historias de Usuario y Criterios de Aceptación | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Waterfall vs mentalidad ágil (10/20)** ⚠️
La respuesta aborda ambas partes (problema de Waterfall y solución ágil) con palabras propias, pero es "demasiado genérica y carece de los conceptos ágiles concretos que la rúbrica esperaba". Sobre Waterfall, no explicita la secuencialidad de fases ni el costo de retrabajo de cambios tardíos. Sobre la solución ágil, no menciona iteraciones cortas, entregas incrementales ni feedback frecuente del cliente. La conexión problema-solución queda a nivel de idea general, no de mecanismo concreto — de ahí el descuento a la mitad del puntaje.

**C2 — Roles de Scrum (20/20)**
Respuesta calificada como "impecable": identifica correctamente al Product Owner (gestiona el Product Backlog, prioriza por valor de negocio) y al Scrum Master (protege al equipo, frena interrupciones a mitad de sprint), con justificación precisa en ambos casos.

**C3 — Kanban y WIP Limit (20/20)**
Identifica claramente la multitarea/cambio de contexto como desperdicio Lean e ilustra con "mucho empezado, nada terminado". Explica con precisión el WIP Limit y la paradoja de que hacer menos en paralelo aumenta la velocidad real de entrega.

**C4 — Pair Programming (20/20)**
Defensa sólida con dos beneficios distintos: revisión de código en tiempo real (bugs detectados cuando arreglarlos es barato) y transferencia de conocimiento (evita el bus factor). Ambos bien vinculados al código final y al equipo.

**C5 — Historias de Usuario y Criterios de Aceptación (20/20)**
Historia de Usuario con los tres componentes de la fórmula, coherente con el contexto. Tres Criterios de Aceptación en formato Given-When-Then, verificables, superando el mínimo de dos.

### Observación General
El `comentario_general` resume: *"El trabajo demuestra una comprensión sólida y madura de los fundamentos ágiles en cuatro de los cinco criterios [...] La única debilidad está en C1, donde la respuesta es conceptualmente acertada pero carece del vocabulario técnico específico y los mecanismos concretos que la rúbrica pedía como evidencia."* La rúbrica concentró correctamente el descuento en C1 (criterio que el nombre del archivo anticipa), aunque el descuento fue parcial (10/20, estado `WARNING`) y no total: la instrucción de puntuación de C1 solo contempla explícitamente los niveles "completo", "una de las dos partes" (techo 10/20), "copiado" (techo 5/20) o "sin responder" (0); el corrector interpretó una respuesta que cubre ambas partes mas de forma vaga como equivalente al techo de 10/20, una interpolación razonable pero no literalmente prevista en las instrucciones del criterio.

---

---

## Entrega: `s2_falla_c2.txt`

### Nota Final: 80 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Waterfall vs mentalidad ágil | 20 | 20 | ✅ Completo |
| C2 | Roles de Scrum | 20 | **0** | ❌ Incorrecto |
| C3 | Kanban y WIP Limit | 20 | 20 | ✅ Completo |
| C4 | Pair Programming | 20 | 20 | ✅ Completo |
| C5 | Historias de Usuario y Criterios de Aceptación | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Waterfall vs mentalidad ágil (20/20)**
Explica con claridad el problema de los cambios en Cascada (fases secuenciales, retrabajo costoso, contrato de alcance fijo) y cómo la mentalidad ágil lo resuelve (iteraciones cortas, sprints de dos semanas, feedback frecuente). Conexión Waterfall→Ágil explícita y coherente.

**C2 — Roles de Scrum (0/20)** ❌
"No se identificó ningún rol de Scrum." Para la priorización de negocio se menciona al "Project Manager o el líder técnico", figuras que no pertenecen a Scrum (correspondía Product Owner). Para las interrupciones externas se propone que cada desarrollador maneje sus horarios individualmente y se trate en retrospectiva, ignorando por completo al Scrum Master. Ambos puntos incorrectos: 0/10 por cada rol, 0/20 en total.

**C3 — Kanban y WIP Limit (20/20)**
Identifica correctamente la multitarea/cambio de contexto y explica con precisión cómo el WIP Limit obliga a terminar antes de empezar, mejorando el throughput real del equipo.

**C4 — Pair Programming (20/20)**
Presenta dos beneficios concretos y distintos, bien argumentados: revisión de código en tiempo real y transferencia de conocimiento (evita bus factor).

**C5 — Historias de Usuario y Criterios de Aceptación (20/20)**
Historia con los tres elementos de la fórmula, coherente con Netflix/Mi Lista. Tres criterios de aceptación en formato Given-When-Then, verificables, superan el mínimo exigido.

### Observación General
Del `comentario_general`: *"El trabajo muestra una comprensión sólida de la mayoría de los conceptos [...] Sin embargo, la confusión en C2 es grave: no se identificó ningún rol de Scrum, reemplazándolos por figuras ajenas al marco (Project Manager) y soluciones individuales, lo que evidencia un vacío en uno de los temas centrales de la materia."* La rúbrica discriminó exactamente como anticipa el nombre del archivo: el descuento total (20 puntos) se concentró íntegramente en C2, sin afectar a los demás criterios.

---

---

## Entrega: `s3_falla_c3.txt`

### Nota Final: 85 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Waterfall vs mentalidad ágil | 20 | 20 | ✅ Completo |
| C2 | Roles de Scrum | 20 | 20 | ✅ Completo |
| C3 | Kanban y WIP Limit | 20 | **5** | ❌ Insuficiente |
| C4 | Pair Programming | 20 | 20 | ✅ Completo |
| C5 | Historias de Usuario y Criterios de Aceptación | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Waterfall vs mentalidad ágil (20/20)**
Explica con argumentos propios ambas partes, con frase de síntesis propia ("Mientras que en Cascada un cambio tardío es una catástrofe, en ágil es algo esperado"). Cubre todas las evidencias esperadas.

**C2 — Roles de Scrum (20/20)**
Identifica y justifica ambos roles con precisión, conectando cada uno con el problema concreto que resuelve.

**C3 — Kanban y WIP Limit (5/20)** ❌
"La respuesta no cumple con los requisitos del criterio." Describe Kanban en términos generales (tablero, columnas) y reconoce que la multitarea es problemática, pero no nombra explícitamente un desperdicio Lean. Lo más grave: no explica cómo el WIP Limit soluciona el problema — de hecho **rechaza explícitamente el concepto**, afirmando "no termino de ver cómo un límite numérico de tareas por columna por sí solo mejora la velocidad" y atribuyendo la mejora solo a la visibilidad del tablero. Se otorgan 5 puntos por reconocer parcialmente el problema de la multitarea.

**C4 — Pair Programming (20/20)**
Dos beneficios distintos y bien argumentados: revisión de código en tiempo real y transferencia de conocimiento entre perfiles junior/senior.

**C5 — Historias de Usuario y Criterios de Aceptación (20/20)**
Historia completa con los tres elementos de la fórmula. Tres criterios de aceptación verificables y pertinentes.

### Observación General
Del `comentario_general`: *"La falla está en C3 (Kanban/WIP Limit), donde no solo omite explicar el concepto central que la pregunta pedía, sino que explícitamente rechaza la efectividad del WIP Limit y reduce Kanban a una herramienta de visualización."* La rúbrica concentró el descuento en C3 tal como anticipa el nombre del archivo, aunque no lo llevó a 0: al reconocer parcialmente el problema de la multitarea, el corrector otorgó 5/20 en lugar de 0/20 — un matiz razonable dado que la instrucción de puntuación de C3 sí prevé un techo de 10/20 para respuestas incompletas, aunque en este caso el resultado (5/20) queda incluso por debajo de ese techo, reflejando el rechazo explícito del WIP Limit por parte del alumno.

---

---

## Entrega: `s4_falla_c4.txt`

### Nota Final: 80 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Waterfall vs mentalidad ágil | 20 | 20 | ✅ Completo |
| C2 | Roles de Scrum | 20 | 20 | ✅ Completo |
| C3 | Kanban y WIP Limit | 20 | 20 | ✅ Completo |
| C4 | Pair Programming | 20 | **0** | ❌ Incorrecto |
| C5 | Historias de Usuario y Criterios de Aceptación | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Waterfall vs mentalidad ágil (20/20)**
Explica el problema de Cascada (fases secuenciales, retrabajo masivo, contratos firmados, costo exponencial del cambio) y la solución ágil (iteraciones cortas, feedback continuo). Conexión lógica sólida.

**C2 — Roles de Scrum (20/20)**
Ambos roles correctamente identificados y justificados, sin confusión de responsabilidades.

**C3 — Kanban y WIP Limit (20/20)**
Identifica correctamente la multitarea/cambio de contexto y explica con precisión el mecanismo "stop starting, start finishing" del WIP Limit y su efecto en el throughput.

**C4 — Pair Programming (0/20)** ❌
"El alumno NO defiende la práctica de Pair Programming. Por el contrario, argumenta EN CONTRA", coincidiendo con la crítica de que es "perder el tiempo de un empleado" y proponiendo code review como alternativa, sin presentar ningún beneficio de la práctica. La rúbrica establece explícitamente: "Si no responde o no defiende la práctica → 0".

**C5 — Historias de Usuario y Criterios de Aceptación (20/20)**
Historia completa con los tres elementos, coherente con el contexto. Dos criterios de aceptación verificables y pertinentes.

### Observación General
Del `comentario_general`: *"El trabajo demuestra un muy buen dominio de metodologías ágiles en 4 de los 5 criterios [...] Sin embargo, en C4 (Pair Programming) el alumno no responde lo solicitado: en lugar de defender la práctica con beneficios concretos, argumenta en contra, lo que resulta en un 0 en ese criterio."* La rúbrica discriminó exactamente como anticipa el nombre del archivo: el descuento total se concentró en C4 sin afectar a los demás criterios.

---

---

## Entrega: `s5_falla_c5.txt`

### Nota Final: 80 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Waterfall vs mentalidad ágil | 20 | 20 | ✅ Completo |
| C2 | Roles de Scrum | 20 | 20 | ✅ Completo |
| C3 | Kanban y WIP Limit | 20 | 20 | ✅ Completo |
| C4 | Pair Programming | 20 | 20 | ✅ Completo |
| C5 | Historias de Usuario y Criterios de Aceptación | 20 | **0** | ❌ Incorrecto |

### Feedback por criterio

**C1 — Waterfall vs mentalidad ágil (20/20)**
Respuesta completa con elaboración propia: fases secuenciales, retrabajo, contratos firmados, costo exponencial del cambio vs. iteraciones cortas y feedback continuo.

**C2 — Roles de Scrum (20/20)**
Product Owner y Scrum Master correctamente explicados, sin confusión de responsabilidades.

**C3 — Kanban y WIP Limit (20/20)**
Identifica correctamente la multitarea/cambio de contexto y explica con precisión cómo el WIP Limit fuerza a terminar antes de empezar, mejorando el throughput.

**C4 — Pair Programming (20/20)**
Dos beneficios distintos y desarrollados: revisión en tiempo real y transferencia de conocimiento.

**C5 — Historias de Usuario y Criterios de Aceptación (0/20)** ❌
Parte (a): "No redacta una Historia de Usuario usando la fórmula estándar". Describe la funcionalidad de forma narrativa pero nunca estructura la historia en el formato "Como/quiero/para" solicitado. Parte (b): no presenta criterios de aceptación verificables — lo escrito ("el equipo de QA debería verificar que todo funcione sin errores...") son instrucciones de testing vagas y genéricas, no una checklist concreta.

### Observación General
Del `comentario_general`: *"El alumno demuestra un dominio sólido de los conceptos de metodologías ágiles en las primeras cuatro preguntas [...] Sin embargo, en la pregunta 5 no sigue el formato estándar de Historia de Usuario solicitado explícitamente y no proporciona criterios de aceptación verificables, dejando sin responder lo que la rúbrica pide en el criterio de mayor peso procedimental."* La rúbrica discriminó exactamente como anticipa el nombre del archivo: el descuento total se concentró en C5.

---

---

## Entrega: `s6_parcial_c1.txt` — Sin corrección disponible

Esta entrega cuenta con el texto de la entrega (`s6_parcial_c1.txt`) y el prompt que se le habría enviado al modelo (`s6_parcial_c1_prompt.txt`), pero **no existe el archivo `s6_parcial_c1_correccion.json`** — la corrección nunca se ejecutó o el resultado se perdió antes de consolidar esta carpeta. `resumen.json` confirma este vacío: registra `"nota": null` y `"meta": "❌"` para el `sid` `s6`, sin objeto de corrección asociado.

No es posible, por lo tanto, reportar nota, desglose por criterio ni feedback real para esta entrega sin inventar contenido que la IA nunca produjo. Esta entrega queda pendiente de re-ejecución de la corrección.

---

---

## Entrega: `s7_parcial_c2.txt`

### Nota Final: 100 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Waterfall vs mentalidad ágil | 20 | 20 | ✅ Completo |
| C2 | Roles de Scrum | 20 | 20 | ✅ Completo |
| C3 | Kanban y WIP Limit | 20 | 20 | ✅ Completo |
| C4 | Pair Programming | 20 | 20 | ✅ Completo |
| C5 | Historias de Usuario y Criterios de Aceptación | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Waterfall vs mentalidad ágil (20/20)**
Describe el modelo Cascada como secuencial y detalla el retrabajo costoso de cambiar requisitos, con mención al plan firmado con el cliente. La solución ágil está bien conectada (iteraciones cortas, entregas incrementales, feedback del cliente).

**C2 — Roles de Scrum (20/20)**
Identifica correctamente ambos roles: Product Owner (prioriza según valor de negocio) y Scrum Master (escudo frente a interrupciones externas), cada uno justificado en función del problema planteado, sin invertir responsabilidades ni inventar roles.

**C3 — Kanban y WIP Limit (20/20)**
Identifica el desperdicio de multitarea/cambio de contexto y desarrolla el WIP Limit con una analogía propia (embudo con autos) para explicar el aumento del throughput.

**C4 — Pair Programming (20/20)**
Dos beneficios concretos y bien diferenciados: revisión continua con detección temprana de errores, y transferencia de conocimiento (aprendizaje cruzado junior-senior, reducción del riesgo por dependencia de una sola persona).

**C5 — Historias de Usuario y Criterios de Aceptación (20/20)**
Historia con los tres elementos de la fórmula, coherente con Netflix. Tres criterios de aceptación en formato Given/When/Then, verificables y pertinentes, superando el mínimo exigido.

### Observación General — Hallazgo
Del `comentario_general`: *"El alumno demuestra dominio sólido de los fundamentos ágiles evaluados. Todas las respuestas están bien argumentadas [...] Excelente trabajo."* No hay ningún descuento, ni siquiera parcial, en C2.

⚠️ **Esta entrega es la que peor valida la hipótesis del test.** El nombre de archivo (`s7_parcial_c2`) y `resumen.json` (`"testea": "C2 parcial (20 pts)"`, `"esperado": "~90"`) indican que esta entrega fue diseñada para contener una **falla parcial en C2** (Roles de Scrum). Sin embargo, al leer el contenido de `s7_parcial_c2.txt`, la respuesta a la Pregunta 2 identifica y justifica ambos roles de forma completa y correcta — de calidad equivalente a la de `s0_perfecta.txt` — sin ningún indicio de comprensión parcial o incompleta. El resultado (`nota: 100`, `meta: "❌"` en `resumen.json`) refleja que **la propia entrega sintética no llegó a embeber la falla parcial que su nombre promete**, no necesariamente un error de la rúbrica o del corrector: dado el contenido real, calificarlo con 100/100 es coherente. El diseño de este caso de prueba debería revisarse (regenerar el texto de la Pregunta 2 con una falla parcial real) para poder validar si la rúbrica discrimina correctamente los aciertos parciales en C2.

---

## Resumen de la Rúbrica — Comportamiento observado

| Escenario de prueba | Comportamiento esperado | Resultado |
|---|---|---|
| Entrega completa y correcta | 100/100 sin penalizaciones | ✅ Correcto — `s0_perfecta.txt`: 100/100 |
| Falla parcial en C1 (Waterfall vs ágil) | Descuento concentrado en C1 | ✅ Correcto en foco, parcial en magnitud — `s1_falla_c1.txt`: 90/100 (C1 a 10/20, resto intacto; esperado ~80) |
| Falla total en C2 (Roles de Scrum) | Descuento de 20 puntos en C2, resto intacto | ✅ Correcto — `s2_falla_c2.txt`: 80/100 (C2 a 0/20) |
| Falla en C3 (Kanban/WIP Limit) | Descuento concentrado en C3 | ✅ Correcto — `s3_falla_c3.txt`: 85/100 (C3 a 5/20, resto intacto; esperado ~80) |
| Falla total en C4 (Pair Programming) | Descuento de 20 puntos en C4, resto intacto | ✅ Correcto — `s4_falla_c4.txt`: 80/100 (C4 a 0/20) |
| Falla total en C5 (Historias de Usuario) | Descuento de 20 puntos en C5, resto intacto | ✅ Correcto — `s5_falla_c5.txt`: 80/100 (C5 a 0/20) |
| Falla parcial en C1 (variante 2) | ~90/100 esperado | ⚠️ Sin datos — `s6_parcial_c1.txt` no tiene `_correccion.json`; no se puede validar este escenario |
| Falla parcial en C2 (variante 2) | ~90/100 esperado | ❌ No validado — `s7_parcial_c2.txt` obtuvo 100/100 porque el contenido real de la entrega no contiene ninguna falla parcial en C2; el caso de prueba no llegó a ejercitar el escenario que pretendía cubrir |

### Conclusiones

1. **Discriminación por criterio:** en los cinco casos con corrección disponible que buscan aislar una falla en un criterio específico (`s1` a `s5`), la rúbrica concentró el descuento exactamente en el criterio nombrado en el archivo, sin "fugas" de puntaje hacia criterios no relacionados. Esto confirma que los criterios se evalúan de forma independiente.

2. **Granularidad del descuento:** la rúbrica no se limita a la dicotomía "0 o puntaje completo". En `s1_falla_c1` y `s3_falla_c3` aplicó descuentos parciales (10/20 y 5/20 respectivamente, con estado `WARNING`/`ERROR`) razonados en el propio texto de las `instrucciones_puntuacion` de cada criterio, aunque en el caso de `s1` el nivel exacto de descuento (mitad de puntaje para una respuesta "vaga mas completa") es una interpolación del corrector, no un nivel explícitamente definido en la rúbrica.

3. **Ninguna condición de desaprobación ni penalización se activó** en las 7 entregas corregidas (`condicion_desaprobacion_aplicada: null`, `penalizaciones_aplicadas: []` en todas). La única condición de desaprobación de esta rúbrica (`CD1`, PDF con imágenes) no aplica a ninguno de los textos de prueba, ya que todos son texto plano.

4. **Límite del corpus de prueba — dato faltante:** `s6_parcial_c1.txt` no tiene corrección asociada (`_correccion.json` ausente), por lo que el escenario "falla parcial en C1, variante 2" queda completamente sin validar. Se recomienda re-ejecutar la corrección de esta entrega antes de sacar conclusiones sobre el comportamiento de la rúbrica frente a fallas parciales repetidas en C1.

5. **Hallazgo sobre el diseño del corpus:** `s7_parcial_c2.txt` no valida el escenario "falla parcial en C2" que su nombre promete, porque el texto de la Pregunta 2 en esa entrega es una respuesta completa y correcta (sin falla), lo que llevó a una nota de 100/100 en lugar del ~90 esperado. Esto no es un error de la rúbrica sino una falla en la construcción de la entrega sintética: el contenido no refleja el escenario de prueba que su identificador de archivo indica. Se recomienda regenerar el texto de `s7_parcial_c2.txt` con una falla parcial real en C2 (por ejemplo, identificar el rol pero sin justificarlo, tal como contempla la propia rúbrica: "Si identifica el rol pero no justifica por qué resuelve el problema → techo 5 por ese rol") para poder evaluar si la rúbrica discrimina correctamente ese caso.
