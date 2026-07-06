# Informe de Correcciones — TP2: Ingeniería de Prompts y Pensamiento Computacional

**Materia:** Organización Empresarial | **Unidad:** 3 - Ingeniería de Prompts | **UTN - Facultad Regional Mendoza**
**Rúbrica aplicada:** `rubrica-tp2-ingenieria-prompts.json` | **Puntaje máximo:** 100 puntos

> Nota metodológica: las 8 entregas analizadas son sintéticas y fueron generadas para probar la discriminación de la rúbrica ante fallas puntuales en cada criterio (C1 a C6). Los prompts de texto plano no contienen identidad de alumno alguna (no hay nombre embebido, a diferencia del TP1 donde el nombre figuraba en `git config`), por lo que cada entrega se referencia únicamente por su identificador de archivo.

---

## Resumen General

| Entrega | Archivo entregado | Testeaba | Nota Final | Estado |
|---|---|---|---|---|
| s0 | `s0_perfecta.txt` | Rúbrica completa (caso ideal) | **100 / 100** | ✅ Sin observaciones |
| s1 | `s1_falla_c1.txt` | C1 discrimina (18 pts) | **91.9 / 100** | ✅ Falla aislada en C1 |
| s2 | `s2_falla_c2.txt` | C2 discrimina (18 pts) | **82 / 100** | ✅ Falla aislada en C2 |
| s3 | `s3_falla_c3.txt` | C3 discrimina (18 pts) | **89.2 / 100** | ✅ Falla aislada en C3 |
| s4 | `s4_falla_c4.txt` | C4 discrimina (16 pts) | **47.0 / 100** | ⚠️ Anomalía — falla generalizada, no aislada en C4 |
| s5 | `s5_falla_c5.txt` | C5 discrimina (16 pts) | **87 / 100** | ✅ Falla aislada en C5 |
| s6 | `s6_falla_c6.txt` | C6 discrimina (14 pts) | **87.5 / 100** | ✅ Falla aislada en C6 |
| s7 | `s7_parcial_c1.txt` | C1 falla parcial (18 pts) | **88.3 / 100** | ✅ Falla aislada en C1 (parcial) |
| — | `manual_entrega_alumno.txt` | Entrega manual (borrador, no sintética) | **84 / 100** | ✅ Falla real en C4 |
| — | `manual_entrega_simulada.md` | Entrega manual (borrador, no sintética) | **89.2 / 100** | ✅ Falla real en C3 |

Las dos últimas filas no son parte de la suite sintética `sN_*` original: son dos entregas manuales previas (`borradores/TP2_Entrega_Alumno.txt` y `borradores/entrega-simulada-tp2.md`), redactadas antes de que existiera el generador automático de sintéticos, y que se corrieron recién ahora contra la rúbrica con `simular_correccion.py` para incorporarlas al mismo flujo ordenado del resto de los TPs.

Ninguna de las 8 correcciones sintéticas activó una condición de desaprobación (`condicion_desaprobacion_aplicada: null` en las 8) ni penalizaciones adicionales (`penalizaciones_aplicadas: []` en las 8) — de hecho la rúbrica declara `"penalizaciones": []` y `"condiciones_desaprobacion": []` en su definición, por lo que todo el puntaje se resuelve exclusivamente vía los descuentos internos de cada criterio (`instrucciones_puntuacion`).

---

---

## Entrega: `s0_perfecta.txt`

### Nota Final: 100 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Arquitectura de la Instrucción | 18 | 18 | ✅ Completo |
| C2 | Laboratorio de Parámetros | 18 | 18 | ✅ Completo |
| C3 | Razonamiento Avanzado (CoT) | 18 | 18 | ✅ Completo |
| C4 | Refactorización de Código | 16 | 16 | ✅ Completo |
| C5 | Seguridad y Ética (Defensa de Prompts) | 16 | 16 | ✅ Completo |
| C6 | Simulación de Sesgos | 14 | 14 | ✅ Completo |

### Feedback por criterio

**C1 — Arquitectura de la Instrucción (18/18)**
Los 4 elementos fundamentales están presentes y claramente identificados: Instrucción, Contexto, Datos de Entrada e Indicador de Salida, delimitados con etiquetas XML (`<INSTRUCCIÓN>`, `<CONTEXTO>`, `<DATOS_DE_ENTRADA>`, `<INDICADOR_DE_SALIDA>`). Las 3 categorías (Urgente, Consulta General, Feedback) están definidas con precisión.

