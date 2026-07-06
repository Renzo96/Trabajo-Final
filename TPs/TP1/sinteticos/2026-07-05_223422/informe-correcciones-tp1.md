# Informe de Correcciones — TP1: Primeros Pasos con Git

**Materia:** Organización Empresarial | **Carrera:** TUPaD | **UTN - Facultad Regional Mendoza**
**Rúbrica aplicada:** `rubrica-tp1-git.json` | **Puntaje máximo:** 100 puntos

---

## Resumen General

| Alumno/a | Archivo entregado | Nota Final | Estado |
|---|---|---|---|
| Lucas Fernández | `s0_perfecta.txt` | **100 / 100** | ✅ Aprobado |
| Agustín Morales | `s1_falla_c2.txt` | **90 / 100** | ✅ Aprobado |
| Camila Suárez | `s2_sin_git_cd2.txt` | **30 / 100** | ⚠️ Condición de desaprobación activa (CD2) |

---

---

## Alumno: Lucas Fernández — `s0_perfecta.txt`

### Nota Final: 100 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Formato y condiciones de entrega | 15 | 15 | ✅ Completo |
| C2 | Versionado manual vs Git | 10 | 10 | ✅ Completo |
| C3 | Estado Staged | 10 | 10 | ✅ Completo |
| C4 | .gitignore | 8 | 8 | ✅ Completo |
| C5 | Ramas (branches) | 7 | 7 | ✅ Completo |
| C6 | Init y configuración | 10 | 10 | ✅ Completo |
| C7 | Archivos iniciales y primer commit | 15 | 15 | ✅ Completo |
| C8 | Rama de desarrollo y segundo commit | 15 | 15 | ✅ Completo |
| C9 | Merge a main | 10 | 10 | ✅ Completo |

### Feedback por criterio

**C1 — Formato y condiciones de entrega (15/15)**
La entrega cumple con todos los requisitos formales. El `.zip` contiene correctamente el PDF de respuestas y la carpeta `.git` con su estructura completa: `HEAD`, `objects/`, `refs/` y los directorios de ramas. No se detectaron imágenes en el PDF. Entrega impecable en este aspecto.

**C2 — Versionado manual vs Git (10/10)**
Respuesta sólida y argumentada. El alumno identifica tres riesgos concretos: pérdida de claridad sobre cuál es la versión vigente, imposibilidad de fusionar cambios de múltiples personas, y pérdida irreversible ante un error humano (borrado accidental). La redacción es propia y contextualizada. Supera el mínimo exigido de un riesgo.

**C3 — Estado Staged (10/10)**
Explicación muy clara con una analogía original y eficaz (la caja de mudanza). Diferencia correctamente los tres estados: Modificado, Staged y Confirmado. La analogía del `git add` como "meter objetos en la caja" y el `git commit` como "cerrarla con cinta" demuestra comprensión genuina del concepto.

**C4 — .gitignore (8/8)**
Explica correctamente la función del `.gitignore` y da un ejemplo concreto y pertinente: el archivo `config-secreta.env` con contraseñas o claves API. Además menciona el riesgo real de que ese archivo quede expuesto en un repositorio público como GitHub.

**C5 — Ramas (7/7)**
Respuesta correcta y completa. Explica el aislamiento que proveen las ramas respecto de `main` y menciona explícitamente que los cambios solo se integran con un `merge` cuando el programador decide hacerlo.

**C6 — Init y configuración (10/10)**
La carpeta está correctamente nombrada (`tp1-git-fernandez-lucas`), el repositorio fue inicializado (carpeta `.git` presente) y el archivo `.git/config` contiene las claves `user.name` y `user.email` con identidad local configurada sin `--global`.

**C7 — Archivos iniciales y primer commit (15/15)**
`README.md` presente con título Markdown (`#`) y descripción del proyecto. `.gitignore` configurado con reglas para `*.env` y `config-secreta.env`. El archivo sensible nunca aparece en el historial de commits. El mensaje del primer commit es descriptivo: *"Agrego README inicial y gitignore con exclusión de .env"*.

**C8 — Rama de desarrollo (15/15)**
La rama `desarrollo-funcionalidad` existe en `refs/heads/`. Se creó `app.py` con código ejecutable. El `README.md` fue modificado en la rama para incluir el subtítulo `## Instrucciones de uso` con sintaxis Markdown correcta. El commit en la rama tiene mensaje descriptivo.

