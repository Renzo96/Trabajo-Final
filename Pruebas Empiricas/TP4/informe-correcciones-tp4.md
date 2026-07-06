# Informe de Correcciones — TP4: El Ecosistema Startup y el Modelo Lean

**Materia:** Organización Empresarial | **Carrera:** Tecnicatura Universitaria en Programación | **UTN - Facultad Regional Mendoza**
**Rúbrica aplicada:** `rubrica-tp4-ecosistema-startup.json` | **Puntaje máximo:** 100 puntos

---

## Resumen General

| Entrega | Escenario testeado | Nota Final | Estado |
|---|---|---|---|
| `s0_perfecta.txt` | Entrega perfecta (control) | **100 / 100** | ✅ Aprobado |
| `s1_falla_c1.txt` | Falla dirigida a C1 (Startup vs PyME) | **90 / 100** | ✅ Aprobado |
| `s2_falla_c2.txt` | Falla dirigida a C2 (Lean Startup / Smoke Test) | **85 / 100** | ✅ Aprobado |
| `s3_falla_c3.txt` | Falla dirigida a C3 (Test de la Madre) | **86 / 100** | ✅ Aprobado |
| `s4_falla_c4.txt` | Falla dirigida a C4 (LTV vs CAC / Churn) | **86 / 100** | ✅ Aprobado |
| `s5_falla_c5.txt` | Falla dirigida a C5 (Modelos de negocio) | **92 / 100** | ✅ Aprobado |
| `s6_parcial_c1.txt` | Falla parcial en C1 | **96 / 100** | ✅ Aprobado |
| `s7_parcial_c2.txt` | Falla parcial en C2 | **92 / 100** | ✅ Aprobado |
| `manual_entrega_tp4.txt` | Entrega manual (borrador, no sintética) | **94 / 100** | ✅ Aprobado |

La última fila no es parte de la suite sintética `sN_*` original: es una entrega manual previa (`borradores/entrega_tp4.txt`), redactada antes de que existiera el generador automático de sintéticos, corrida recién ahora contra la rúbrica con `simular_correccion.py` para incorporarla al mismo flujo ordenado del resto de los TPs.

Ninguna de las 8 entregas sintéticas activó la condición de desaprobación `CD1` (imágenes en el PDF) ni penalizaciones (el array `penalizaciones` de la rúbrica está vacío). Todos los campos `condicion_desaprobacion_aplicada` y `penalizaciones_aplicadas` de las correcciones son `null` / `[]`.

---

---

## Entrega `s0_perfecta.txt`

### Nota Final: 100 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Startup vs PyME | 20 | 20 | ✅ Completo |
| C2 | Lean Startup y MVP Smoke Test | 20 | 20 | ✅ Completo |
| C3 | Test de la Madre (Customer Discovery) | 20 | 20 | ✅ Completo |
| C4 | LTV vs CAC y Retención | 20 | 20 | ✅ Completo |
| C5 | Modelos de negocio en software | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Startup vs PyME (20/20)**
Aplica ambos conceptos al caso concreto de forma impecable. Explica la escalabilidad de la app (costo marginal → cero, crecimiento exponencial, sin hornos ni locales propios) y el crecimiento lineal de la panadería (límites físicos, geográficos, proporcionalidad de costos). Explica la incertidumbre extrema de la app (no se sabe si habrá demanda, si el modelo funcionará o si pagarán) y la certeza relativa de la panadería (modelo probado por siglos, clientes conocidos). Cubre todas las evidencias esperadas.

**C2 — Lean Startup y MVP Smoke Test (20/20)**
Explica Lean Startup mencionando el ciclo Construir-Medir-Aprender e identifica correctamente el error de los programadores (enamorarse de la idea, construir sin validar demanda). Define el MVP Smoke Test como landing page con CTA y lo aplica al caso concreto con un ejemplo claro (PetConnect, registro, publicidad en grupos de Facebook). La conexión entre teoría y caso es perfecta.

