# Informe de Correcciones — TP6: Automatización de Flujos con n8n

**Materia:** Organización Empresarial | **Carrera:** TUPaD | **UTN - Facultad Regional Mendoza**
**Rúbrica aplicada:** `rubrica-tp6-n8n.json` | **Puntaje máximo:** 100 puntos

---

## Resumen General

| Alumno/a | Archivo entregado | Nota Final | Estado |
|---|---|---|---|
| Sofía Vargas | `s0_perfecta.txt` | **100 / 100** | ✅ Aprobado |
| Emiliano Castro | `s1_falla_c7.txt` | **91 / 100** | ✅ Aprobado |
| Valentina Herrera | `s2_sin_json_cd2.txt` | **30 / 100** | ⚠️ Condición de desaprobación activa (CD2) |

---

---

## Alumno/a: Sofía Vargas — `s0_perfecta.txt`

### Nota Final: 100 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Formato y condiciones de entrega | 10 | 10 | ✅ Completo |
| C2 | Valor comercial del Low-Code | 12 | 12 | ✅ Completo |
| C3 | Triggers vs Acciones | 15 | 15 | ✅ Completo |
| C4 | Gestión de secretos | 13 | 13 | ✅ Completo |
| C5 | Nodo Edit Fields (Set) | 10 | 10 | ✅ Completo |
| C6 | Schedule Trigger configurado | 10 | 10 | ✅ Completo |
| C7 | Edit Fields con campo `mensaje_recordatorio` | 15 | 15 | ✅ Completo |
| C8 | Nodo mensajería con expresión mapeada | 15 | 15 | ✅ Completo |

### Feedback por criterio

**C1 — Formato y condiciones de entrega (10/10)**
Entrega impecable. El `.zip` contiene el PDF de respuestas (solo texto, sin imágenes, con las cuatro consignas teóricas respondidas) y el archivo `tp-n8n-vargas-sofia.json`. El JSON tiene estructura de workflow de n8n reconocible con los campos `nodes`, `connections`, `name` y `meta`. El nombre del archivo sigue la convención `tp-n8n-apellido-nombre.json`.

**C2 — Valor comercial del Low-Code (12/12)**
Respuesta que va claramente más allá de "es más fácil". Identifica múltiples beneficios comerciales concretos: reducción del tiempo de desarrollo de integraciones (de días a horas), menor costo de mantenimiento porque los conectores ya vienen probados por la comunidad, y la posibilidad de que perfiles no técnicos (marketing, operaciones) armen o ajusten flujos sin depender de un desarrollador. Contextualiza bien el valor en términos de productividad y ahorro para la empresa.

**C3 — Triggers vs Acciones (15/15)**
Diferenciación correcta: el Nodo Trigger define el "cuándo" (dispara el flujo), el Nodo de Acción ejecuta una tarea concreta en respuesta. Los ejemplos son válidos y pertinentes: Schedule Trigger para el reporte de ventas de los lunes a la mañana; Webhook para reaccionar cuando alguien completa un formulario web. Ambos subcriterios (C3.1 y C3.2) cumplidos.

**C4 — Gestión de secretos (13/13)**
Respuesta sólida con más de dos motivos de seguridad. Menciona: (1) la exposición visual de la contraseña a cualquiera que acceda al workflow o reciba una copia del `.json` exportado; (2) la posibilidad de rotar o revocar una clave sin editar cada nodo; (3) la reutilización del equipo sin que nadie tenga que conocer la contraseña real. La mención específica al riesgo en los exports `.json` es un punto de precisión técnica destacable.

**C5 — Nodo Edit Fields (10/10)**
Explica con claridad que el nodo permite crear, renombrar o filtrar campos del JSON que viaja entre nodos. Contextualiza correctamente: los datos que llegan de una plataforma suelen tener campos con nombres raros o información de más, y el nodo los reestructura para que el siguiente nodo reciba exactamente lo que espera. Ambas evidencias de C5.1 cumplidas.

**C6 — Schedule Trigger configurado (10/10)**
El JSON contiene el nodo `n8n-nodes-base.scheduleTrigger` con la configuración correcta: `field: "weeks"`, `triggerAtDay: [1]` (lunes), `triggerAtHour: 8`, `triggerAtMinute: 0`. Configuración exacta según la consigna.

**C7 — Edit Fields con campo `mensaje_recordatorio` (15/15)**
El nodo `n8n-nodes-base.set` está presente y conectado al Schedule Trigger en el objeto `connections`. Define un campo con el nombre exacto `"mensaje_recordatorio"`, tipo `"string"` y un valor no vacío con mensaje motivacional. Los tres puntos de C7.1 cumplidos.

**C8 — Nodo mensajería con expresión mapeada (15/15)**
El nodo Telegram está presente, conectado a la salida del Edit Fields en el objeto `connections`. El campo `text` usa la expresión dinámica `"={{ $json.mensaje_recordatorio }}"`, que referencia exactamente el campo creado en el nodo anterior. No se usó texto estático. Las credenciales no están configuradas, pero la consigna aclara explícitamente que no es obligatorio para la nota completa.

---

---