**C9 — Merge a main (10/10)**
El historial muestra un merge commit explícito (`4e7a1c2 Merge branch 'desarrollo-funcionalidad'`), con la estructura de grafo esperada. Los archivos creados en la rama (`app.py`, `README.md` actualizado) están presentes en `main` después del merge.

---

---

## Alumno: Agustín Morales — `s1_falla_c2.txt`

### Nota Final: 90 / 100

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Formato y condiciones de entrega | 15 | 15 | ✅ Completo |
| C2 | Versionado manual vs Git | 10 | **0** | ❌ Sin respuesta |
| C3 | Estado Staged | 10 | 10 | ✅ Completo |
| C4 | .gitignore | 8 | 8 | ✅ Completo |
| C5 | Ramas (branches) | 7 | 7 | ✅ Completo |
| C6 | Init y configuración | 10 | 10 | ✅ Completo |
| C7 | Archivos iniciales y primer commit | 15 | 15 | ✅ Completo |
| C8 | Rama de desarrollo y segundo commit | 15 | 15 | ✅ Completo |
| C9 | Merge a main | 10 | 10 | ✅ Completo |

### Feedback por criterio

**C1 — Formato y condiciones de entrega (15/15)**
Entrega correctamente estructurada. `.zip` válido, PDF sin imágenes, carpeta `.git` presente con `HEAD`, `objects/` y `refs/`. La identidad en `.git/config` está configurada. Sin observaciones en este criterio.

**C2 — Versionado manual vs Git (0/10)** ⚠️
**Pregunta dejada en blanco.** Este es el único criterio con descuento en toda la entrega. La pregunta solicita explicar los riesgos del versionado con carpetas manuales (proyecto_final, proyecto_final_v2, etc.) e identificar al menos un riesgo concreto. No hay respuesta registrada. Según las instrucciones de puntuación, la ausencia de respuesta equivale a 0 puntos en este criterio. Se descuentan 10 puntos sobre 100.

**C3 — Estado Staged (10/10)**
Respuesta correcta. Identifica que "Staged" es el paso intermedio entre "Modificado" y "Confirmado", y que se activa con `git add`. Sin la analogía elaborada del alumno anterior, pero la definición es precisa y suficiente.

**C4 — .gitignore (8/8)**
Correcta. Menciona la función del `.gitignore` y da un ejemplo concreto (archivos `.env` con contraseñas o claves API).

**C5 — Ramas (7/7)**
Correcta. Explica el aislamiento de la rama y que los cambios se integran a `main` con el `merge` cuando el programador lo decide.

**C6 — Init y configuración (10/10)**
Carpeta correctamente nombrada (`tp1-git-morales-agustin`), `.git/config` con `user.name` y `user.email`. Todo en orden.

**C7 — Archivos iniciales y primer commit (15/15)**
`README.md` presente con título Markdown. `.gitignore` con reglas para `config-secreta.env` y `*.env`. El archivo sensible no aparece en el historial. Mensaje del primer commit descriptivo.

**C8 — Rama de desarrollo (15/15)**
Rama `desarrollo-funcionalidad` presente en `refs/heads/`. `app.py` creado con código. `README.md` actualizado con `## Instrucciones de uso`. Commit en la rama con mensaje descriptivo.

**C9 — Merge a main (10/10)**
Merge commit visible en el historial (`7c2f9a1 Merge branch 'desarrollo-funcionalidad'`). Archivos de la rama integrados en `main`.

### Observación General
La entrega es técnicamente correcta en todos los demás aspectos. La parte práctica y las respuestas teóricas restantes (C3, C4, C5) están bien resueltas. La única penalización es la pregunta 1 omitida. Un descuido puntual en una entrega por lo demás muy sólida.

---

---

## Alumno: Camila Suárez — `s2_sin_git_cd2.txt`

### ⚠️ Condición de Desaprobación Activada: CD2

> **CD2:** La carpeta `.git` está ausente en el `.zip` entregado → `nota_maxima: 30`

La rúbrica establece que la ausencia de la carpeta `.git` impone un techo máximo de **30 puntos**, independientemente del puntaje acumulado en los criterios teóricos.

### Nota Final: 30 / 100 (techo por CD2)

### Desglose por criterio

