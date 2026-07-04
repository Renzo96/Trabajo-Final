#!/usr/bin/env python3
"""
Genera entregas sintéticas a partir de una rúbrica y las testea con simular_correccion.

Estrategia de mutación:
  S0 → entrega perfecta (todas las evidencias cumplidas)
  Si → entrega que falla SOLO el criterio Ci, perfecta en el resto

Cada sintético se guarda como .txt y se corrige con la rúbrica. Al final se
muestra una tabla comparativa para detectar criterios que no discriminan.

Uso:
    python generar_y_testear_sinteticos.py --rubrica <rubrica.json>
        [--cantidad N] [--materia "Nombre"] [--formato-entrega "descripción"]
        [--model <id>] [--out <carpeta>] [--no-run]
        [--solo-sintetico s2] [--modo solo_codigo]
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime

# Import shared functions from simular_correccion
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from simular_correccion import (
    cargar_rubrica, build_prompt, consolidar, extraer_json,
    normalizar_nota, informe, imprimir,
)


# ── LLM caller ───────────────────────────────────────────────────────────

def llamar_opencode(prompt: str, model: str | None = None, timeout: int = 600) -> str:
    """Llama al LLM via opencode run --format json usando pwsh como pipe."""
    fd, tmp = tempfile.mkstemp(suffix=".txt", prefix="opencode_prompt_")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(prompt)

        model_flag = f" --model {model}" if model else ""
        ps_cmd = (
            f'Get-Content -LiteralPath "{tmp}" -Raw | '
            f"opencode run --format json --dangerously-skip-permissions{model_flag}"
        )
        r = subprocess.run(
            ["pwsh", "-NoProfile", "-Command", ps_cmd],
            text=True, capture_output=True, encoding="utf-8", timeout=timeout,
        )
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass

    if r.returncode != 0:
        raise SystemExit(f"opencode falló (exit {r.returncode}):\n{r.stderr}")

    textos: list[str] = []
    for line in r.stdout.strip().splitlines():
        if not line.strip():
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "text":
            textos.append(ev.get("part", {}).get("text", ""))
    return "".join(textos)


# ── Rubric helpers ───────────────────────────────────────────────────────

def _build_criterios_completos(rubrica: dict) -> str:
    """Arma una descripción textual de todos los criterios con sus evidencias."""
    partes: list[str] = []
    for c in rubrica["criterios"]:
        partes.append(
            f"### {c['id']} - {c['nombre']} (Peso: {c['peso']} pts)\n"
            f"Descripción: {c['descripcion']}\n"
        )
        if c.get("instrucciones_puntuacion"):
            partes.append(f"Reglas de puntuación: {c['instrucciones_puntuacion']}\n")
        subs = c.get("subcriterios") or []
        if subs:
            partes.append("Evidencias que deben cumplirse:\n")
            for sub in subs:
                for ev in (sub.get("evidencias") or []):
                    partes.append(f"  - {ev}\n")
        partes.append("")
    return "\n".join(partes)


def _build_falla_detalle(rubrica: dict, cid: str) -> str:
    """Arma la descripción detallada del criterio que debe fallar."""
    for c in rubrica["criterios"]:
        if c["id"] == cid:
            partes = [f"### {c['id']} - {c['nombre']} (Peso: {c['peso']} pts)"]
            partes.append(f"Descripción: {c['descripcion']}")
            if c.get("instrucciones_puntuacion"):
                partes.append(f"Reglas de puntuación: {c['instrucciones_puntuacion']}")
            subs = c.get("subcriterios") or []
            if subs:
                partes.append("Evidencias que debe INCUMPLIR:")
                for sub in subs:
                    for ev in (sub.get("evidencias") or []):
                        partes.append(f"  - NO debe cumplir: {ev}")
            return "\n".join(partes)
    return f"Criterio {cid} (no encontrado en la rúbrica)"


# ── Synthetic generation ─────────────────────────────────────────────────

def generar_sintetico(
    rubrica: dict,
    criterio_a_fallar: str | None,
    formato_entrega: str,
    model: str | None = None,
    falla_parcial: bool = False,
) -> str:
    """Genera una entrega sintética.

    - criterio_a_fallar=None → perfecta
    - criterio_a_fallar=CID + falla_parcial=False → falla completa de ese criterio
    - criterio_a_fallar=CID + falla_parcial=True  → falla parcial (respuesta incompleta)
    """

    if criterio_a_fallar is None:
        # ── Perfect ──
        criterios_completos = _build_criterios_completos(rubrica)
        prompt = (
            f"Sos un estudiante universitario que entrega un trabajo práctico.\n\n"
            f"Trabajo: {rubrica['titulo']}\n"
            f"Consigna: {rubrica.get('descripcion', 'Sin descripción')}\n\n"
            f"RÚBRICA COMPLETA (tu entrega debe cumplir TODO):\n\n"
            f"{criterios_completos}\n"
            f"---\n\n"
            f"Generá la entrega COMPLETA de un alumno que cumple PERFECTAMENTE "
            f"TODOS los criterios y TODAS las evidencias listadas arriba. "
            f"Escribí como un alumno real: mostrá comprensión genuina, usá tus "
            f"propias palabras, incluí detalles y ejemplos cuando corresponda.\n\n"
            f"REGLAS:\n"
            f"- NO incluyas comentarios sobre la rúbrica ni sobre lo que estás haciendo.\n"
            f"- NO uses frases como 'Acá cumplo con el criterio X'.\n"
            f"- NO agregues metadata, encabezados de sistema ni tu nombre.\n"
            f"- Entregá SOLO el contenido que el alumno subiría.\n\n"
            f"Formato de entrega esperado: {formato_entrega}"
        )
    elif falla_parcial:
        # ── Partial failure ──
        falla_detalle = _build_falla_detalle(rubrica, criterio_a_fallar)
        otros_criterios = [
            c for c in rubrica["criterios"] if c["id"] != criterio_a_fallar
        ]
        otros_completos = _build_criterios_completos(
            {"criterios": otros_criterios}
        )

        prompt = (
            f"Sos un estudiante universitario que entrega un trabajo práctico.\n\n"
            f"Trabajo: {rubrica['titulo']}\n"
            f"Consigna: {rubrica.get('descripcion', 'Sin descripción')}\n\n"
            f"---\n\n"
            f"CRITERIOS QUE TU ENTREGA DEBE CUMPLIR PERFECTAMENTE:\n\n"
            f"{otros_completos}\n"
            f"---\n\n"
            f"CRITERIO QUE DEBE CUMPLIRSE PARCIALMENTE:\n\n"
            f"{falla_detalle}\n"
            f"---\n\n"
            f"Generá una entrega donde:\n"
            f"1. Todos los criterios de la PRIMERA sección están IMPECABLES.\n"
            f"2. El criterio de la SEGUNDA sección se cumple PARCIALMENTE:\n"
            f"   - Un alumno que entiende el concepto pero responde incompleto.\n"
            f"   - Cubre ALGUNAS evidencias, pero NO TODAS.\n"
            f"   - La respuesta tiene algo de valor pero es insuficiente para "
            f"el puntaje completo.\n"
            f"   - Respondió solo una parte de lo pedido, o dio una respuesta "
            f"superficial sin desarrollar.\n"
            f"3. Escribí como un alumno real que estudió pero le faltó profundidad.\n\n"
            f"REGLAS:\n"
            f"- NO menciones qué criterio estás fallando parcialmente.\n"
            f"- NO uses frases como 'Acá cumplo con el criterio X'.\n"
            f"- NO agregues metadata, encabezados de sistema ni tu nombre.\n"
            f"- Entregá SOLO el contenido que el alumno subiría.\n\n"
            f"Formato de entrega esperado: {formato_entrega}"
        )
    else:
        # ── Complete failure ──
        falla_detalle = _build_falla_detalle(rubrica, criterio_a_fallar)
        otros_criterios = [
            c for c in rubrica["criterios"] if c["id"] != criterio_a_fallar
        ]
        otros_completos = _build_criterios_completos(
            {"criterios": otros_criterios}
        )

        prompt = (
            f"Sos un estudiante universitario que entrega un trabajo práctico.\n\n"
            f"Trabajo: {rubrica['titulo']}\n"
            f"Consigna: {rubrica.get('descripcion', 'Sin descripción')}\n\n"
            f"---\n\n"
            f"CRITERIOS QUE TU ENTREGA DEBE CUMPLIR PERFECTAMENTE:\n\n"
            f"{otros_completos}\n"
            f"---\n\n"
            f"CRITERIO QUE DEBE FALLAR (fallo creíble de alumno):\n\n"
            f"{falla_detalle}\n"
            f"---\n\n"
            f"Generá una entrega donde:\n"
            f"1. Todos los criterios de la PRIMERA sección están IMPECABLES.\n"
            f"2. El criterio de la SEGUNDA sección FALLA de forma creíble:\n"
            f"   - Un alumno que no entendió ese concepto, o lo omitió, o dio una\n"
            f"     respuesta superficial/equivocada.\n"
            f"   - La falla debe ser evidente al leer la entrega.\n"
            f"3. Escribí como un alumno real: conocimiento parcial, no perfecto en todo.\n\n"
            f"REGLAS:\n"
            f"- NO menciones qué criterio estás fallando.\n"
            f"- NO uses frases como 'Acá cumplo con el criterio X'.\n"
            f"- NO agregues metadata, encabezados de sistema ni tu nombre.\n"
            f"- Entregá SOLO el contenido que el alumno subiría.\n\n"
            f"Formato de entrega esperado: {formato_entrega}"
        )

    sys.stdout.write("  🤖 Generando... ")
    sys.stdout.flush()
    respuesta = llamar_opencode(prompt, model)
    print("✓")
    return respuesta


# ── Corrección de un sintético ──────────────────────────────────────────

def corregir_sintetico(
    rubrica: dict,
    archivo: str,
    materia: str,
    alumno: str,
    label: str,
    modo: str,
    model: str | None,
    out_dir: str,
) -> dict:
    """Corrige un sintético y devuelve el diccionario de resultado."""
    codigo = consolidar(archivo, modo, None)
    prompt = build_prompt(rubrica, codigo, materia, f"{alumno} ({label})")

    # Save prompt for debugging
    sid = os.path.splitext(os.path.basename(archivo))[0]
    prompt_path = os.path.join(out_dir, f"{sid}_prompt.txt")
    with open(prompt_path, "w", encoding="utf-8") as f:
        f.write(prompt)

    sys.stdout.write("  🧪 Corrigiendo... ")
    sys.stdout.flush()
    salida = llamar_opencode(prompt, model)
    print("✓")

    try:
        corr = extraer_json(salida)
    except Exception as e:
        return {"error": str(e), "raw": salida[:500]}

    corr.setdefault("fortalezas", [])
    corr.setdefault("recomendaciones", [])
    corr.setdefault("comentario_general", "")
    corr.setdefault("condicion_desaprobacion_aplicada", None)
    corr.setdefault("penalizaciones_aplicadas", [])
    normalizar_nota(corr)

    # Save correction
    corr_path = os.path.join(out_dir, f"{sid}_correccion.json")
    with open(corr_path, "w", encoding="utf-8") as f:
        json.dump(corr, f, ensure_ascii=False, indent=2)

    warns = informe(rubrica, corr)
    return {"nota": corr.get("nota"), "warns": warns, "corr": corr}


# ── Report ───────────────────────────────────────────────────────────────

def _crit_id_to_label(cid: str) -> str:
    return cid.lower().replace(" ", "_")


def imprimir_tabla(
    sinteticos: dict,
    resultados: dict,
    rubrica: dict,
    out_dir: str,
) -> None:
    """Imprime la tabla resumen y el meta-análisis."""
    peso_por_id = {c["id"]: c["peso"] for c in rubrica["criterios"]}

    print(f"\n{'=' * 80}")
    print("  RESUMEN DE RESULTADOS")
    print(f"{'=' * 80}")
    print(f"\n{'Sintético':<14} {'Testea':<30} {'Esperado':>8} {'Real':>6} {'Meta'}")
    print(f"{'─' * 14} {'─' * 30} {'─' * 8} {'─' * 6} {'─' * 6}")

    meta_resultados = []
    for sid, sinfo in sinteticos.items():
        res = resultados.get(sid, {})
        nota = res.get("nota")
        cf = sinfo["criterio_fallado"]
        es_parcial = sinfo.get("falla_parcial", False)

        if cf is None:
            esperado = "≥90"
            testea = "rúbrica completa"
            if nota is not None:
                meta = "✅" if nota >= 90 else "❌"
            else:
                meta = "❌"
        elif es_parcial:
            peso = peso_por_id.get(cf, 0)
            esperado = f"~{100 - peso // 2}"
            testea = f"{cf} parcial ({peso} pts)"
            if nota is not None:
                # Partial: should lose some points but not all.
                # Passes if score dropped at least 15% of weight but not >85%
                perdida = 100 - nota
                meta = "✅" if (peso * 0.15 <= perdida <= peso * 0.85) else "❌"
            else:
                meta = "❌"
        else:
            peso = peso_por_id.get(cf, 0)
            esperado = f"~{100 - peso}"
            testea = f"{cf} discrimina ({peso} pts)"
            if nota is not None:
                techo_pase = 100 - (peso * 0.4)
                meta = "✅" if nota <= techo_pase else "❌"
            else:
                meta = "❌"

        nota_str = f"{nota:.0f}" if nota is not None else "ERR"
        print(f"{sid:<14} {testea:<30} {esperado:>8} {nota_str:>6}  {meta}")

        meta_resultados.append({
            "sid": sid,
            "testea": testea,
            "esperado": esperado,
            "nota": nota,
            "meta": meta,
            "warns": res.get("warns", []),
        })

    # Fallos del meta-test
    fallos = [m for m in meta_resultados if m["meta"] == "❌"]
    if fallos:
        print(f"\n{'─' * 80}")
        print(f"  ⚠️  {len(fallos)} sintético(s) no discriminaron como se esperaba:")
        for fm in fallos:
            print(f"\n    {fm['sid']}: {fm['testea']} (nota: {fm['nota']})")
            if fm["warns"]:
                for w in fm["warns"]:
                    print(f"      • {w}")
            print(f"      ↳ Posible causa: evidencias demasiado vagas, "
                  f"instrucciones_puntuacion poco claras, o el criterio "
                  f"no logra que el corrector descuente.")
    else:
        print(f"\n  ✅ Todos los sintéticos discriminaron correctamente.")

    # Save summary
    summary_path = os.path.join(out_dir, "resumen.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(meta_resultados, f, ensure_ascii=False, indent=2)
    print(f"\n💾 Resumen guardado en: {summary_path}")


# ── Main ────────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Genera entregas sintéticas a partir de una rúbrica y las testea."
    )
    ap.add_argument("--rubrica", required=True, help="JSON de la rúbrica")
    ap.add_argument("--cantidad", type=int, default=None,
                    help="Cantidad de sintéticos (default: interactivo)")
    ap.add_argument("--materia", default="Materia de prueba",
                    help="Nombre de la materia (se inyecta en el prompt)")
    ap.add_argument("--alumno", default="Alumno Sintético",
                    help="Nombre del alumno para los metadatos de corrección")
    ap.add_argument("--modo", default="solo_codigo",
                    help="Modo de consolidación para simular_correccion")
    ap.add_argument("--out", default=None,
                    help="Carpeta de salida (default: <rubrica_dir>/sinteticos/<timestamp>)")
    ap.add_argument("--model", default=None,
                    help="Modelo para opencode run (ej: claude-sonnet-4-20250514)")
    ap.add_argument("--formato-entrega", default="documento de texto plano con respuestas",
                    help="Descripción del formato de entrega esperado")
    ap.add_argument("--no-run", action="store_true",
                    help="Solo genera los sintéticos, no los corrige")
    ap.add_argument("--solo-sintetico", default=None,
                    help="Re-testea solo un sintético existente (ej: s2)")
    args = ap.parse_args()

    # ── Load rubric ──
    rubrica = cargar_rubrica(args.rubrica)
    if not rubrica.get("tipo"):
        rubrica["tipo"] = "TP"
    if not rubrica.get("criterios"):
        raise SystemExit("La rúbrica no tiene criterios.")

    n_criterios = len(rubrica["criterios"])
    max_sint = n_criterios + 1  # S0 + uno por criterio (falla completa)

    # ── Determine how many synthetics ──
    if args.solo_sintetico:
        cantidad = 0  # skip generation
    elif args.cantidad is not None:
        cantidad = min(args.cantidad, 16)  # hard cap at 16
    else:
        # Interactive
        print(f"\nRúbrica: {rubrica['titulo']}")
        print(f"Criterios ({n_criterios}):")
        for c in rubrica["criterios"]:
            print(f"  {c['id']} · {c['nombre'][:55]:55s} {c['peso']} pts")

        print(f"\nSintéticos disponibles (máx. {max_sint + n_criterios}):")
        print(f"  S0 · PERFECTA (base, todos los criterios OK)")
        for i, c in enumerate(rubrica["criterios"], 1):
            print(f"  S{i} · Falla {c['id']} — {c['nombre'][:50]}")
        for i, c in enumerate(rubrica["criterios"][:3], n_criterios + 1):
            print(f"  S{i} · Parcial {c['id']} — mitad de puntaje en {c['nombre'][:40]}")

        try:
            val = input(f"\n¿Cuántos querés generar? (0 para salir, recomendado: 8) → ")
            cantidad = int(val)
        except (ValueError, EOFError):
            print("Cancelado.")
            return 0

    if cantidad == 0 and not args.solo_sintetico:
        print("Nada que generar.")
        return 0

    # ── Output directory ──
    if args.out:
        out_dir = args.out
    else:
        rubrica_dir = os.path.dirname(os.path.abspath(args.rubrica))
        out_dir = os.path.join(rubrica_dir, "sinteticos",
                               datetime.now().strftime("%Y-%m-%d_%H%M%S"))
    os.makedirs(out_dir, exist_ok=True)
    print(f"\n📁 Salida: {out_dir}\n")

    # ── Generate synthetics ──
    sinteticos: dict[str, dict] = {}

    if args.solo_sintetico is None:
        for i in range(cantidad):
            if i == 0:
                label = "S0 (perfecta)"
                cf = None
                es_parcial = False
            elif i <= n_criterios:
                # Complete failure of criterion i
                cid = rubrica["criterios"][i - 1]["id"]
                label = f"S{i} (falla {cid})"
                cf = cid
                es_parcial = False
            else:
                # Partial failure: cycle through criteria
                idx = (i - 1) % n_criterios
                cid = rubrica["criterios"][idx]["id"]
                label = f"S{i} (parcial {cid})"
                cf = cid
                es_parcial = True

            print(f"{'─' * 50}")
            print(f"  {label}")
            print(f"{'─' * 50}")

            contenido = generar_sintetico(
                rubrica, cf, args.formato_entrega, args.model,
                falla_parcial=es_parcial,
            )

            if cf is None:
                fname = "s0_perfecta.txt"
            elif es_parcial:
                fname = f"s{i}_parcial_{_crit_id_to_label(cf)}.txt"
            else:
                fname = f"s{i}_falla_{_crit_id_to_label(cf)}.txt"
            fpath = os.path.join(out_dir, fname)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(contenido)

            sinteticos[f"s{i}"] = {
                "label": label,
                "file": fpath,
                "criterio_fallado": cf,
                "falla_parcial": es_parcial,
            }

        print(f"\n✅ {len(sinteticos)} sintéticos generados.")

    # ── Discover existing synthetics (for --solo-sintetico or re-run) ──
    if args.solo_sintetico:
        sid = args.solo_sintetico.lower()
        found = False
        for fname in os.listdir(out_dir):
            if fname.startswith(f"{sid}_") and fname.endswith(".txt"):
                fpath = os.path.join(out_dir, fname)
                # Determine what it tests
                if "perfecta" in fname:
                    cf = None
                else:
                    cf = fname.split("_falla_")[-1].replace(".txt", "").upper()
                    if cf.startswith("C"):
                        cf = cf.split("_")[0] if "_" in cf else cf
                sinteticos[sid] = {
                    "label": f"{sid} (cargado)",
                    "file": fpath,
                    "criterio_fallado": cf if cf else None,
                }
                found = True
                break
        if not found:
            raise SystemExit(f"No se encontró un sintético '{sid}' en {out_dir}")

    if not sinteticos:
        print("No hay sintéticos para testear.")
        return 0

    if args.no_run:
        print(f"\n--no-run: sintéticos guardados en {out_dir}, sin corregir.")
        return 0

    # ── Test each synthetic ──
    print(f"\n{'=' * 60}")
    print("  EJECUTANDO CORRECCIONES")
    print(f"{'=' * 60}")

    resultados: dict[str, dict] = {}
    for sid, sinfo in sinteticos.items():
        print(f"\n── {sinfo['label']} ──")
        res = corregir_sintetico(
            rubrica, sinfo["file"], args.materia, args.alumno,
            sinfo["label"], args.modo, args.model, out_dir,
        )
        resultados[sid] = res

        if res.get("error"):
            print(f"  ❌ Error: {res['error']}")
        else:
            nota = res.get("nota", "?")
            print(f"  📊 Nota: {nota}")

    # ── Report ──
    imprimir_tabla(sinteticos, resultados, rubrica, out_dir)
    print(f"📁 Sintéticos y correcciones en: {out_dir}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