**C2 — Laboratorio de Parámetros (18/18)**
Caso A (Temperatura 0.1 / Top-p 0.1) y Caso B (Temperatura 0.9 / Top-p 0.95) con justificaciones sólidas que explican el efecto de la temperatura sobre la distribución de probabilidad y referencian explícitamente la teoría de Predicción de Tokens en ambos casos.

**C3 — Razonamiento Avanzado / CoT (18/18)**
El ejemplo previo (grifos llenando tanques) es de un dominio distinto al de las camisas y muestra 4 pasos de razonamiento explícito. El problema objetivo está incluido con su redacción exacta y la instrucción final pide replicar el esquema.

**C4 — Refactorización de Código (16/16)**
Rol de Senior con 10+ años definido, código original incluido textualmente, y los 4 requisitos técnicos (type hints, Docstring, refactorización con buenas prácticas, explicación línea por línea) enumerados sin omisiones.

**C5 — Seguridad y Ética (16/16)**
System Prompt formulado como instrucción directa al modelo, con propósito definido (orientación académica). Protección contra Jailbreaking con ejemplos concretos de frases de ataque y protección contra Prompt Leaking que prohíbe revelar instrucciones internas, claves API y datos sensibles.

**C6 — Simulación de Sesgos (14/14)**
Instrucciones explícitas contra sesgos de género y culturales, diversidad geográfica y foco en competencias profesionales universales. La justificación explica el origen del sesgo en los datos de entrenamiento con profundidad ("el modelo no corrige solo").

### Observación General
Las 6 actividades cubren todas las evidencias exigidas sin omisiones ni ambigüedades. El corrector destaca comprensión conceptual profunda (fundamentación en teoría de Predicción de Tokens en C2 y C6) y sugiere solo mejoras cosméticas menores en las `recomendaciones` (ninguna afecta el puntaje): Top-p demasiado restrictivo en C2, falta de un estilo único de Docstring en C4, y ausencia de regla contra ataques iterativos en C5.

---

---

## Entrega: `s1_falla_c1.txt`

### Nota Final: 91.9 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Arquitectura de la Instrucción | 18 | **9.9** | ⚠️ Parcial (-25% delimitadores, -20% categorías) |
| C2 | Laboratorio de Parámetros | 18 | 18 | ✅ Completo |
| C3 | Razonamiento Avanzado (CoT) | 18 | 18 | ✅ Completo |
| C4 | Refactorización de Código | 16 | 16 | ✅ Completo |
| C5 | Seguridad y Ética (Defensa de Prompts) | 16 | 16 | ✅ Completo |
| C6 | Simulación de Sesgos | 14 | 14 | ✅ Completo |

### Feedback por criterio

**C1 — Arquitectura de la Instrucción (9.9/18)** ⚠️
Los 4 elementos están presentes conceptualmente (instrucción, contexto, datos de entrada e indicador de salida narrados en prosa), pero el prompt no usa ningún delimitador visible entre secciones (-25%, 4.5 pts) y las 3 categorías requeridas no se nombran textualmente sino que se parafrasean ("para ya mismo", "pueden esperar", "comentario de un cliente") en vez de decir "Urgente", "Consulta General" y "Feedback" (-20%, 3.6 pts). Los descuentos son acumulables, quedando el criterio en un prompt "coloquial y poco profesional".

**C2 — Laboratorio de Parámetros (18/18)**
Caso A y Caso B con valores correctos y justificaciones que referencian la teoría de Predicción de Tokens. Se señala solo un error tipográfico menor ("Tokenos") que no afecta la corrección técnica ni resta puntos.

**C3 — Razonamiento Avanzado / CoT (18/18)**
Ejemplo previo distinto (gallinas y vacas) con razonamiento algebraico completo (planteo de ecuaciones, sustitución, verificación) antes del problema target de las camisas, correctamente delimitado con "---".

**C4 — Refactorización de Código (16/16)**
Rol Senior definido, código original incluido, y los 4 requisitos técnicos enunciados con claridad.

**C5 — Seguridad y Ética (16/16)**
System Prompt correcto con propósito de ciberseguridad empresarial, protección contra Jailbreaking (regla 2, con respuesta predefinida) y contra Prompt Leaking (regla 1, mención explícita de claves de API).

**C6 — Simulación de Sesgos (14/14)**
Instrucciones explícitas de diversidad de género y cultural, con justificación que identifica el origen del sesgo en "patrones históricos del mundo real" y "hombres de determinados perfiles culturales".