| Criterio | Descripción | Peso | Obtenido | Estado |
|---|---|---|---|---|
| C1 | Formato y condiciones de entrega | 15 | **7** | ⚠️ Parcial (-8 por falta de .git) |
| C2 | Versionado manual vs Git | 10 | 10 | ✅ Completo |
| C3 | Estado Staged | 10 | 10 | ✅ Completo |
| C4 | .gitignore | 8 | 8 | ✅ Completo |
| C5 | Ramas (branches) | 7 | 7 | ✅ Completo |
| C6 | Init y configuración | 10 | **0** | ❌ Sin evidencia verificable |
| C7 | Archivos iniciales y primer commit | 15 | **0** | ❌ Sin evidencia verificable |
| C8 | Rama de desarrollo y segundo commit | 15 | **0** | ❌ Sin evidencia verificable |
| C9 | Merge a main | 10 | **0** | ❌ Sin evidencia verificable |
| **Subtotal bruto** | | 100 | **42** | |
| **Techo CD2** | | | **→ 30** | ⚠️ |

### Feedback por criterio

**C1 — Formato y condiciones de entrega (7/15)**
El `.zip` es válido y el PDF cumple con el formato (solo texto, sin imágenes). Sin embargo, la carpeta `.git` está ausente por completo de la entrega. Las instrucciones de puntuación establecen un descuento de 8 puntos por este faltante dentro del propio criterio C1 (independientemente de la condición CD2).

**C2 — Versionado manual vs Git (10/10)**
Respuesta completa. Identifica la pérdida de historial, la imposibilidad de rastrear quién modificó qué y cuándo, y el riesgo de pérdida irreversible ante un borrado accidental. Bien argumentada y con palabras propias.

**C3 — Estado Staged (10/10)**
Correcta. Define Staged como el estado intermedio entre "Modificado" y "Confirmado", activado con `git add`.

**C4 — .gitignore (8/8)**
Correcta. Explica la función del archivo y da como ejemplo concreto un `.env` con contraseñas o claves API.

**C5 — Ramas (7/7)**
Correcta. Menciona el aislamiento respecto a `main` y que los cambios se integran con `merge` solo cuando el programador lo decide.

**C6 — Init y configuración (0/10)** ❌
Sin la carpeta `.git` no hay forma de verificar que se ejecutó `git init`, ni que la identidad local fue configurada (nombre y correo en `.git/config`). Ninguna de las evidencias de este criterio es auditable. Lo que el alumno afirme en el PDF no es suficiente sin el repositorio para corroborarlo.

**C7 — Archivos iniciales y primer commit (0/15)** ❌
Sin `.git` no hay historial de commits, no hay evidencia de que `README.md` fue rastreado ni de que el `.gitignore` funcionó correctamente. No es posible verificar que `config-secreta.env` fue excluido del historial ni que el primer commit tiene mensaje descriptivo.

**C8 — Rama de desarrollo (0/15)** ❌
Sin `refs/heads/` no hay manera de confirmar la existencia de la rama `desarrollo-funcionalidad`, ni el commit asociado, ni las modificaciones al `README.md` y la creación de `app.py`.

**C9 — Merge a main (0/10)** ❌
Sin historial `.git` no existe evidencia del merge. No hay merge commit auditable.

### Observación General
La parte teórica (C2 a C5) está bien resuelta y alcanza los 35 puntos posibles en esos criterios. Sin embargo, la ausencia de la carpeta `.git` hace que toda la parte práctica (C6 a C9, 50 puntos) sea imposible de corregir. El corrector no puede evaluar lo que el alumno afirma haber hecho si no hay repositorio que lo respalde. Adicionalmente, la condición de desaprobación CD2 limita la nota máxima a 30 puntos. La entrega evidencia comprensión teórica del TP pero un error crítico en el proceso de empaquetado: el `.git` debe incluirse explícitamente al comprimir, dado que es una carpeta oculta que los gestores de archivos frecuentemente omiten por defecto.

---

## Resumen de la Rúbrica — Comportamiento observado

| Escenario de prueba | Comportamiento esperado | Resultado |
|---|---|---|
| Entrega completa y correcta | 100/100 sin penalizaciones | ✅ Correcto — Lucas Fernández: 100/100 |
| Falla en criterio teórico único (C2) | Descuento de 10 puntos, resto intacto | ✅ Correcto — Agustín Morales: 90/100 |
| Ausencia de .git (CD2) | Techo de 30 puntos, práctica anulada | ✅ Correcto — Camila Suárez: 30/100 |

La rúbrica discrimina correctamente los tres casos. Los descuentos parciales por criterios individuales funcionan de forma aislada (C2 no afecta a C3, C4, etc.) y la condición de desaprobación CD2 se activa correctamente sin eliminar el puntaje de los criterios teóricos evaluables.
