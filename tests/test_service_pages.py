import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from tools.generate_service_pages import (
    SERVICES,
    SITE_URL,
    build_whatsapp_url,
    render_service_page,
    validate_services,
)


EXPECTED_SLUGS = {
    "desintoxicacion-ionica",
    "terapia-neural",
    "sueroterapia-ortomolecular",
    "terapia-fisica",
    "limpieza-facial-profunda",
    "plasma-rico-en-plaquetas-prp",
}

PENDING_SLUGS = {
    "dermapen-y-fototerapia",
    "peelings-hidratacion-y-melasma",
    "eliminacion-de-lunares-y-verrugas",
    "tratamientos-corporales",
    "reduccion-de-medidas",
    "masajes-reductores-y-post-quirurgico",
}

ROOT = Path(__file__).resolve().parents[1]


class ServicePageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.title_count = 0
        self.title_text = ""
        self.in_title = False
        self.meta_description = ""
        self.stylesheets = []
        self.scripts = []
        self.whatsapp_links = []
        self.external_links = []
        self.has_skip_link = False
        self.has_breadcrumb = False
        self.details_count = 0
        self.canonical_links = []
        self.has_og_url = False
        self.images = []
        self.json_ld = []
        self.in_json_ld = False
        self.json_ld_buffer = []
        self.local_references = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = set(attributes.get("class", "").split())

        if tag == "h1":
            self.h1_count += 1
        elif tag == "title":
            self.title_count += 1
            self.in_title = True
        elif tag == "meta":
            if attributes.get("name") == "description":
                self.meta_description = attributes.get("content", "")
            if attributes.get("property") == "og:url":
                self.has_og_url = True
        elif tag == "link":
            if attributes.get("href"):
                self.local_references.append(attributes["href"])
            if attributes.get("rel") == "stylesheet":
                self.stylesheets.append(attributes.get("href"))
            if attributes.get("rel") == "canonical":
                self.canonical_links.append(attributes.get("href"))
        elif tag == "script":
            if attributes.get("src"):
                self.scripts.append(attributes["src"])
                self.local_references.append(attributes["src"])
            if attributes.get("type") == "application/ld+json":
                self.in_json_ld = True
                self.json_ld_buffer = []
        elif tag == "a":
            href = attributes.get("href", "")
            if href:
                self.local_references.append(href)
            if "skip-link" in classes and href == "#contenido":
                self.has_skip_link = True
            if href.startswith("https://wa.me/"):
                self.whatsapp_links.append(attributes)
            if href.startswith("http"):
                self.external_links.append(attributes)
        elif tag == "nav" and "breadcrumb" in classes:
            self.has_breadcrumb = True
        elif tag == "details":
            self.details_count += 1
        elif tag == "img":
            self.images.append(attributes)
            if attributes.get("src"):
                self.local_references.append(attributes["src"])
            for candidate in attributes.get("srcset", "").split(","):
                path = candidate.strip().split(" ", 1)[0]
                if path:
                    self.local_references.append(path)
        elif tag in {"source", "video"}:
            if attributes.get("src"):
                self.local_references.append(attributes["src"])
            if attributes.get("poster"):
                self.local_references.append(attributes["poster"])
            for candidate in attributes.get("srcset", "").split(","):
                path = candidate.strip().split(" ", 1)[0]
                if path:
                    self.local_references.append(path)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.in_json_ld:
            self.json_ld.append("".join(self.json_ld_buffer).strip())
            self.in_json_ld = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data
        if self.in_json_ld:
            self.json_ld_buffer.append(data)