**C3 — Test de la Madre (20/20)**
Explica por qué las respuestas no sirven abordando tres razones válidas: sesgo de confirmación/cortesía social, predicciones futuras no confiables, y falta de información accionable. Propone preguntas alternativas basadas en comportamiento pasado (cómo consiguió resúmenes la última vez, cuánto tiempo perdió buscando apuntes, si pagó por material de estudio). Las preguntas se enfocan en hechos concretos y acciones reales.

**C4 — LTV vs CAC y Retención (20/20)**
Demuestra numéricamente que LTV ($2.000) < CAC ($5.000) y concluye correctamente que el negocio pierde $3.000 por cliente. Define Churn Rate y lo conecta causalmente con el LTV: un churn alto reduce la vida útil del cliente, lo que achata el LTV. Incluso calcula el punto de equilibrio (5 meses) donde el modelo se volvería viable, mostrando dominio completo de la relación entre métricas.

**C5 — Modelos de negocio en software (20/20)**
Elige Freemium (modelo válido visto en clase), lo explica correctamente (versión gratuita con limitaciones + planes pagos premium, motor de adquisición) y da ejemplos pertinentes (Spotify, Notion, Canva). El desafío técnico (feature flagging) es específico, pertinente al modelo elegido y está desarrollado con profundidad: middleware de autorización por plan, componentes frontend condicionales, esquemas de suscripción en BD, A/B testing de pricing, prevención de acceso no autorizado a endpoints.

---

---

## Entrega `s1_falla_c1.txt`

### Nota Final: 90 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Startup vs PyME | 20 | **10** | ⚠️ Parcial (techo por aplicación defectuosa) |
| C2 | Lean Startup y MVP Smoke Test | 20 | 20 | ✅ Completo |
| C3 | Test de la Madre (Customer Discovery) | 20 | 20 | ✅ Completo |
| C4 | LTV vs CAC y Retención | 20 | 20 | ✅ Completo |
| C5 | Modelos de negocio en software | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Startup vs PyME (10/20)** ⚠️
Define ambos conceptos y no confunde cuál es la startup y cuál la PyME, pero la aplicación al caso falla en puntos clave. En Escalabilidad, afirma que "los dos negocios pueden crecer" y que "la panadería puede abrir sucursales", lo cual contradice la idea de crecimiento lineal limitado por capacidad física de la panadería: la diferencia no es solo "más rápido por ser digital", sino que la app escala sin aumentar costos proporcionalmente. En Incertidumbre, afirma que "las dos tienen incertidumbre", cuando la panadería opera con certeza relativa porque su modelo de negocio es conocido y probado hace siglos. Al mezclar ambos lados del contraste sin diferenciarlos con claridad, la rúbrica aplica el techo correspondiente a "define los conceptos pero no los aplica correctamente al caso".

**C2 — Lean Startup y MVP Smoke Test (20/20)**
Explica el ciclo Construir-Medir-Aprender, identifica el error de los programadores ("enamorarse de la idea" sin validar demanda), define correctamente el MVP Smoke Test como landing page con llamado a la acción, y lo conecta con el caso concreto de PetConnect con nivel de detalle impecable, incluyendo métricas de conversión con anuncios de Instagram.

**C3 — Test de la Madre (20/20)**
Explica con claridad por qué las respuestas no sirven: sesgo de confirmación/social (cortesía), la gente es mala prediciendo su comportamiento futuro, y la pregunta gira alrededor de la idea en vez del problema. Propone dos preguntas alternativas basadas en comportamiento pasado concreto, ambas enfocadas en hechos reales.

**C4 — LTV vs CAC y Retención (20/20)**
Demuestra numéricamente que LTV ($2.000) < CAC ($5.000) con pérdida de $3.000 por cliente, y conecta claramente el Churn Rate con el problema: churn alto → vida útil corta → LTV bajo → imposible superar el CAC.

**C5 — Modelos de negocio en software (20/20)**
Elige Freemium, lo explica correctamente con el ejemplo de Spotify, e identifica un desafío técnico pertinente y específico: feature flagging para controlar funcionalidades por plan sin deployar código, verificado en cada request desde el backend.