### Observación General
La única falla de la entrega está localizada en C1: el corrector señala explícitamente que se trata de un prompt sin estructura profesional, sin delimitadores y sin nombrar las categorías por su designación exacta. Las recomendaciones apuntan puntualmente a corregir esos dos aspectos. El resto de la entrega (C2 a C6) es impecable.

---

---

## Entrega: `s2_falla_c2.txt`

### Nota Final: 82 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Arquitectura de la Instrucción | 18 | 18 | ✅ Completo |
| C2 | Laboratorio de Parámetros | 18 | **0** | ❌ Valores invertidos |
| C3 | Razonamiento Avanzado (CoT) | 18 | 18 | ✅ Completo |
| C4 | Refactorización de Código | 16 | 16 | ✅ Completo |
| C5 | Seguridad y Ética (Defensa de Prompts) | 16 | 16 | ✅ Completo |
| C6 | Simulación de Sesgos | 14 | 14 | ✅ Completo |

### Feedback por criterio

**C1 — Arquitectura de la Instrucción (18/18)**
Los 4 elementos presentes y delimitados con `###`, las 3 categorías mencionadas, orientado correctamente al caso de soporte técnico.

**C2 — Laboratorio de Parámetros (0/18)** ❌
Ambos casos tienen los valores invertidos respecto de lo esperado: en el Caso A (que requiere determinismo) se proponen Temperatura 0.85 / Top-p 0.92 —valores altos, propios de creatividad—; en el Caso B (que requiere creatividad) se proponen Temperatura 0.25 / Top-p 0.35 —valores bajos, propios de determinismo—. Las justificaciones, además, no referencian la teoría de Predicción de Tokens. Según la instrucción de puntuación ("si valores incorrectos o contradictorios, 0 en ese caso"), ambos casos reciben 0 puntos.

**C3 — Razonamiento Avanzado / CoT (18/18)**
Ejemplo previo distinto (máquinas y piezas) con razonamiento paso a paso en 4 etapas, problema objetivo de las camisas incluido y diseñado para replicar el esquema CoT.

**C4 — Refactorización de Código (16/16)**
Rol Senior, código original y los 4 requisitos técnicos presentes, incluyendo mención de casos borde.

**C5 — Seguridad y Ética (16/16)**
System Prompt con propósito definido (recomendaciones de libros), protección contra Jailbreaking (reglas 3 y 4) y contra Prompt Leaking (reglas 1 y 2), reforzado por una regla 5 de criterio restrictivo.

**C6 — Simulación de Sesgos (14/14)**
Mitigación de sesgos de género y diversidad cultural/geográfica, con justificación sólida sobre la sobrerrepresentación de hombres occidentales en el corpus de entrenamiento.

### Observación General
El corrector aísla el error en una "confusión conceptual crítica": el alumno invirtió los valores de Temperatura/Top-p entre el caso determinista y el creativo, evidenciando que no comprende cómo estos parámetros controlan la distribución de probabilidad. El resto de los criterios (C1, C3, C4, C5, C6) se resuelven con calidad "alta" según el comentario general.

---

---

## Entrega: `s3_falla_c3.txt`

### Nota Final: 89.2 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Arquitectura de la Instrucción | 18 | 18 | ✅ Completo |
| C2 | Laboratorio de Parámetros | 18 | 18 | ✅ Completo |
| C3 | Razonamiento Avanzado (CoT) | 18 | **7.2** | ⚠️ Zero-shot, techo 40% |
| C4 | Refactorización de Código | 16 | 16 | ✅ Completo |
| C5 | Seguridad y Ética (Defensa de Prompts) | 16 | 16 | ✅ Completo |
| C6 | Simulación de Sesgos | 14 | 14 | ✅ Completo |

### Feedback por criterio

**C1 — Arquitectura de la Instrucción (18/18)**
Los 4 elementos identificados, delimitados con `<<<...>>>`, categorías mencionadas y salida en formato JSON.

**C2 — Laboratorio de Parámetros (18/18)**
Caso A (Temperatura 0.1 / Top-p 0.15) y Caso B (Temperatura 0.9 / Top-p 0.95) correctos, con justificaciones que referencian la teoría de Predicción de Tokens.

**C3 — Razonamiento Avanzado / CoT (7.2/18)** ⚠️
El prompt usa estrategia Zero-shot CoT ("pensá paso a paso") e incluye el problema objetivo de las camisas, pero **no contiene ningún ejemplo previo** de un problema distinto con razonamiento paso a paso, requisito explícito de la consigna (Few-shot CoT). Al ser zero-shot sin ejemplos, se aplica el techo del 40% (7.2 pts). El corrector sugiere agregar un ejemplo tipo "3 pintores pintan 3 casas en 3 días..." resuelto paso a paso antes del problema target.

