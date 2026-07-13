# `.agents/skills/rubrica-builder` — carpeta gestionada, no editar a mano

Esta carpeta **no es código propio de esta tesis**. Es la skill
[`rubrica-builder`](https://github.com/JuanCruzRobledo/rubrica-builder), propiedad
de **Juan Cruz Robledo**, distribuida bajo licencia **Apache-2.0** (ver `LICENSE`
dentro de esta misma carpeta), instalada mediante el gestor `npx skills`:

```bash
npx skills add https://github.com/JuanCruzRobledo/rubrica-builder
```

El archivo [`../../skills-lock.json`](../../skills-lock.json) (en la raíz del
repo) registra la fuente y el hash de la versión instalada — es el equivalente a
un lockfile de dependencias. **No modifiques archivos dentro de esta carpeta
manualmente**: si necesitás una versión más nueva, volvé a correr el comando de
instalación.

Se usa en este repositorio **exclusivamente con fines educativos**, como
herramienta central del caso de estudio documentado en
[`informe/Informe_Tesis_Rubrica_Builder.html`](../../informe/Informe_Tesis_Rubrica_Builder.html).
No se reclama ninguna autoría sobre su diseño, lógica o código.