### Observación General
El TP está muy bien resuelto en 4 de 5 preguntas. La Pregunta 1 (Startup vs PyME) es el punto débil: la distinción entre escalabilidad exponencial vs. lineal y entre incertidumbre extrema vs. certeza relativa no queda clara, y afirmar que ambos tipos de empresa tienen incertidumbre y pueden escalar diluye el contraste que la consigna pide explicar.

> **Hallazgo:** el nombre del archivo (`falla_c1`) sugiere una falla total del criterio, pero el texto entregado en realidad aplica ambos conceptos de forma confusa/contradictoria, no ausente. La rúbrica lo tipificó correctamente como el escalón "define pero no aplica bien" (techo 10/20) y no como fallo total (0/20). El descuento resultante (-10) es menor al `esperado: ~80` de `resumen.json`, pero el propio `resumen.json` marca `meta: ✅`, es decir, el comportamiento fue aceptado como correcto por el diseño de la prueba.

---

---

## Entrega `s2_falla_c2.txt`

### Nota Final: 85 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Startup vs PyME | 20 | 20 | ✅ Completo |
| C2 | Lean Startup y MVP Smoke Test | 20 | **5** | ❌ Insuficiente |
| C3 | Test de la Madre (Customer Discovery) | 20 | 20 | ✅ Completo |
| C4 | LTV vs CAC y Retención | 20 | 20 | ✅ Completo |
| C5 | Modelos de negocio en software | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Startup vs PyME (20/20)**
Aplica correctamente los conceptos de Escalabilidad e Incertidumbre al caso concreto de la app tipo Uber vs. la panadería de barrio, explicando el crecimiento exponencial de la app frente al crecimiento lineal de la panadería, y la incertidumbre extrema de la app frente a la certeza relativa del modelo de negocio tradicional.

**C2 — Lean Startup y MVP Smoke Test (5/20)** ❌
Respuesta superficial e incorrecta. Menciona conceptos genéricos ("fallar rápido", "versiones chiquitas") pero NO menciona el ciclo Construir-Medir-Aprender ni define qué es un MVP Smoke Test. En lugar de proponer una landing page con llamado a la acción para medir interés real, propone un grupo de Facebook o WhatsApp como validación, lo cual NO es un Smoke Test. No cumple con las evidencias esperadas de definir el concepto ni aplicarlo correctamente al caso de la red social de mascotas.

**C3 — Test de la Madre (20/20)**
Explica por qué las respuestas a "¿usarían una app para compartir resúmenes?" son inútiles (sesgo de confirmación, opiniones vs. hechos, predicciones futuras no confiables) y propone preguntas alternativas basadas en comportamiento pasado y hechos concretos.

**C4 — LTV vs CAC y Retención (20/20)**
Demuestra que LTV ($2.000) < CAC ($5.000), por lo tanto se pierde dinero con cada usuario, y conecta correctamente el Churn Rate alto (usuario se va a los 2 meses) con la reducción de la vida útil del cliente que impide que el LTV supere al CAC.

**C5 — Modelos de negocio en software (20/20)**
Elige un modelo de ingresos válido de los vistos en clase, lo explica correctamente y menciona un desafío técnico de programación o arquitectura pertinente y específico al modelo elegido.

### Observación General
La entrega demuestra buen dominio de la mayoría de los conceptos evaluados, pero C2 evidencia una comprensión superficial de Lean Startup que le costó 15 puntos. La confusión entre validación informal (grupos de redes sociales) y un Smoke Test metodológico (landing page) indica que no se internalizó la diferencia entre "preguntar" y "medir comportamiento real", que es justamente el corazón del método Lean. El resto de las respuestas son sólidas y bien fundamentadas.

---

---

## Entrega `s3_falla_c3.txt`

### Nota Final: 86 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Startup vs PyME | 20 | 20 | ✅ Completo |
| C2 | Lean Startup y MVP Smoke Test | 20 | 20 | ✅ Completo |
| C3 | Test de la Madre (Customer Discovery) | 20 | **6** | ❌ Insuficiente |
| C4 | LTV vs CAC y Retención | 20 | 20 | ✅ Completo |
| C5 | Modelos de negocio en software | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Startup vs PyME (20/20)**
Aplica correctamente ambos conceptos al caso. Escalabilidad: crecimiento exponencial de la app (costo marginal ≈ 0) frente al crecimiento lineal de la panadería. Incertidumbre: incertidumbre extrema de la app frente a la certeza relativa de la panadería. Respuesta completa y precisa.