**C4 — Refactorización de Código (16/16)**
Rol Senior, código original y los 4 requisitos técnicos presentes.

**C5 — Seguridad y Ética (16/16)**
System Prompt con propósito definido, protección contra Jailbreaking y contra Prompt Leaking sin observaciones.

**C6 — Simulación de Sesgos (14/14)**
Instrucciones de diversidad de género, cultural y geográfica; justificación que explica el origen del sesgo en los datos de entrenamiento.

### Observación General
La falla está exclusivamente en C3: el corrector identifica con precisión la diferencia entre Zero-shot y Few-shot CoT, y aplica el techo previsto en la rúbrica para esta falla específica. El resto de la entrega es sólido ("consistencia en la calidad" en C1, C2, C4, C5 y C6, según las fortalezas señaladas).

---

---

## Entrega: `s4_falla_c4.txt`

### Nota Final: 47.0 / 100

> ⚠️ **Hallazgo — el archivo no contiene la entrega real.** A diferencia de las demás muestras sintéticas, `s4_falla_c4.txt` no son los 6 prompts completos: es un **resumen/meta-descripción** de lo que "se habría entregado" (ej. *"C4 — Falla creíble: el alumno escribe un prompt genérico..."*), incluso con una frase final rompiendo la cuarta pared ("¿Se entiende?"). El corrector detectó correctamente que no podía verificar el contenido real de casi ningún criterio y penalizó en consecuencia — pero como resultado la falla NO quedó aislada en C4 como pretendía el nombre del archivo: los 6 criterios recibieron descuentos. Esto no es un fallo de la rúbrica sino un defecto en la generación de esta muestra sintética en particular.

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Arquitectura de la Instrucción | 18 | **9.0** | ⚠️ No verificable (techo 60%) |
| C2 | Laboratorio de Parámetros | 18 | **12.0** | ⚠️ Valores ok, justificación no verificable |
| C3 | Razonamiento Avanzado (CoT) | 18 | **10.0** | ⚠️ No verificable |
| C4 | Refactorización de Código | 16 | **0** | ❌ Falla real confirmada (0/16) |
| C5 | Seguridad y Ética (Defensa de Prompts) | 16 | **8.0** | ⚠️ No verificable |
| C6 | Simulación de Sesgos | 14 | **8.0** | ⚠️ No verificable |

### Feedback por criterio

**C1 — Arquitectura de la Instrucción (9/18)** ⚠️
El resumen menciona los 4 elementos, los delimitadores `###` y las 3 categorías por nombre, pero el prompt completo no está en la entrega: no puede verificarse la estructura real. Techo de 60% (10.8 pts) más un descuento adicional por delimitadores no verificables. Puntaje final: 9/18.

**C2 — Laboratorio de Parámetros (12/18)** ⚠️
Los valores declarados (0.1/0.1 y 0.9/0.95) son correctos y están en rango, pero el texto completo de las justificaciones no está presente, por lo que no puede verificarse su profundidad. Se aplica un descuento del 30% por caso por justificación no verificable.

**C3 — Razonamiento Avanzado / CoT (10/18)** ⚠️
El resumen indica Few-shot CoT con ejemplo de máquinas y tornillos, pero al no estar el prompt completo no puede verificarse que el ejemplo muestre razonamiento paso a paso explícito ni que el problema target esté correctamente formulado.

**C4 — Refactorización de Código (0/16)** ❌
El propio resumen declara que el alumno "escribió un prompt genérico pidiendo opinión sobre el código", sin rol Senior, sin el código original y sin ninguno de los 4 requisitos técnicos. Se aplican los descuentos acumulables completos (-20% rol, -20% código original, -15% × 4 requisitos = 16 pts), dejando el criterio en 0/16. Este es el único criterio cuya falla fue confirmada con certeza (no por falta de evidencia, sino porque el propio resumen admite el defecto).

**C5 — Seguridad y Ética (8/16)** ⚠️
El resumen afirma protección contra Jailbreaking y Prompt Leaking, pero el System Prompt completo no está presente para confirmar que el texto esté formulado como instrucciones al sistema y no como análisis teórico.