class ServiceDataTests(unittest.TestCase):
    def test_contains_exactly_the_six_approved_services(self):
        self.assertEqual(set(SERVICES), EXPECTED_SLUGS)
        self.assertEqual(len(SERVICES), 6)

    def test_required_content_is_complete(self):
        required_fields = {
            "name",
            "category",
            "meta_description",
            "summary",
            "hero_cta",
            "whatsapp_message",
            "intro_heading",
            "intro",
            "orientation",
            "process",
            "areas",
            "intermediate_cta",
            "considerations",
            "preparation",
            "faq",
            "image",
            "image_alt",
            "image_width",
            "image_height",
            "related",
        }

        for slug, service in SERVICES.items():
            with self.subTest(slug=slug):
                self.assertEqual(set(service), required_fields)
                self.assertGreaterEqual(len(service["faq"]), 5)
                for question, answer in service["faq"]:
                    self.assertTrue(question.strip())
                    self.assertTrue(answer.strip())

        self.assertEqual(
            [area[0] for area in SERVICES["plasma-rico-en-plaquetas-prp"]["areas"]],
            ["PRP facial", "PRP capilar", "PRP musculoesquelético"],
        )

    def test_service_data_validates(self):
        self.assertIsNone(validate_services())

    def test_whatsapp_urls_are_specific_and_encoded(self):
        for slug, service in SERVICES.items():
            with self.subTest(slug=slug):
                url = build_whatsapp_url(service["whatsapp_message"])
                parsed = urlparse(url)
                self.assertEqual(parsed.scheme, "https")
                self.assertEqual(parsed.netloc, "wa.me")
                self.assertEqual(parsed.path, "/593983956295")
                self.assertEqual(
                    parse_qs(parsed.query)["text"],
                    [service["whatsapp_message"]],
                )

    def test_site_url_is_empty_until_publication(self):
        self.assertEqual(SITE_URL, "")

    def test_related_services_only_reference_generated_pages(self):
        for slug, service in SERVICES.items():
            with self.subTest(slug=slug):
                self.assertTrue(set(service["related"]).issubset(EXPECTED_SLUGS))
                self.assertTrue(set(service["related"]).isdisjoint(PENDING_SLUGS))

    def test_approved_related_service_rules_are_preserved(self):
        self.assertEqual(
            SERVICES["terapia-neural"]["related"],
            ["terapia-fisica", "plasma-rico-en-plaquetas-prp"],
        )
        self.assertEqual(
            SERVICES["sueroterapia-ortomolecular"]["related"],
            ["terapia-neural"],
        )
        self.assertEqual(
            SERVICES["plasma-rico-en-plaquetas-prp"]["related"],
            ["terapia-fisica"],
        )
        self.assertEqual(SERVICES["limpieza-facial-profunda"]["related"], [])


class RenderedServicePageTests(unittest.TestCase):
    def setUp(self):
        self.pages = {
            slug: render_service_page(slug, service)
            for slug, service in SERVICES.items()
        }

    def parse(self, html):
        parser = ServicePageParser()
        parser.feed(html)
        return parser

    def test_each_page_has_required_semantics_and_metadata(self):
        titles = set()
        descriptions = set()

        for slug, html in self.pages.items():
            with self.subTest(slug=slug):
                document = self.parse(html)
                self.assertEqual(document.h1_count, 1)
                self.assertEqual(document.title_count, 1)
                self.assertTrue(document.title_text.endswith(" | KADYFER"))
                self.assertTrue(document.meta_description)
                self.assertTrue(document.has_skip_link)
                self.assertTrue(document.has_breadcrumb)
                self.assertGreaterEqual(document.details_count, 5)
                self.assertEqual(document.canonical_links, [])
                self.assertFalse(document.has_og_url)
                titles.add(document.title_text)
                descriptions.add(document.meta_description)

        self.assertEqual(len(titles), 6)
        self.assertEqual(len(descriptions), 6)

    def test_each_page_uses_shared_assets_with_file_safe_paths(self):
        for slug, html in self.pages.items():
            with self.subTest(slug=slug):
                document = self.parse(html)
                self.assertEqual(
                    document.stylesheets,
                    ["../styles.css", "../service-pages.css"],
                )
                self.assertEqual(document.scripts, ["../boot.js", "../script.js"])
                self.assertIn('href="../index.html"', html)
                self.assertIn('href="../index.html#servicios"', html)
                self.assertIn('src="../assets/', html)
                self.assertIn('href="../assets/brand/favicon.png"', html)

    def test_each_page_has_secure_specific_whatsapp_links(self):
        for slug, html in self.pages.items():
            service = SERVICES[slug]
            expected_url = build_whatsapp_url(service["whatsapp_message"])
            with self.subTest(slug=slug):
                document = self.parse(html)
                self.assertGreaterEqual(len(document.whatsapp_links), 3)
                for link in document.whatsapp_links:
                    self.assertEqual(link["href"], expected_url)
                    self.assertEqual(link.get("target"), "_blank")
                    self.assertIn("noopener", link.get("rel", ""))
                    self.assertIn("noreferrer", link.get("rel", ""))

    def test_external_links_are_opened_safely(self):
        for slug, html in self.pages.items():
            with self.subTest(slug=slug):
                for link in self.parse(html).external_links:
                    self.assertEqual(link.get("target"), "_blank")
                    self.assertIn("noopener", link.get("rel", ""))
                    self.assertIn("noreferrer", link.get("rel", ""))

    def test_each_page_has_an_explicitly_sized_hero_image(self):
        for slug, html in self.pages.items():
            with self.subTest(slug=slug):
                images = self.parse(html).images
                self.assertGreaterEqual(len(images), 2)
                hero_image = next(
                    image for image in images if "service-hero-image" in image.get("class", "")
                )
                self.assertTrue(hero_image.get("alt"))
                self.assertTrue(hero_image.get("width"))
                self.assertTrue(hero_image.get("height"))
                self.assertEqual(hero_image.get("fetchpriority"), "high")

    def test_breadcrumb_json_ld_is_valid_without_an_invented_domain(self):
        for slug, html in self.pages.items():
            with self.subTest(slug=slug):
                scripts = self.parse(html).json_ld
                self.assertEqual(len(scripts), 1)
                data = json.loads(scripts[0])
                self.assertEqual(data["@type"], "BreadcrumbList")
                self.assertEqual(len(data["itemListElement"]), 3)
                for item in data["itemListElement"]:
                    self.assertNotIn("item", item)

    def test_pending_service_urls_are_not_rendered(self):
        for slug, html in self.pages.items():
            with self.subTest(slug=slug):
                for pending_slug in PENDING_SLUGS:
                    self.assertNotIn(f"{pending_slug}.html", html)

    def test_prp_renders_three_distinct_application_areas(self):
        html = self.pages["plasma-rico-en-plaquetas-prp"]
        for heading in ("PRP facial", "PRP capilar", "PRP musculoesquelético"):
            self.assertIn(f"<h3>{heading}</h3>", html)