**C2 — Lean Startup y MVP Smoke Test (20/20)**
Explica con precisión el ciclo Build-Measure-Learn, identifica correctamente el error de los programadores y describe el Smoke Test MVP (landing page con CTA sin producto real). Conecta ambos con un ejemplo concreto de landing page para la red social de mascotas midiendo registros.

**C3 — Test de la Madre (6/20)** ❌
La explicación de por qué "¿usarían?" no funciona es insuficiente: solo menciona que responden "por compromiso" (toca superficialmente el sesgo de cortesía) y agrega "cada persona tiene necesidades distintas", que no es un concepto del Test de la Madre. Omite explicar que las preguntas sobre intenciones futuras generan opiniones, no hechos. Además, las alternativas propuestas ("¿pagarían por una app así?" y "¿qué funcionalidades les gustaría?") son preguntas de intención futura y opinión, exactamente el tipo de pregunta que el Test de la Madre enseña a NO hacer — cae en la misma trampa que la pregunta original.

**C4 — LTV vs CAC y Retención (20/20)**
Calcula correctamente LTV ($2.000) < CAC ($5.000), pérdida de $3.000 por cliente, concluye que el modelo quiebra, y explica con claridad la relación con el Churn Rate, proponiendo correctamente que la solución de fondo es reducir el Churn para que el LTV supere al CAC.

**C5 — Modelos de negocio en software (20/20)**
Elige SaaS, lo explica correctamente (software en la nube con suscripción recurrente) con ejemplos pertinentes. El desafío técnico es específico y relevante: facturación recurrente con control de acceso por tiers, manejo de pagos fallidos, upgrades/downgrades con prorrateo, integración con pasarela de pagos.

### Observación General
El estudiante demuestra un manejo sólido de escalabilidad, incertidumbre, Lean Startup, métricas LTV/CAC y modelos de negocio SaaS en cuatro de los cinco criterios. Sin embargo, en el Test de la Madre (C3) comete un error conceptual crítico: las alternativas propuestas caen exactamente en la misma trampa que la pregunta original, revelando que no se internalizó la distinción entre hechos del pasado y opiniones sobre el futuro, base del Customer Discovery.

---

---

## Entrega `s4_falla_c4.txt`

### Nota Final: 86 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Startup vs PyME | 20 | 20 | ✅ Completo |
| C2 | Lean Startup y MVP Smoke Test | 20 | 20 | ✅ Completo |
| C3 | Test de la Madre (Customer Discovery) | 20 | 20 | ✅ Completo |
| C4 | LTV vs CAC y Retención | 20 | **6** | ❌ Insuficiente |
| C5 | Modelos de negocio en software | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Startup vs PyME (20/20)**
Explica y aplica correctamente ambos conceptos al caso concreto de la panadería de barrio vs. la app tipo Uber, con aplicación directa y precisa.

**C2 — Lean Startup y MVP Smoke Test (20/20)**
Explica correctamente Lean Startup (ciclo Construir-Medir-Aprender, error de enamorarse de la idea) y describe con precisión el MVP Smoke Test, conectándolo con el caso concreto (landing page, medir registros, ahorro de dos años de desarrollo).

**C3 — Test de la Madre (20/20)**
Explica por qué las respuestas no sirven (sesgo social/de confirmación, predicciones futuras) y propone preguntas alternativas específicas y accionables basadas en comportamiento pasado.

**C4 — LTV vs CAC y Retención (6/20)** ❌
Identifica los números (LTV = $2.000, CAC = $5.000), pero NO cumple con la consigna. En lugar de explicar por qué el modelo está destinado a quebrar, argumenta lo contrario: dice que "el problema no es tan grave", que "es cuestión de timing" y que se puede revertir si los usuarios se quedan más. La pregunta pide explicar POR QUÉ quiebra, no argumentar que no lo hace. Además, nunca menciona el concepto de Churn Rate ni lo relaciona con el LTV, parte central de la pregunta. El techo por no conectar con Churn Rate es 12/20, y la conclusión incorrecta deja el puntaje en la franja baja de ese techo.