**C6 — Simulación de Sesgos (8/14)** ⚠️
El resumen menciona diversidad e identifica el origen del sesgo en los datos de entrenamiento (mención verificable en el propio texto), pero ni el prompt de mitigación ni la justificación completa están presentes para confirmar profundidad.

### Observación General
El comentario general del corrector es explícito: *"la entrega consiste en un resumen descriptivo en lugar de los prompts completos solicitados... la Actividad 4 es la más crítica: está explícitamente incompleta y debe rehacerse por completo"*. La nota de 47.0 queda muy por debajo del "~84" que el `resumen.json` declaraba como esperado para esta muestra, precisamente porque la falla no quedó acotada a C4 sino que degradó los 6 criterios por falta de artefacto verificable.

---

---

## Entrega: `s5_falla_c5.txt`

### Nota Final: 87 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Arquitectura de la Instrucción | 18 | 18 | ✅ Completo |
| C2 | Laboratorio de Parámetros | 18 | 18 | ✅ Completo |
| C3 | Razonamiento Avanzado (CoT) | 18 | 18 | ✅ Completo |
| C4 | Refactorización de Código | 16 | 16 | ✅ Completo |
| C5 | Seguridad y Ética (Defensa de Prompts) | 16 | **3** | ❌ No es un System Prompt |
| C6 | Simulación de Sesgos | 14 | 14 | ✅ Completo |

### Feedback por criterio

**C1 — Arquitectura de la Instrucción (18/18)**
Los 4 elementos delimitados con `====`, correo concreto como dato de entrada y las 3 categorías mencionadas explícitamente.

**C2 — Laboratorio de Parámetros (18/18)**
Caso A (0.1/0.2) y Caso B (0.9/0.95) correctos, con justificaciones que explican el achatamiento/suavizado de la distribución de probabilidad y referencian la predicción de tokens.

**C3 — Razonamiento Avanzado / CoT (18/18)**
Ejemplo previo (probabilidad de frutas en una caja) con 4 pasos de razonamiento explícito, seguido del problema target de las camisas con instrucción de replicar el método.

**C4 — Refactorización de Código (16/16)**
Rol Senior con 10+ años, código original y los 4 requisitos, incluyendo mención de casos borde y escalabilidad.

**C5 — Seguridad y Ética (3/16)** ❌
El texto entregado **no es un System Prompt**: es un ensayo teórico que explica qué son jailbreaking y prompt leaking y propone defensas externas (filtros de entrada/salida, rate limiting, regex en servidor) en lugar de instrucciones dirigidas al modelo. Se aplica el techo de 40% (6.4 pts) por falta de estructura de System Prompt, y se otorgan igualmente solo 3 pts por la comprensión conceptual demostrada, ya que "no hay instrucciones al modelo para ignorar/rechazar jailbreaking ni para no revelar instrucciones internas".

**C6 — Simulación de Sesgos (14/14)**
Prompt de mitigación completo con diversidad de género/geográfica y foco en competencias universales; justificación "excepcional" que ancla el sesgo en la sobrerrepresentación histórica de CEOs hombres y en la co-ocurrencia estadística de la predicción de tokens.

### Observación General
El corrector aísla correctamente la falla en C5: la actividad pedía un System Prompt con instrucciones defensivas, y en su lugar se entregó un análisis teórico sobre seguridad en LLMs. El comentario general lo resume como "un error de formato que penaliza fuerte porque el corrector no tiene un prompt de sistema que evaluar, por más que el análisis conceptual sea acertado".

---

---

## Entrega: `s6_falla_c6.txt`

### Nota Final: 87.5 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Arquitectura de la Instrucción | 18 | 18 | ✅ Completo |
| C2 | Laboratorio de Parámetros | 18 | 18 | ✅ Completo |
| C3 | Razonamiento Avanzado (CoT) | 18 | 18 | ✅ Completo |
| C4 | Refactorización de Código | 16 | 16 | ✅ Completo |
| C5 | Seguridad y Ética (Defensa de Prompts) | 16 | 16 | ✅ Completo |
| C6 | Simulación de Sesgos | 14 | **1.5** | ❌ Prompt original sin intervenir |

### Feedback por criterio

**C1 — Arquitectura de la Instrucción (18/18)**
Los 4 elementos delimitados con `###`, salida JSON que especifica las 3 categorías requeridas.

**C2 — Laboratorio de Parámetros (18/18)**
Caso A (0.1/0.2) y Caso B (0.9/0.95) correctos, justificados con referencia a softmax, logits y distribución de probabilidad.

