# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Chinese translation of the BentoBoxWorld documentation site. It is an MkDocs (Material theme) project that publishes the user-facing docs for BentoBox, its game modes, and its addons. The English source lives at https://github.com/BentoBoxWorld/docs — this repo mirrors that structure with content translated into Chinese. The current working branch is typically `update/sync-with-english`, which is used to pull new English content over and translate it.

## Common commands

```bash
pip install -r requirements.txt    # install MkDocs + plugins (pinned old versions, see note below)
mkdocs serve                       # local preview at http://127.0.0.1:8000
mkdocs build                       # build static site into ./site
```

Note: `requirements.txt` pins fairly old versions (mkdocs 1.3.0, mkdocs-material 8.2.15, macros 0.6.0). If installing fresh, use a venv to avoid conflicts with system packages.

## Architecture

Three pieces work together to produce the site:

1. **`mkdocs.yml`** — defines the navigation tree (in Chinese), theme, markdown extensions, and the plugin chain (`search`, `git-revision-date-localized`, `minify`, `macros`). The nav is the source of truth for which pages are published; new translated pages must be added here or they will not appear.

2. **`docs/`** — the translated Markdown content, organized to mirror the English repo:
   - `BentoBox/` — core BentoBox docs and About/ pages
   - `gamemodes/<Name>/` — one folder per game mode (AcidIsland, BSkyBlock, etc.)
   - `addons/<Name>/` — one folder per addon (Bank, Challenges, Level, …)
   - `Tutorials/` — API and general tutorials
   - `stylesheets/bentobox-theme.css` — Blueprint palette override for Material slate (navy/cyan; Space Grotesk + Inter Tight + JetBrains Mono); also defines `.bb-*` layout classes for `docs/index.md`
   - `stylesheets/icons-minecraft-0.5.css` — referenced via `extra_css`

### Homepage (`docs/index.md`)

`index.md` is structurally different from all other pages. It uses `hide: [navigation, toc]` frontmatter and its body is a single raw HTML block (no Markdown) built from `.bb-*` CSS classes defined in `bentobox-theme.css`. Do not add Markdown content or macros directly inside the `.bb-homepage` wrapper — use plain HTML.

3. **`main.py`** — an `mkdocs-macros` module that injects Jinja-callable macros into every page. Pages call these macros (e.g. `{{ translations(123, [...]) }}`) and the macro generates a Markdown table on the fly. The important macros are:
   - `translations(gitlocalize_id, available_translations)` — emits the "help us translate" admonition + a table of all supported languages, marking which have translations available. The intro/admonition text is **already Chinese-translated** in `main.py` itself; English source has the English version. When syncing, keep the Chinese intro intact.
   - `addon_description(addon_name, beta=False)` — emits the standard "Useful links" box (GitHub repo, issues, CI) for an addon. The labels are Chinese-translated.
   - `placeholders_bundle` / `placeholders_source` — read `data/placeholders.csv` and emit placeholder tables for game modes / addons.
   - `flags_bundle` / `flags_source` — read `data/flags.csv` and emit protection/setting flag tables, joining against `data/minecraft-block-and-entity.json` via `icon_css()` to render Minecraft block icons.

   Because table data comes from CSVs at build time, the **column headers in those tables remain in English** — translating them requires editing `main.py`, not the Markdown pages.

4. **`data/`** — the CSV/JSON sources that drive the macro-generated tables (`flags.csv`, `placeholders.csv`, `permissions.csv`, `minecraft-block-and-entity.json`). These are typically synced verbatim from the English repo; do not translate column values that are referenced as IDs in code.

## Translation workflow notes

- This repo's purpose is translation, not original authoring. When the English `docs` repo gains new pages, they should be copied here, translated, and added to the `nav:` section of `mkdocs.yml` (under the appropriate Chinese section heading).
- Page filenames and folder paths must match the English repo so internal links and image paths resolve identically.
- Macro calls (`{{ ... }}`) inside Markdown pages should be left as-is — the macro output handles its own (mostly Chinese) text.
- `site/` and `__pycache__/` are build/runtime artifacts and should not be committed.