**C5 — Modelos de negocio en software (20/20)**
Elige Freemium, lo explica correctamente con ejemplos pertinentes (Spotify, Evernote). El desafío técnico (feature flagging a nivel de backend, autorización por request, manejo de transiciones entre planes) es específico y bien desarrollado.

### Observación General
El alumno demuestra comprensión sólida y bien articulada de Startup vs PyME, Lean Startup, Test de la Madre y modelos de negocio (C1, C2, C3, C5). Sin embargo, en C4 no responde lo que se le pide: en lugar de explicar por qué el modelo está destinado a quebrar (LTV < CAC) y conectar con Churn Rate, argumenta lo contrario y omite completamente el concepto de retención, lo que le cuesta casi todo el puntaje de ese criterio.

---

---

## Entrega `s5_falla_c5.txt`

### Nota Final: 92 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Startup vs PyME | 20 | 20 | ✅ Completo |
| C2 | Lean Startup y MVP Smoke Test | 20 | 20 | ✅ Completo |
| C3 | Test de la Madre (Customer Discovery) | 20 | 20 | ✅ Completo |
| C4 | LTV vs CAC y Retención | 20 | 20 | ✅ Completo |
| C5 | Modelos de negocio en software | 20 | **12** | ⚠️ Parcial (desafío técnico genérico) |

### Feedback por criterio

**C1 — Startup vs PyME (20/20)**
Aplica correctamente ambos conceptos al caso concreto: escalabilidad (costo marginal → cero vs. límites geográficos y físicos) e incertidumbre (extrema en la app vs. certeza relativa en la panadería, con demanda diaria conocida).

**C2 — Lean Startup y MVP Smoke Test (20/20)**
Explica el ciclo Construir-Medir-Aprender e identifica el error clásico de enamorarse de la solución sin validar el problema. Describe correctamente el MVP Smoke Test como landing page con CTA y lo conecta al caso de la red social de mascotas.

**C3 — Test de la Madre (20/20)**
Explica con claridad por qué las respuestas no sirven (sesgo de confirmación, predicciones futuras poco fiables) y propone alternativas excelentes basadas en comportamiento pasado.

**C4 — LTV vs CAC y Retención (20/20)**
Demuestra numéricamente que LTV ($2.000) < CAC ($5.000), pérdida de $3.000 por cliente, y conecta explícitamente el Churn Rate con la vida útil y el LTV, calculando incluso el punto de equilibrio (5+ meses de retención).

**C5 — Modelos de negocio en software (12/20)** ⚠️
Elige SaaS (modelo válido) y lo explica correctamente (suscripción, cloud-hosted, ejemplo Netflix). Sin embargo, el desafío técnico mencionado —alta disponibilidad 24/7, redundancia, backups— es genérico y aplica a prácticamente cualquier servicio online, no es específico del modelo SaaS. Desafíos verdaderamente pertinentes serían facturación recurrente, control de acceso por tiers o multi-tenancy. Por ser un desafío genérico, se aplica el techo de 12/20 según la instrucción de puntuación del criterio.

### Observación General
Comprensión profunda de los conceptos del ecosistema startup, Lean Startup y métricas de negocio. Las respuestas de C1 a C4 son impecables. El criterio C5 es el punto débil porque el desafío técnico elegido (alta disponibilidad) es genérico y no exclusivo del modelo SaaS; la explicación del modelo en sí es correcta, pero el desafío no alcanza la especificidad que la rúbrica pide para el puntaje completo.

> **Hallazgo:** el descuento real (-8, techo 12/20) es sensiblemente menor al `esperado: ~80` estimado en `resumen.json`. La rúbrica no trata un desafío técnico "genérico pero presente" igual que una ausencia total de desafío (que tendría techo 10/20) — el criterio de puntuación distingue matices que un descuento plano de -20 no habría capturado. El descuento sigue concentrado correctamente en C5, solo que es más moderado de lo que el nombre del archivo sugiere.