**C3 — Razonamiento Avanzado / CoT (18/18)**
Ejemplo previo distinto (gallinas y huevos) con 4 pasos de razonamiento explícito, problema objetivo de las camisas incluido.

**C4 — Refactorización de Código (16/16)**
Rol Senior, código original y los 4 requisitos, con formato de entrega estructurado en bloques.

**C5 — Seguridad y Ética (16/16)**
System Prompt con propósito definido (VitalConnect), protección contra Jailbreaking con ejemplos concretos y contra Prompt Leaking mencionando claves API.

**C6 — Simulación de Sesgos (1.5/14)** ❌
El prompt entregado **no incluye ninguna instrucción de diversidad, inclusión o competencias profesionales universales: es el prompt original sin modificar**, lo que activa el techo del 30% (4.2 pts). Peor aún, la justificación escrita "argumenta en contra de intervenir, contradiciendo el objetivo de la actividad" y confunde "realidad estadística del mundo corporativo" con sesgo algorítmico, sin mencionar el origen del sesgo en los datos de entrenamiento. Por eso el puntaje cae por debajo incluso del techo nominal, a 1.5/14.

### Observación General
El corrector identifica el error como conceptual y no meramente formal: el alumno "argumenta en contra de la intervención y confunde realidad estadística con sesgo algorítmico, incumpliendo completamente el objetivo de la actividad. Esta confusión... es justamente lo que la unidad busca desarmar". El resto de la entrega (C1 a C5) es calificado como "técnicamente impecable".

---

---

## Entrega: `s7_parcial_c1.txt`

### Nota Final: 88.3 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Arquitectura de la Instrucción | 18 | **6.3** | ❌ Falta Indicador de Salida + sin delimitadores |
| C2 | Laboratorio de Parámetros | 18 | 18 | ✅ Completo |
| C3 | Razonamiento Avanzado (CoT) | 18 | 18 | ✅ Completo |
| C4 | Refactorización de Código | 16 | 16 | ✅ Completo |
| C5 | Seguridad y Ética (Defensa de Prompts) | 16 | 16 | ✅ Completo |
| C6 | Simulación de Sesgos | 14 | 14 | ✅ Completo |

### Feedback por criterio

**C1 — Arquitectura de la Instrucción (6.3/18)** ❌
El prompt define el rol y menciona las 3 categorías requeridas, e incluye un correo de ejemplo como Datos de Entrada, pero **falta el Indicador de Salida** (no especifica en qué formato debe responder el modelo), lo que activa el techo de 60% (10.8 pts). Además no hay delimitadores visibles entre secciones (todo en un solo párrafo), lo que descuenta otros 4.5 pts adicionales. Puntaje final: 10.8 − 4.5 = 6.3/18.

**C2 — Laboratorio de Parámetros (18/18)**
Caso A (0.1/0.1) y Caso B (0.9/0.9) correctos, con justificación técnica sólida que referencia la teoría de Predicción de Tokens en ambos casos.

**C3 — Razonamiento Avanzado / CoT (18/18)**
Ejemplo previo distinto (pintores y casas) con razonamiento paso a paso detallado, seguido del problema objetivo de las camisas con instrucción explícita de replicar el método.

**C4 — Refactorización de Código (16/16)**
Rol Senior, código original y los 4 requisitos técnicos, incluyendo convenciones PEP.

**C5 — Seguridad y Ética (16/16)**
System Prompt de recomendaciones literarias, con protección contra Jailbreaking (reglas 1 y 2, con ejemplos concretos de ataques) y contra Prompt Leaking (regla 3, mención explícita de claves API).

**C6 — Simulación de Sesgos (14/14)**
Instrucciones de diversidad de género/cultural, justificación que explica el origen del sesgo en los datos de entrenamiento y la falta de "mecanismos automáticos para corregirlo" del modelo.

### Observación General
La falla queda acotada a C1 por dos motivos acumulables (falta de Indicador de Salida y ausencia de delimitadores), tal como anticipaba el nombre del archivo ("parcial_c1"). El comentario general lo resume: *"Corregir ese único detalle llevaría el trabajo a un puntaje perfecto de 100"*.

---

## Entrega: `manual_entrega_alumno.txt` (borrador manual)

### Nota Final: 84 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Arquitectura de la Instrucción | 18 | 18 | ✅ Completo |
| C2 | Laboratorio de Parámetros | 18 | 18 | ✅ Completo |
| C3 | Razonamiento Avanzado (CoT) | 18 | 18 | ✅ Completo |
| C4 | Refactorización de Código | 16 | **0** | ❌ Prompt genérico, sin requisitos |
| C5 | Seguridad y Ética (Defensa de Prompts) | 16 | 16 | ✅ Completo |
| C6 | Simulación de Sesgos | 14 | 14 | ✅ Completo |

