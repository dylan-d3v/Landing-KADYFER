# KADYFER Service Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate and integrate six accessible, responsive, static KADYFER service pages from one tested Python template.

**Architecture:** A standard-library Python generator owns approved service data and shared HTML structure. It writes six committed HTML files that reuse the existing global stylesheet plus a focused service stylesheet; the public site remains dependency-free and works through `file://` without JavaScript.

**Tech Stack:** HTML5, CSS, vanilla JavaScript, Python 3 standard library, `unittest`.

---

### Task 1: Generator Contract

**Files:**
- Create: `tests/test_service_pages.py`
- Create: `tools/generate_service_pages.py`

- [ ] **Step 1: Write failing generator tests**

Create `unittest` cases that import the generator and require:

```python
EXPECTED_SLUGS = {
    "desintoxicacion-ionica",
    "terapia-neural",
    "sueroterapia-ortomolecular",
    "terapia-fisica",
    "limpieza-facial-profunda",
    "plasma-rico-en-plaquetas-prp",
}
```

The tests must assert exactly six services, required fields, five or more FAQ
entries, safe WhatsApp URLs, omission of domain-dependent metadata while
`SITE_URL` is empty, and omission of unavailable related services.

- [ ] **Step 2: Verify RED**

Run: `python -m unittest tests.test_service_pages -v`

Expected: FAIL because `tools.generate_service_pages` does not exist.

- [ ] **Step 3: Implement the minimum generator API**

Define `SITE_URL`, `SERVICES`, `validate_services()`, `build_whatsapp_url()`,
`render_service_page()`, and `generate_pages()`. Store all approved service
content and FAQ answers as structured dictionaries and escape inserted text.

- [ ] **Step 4: Verify GREEN**

Run: `python -m unittest tests.test_service_pages -v`

Expected: all generator contract tests pass.

### Task 2: Static Page Generation

**Files:**
- Modify: `tests/test_service_pages.py`
- Modify: `tools/generate_service_pages.py`
- Create: `servicios/desintoxicacion-ionica.html`
- Create: `servicios/terapia-neural.html`
- Create: `servicios/sueroterapia-ortomolecular.html`
- Create: `servicios/terapia-fisica.html`
- Create: `servicios/limpieza-facial-profunda.html`
- Create: `servicios/plasma-rico-en-plaquetas-prp.html`

- [ ] **Step 1: Add failing rendered-page tests**

Parse generated HTML with `html.parser.HTMLParser` and assert per page:

```python
self.assertEqual(document.h1_count, 1)
self.assertGreaterEqual(document.whatsapp_link_count, 2)
self.assertTrue(document.has_skip_link)
self.assertTrue(document.has_breadcrumb)
self.assertTrue(document.has_faq)
self.assertFalse(document.has_canonical)
```

Also assert relative CSS, script, landing and asset paths; explicit image
dimensions; unique title and description; JSON-LD; secure external links; and
absence of pending service URLs.

- [ ] **Step 2: Verify RED**

Run: `python -m unittest tests.test_service_pages -v`

Expected: FAIL because complete service HTML has not been rendered.

- [ ] **Step 3: Implement the shared HTML template**

Render semantic header, breadcrumb, service hero, information sections,
intermediate CTA, considerations, FAQ, optional related services, final CTA and
footer. Include literal WhatsApp `href` values and relative navigation that
works through `file://`.

- [ ] **Step 4: Generate the six pages**

Run: `python tools/generate_service_pages.py`

Expected: six files written under `servicios/`.

- [ ] **Step 5: Verify GREEN and determinism**

Run:

```powershell
python -m unittest tests.test_service_pages -v
python tools/generate_service_pages.py --check
```

Expected: tests pass and generated files match the generator output.

### Task 3: Shared Styling and Progressive Navigation

**Files:**
- Modify: `tests/test_service_pages.py`
- Create: `service-pages.css`
- Modify: `styles.css`

- [ ] **Step 1: Add failing style and no-JS tests**

Require every generated page to load `../styles.css` followed by
`../service-pages.css`, and require the stylesheet to contain service hero,
breadcrumb, content, CTA and related-service rules plus 320 px-safe responsive
behavior.

- [ ] **Step 2: Verify RED**

Run: `python -m unittest tests.test_service_pages -v`

Expected: FAIL because `service-pages.css` does not exist.

- [ ] **Step 3: Implement service page styles**

Reuse existing variables and component classes. Add only the new page layouts,
using single-column defaults, fluid type and spacing, stable image ratios,
visible keyboard focus, and multi-column enhancements from 800 px.

- [ ] **Step 4: Harden the existing no-JS mobile navigation**

Keep `.site-nav` visible by default. Apply collapsed-menu positioning only
under `.js`, preserving direct links when JavaScript is unavailable.

- [ ] **Step 5: Verify GREEN**

Run: `python -m unittest tests.test_service_pages -v`

Expected: all style and no-JS contract tests pass.

### Task 4: Landing Integration and Full Verification

**Files:**
- Modify: `tests/test_service_pages.py`
- Modify: `index.html`

- [ ] **Step 1: Add failing landing-link tests**

Require the catalog to link exactly the six implemented services and keep the
six pending names as plain text. Require all local `href`, `src` and `srcset`
targets to exist.

- [ ] **Step 2: Verify RED**

Run: `python -m unittest tests.test_service_pages -v`

Expected: FAIL because catalog service names are not links.

- [ ] **Step 3: Link only implemented services**

Wrap the six approved catalog names in relative anchors and preserve existing
numbering and visual hierarchy. Do not link pending services.

- [ ] **Step 4: Verify automated checks**

Run:

```powershell
python -m unittest discover -s tests -v
python tools/generate_service_pages.py --check
git diff --check
```

Expected: all tests pass, output is deterministic, and no whitespace errors are
reported.

- [ ] **Step 5: Verify rendered behavior**

Open `index.html` and representative medical, aesthetic and PRP service pages
in the in-app Browser. Check desktop and 320 px mobile, menu interaction,
keyboard-visible navigation, FAQ disclosure, WhatsApp URL, console health,
image loading and horizontal overflow. Repeat with JavaScript disabled or by
removing the `.js` class in the page context to verify fallback navigation.

- [ ] **Step 6: Review scope**

Confirm Git contains exactly six service pages, no pending-service pages,
medical copy matches the approved source, and no domain has been invented.