class ServicePageStyleTests(unittest.TestCase):
    def test_service_stylesheet_defines_the_shared_page_components(self):
        stylesheet_path = ROOT / "service-pages.css"
        self.assertTrue(stylesheet_path.exists())
        css = stylesheet_path.read_text(encoding="utf-8")

        for selector in (
            ".service-hero",
            ".breadcrumb",
            ".service-overview-grid",
            ".service-process-grid",
            ".service-mid-cta",
            ".considerations-grid",
            ".application-grid",
            ".related-grid",
        ):
            with self.subTest(selector=selector):
                self.assertIn(selector, css)

        self.assertIn("var(--gold)", css)
        self.assertIn("var(--section-space)", css)
        self.assertRegex(css, r"@media\s+\(min-width:\s*800px\)")

    def test_service_layout_is_mobile_first(self):
        css = (ROOT / "service-pages.css").read_text(encoding="utf-8")
        desktop_media = re.search(r"@media\s+\(min-width:\s*800px\)", css)
        self.assertIsNotNone(desktop_media)
        mobile_css = css[: desktop_media.start()]
        self.assertIn("grid-template-columns: minmax(0, 1fr);", mobile_css)
        self.assertIn("overflow-wrap: anywhere;", mobile_css)

    def test_existing_mobile_navigation_collapses_only_when_javascript_runs(self):
        css = (ROOT / "styles.css").read_text(encoding="utf-8")
        mobile_block = css[css.index("@media (max-width: 799px)") :]
        self.assertIn(".js .site-nav", mobile_block)
        self.assertNotRegex(
            mobile_block,
            r"(?m)^\s{2}\.site-nav\s*\{\s*\n\s*position:\s*absolute",
        )


class LandingIntegrationTests(unittest.TestCase):
    def test_shared_script_preserves_an_explicit_page_favicon(self):
        script = (ROOT / "script.js").read_text(encoding="utf-8")
        self.assertIn(
            'if (favicon.getAttribute("href") !== "data:,") return;',
            script,
        )

    def test_catalog_links_exactly_the_six_generated_service_pages(self):
        index_html = (ROOT / "index.html").read_text(encoding="utf-8")
        linked_slugs = set(
            re.findall(r'href="servicios/([^"]+)\.html"', index_html)
        )
        self.assertEqual(linked_slugs, EXPECTED_SLUGS)

        expected_catalog_links = {
            "desintoxicacion-ionica": "Desintoxicación Iónica",
            "terapia-neural": "Terapia Neural",
            "sueroterapia-ortomolecular": "Sueroterapia Ortomolecular",
            "terapia-fisica": "Terapia Física",
            "plasma-rico-en-plaquetas-prp": "PRP",
            "limpieza-facial-profunda": "Limpieza Facial Profunda",
        }
        for slug, name in expected_catalog_links.items():
            with self.subTest(slug=slug):
                self.assertIn(
                    f'<a href="servicios/{slug}.html">{name}</a>',
                    index_html,
                )

    def test_pending_catalog_services_remain_unlinked(self):
        index_html = (ROOT / "index.html").read_text(encoding="utf-8")
        for pending_slug in PENDING_SLUGS:
            with self.subTest(slug=pending_slug):
                self.assertNotIn(f"servicios/{pending_slug}.html", index_html)

    def test_all_local_html_references_resolve_to_existing_files(self):
        html_paths = [ROOT / "index.html", *sorted((ROOT / "servicios").glob("*.html"))]
        self.assertEqual(len(html_paths), 7)

        missing = []
        for html_path in html_paths:
            parser = ServicePageParser()
            parser.feed(html_path.read_text(encoding="utf-8"))

            for reference in parser.local_references:
                if reference.startswith(("http:", "https:", "tel:", "mailto:", "data:", "#")):
                    continue
                file_reference = reference.split("#", 1)[0].split("?", 1)[0]
                if not file_reference:
                    continue
                target = (html_path.parent / file_reference).resolve()
                if not target.exists():
                    missing.append(
                        f"{html_path.relative_to(ROOT)} -> {reference}"
                    )

        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