### Feedback por criterio

**C1 — Arquitectura de la Instrucción (18/18)**
Los 4 elementos fundamentales están claramente etiquetados con delimitadores consistentes, y las 3 categorías requeridas están mencionadas y definidas tanto en la instrucción como en el contexto.

**C2 — Laboratorio de Parámetros (18/18)**
Caso A (0.1/0.1) y Caso B (0.9/0.95) correctos, con justificación que referencia explícitamente la teoría de Predicción de Tokens y el nucleus sampling en ambos casos.

**C3 — Razonamiento Avanzado / CoT (18/18)**
Ejemplo previo (máquinas y tornillos) con razonamiento paso a paso en 4 pasos, problema objetivo de las camisas incluido y solicitud explícita de replicar el método.

**C4 — Refactorización de Código (0/16)** ❌
El prompt entregado ("Hola, necesito que me ayudes con esta función de Python. Contame si el código está bien escrito...") no define el rol de Senior, no incluye el código original `def suma(a,b): return a+b`, y no pide ninguno de los 4 requisitos técnicos (type hints, docstring, explicación línea por línea, refactorización). Es un pedido genérico de opinión, no una refactorización estructurada. Descuentos acumulables del 100% (20% rol + 20% código + 15%×4 requisitos).

**C5 — Seguridad y Ética (16/16)**
System Prompt de asistente bancario con protección explícita contra Jailbreaking (rechazo de cambios de rol) y contra Prompt Leaking (nunca revelar el contenido del system prompt ni datos sensibles).

**C6 — Simulación de Sesgos (14/14)**
Instrucciones explícitas de diversidad de género y cultural, con justificación que conecta el sesgo con la sobrerrepresentación histórica en los datos de entrenamiento.

### Observación General
Entrega manual real (no generada sintéticamente) con un desempeño sólido en 5 de las 6 actividades. La única falla — Actividad 4 completamente fuera de consigna — es una falla genuina de esta entrega puntual, no un artefacto de generación como en `s4_falla_c4.txt`: acá el prompt sí está completo, solo que no cumple los requisitos pedidos.

---

---

## Entrega: `manual_entrega_simulada.md` (borrador manual)

### Nota Final: 89.2 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Arquitectura de la Instrucción | 18 | 18 | ✅ Completo |
| C2 | Laboratorio de Parámetros | 18 | 18 | ✅ Completo |
| C3 | Razonamiento Avanzado (CoT) | 18 | **7.2** | ⚠️ Zero-shot, techo 40% |
| C4 | Refactorización de Código | 16 | 16 | ✅ Completo |
| C5 | Seguridad y Ética (Defensa de Prompts) | 16 | 16 | ✅ Completo |
| C6 | Simulación de Sesgos | 14 | 14 | ✅ Completo |

### Feedback por criterio

**C1 — Arquitectura de la Instrucción (18/18)**
Los 4 elementos delimitados con `<<<...>>>`, correo de ejemplo como dato de entrada y salida en formato JSON especificado. Las 3 categorías mencionadas explícitamente.

**C2 — Laboratorio de Parámetros (18/18)**
Caso A (0.1/0.15) y Caso B (0.9/0.95) correctos, con justificación que explica el achatamiento de la distribución de probabilidad y referencia la teoría de Predicción de Tokens.

**C3 — Razonamiento Avanzado / CoT (7.2/18)** ⚠️
El prompt incluye el problema objetivo de las camisas y pide razonar paso a paso, pero es **Zero-shot**: no incluye ningún ejemplo previo resuelto de un problema distinto, requisito central de la técnica Few-shot CoT pedida. Se aplica el techo del 40% (7.2 pts), igual que en `s3_falla_c3.txt`.

**C4 — Refactorización de Código (16/16)**
Rol de Desarrollador Senior definido, código original incluido, y los 4 requisitos técnicos presentes.

**C5 — Seguridad y Ética (16/16)**
System Prompt de asistente bancario en segunda persona/imperativo, con protección explícita contra Jailbreaking y Prompt Leaking, incluyendo respuesta predefinida ante intentos de extracción.

**C6 — Simulación de Sesgos (14/14)**
Instrucciones explícitas de no asumir género u origen específico, diversidad cultural, y foco en competencias profesionales universales; justificación que conecta el sesgo con los datos de entrenamiento.