## Alumno: Emiliano Castro — `s1_falla_c7.txt`

### Nota Final: 91 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Formato y condiciones de entrega | 10 | 10 | ✅ Completo |
| C2 | Valor comercial del Low-Code | 12 | 12 | ✅ Completo |
| C3 | Triggers vs Acciones | 15 | 15 | ✅ Completo |
| C4 | Gestión de secretos | 13 | 13 | ✅ Completo |
| C5 | Nodo Edit Fields (Set) | 10 | 10 | ✅ Completo |
| C6 | Schedule Trigger configurado | 10 | 10 | ✅ Completo |
| C7 | Edit Fields con campo `mensaje_recordatorio` | 15 | **10** | ⚠️ Parcial — nombre de campo incorrecto |
| C8 | Nodo mensajería con expresión mapeada | 15 | **11** | ⚠️ Parcial — expresión referencia campo incorrecto |

### Feedback por criterio

**C1 — Formato y condiciones de entrega (10/10)**
Formato correcto. `.zip` válido con PDF (solo texto, cuatro consignas respondidas) y archivo `.json` con estructura de workflow de n8n reconocible. Sin observaciones.

**C2 — Valor comercial del Low-Code (12/12)**
Respuesta concisa pero suficiente. Menciona velocidad (integraciones que llevan días se arman en minutos), reducción del costo de desarrollo y de mantenimiento de conexiones rutinarias. Contextualiza en términos de productividad. Cumple el criterio.

**C3 — Triggers vs Acciones (15/15)**
Diferenciación correcta entre Trigger (define cuándo arranca el flujo) y Acción (ejecuta una tarea en respuesta). Ejemplos válidos: Schedule para reporte semanal, Webhook para formulario web. Puntaje completo.

**C4 — Gestión de secretos (13/13)**
Menciona la exposición de la contraseña a quien acceda al workflow y la reutilización del equipo sin compartir contraseñas. Dos motivos de seguridad presentes. Puntaje completo.

**C5 — Nodo Edit Fields (10/10)**
Correcta. Explica creación y renombrado de campos, y contextualiza con datos desordenados que llegan de plataformas externas.

**C6 — Schedule Trigger configurado (10/10)**
El nodo `n8n-nodes-base.scheduleTrigger` en el JSON tiene la configuración correcta: `triggerAtDay: [1]` (lunes), `triggerAtHour: 8`, `triggerAtMinute: 0`. Sin observaciones.

**C7 — Edit Fields con campo `mensaje_recordatorio` (10/15)** ⚠️
Aquí está el primer descuento. El nodo `n8n-nodes-base.set` existe y está correctamente conectado al Schedule Trigger. El valor asignado no está vacío. Sin embargo, el campo fue nombrado **`"mensaje"`** en lugar de **`"mensaje_recordatorio"`** como exige la consigna y la rúbrica.

La consigna es explícita: *"un campo de tipo String llamado exactamente 'mensaje_recordatorio'"*. El nombre es incorrecto. Según las instrucciones de puntuación: *"Nodo presente pero nombre del campo incorrecto (ej: 'mensaje') → -5"*. Descuento aplicado: **-5 puntos**. C7 = 15 - 5 = **10/15**.

**C8 — Nodo mensajería con expresión mapeada (11/15)** ⚠️
El nodo Telegram está presente y correctamente conectado a la salida del Edit Fields. El campo `text` usa una expresión dinámica (no texto estático), lo cual es correcto en su forma. Sin embargo, la expresión es `"={{ $json.mensaje }}"` en lugar de `"={{ $json.mensaje_recordatorio }}"`.

La expresión referencia el campo erróneo (`mensaje`) porque ese fue el nombre que se le asignó en el nodo Edit Fields. La consecuencia es doble: el campo no tiene el nombre correcto (C7) y la expresión tampoco referencia la variable correcta (C8). Son dos criterios afectados por el mismo error de nomenclatura.

Según las instrucciones: *"Nodo presente con expresión incorrecta → -4"*. Descuento aplicado: **-4 puntos**. C8 = 15 - 4 = **11/15**.

### Observación General
La entrega muestra dominio técnico claro del ecosistema n8n. El workflow está bien estructurado, las conexiones son correctas y la lógica del flujo es la adecuada. El único problema es de nomenclatura: usar `"mensaje"` en lugar del nombre exacto `"mensaje_recordatorio"` que exige la consigna. Ese error de precisión en el nombre del campo se propaga a dos criterios (C7 y C8), sumando un descuento total de 9 puntos. En un contexto real de producción, este error haría que la expresión del nodo Telegram devuelva `undefined` porque el campo al que referencia no existe con ese nombre.

---

---

## Alumno/a: Valentina Herrera — `s2_sin_json_cd2.txt`

### ⚠️ Condición de Desaprobación Activada: CD2

> **CD2:** No se incluye el archivo `.json` exportado desde n8n en el `.zip` entregado → `nota_maxima: 30`

La rúbrica establece que la ausencia del workflow `.json` impone un techo máximo de **30 puntos**, independientemente del puntaje acumulado en los criterios teóricos.