---

---

## Entrega `s6_parcial_c1.txt`

### Nota Final: 96 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Startup vs PyME | 20 | **16** | ⚠️ Parcial (falta contraste de incertidumbre) |
| C2 | Lean Startup y MVP Smoke Test | 20 | 20 | ✅ Completo |
| C3 | Test de la Madre (Customer Discovery) | 20 | 20 | ✅ Completo |
| C4 | LTV vs CAC y Retención | 20 | 20 | ✅ Completo |
| C5 | Modelos de negocio en software | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Startup vs PyME (16/20)** ⚠️
Excelente aplicación del concepto de escalabilidad: crecimiento exponencial de la app (sin costos proporcionales) versus crecimiento lineal de la panadería (limitada por local, empleados y geografía). En incertidumbre, explica bien que la startup opera sin saber si el modelo funcionará, pero falta el contraste explícito del lado de la panadería: no menciona que la panadería opera con certeza relativa porque su modelo de negocio es conocido y probado. La incertidumbre queda "sin el espejo del negocio tradicional".

**C2 — Lean Startup y MVP Smoke Test (20/20)**
Respuesta completa y precisa: ciclo Construir-Medir-Aprender, error de los programadores, definición del Smoke Test y conexión con el ejemplo concreto (PetConnect, "Sé de los primeros, registrate acá").

**C3 — Test de la Madre (20/20)**
Sólida comprensión: sesgo social/de confirmación, intenciones futuras que no predicen comportamiento real, y tres preguntas alternativas excelentes basadas en comportamiento pasado.

**C4 — LTV vs CAC y Retención (20/20)**
Respuesta impecable: cálculo correcto de LTV, demostración de que LTV < CAC, definición de Churn Rate y conexión con la vida útil del cliente, incluyendo las dos vías de solución (bajar CAC o mejorar retención).

**C5 — Modelos de negocio en software (20/20)**
Elige SaaS correctamente, lo explica con precisión, y el desafío técnico (facturación recurrente, control de acceso por tiers, integración con procesadores de pago, manejo de cobros fallidos) es pertinente y detallado.

### Observación General
Trabajo muy sólido, con comprensión real de los conceptos (no solo definiciones de memoria) en C2 a C5. El único punto débil menor está en C1, donde el contraste de incertidumbre queda incompleto del lado de la panadería, lo que activa un descuento parcial de 4 puntos sobre ese criterio.

---

---

## Entrega `s7_parcial_c2.txt`

### Nota Final: 92 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Startup vs PyME | 20 | 20 | ✅ Completo |
| C2 | Lean Startup y MVP Smoke Test | 20 | **12** | ⚠️ Parcial (no describe el Smoke Test) |
| C3 | Test de la Madre (Customer Discovery) | 20 | 20 | ✅ Completo |
| C4 | LTV vs CAC y Retención | 20 | 20 | ✅ Completo |
| C5 | Modelos de negocio en software | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Startup vs PyME (20/20)**
Explica correctamente ambos conceptos aplicados al caso concreto, identificando correctamente cuál es la startup y cuál la PyME. Todas las evidencias esperadas están cubiertas.

**C2 — Lean Startup y MVP Smoke Test (12/20)** ⚠️
Explica correctamente la metodología Lean Startup (validar antes de construir, error de enamorarse de la idea), pero NO describe el concepto específico de MVP Smoke Test: no menciona landing page, llamado a la acción ni cómo medir interés real antes de desarrollar. Habla genéricamente de "un prototipo chiquito" sin definir ni aplicar el Smoke Test al caso concreto. Según la rúbrica, explicar Lean Startup sin mencionar el Smoke Test implica techo 12/20; se asigna el máximo permitido por el techo dado que la explicación de Lean Startup es sólida.

**C3 — Test de la Madre (20/20)**
Explica con claridad las tres razones por las que las respuestas no sirven y propone tres preguntas alternativas excelentes basadas en comportamiento pasado concreto.