### Observación General
Misma falla que `s3_falla_c3.txt` (CoT Zero-shot en vez de Few-shot), pero en una entrega manual independiente — confirma que el criterio C3 discrimina de forma consistente esta falla específica en dos muestras distintas generadas por vías diferentes (una sintética, una manual).

---

## Resumen de la Rúbrica — Comportamiento observado

| Escenario de prueba | Comportamiento esperado (según `resumen.json`) | Resultado real | ¿Aislado en el criterio esperado? |
|---|---|---|---|
| Entrega completa y correcta (s0) | 100/100 sin penalizaciones | ✅ 100/100 | Sí |
| C1 discrimina (s1) | ~82 | 91.9/100 | Sí — descuento concentrado en C1 (9.9/18) |
| C2 discrimina (s2) | ~82 | 82/100 | Sí — descuento concentrado en C2 (0/18) |
| C3 discrimina (s3) | ~82 | 89.2/100 | Sí — descuento concentrado en C3 (7.2/18) |
| C4 discrimina (s4) | ~84 | **47.0/100** | **No** — los 6 criterios recibieron descuento |
| C5 discrimina (s5) | ~84 | 87/100 | Sí — descuento concentrado en C5 (3/16) |
| C6 discrimina (s6) | ~86 | 87.5/100 | Sí — descuento concentrado en C6 (1.5/14) |
| C1 parcial (s7) | ~91 | 88.3/100 | Sí — descuento concentrado en C1 (6.3/18) |

**Discriminación de la rúbrica:** en 7 de las 8 muestras sintéticas (s0, s1, s2, s3, s5, s6, s7), la rúbrica se comportó exactamente como estaba diseñada: la entrega perfecta obtuvo 100/100, y cada muestra `sN_falla_cX` concentró su descuento en el criterio CX correspondiente al nombre del archivo, dejando el resto de los criterios en su puntaje máximo. Esto confirma que los descuentos definidos en `instrucciones_puntuacion` de cada criterio operan de forma aislada entre sí (una falla en C5, por ejemplo, no contamina el puntaje de C1 a C4 o C6), tal como también se observó en el TP1 con la rúbrica de Git.

**Hallazgo — inconsistencia en `s4_falla_c4.txt`:** esta es la única muestra donde el nombre del archivo NO coincide con el criterio realmente penalizado en un sentido estricto. El archivo debía testear una falla aislada en C4 (~84 puntos esperados), pero su contenido real no son los 6 prompts completos sino un **resumen/meta-descripción en tercera persona** de lo que se habría entregado (con una frase final del tipo "¿Se entiende?" que rompe la cuarta pared). El corrector de IA identificó correctamente que no podía verificar el contenido de C1, C2, C3, C5 y C6 contra un artefacto real, y aplicó techos de "no verificable" en los cinco, además del 0/16 legítimo en C4 (el único criterio cuya falla fue confirmada explícitamente por el propio texto). El resultado es una nota de 47.0, muy por debajo del ~84 esperado, y una falla que terminó distribuida en 6 criterios en lugar de uno solo.

Esto no es un problema de la rúbrica en sí — su lógica de puntuación por evidencias respondió razonablemente ante un artefacto incompleto (no puede otorgar puntaje pleno a algo que no puede verificar) — sino un **defecto en la generación de esta muestra sintética puntual**, que no cumple el contrato implícito de las demás (`prompt de texto plano equivalente a una entrega real, con exactamente una falla en el criterio indicado por el nombre del archivo`). De cara a una futura regeneración de sintéticos, `s4_falla_c4.txt` debería reescribirse como los 6 prompts completos con la falla de C4 embebida (como en el resto de las muestras), en lugar de una descripción resumida de la entrega.

**Entregas manuales adicionales:** `manual_entrega_alumno.txt` y `manual_entrega_simulada.md` eran borradores previos al pipeline de sintéticos (antes en `borradores/`, movidos aquí y corridos recién ahora contra la rúbrica). Ambas confirman el comportamiento observado en la suite sintética: `manual_entrega_alumno` reproduce una falla real y aislada en C4 (0/16, prompt fuera de consigna), y `manual_entrega_simulada` reproduce la misma falla que `s3_falla_c3.txt` (CoT Zero-shot, techo 40%) mediante un texto redactado de forma completamente independiente — evidencia adicional de que la rúbrica discrimina esa falla de forma robusta y no por casualidad de una única muestra.
