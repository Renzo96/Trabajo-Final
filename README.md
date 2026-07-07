# Concepto de Rúbrica — Implementación de IA Agéntica para la Creación de Rúbricas

Trabajo Final de Grado — **Emmanuel Avellaneda** y **Renzo Sosa**.

Este repositorio documenta la implementación de una **IA agéntica** (Claude Code)
junto con la skill [`rubrica-builder`](.agents/skills/rubrica-builder) para curar
consignas, crear, auditar y testear **rúbricas de evaluación autosuficientes**,
usadas en el marco del sistema de corrección automática **Active-IA**. La materia
tomada como caso de estudio es **Organización Empresarial (OE)**.

> ⚠️ La skill `rubrica-builder` es propiedad intelectual de **Juan Cruz Robledo**
> (Apache-2.0). Se usa acá exclusivamente con fines educativos, como caso de
> estudio de esta tesis. Ver detalle en
> [`informe/Informe_Tesis_Rubrica_Builder.html`](informe/Informe_Tesis_Rubrica_Builder.html),
> sección 12.

## 📄 El informe

El documento central de este repositorio está en [`informe/`](informe/):

- [`Informe_Tesis_Rubrica_Builder.html`](informe/Informe_Tesis_Rubrica_Builder.html) — versión con formato de tesis (portada, índice, estilos), lista para imprimir a PDF.
- [`Informe_Final.pdf`](informe/Informe_Final.pdf) — versión final exportada.

## 🎥 Video de la tesis (fundamentos y motivaciones)

[https://www.youtube.com/watch?v=l34laR3YpRk](https://www.youtube.com/watch?v=l34laR3YpRk)

## 📂 Estructura del repositorio

```
.
├── informe/             Informe de la tesis (html / pdf)
├── teoria/              Material teórico de la cursada de Organización Empresarial (PDFs por unidad)
├── .agents/skills/      Skill rubrica-builder vendorizada (gestionada por `npx skills`, no editar a mano)
├── skills-lock.json     Lockfile de la skill instalada (versión/hash)
├── TPs/
│   ├── TP1/ … TP6/      Rúbrica de cada TP de OE, con sus entregas sintéticas de testeo (sinteticos/)
│   └── TPI/             Rúbrica y testeo del Trabajo Práctico Integrador
└── borradores/          Archivos de prueba manual previos al flujo ordenado por TP (histórico, no autoritativo)
```

Cada carpeta `TPs/TP*/sinteticos/<timestamp>/` contiene el rastro completo de una
corrida del modo TEST de la skill: la entrega sintética, el prompt real enviado al
modelo y el resultado de corrección — la evidencia empírica de que cada rúbrica
discrimina lo que tiene que discriminar (ver sección 8 del informe).

## 🧾 Trabajos Prácticos realizados

Cada carpeta contiene la rúbrica de un TP real de la cursada, con formato de
entrega restringido a texto plano / `.zip` sin imágenes (por la normalización
descripta en la sección 4 del informe) y su propio bloque de conceptos teóricos
evaluados:

| Carpeta | TP | Temas / teoría propia evaluados |
|---|---|---|
| `TPs/TP1/` | **TP1 — Primeros Pasos con Git** | Versionado, estados de archivos, `.gitignore`, ramas; flujo `init` → commits → rama de desarrollo → merge |
| `TPs/TP2/` | **TP2 — Ingeniería de Prompts y Pensamiento Computacional** | Arquitectura de la instrucción (Instrucción/Contexto/Datos de Entrada/Indicador de Salida), parámetros de LLM (Temperatura, Top-p) y Predicción de Tokens, razonamiento Chain-of-Thought |
| `TPs/TP3/` | **TP3 — Fundamentos de Metodologías Ágiles** | Waterfall vs. mentalidad ágil, roles de Scrum, Kanban y WIP Limit, Pair Programming (XP), Historias de Usuario con Criterios de Aceptación |
| `TPs/TP4/` | **TP4 — El Ecosistema Startup y el Modelo Lean** | Startup vs. PyME (escalabilidad e incertidumbre), Lean Startup y MVP, Test de la Madre (Customer Discovery), métricas LTV vs. CAC y Churn Rate, modelos de negocio en software |
| `TPs/TP5/` | **TP5 — Live Coding: El Arte de Programar en Tiempo Real** | Transparencia del proceso y explicación en paralelo en entrevistas técnicas, Boilerplate y Snippet Management, Hot Reloading, planificación con Checkpoints |
| `TPs/TP6/` | **TP6 — Automatización de Flujos con n8n** | Ecosistema Low-Code, triggers vs. acciones, gestión de secretos, nodo Edit Fields, construcción de un workflow (`Schedule Trigger → Edit Fields → nodo de mensajería`) |
| `TPs/TPI/` | **TPI — Del MVP a la Automatización (Parte 2: Automatización y Control de Versiones)** | Construcción de un flujo n8n (`Webhook → Edit Fields` con expresión dinámica) + evidencia de uso de Git (`git log --oneline --stat`). La Parte 1 (teoría en PDF) se corrige manualmente y no forma parte de esta rúbrica |

> **Nota de numeración corregida:** las rúbricas de `TP5` y `TP6` tenían
> originalmente los títulos "TP4" y "TP5" (coincidiendo por error con el TP4 de
> `TP4/`). Se corrigieron a "TP5" y "TP6" para que el título interno del JSON
> coincida con el número de carpeta.

> **Nota sobre la relación con `teoria/`:** el material de `teoria/` corresponde
> a la numeración de unidades del programa de la materia (Unidad 1 a 5: TGS,
> Organizaciones/Empresas, Dato e Información/Toma de Decisiones, Administración,
> Procesos), mientras que el campo `metadata.unidad` de algunas rúbricas (`TP2` →
> "3", `TP5` → "Unidad 6", `TP6` → "Unidad 7") usa una numeración distinta, propia
> del cronograma de TPs. **No son la misma numeración** — no correspondas
> directamente un TP con el PDF de teoría del mismo número sin verificar el
> contenido primero.

## 🛠️ Reproducir el trabajo

1. Instalar Claude Code (ver sección 3.1 del informe).
2. Instalar la skill: `npx skills add https://github.com/JuanCruzRobledo/rubrica-builder`
3. Usar los modos CURAR → CREAR → AUDITAR → TEST descriptos en `.agents/skills/rubrica-builder/SKILL.md`.

## 📚 Créditos

- Skill `rubrica-builder` © Juan Cruz Robledo — [github.com/JuanCruzRobledo/rubrica-builder](https://github.com/JuanCruzRobledo/rubrica-builder) — Apache-2.0.
- Material teórico y rúbricas de Organización Empresarial: producción propia de los autores de esta tesis.