**C4 — LTV vs CAC y Retención (20/20)**
Calcula correctamente LTV = $2.000, demuestra LTV < CAC, relaciona el Churn Rate con el problema y menciona las dos palancas para arreglar el modelo (bajar CAC o aumentar retención).

**C5 — Modelos de negocio en software (20/20)**
Elige SaaS, lo explica correctamente con ejemplos pertinentes (Netflix, Spotify, Google Workspace). El desafío técnico es específico y bien desarrollado: facturación recurrente, control de acceso por tiers, manejo de fallos de pago, upgrades/downgrades con prorrateo.

### Observación General
El alumno demuestra un dominio sólido de los conceptos centrales de la materia en cuatro de los cinco criterios. La única debilidad está en la pregunta 2, donde explica correctamente Lean Startup pero omite describir el concepto específico de MVP Smoke Test y su aplicación concreta al caso, lo que activa el techo de 12/20 en ese criterio.

---

## Entrega `manual_entrega_tp4.txt` (borrador manual)

### Nota Final: 94 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Startup vs PyME | 20 | 20 | ✅ Completo |
| C2 | Lean Startup y MVP Smoke Test | 20 | **14** | ⚠️ Parcial (Smoke Test poco preciso) |
| C3 | Test de la Madre (Customer Discovery) | 20 | 20 | ✅ Completo |
| C4 | LTV vs CAC y Retención | 20 | 20 | ✅ Completo |
| C5 | Modelos de negocio en software | 20 | 20 | ✅ Completo |

### Feedback por criterio

**C1 — Startup vs PyME (20/20)**
Distingue con claridad el crecimiento exponencial de la app frente al lineal de la panadería (limitada por harina, hornos, empleados y local), y la incertidumbre de si la app tendrá demanda frente al modelo validado de la panadería. No confunde los roles de startup y PyME.

**C2 — Lean Startup y MVP Smoke Test (14/20)** ⚠️
Explica bien la idea central de Lean Startup y conecta correctamente con el error de construir sin validar interés real, pero en vez de describir el Smoke Test como landing page con llamado a la acción (registro, email o pre-orden), propone una página de Facebook o grupo de WhatsApp — una aproximación válida pero que no captura la mecánica concreta de medir intención de registro/pago que pide la consigna.

**C3 — Test de la Madre (20/20)**
Identifica el sesgo social/cortesía hacia conocidos y distingue opiniones/predicciones futuras de hechos reales. Propone preguntas alternativas centradas en comportamiento pasado y concreto.

**C4 — LTV vs CAC y Retención (20/20)**
Calcula correctamente LTV = $2.000 y CAC = $5.000, concluye que la empresa pierde $3.000 por cliente, y relaciona el Churn Rate alto con la reducción del LTV.

**C5 — Modelos de negocio en software (20/20)**
Elige Freemium y lo explica correctamente con ejemplos reales (Spotify, Dropbox, Notion). El desafío técnico mencionado (feature flagging con consideraciones de arquitectura concretas: permisos en backend, riesgo de fuga de features premium, trade-off tiempo real vs. cacheo) es específico y pertinente.

### Observación General
Entrega manual real (no generada sintéticamente) con la misma falla exacta que se observa en `s7_parcial_c2.txt`: Lean Startup bien explicado, pero el Smoke Test resuelto con una aproximación genérica en vez de la mecánica específica de landing page + CTA. Confirma, con un texto redactado de forma completamente independiente, que la rúbrica discrimina esa falla de manera consistente.

---

## Resumen de la Rúbrica — Comportamiento observado