### Nota Final: 30 / 100 (techo por CD2)

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Formato y condiciones de entrega | 10 | **5** | ⚠️ Parcial (-5 por falta de .json) |
| C2 | Valor comercial del Low-Code | 12 | 12 | ✅ Completo |
| C3 | Triggers vs Acciones | 15 | 15 | ✅ Completo |
| C4 | Gestión de secretos | 13 | 13 | ✅ Completo |
| C5 | Nodo Edit Fields (Set) | 10 | 10 | ✅ Completo |
| C6 | Schedule Trigger configurado | 10 | **0** | ❌ Sin evidencia verificable |
| C7 | Edit Fields con `mensaje_recordatorio` | 15 | **0** | ❌ Sin evidencia verificable |
| C8 | Nodo mensajería con expresión mapeada | 15 | **0** | ❌ Sin evidencia verificable |
| **Subtotal bruto** | | 100 | **55** | |
| **Techo CD2** | | | **→ 30** | ⚠️ |

### Feedback por criterio

**C1 — Formato y condiciones de entrega (5/10)**
El `.zip` contiene el PDF de respuestas teóricas (solo texto, sin imágenes, con las cuatro consignas respondidas). Sin embargo, el archivo `.json` exportado desde n8n está completamente ausente. Las instrucciones de C1 establecen: *"Si falta el .json de n8n → -5 puntos"*. C1 = 10 - 5 = **5/10**.

**C2 — Valor comercial del Low-Code (12/12)**
Respuesta correcta. Menciona velocidad (días a minutos), reducción del costo de desarrollo y mantenimiento. Contextualiza en términos de productividad y ahorro. Cumple el criterio.

**C3 — Triggers vs Acciones (15/15)**
Diferenciación correcta entre Trigger y Acción. Ejemplos válidos: Schedule para reporte semanal, Webhook para formulario web completado. Puntaje completo.

**C4 — Gestión de secretos (13/13)**
Menciona la exposición de la contraseña en el workflow o su exportación y la reutilización sin compartir contraseñas. Dos motivos de seguridad presentes. Puntaje completo.

**C5 — Nodo Edit Fields (10/10)**
Explica creación y renombrado de campos, y contextualiza con datos desordenados de plataformas externas que se transforman para el nodo siguiente. Cumple el criterio.

**C6 — Schedule Trigger configurado (0/10)** ❌
Sin el archivo `.json` del workflow no existe ninguna evidencia verificable de la existencia ni la configuración del Schedule Trigger. No hay nodo que auditar.

**C7 — Edit Fields con campo `mensaje_recordatorio` (0/15)** ❌
Sin el `.json` no hay nodo Edit Fields que verificar. No es posible comprobar el nombre del campo (`mensaje_recordatorio`), su tipo ni su valor. Lo que el alumno afirme en el PDF sobre lo que hizo no reemplaza la evidencia del workflow exportado.

**C8 — Nodo mensajería con expresión mapeada (0/15)** ❌
Sin el `.json` no hay nodo de mensajería que auditar. No existe forma de verificar la expresión `{{ $json.mensaje_recordatorio }}` ni la conexión de los nodos.

### Observación General
La parte teórica (C2 a C5) está resuelta correctamente y alcanza 50 de los 55 puntos brutos acumulados. Sin embargo, la ausencia del archivo `.json` hace que toda la parte práctica (C6, C7, C8 — 40 puntos en total) sea imposible de corregir. El corrector no puede evaluar un workflow que no existe en la entrega. Adicionalmente, la condición de desaprobación CD2 limita la nota máxima a 30 puntos. Esta situación es análoga a la de TP1 sin la carpeta `.git`: comprensión teórica presente pero sin el artefacto práctico que la respalda. La entrega evidencia que la alumna comprende los conceptos del TP pero no adjuntó el producto principal de la parte práctica.

---

## Resumen de la Rúbrica — Comportamiento observado

| Escenario de prueba | Comportamiento esperado | Resultado |
|---|---|---|
| Entrega completa y correcta | 100/100 sin penalizaciones | ✅ Correcto — Sofía Vargas: 100/100 |
| Nombre de campo incorrecto en C7 (cascada a C8) | -5 en C7, -4 en C8 → descuento total de 9 puntos | ✅ Correcto — Emiliano Castro: 91/100 |
| Ausencia del .json (CD2) | Techo de 30 puntos, práctica anulada | ✅ Correcto — Valentina Herrera: 30/100 |

### Observación sobre la propagación del error en C7→C8

El caso de Emiliano Castro expone un comportamiento interesante de la rúbrica: un error de nomenclatura en C7 (nombre de campo incorrecto) se propaga automáticamente a C8 (expresión que referencia ese campo). La rúbrica penaliza ambos criterios por separado, lo cual es técnicamente correcto porque son defectos independientes: uno en la definición del campo, otro en la referencia a ese campo. Sin embargo, la causa raíz es única (el nombre `"mensaje"` en lugar de `"mensaje_recordatorio"`). Este comportamiento es deliberado en el diseño de la rúbrica: C7 y C8 evalúan componentes distintos del workflow, y ambos tienen evidencias propias que verificar.