| Escenario de prueba | Comportamiento esperado | Resultado |
|---|---|---|
| Entrega completa y correcta (s0) | 100/100 sin penalizaciones | ✅ Correcto — 100/100 |
| Falla total en C1 (s1) | Descuento concentrado en C1 | ✅ Correcto — descuento concentrado en C1 (10/20); nota final 90/100 |
| Falla total en C2 (s2) | Descuento concentrado en C2 | ✅ Correcto — descuento concentrado en C2 (5/20); nota final 85/100 |
| Falla total en C3 (s3) | Descuento concentrado en C3 | ✅ Correcto — descuento concentrado en C3 (6/20); nota final 86/100 |
| Falla total en C4 (s4) | Descuento concentrado en C4 | ✅ Correcto — descuento concentrado en C4 (6/20); nota final 86/100 |
| Falla total en C5 (s5) | Descuento concentrado en C5 | ✅ Correcto — descuento concentrado en C5 (12/20); nota final 92/100 |
| Falla parcial en C1 (s6) | Descuento leve concentrado en C1 | ✅ Correcto — descuento concentrado en C1 (16/20); nota final 96/100 |
| Falla parcial en C2 (s7) | Descuento leve concentrado en C2 | ✅ Correcto — descuento concentrado en C2 (12/20); nota final 92/100 |

### Discriminación por criterio: correcta en las 8 entregas
En ningún caso el descuento recayó sobre un criterio distinto al que el nombre del archivo indicaba como objetivo de la prueba (`sN_falla_cX` → el criterio CX es siempre el único o el más afectado). Los criterios restantes de cada entrega se mantuvieron en 20/20, confirmando que los descuentos son aislados y no "contaminan" la evaluación de otros criterios — mismo comportamiento de independencia observado en el análisis de TP1.

### Hallazgo 1 — Los "techos" de las `instrucciones_puntuacion` producen descuentos más moderados que la aproximación gruesa de `resumen.json`
`resumen.json` estima informalmente un "esperado" de ~80 para las fallas totales (`s1`–`s5`) y ~90 para las parciales (`s6`, `s7`), asumiendo implícitamente que "fallar" un criterio equivale a perder los 20 puntos completos. En la práctica, la rúbrica define escalones de puntuación parcial muy específicos por criterio (ej. C1: techo 10/20 si usa un solo concepto; C2: techo 12/20 si no describe el Smoke Test; C5: techo 12/20 si el desafío técnico es genérico), y las entregas sintéticas de "falla" en general no dejan el criterio en blanco sino que entregan una respuesta incompleta o parcialmente incorrecta — que la rúbrica puntúa según ese escalón intermedio, no en 0. Esto explica por qué las notas reales (85–96) quedan sistemáticamente por encima del "esperado" aproximado (80–90). El propio `resumen.json` marca `meta: ✅` en los 8 casos, por lo que esto no es un fallo de la rúbrica sino evidencia de que su granularidad de puntuación parcial es más fina que la heurística usada para diseñar el "esperado" del test.

### Hallazgo 2 — La condición de desaprobación `CD1` nunca fue ejercitada
La rúbrica define una única condición de desaprobación (`CD1`: PDF con imágenes o capturas en lugar de texto plano → nota máxima 0), pero ninguna de las 8 entregas sintéticas la activa (`condicion_desaprobacion_aplicada` es `null` en las 8 correcciones). A diferencia de TP1 —que sí tenía un caso dedicado a probar su condición de desaprobación (CD2)— la batería de TP4 cubre los 5 criterios de contenido pero deja sin cobertura de prueba el único gate de formato de la rúbrica.

### Conclusión
La rúbrica de TP4 discrimina correctamente entre los 5 criterios de contenido: cada entrega "falla" o "parcial" concentra su descuento exactamente en el criterio que fue diseñado para fallar, sin fugas hacia otros criterios. El punto de atención no es un error de discriminación sino de calibración de expectativas: el `resumen.json` subestima el puntaje resultante porque no anticipa el uso de los techos parciales definidos en `instrucciones_puntuacion`, y falta un caso de prueba que ejercite la condición de desaprobación `CD1`.

**Entrega manual adicional:** `manual_entrega_tp4.txt` era un borrador previo al pipeline de sintéticos (antes en `borradores/`, movido aquí y corrido recién ahora contra la rúbrica). Reproduce, en un texto redactado de forma completamente independiente, la misma falla parcial en C2 observada en `s7_parcial_c2.txt` (Smoke Test explicado de forma genérica en vez de la mecánica específica de landing page + CTA) — evidencia adicional de que esa falla se discrimina de forma robusta y no por casualidad de una única muestra.
