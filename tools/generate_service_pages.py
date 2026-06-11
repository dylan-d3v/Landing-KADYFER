import argparse
import json
from html import escape
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "servicios"
SITE_URL = ""
WHATSAPP_NUMBER = "593983956295"


SERVICES = {
    "desintoxicacion-ionica": {
        "name": "Desintoxicación Iónica",
        "category": "Servicios médicos y regenerativos",
        "meta_description": (
            "Conoce la sesión de Desintoxicación Iónica de KADYFER, una "
            "experiencia complementaria de bienestar y cuidado de los pies."
        ),
        "summary": (
            "Una sesión de bienestar y descanso realizada mediante un baño "
            "iónico de pies, en un entorno cómodo y supervisado."
        ),
        "hero_cta": "Consultar este servicio por WhatsApp",
        "whatsapp_message": (
            "Hola, quiero información sobre Desintoxicación Iónica en KADYFER."
        ),
        "intro_heading": "¿En qué consiste?",
        "intro": (
            "Los pies se colocan en un recipiente con agua mientras funciona "
            "un dispositivo iónico. La sesión se desarrolla en un ambiente "
            "preparado para brindar comodidad y relajación."
        ),
        "orientation": (
            "Para personas que desean incorporar una experiencia "
            "complementaria de bienestar y cuidado de los pies, siempre que "
            "no existan condiciones que requieran posponerla."
        ),
        "process": [
            "Revisión breve de consideraciones relevantes.",
            "Preparación del recipiente e inmersión de los pies.",
            "Recomendaciones básicas al finalizar la sesión.",
        ],
        "areas": [],
        "intermediate_cta": (
            "¿Tienes dudas sobre si puedes realizar la sesión? Escríbenos "
            "antes de agendar."
        ),
        "considerations": (
            "Antes de la sesión deben informarse heridas, infecciones, "
            "irritación, sensibilidad reducida u otras condiciones relevantes "
            "en los pies. El servicio puede posponerse si la piel requiere "
            "otro tipo de atención."
        ),
        "preparation": "",
        "faq": [
            (
                "¿Cuánto dura la sesión?",
                "El tiempo se define según el protocolo del establecimiento y "
                "se confirma antes de comenzar.",
            ),
            (
                "¿Qué debo informar antes?",
                "Heridas, infecciones, irritación, sensibilidad reducida y "
                "otras condiciones relevantes de los pies.",
            ),
            (
                "¿Puedo realizarla si tengo una herida?",
                "Puede ser necesario posponerla hasta que la piel se encuentre "
                "en condiciones adecuadas.",
            ),
            (
                "¿Qué debo llevar?",
                "No necesitas elementos especiales; se recomienda asistir con "
                "ropa cómoda.",
            ),
            (
                "¿Qué cuidados siguen después?",
                "Mantener los pies limpios y secos y seguir cualquier "
                "indicación proporcionada al finalizar.",
            ),
        ],
        "image": "assets/gallery/hero-kadyfer.jpg",
        "image_alt": "Cabina principal de atención de KADYFER",
        "image_width": 1440,
        "image_height": 1080,
        "related": [],
    },
    "terapia-neural": {
        "name": "Terapia Neural",
        "category": "Servicios médicos y regenerativos",
        "meta_description": (
            "Conoce la Terapia Neural en KADYFER y agenda una valoración "
            "profesional para determinar si este abordaje puede ser adecuado."
        ),
        "summary": (
            "Un abordaje médico personalizado que requiere valoración previa "
            "para determinar si puede ser adecuado para tu caso."
        ),
        "hero_cta": "Agendar valoración por WhatsApp",
        "whatsapp_message": (
            "Hola, quiero agendar una valoración para Terapia Neural en KADYFER."
        ),
        "intro_heading": "¿Qué es la Terapia Neural?",
        "intro": (
            "Es un procedimiento médico en el que se realizan aplicaciones "
            "cuidadosamente seleccionadas de un anestésico local en puntos "
            "definidos durante la valoración. La técnica y los puntos de "
            "aplicación dependen de los antecedentes y necesidades de cada "
            "persona."
        ),
        "orientation": (
            "Para personas que buscan una valoración profesional de molestias "
            "persistentes o situaciones en las que el profesional considere "
            "pertinente este tipo de abordaje complementario."
        ),
        "process": [
            "Conversación clínica y revisión de antecedentes.",
            "Valoración y explicación del procedimiento.",
            "Aplicación solo si el profesional determina que corresponde.",
        ],
        "areas": [],
        "intermediate_cta": (
            "¿No sabes si este servicio es para ti? Escríbenos para coordinar "
            "una valoración."
        ),
        "considerations": (
            "No todas las personas son candidatas. Antes del procedimiento "
            "deben revisarse antecedentes, alergias, medicamentos, embarazo o "
            "lactancia y otras condiciones relevantes. Los resultados varían "
            "y no pueden garantizarse."
        ),
        "preparation": "",
        "faq": [
            (
                "¿Requiere valoración previa?",
                "Sí. La valoración permite revisar antecedentes y determinar "
                "si este procedimiento puede ser pertinente.",
            ),
            (
                "¿Qué debo informar antes de la cita?",
                "Alergias, medicamentos, embarazo o lactancia, enfermedades "
                "actuales y procedimientos recientes.",
            ),
            (
                "¿Cuánto dura la sesión?",
                "Depende de la valoración y del procedimiento indicado. Se "
                "informará antes de realizarlo.",
            ),
            (
                "¿Puedo retomar mis actividades?",
                "Depende de la zona tratada y de la respuesta individual. "
                "Recibirás indicaciones al finalizar.",
            ),
            (
                "¿Cuántas sesiones necesito?",
                "No existe un número igual para todas las personas. Se "
                "determina según valoración y evolución.",
            ),
        ],
        "image": "assets/gallery/05-terapia-neural.jpg",
        "image_alt": "Valoración de puntos para un procedimiento de Terapia Neural",
        "image_width": 899,
        "image_height": 1599,
        "related": ["terapia-fisica", "plasma-rico-en-plaquetas-prp"],
    },
    "sueroterapia-ortomolecular": {
        "name": "Sueroterapia Ortomolecular",
        "category": "Servicios médicos y regenerativos",
        "meta_description": (
            "Información sobre Sueroterapia Ortomolecular en KADYFER, un "
            "procedimiento intravenoso sujeto a valoración profesional previa."
        ),
        "summary": (
            "Administración intravenosa de una formulación seleccionada de "
            "manera individual, sujeta a valoración profesional previa."
        ),
        "hero_cta": "Consultar sueroterapia por WhatsApp",
        "whatsapp_message": (
            "Hola, quiero información sobre Sueroterapia Ortomolecular en KADYFER."
        ),
        "intro_heading": "¿Qué es la Sueroterapia Ortomolecular?",
        "intro": (
            "Es un procedimiento intravenoso mediante el cual se administran "
            "líquidos y componentes seleccionados por el profesional "
            "responsable. La formulación no es igual para todas las personas y "
            "debe responder a la valoración realizada."
        ),
        "orientation": (
            "Para personas cuya valoración profesional determine que una "
            "administración intravenosa puede ser pertinente. La página no "
            "permite saber por sí sola si el procedimiento es adecuado para un "
            "caso concreto."
        ),
        "process": [
            "Revisión de antecedentes y medicamentos.",
            "Valoración y selección del protocolo cuando corresponda.",
            "Administración con seguimiento durante la sesión.",
        ],
        "areas": [],
        "intermediate_cta": (
            "¿Quieres saber si este servicio puede ser adecuado para ti? "
            "Escríbenos para coordinar una valoración."
        ),
        "considerations": (
            "No todas las personas son candidatas. Antes de la sesión deben "
            "revisarse alergias, medicamentos, antecedentes renales o "
            "cardiacos, embarazo o lactancia y otras condiciones relevantes. "
            "La composición y duración dependen del protocolo indicado."
        ),
        "preparation": "",
        "faq": [
            (
                "¿Requiere valoración previa?",
                "Sí. La formulación y pertinencia deben definirse de manera "
                "individual.",
            ),
            (
                "¿La fórmula es igual para todos?",
                "No. Los componentes se seleccionan según la valoración "
                "profesional.",
            ),
            (
                "¿Qué información debo comunicar?",
                "Alergias, medicamentos, antecedentes renales o cardiacos, "
                "embarazo o lactancia y condiciones relevantes.",
            ),
            (
                "¿Cuánto dura la sesión?",
                "Depende del protocolo indicado. El tiempo se confirmará antes "
                "de la cita.",
            ),
            (
                "¿Qué cuidados debo seguir después?",
                "El profesional proporcionará indicaciones según el protocolo "
                "y tu respuesta durante la sesión.",
            ),
        ],
        "image": "assets/gallery/04-sueroterapia.jpg",
        "image_alt": "Aplicación supervisada de un procedimiento de sueroterapia",
        "image_width": 1100,
        "image_height": 1162,
        "related": ["terapia-neural"],
    },
    "terapia-fisica": {
        "name": "Terapia Física",
        "category": "Servicios médicos y regenerativos",
        "meta_description": (
            "Conoce la atención de Terapia Física en KADYFER, orientada a la "
            "movilidad, recuperación funcional y bienestar según valoración."
        ),
        "summary": (
            "Atención personalizada orientada a acompañar el movimiento, la "
            "movilidad y el bienestar físico según las necesidades de cada "
            "persona."
        ),
        "hero_cta": "Consultar Terapia Física por WhatsApp",
        "whatsapp_message": (
            "Hola, quiero información sobre Terapia Física en KADYFER."
        ),
        "intro_heading": "¿En qué consiste?",
        "intro": (
            "Es una atención basada en la valoración del estado físico y en la "
            "selección de actividades o recursos adecuados para acompañar "
            "objetivos de movilidad, recuperación funcional y bienestar."
        ),
        "orientation": (
            "Para personas que desean recibir orientación sobre movilidad, "
            "rigidez, recuperación física o retorno progresivo a sus "
            "actividades. La pertinencia del servicio depende de la valoración "
            "inicial."
        ),
        "process": [
            "Conversación inicial y revisión de antecedentes relevantes.",
            "Observación del movimiento y definición de objetivos.",
            "Aplicación de un plan ajustado a la respuesta de la persona.",
        ],
        "areas": [],
        "intermediate_cta": (
            "Cuéntanos qué deseas mejorar y te orientaremos sobre el siguiente "
            "paso."
        ),
        "considerations": (
            "Deben informarse lesiones recientes, cirugías, dolor intenso, "
            "inflamación, limitaciones importantes y recomendaciones médicas "
            "previas. Algunas situaciones requieren evaluación o autorización "
            "médica antes de iniciar."
        ),
        "preparation": "",
        "faq": [
            (
                "¿Requiere valoración previa?",
                "Sí. La valoración permite conocer tus necesidades, "
                "limitaciones y objetivos.",
            ),
            (
                "¿Qué ropa debo usar?",
                "Ropa cómoda que permita observar y movilizar la zona que será "
                "valorada.",
            ),
            (
                "¿Qué antecedentes debo informar?",
                "Lesiones, cirugías, dolor intenso, inflamación, diagnósticos y "
                "recomendaciones médicas previas.",
            ),
            (
                "¿Cuánto dura una sesión?",
                "Depende de la valoración y del plan seleccionado. Se informará "
                "al coordinar la atención.",
            ),
            (
                "¿Cuántas sesiones pueden necesitarse?",
                "Depende del objetivo, la evolución y la respuesta individual.",
            ),
        ],
        "image": "assets/gallery/hero-kadyfer.jpg",
        "image_alt": "Espacio de atención preparado en KADYFER",
        "image_width": 1440,
        "image_height": 1080,
        "related": [],
    },
    "limpieza-facial-profunda": {
        "name": "Limpieza Facial Profunda",
        "category": "Servicios estéticos y dermocosmiátricos",
        "meta_description": (
            "Conoce la Limpieza Facial Profunda de KADYFER, un protocolo "
            "personalizado para retirar impurezas y cuidar la piel."
        ),
        "summary": (
            "Un protocolo de cuidado facial orientado a retirar impurezas, "
            "trabajar la congestión visible y complementar la rutina de la piel."
        ),
        "hero_cta": "Consultar limpieza facial por WhatsApp",
        "whatsapp_message": (
            "Hola, quiero información sobre Limpieza Facial Profunda en KADYFER."
        ),
        "intro_heading": "¿En qué consiste?",
        "intro": (
            "Es un procedimiento estético que combina limpieza, preparación de "
            "la piel y pasos seleccionados según sus características. Puede "
            "incluir extracción controlada cuando corresponde, además de "
            "hidratación y cuidado final."
        ),
        "orientation": (
            "Para personas que desean complementar su cuidado facial o "
            "presentan acumulación de impurezas y congestión visible. Si existe "
            "acné inflamatorio, irritación intensa o una condición "
            "dermatológica, puede requerirse otra valoración."
        ),
        "process": [
            "Observación inicial, higiene y preparación de la piel.",
            "Extracción solo cuando es adecuada.",
            "Productos seleccionados, hidratación y recomendaciones posteriores.",
        ],
        "areas": [],
        "intermediate_cta": (
            "¿Quieres conocer el protocolo adecuado para tu piel? Escríbenos y "
            "cuéntanos qué deseas mejorar."
        ),
        "considerations": (
            "El protocolo puede cambiar según sensibilidad, tratamientos "
            "recientes y estado de la piel. Puede presentarse enrojecimiento "
            "temporal. La limpieza facial no sustituye el tratamiento médico "
            "de acné, rosácea, dermatitis u otras enfermedades de la piel."
        ),
        "preparation": "",
        "faq": [
            (
                "¿La extracción se realiza siempre?",
                "No. Solo se realiza cuando el estado de la piel permite "
                "hacerlo de forma adecuada.",
            ),
            (
                "¿Es adecuada para piel sensible?",
                "Puede adaptarse, pero primero debe observarse la sensibilidad "
                "y el estado actual de la piel.",
            ),
            (
                "¿Puedo maquillarme después?",
                "Generalmente se recomienda esperar y seguir las indicaciones "
                "recibidas para evitar irritación.",
            ),
            (
                "¿Cada cuánto puede realizarse?",
                "La frecuencia depende del tipo de piel, su estado y la rutina "
                "de cuidado.",
            ),
            (
                "¿Qué debo informar antes de la cita?",
                "Sensibilidad, alergias, tratamientos dermatológicos, productos "
                "activos y procedimientos recientes.",
            ),
        ],
        "image": "assets/gallery/03-limpieza-facial.jpg",
        "image_alt": "Aplicación de fototerapia durante un cuidado facial",
        "image_width": 899,
        "image_height": 1599,
        "related": [],
    },
    "plasma-rico-en-plaquetas-prp": {
        "name": "Plasma Rico en Plaquetas (PRP)",
        "category": "Servicios médicos y regenerativos",
        "meta_description": (
            "Información sobre Plasma Rico en Plaquetas en KADYFER para "
            "aplicaciones faciales, capilares y musculoesqueléticas."
        ),
        "summary": (
            "Procedimiento autólogo que utiliza una preparación obtenida de la "
            "propia sangre de la persona, según el objetivo definido durante "
            "la valoración."
        ),
        "hero_cta": "Agendar valoración para PRP",
        "whatsapp_message": (
            "Hola, quiero agendar una valoración para PRP en KADYFER."
        ),
        "intro_heading": "¿Qué es el PRP?",
        "intro": (
            "Se obtiene una muestra de sangre, se procesa para separar una "
            "fracción con mayor concentración de plaquetas y se aplica mediante "
            "el protocolo seleccionado. La preparación, la zona y la técnica "
            "dependen del objetivo y de la valoración profesional."
        ),
        "orientation": (
            "La valoración previa permite definir el área de aplicación, "
            "revisar antecedentes y determinar si este procedimiento puede ser "
            "pertinente para el objetivo de cada persona."
        ),
        "process": [
            "Valoración y revisión de antecedentes.",
            "Toma y preparación de una muestra de sangre.",
            "Aplicación según el protocolo y recomendaciones posteriores.",
        ],
        "areas": [
            (
                "PRP facial",
                "Puede considerarse dentro de protocolos orientados al aspecto "
                "y la calidad de la piel. Los resultados y el nivel de "
                "evidencia varían según la técnica y el caso.",
            ),
            (
                "PRP capilar",
                "Puede valorarse como parte de un abordaje para ciertas formas "
                "de pérdida de cabello. Antes debe identificarse la causa y "
                "determinar si el procedimiento es pertinente.",
            ),
            (
                "PRP musculoesquelético",
                "Puede evaluarse en determinados problemas de tendones, "
                "articulaciones o tejidos blandos. La indicación depende de la "
                "lesión, el diagnóstico y otras opciones de tratamiento.",
            ),
        ],
        "intermediate_cta": (
            "Selecciona el área que deseas consultar y coordinaremos una "
            "valoración antes del procedimiento."
        ),
        "considerations": (
            "Deben informarse medicamentos, alteraciones de coagulación, "
            "infecciones, enfermedades activas, embarazo o lactancia y "
            "procedimientos recientes. Puede existir dolor, inflamación, "
            "hematomas u otras reacciones locales."
        ),
        "preparation": "",
        "faq": [
            (
                "¿El PRP proviene de mi propia sangre?",
                "Sí. Se obtiene de una muestra de sangre de la propia persona.",
            ),
            (
                "¿Requiere valoración previa?",
                "Sí. Debe definirse el objetivo, la zona y si el procedimiento "
                "es pertinente.",
            ),
            (
                "¿La preparación es igual para todos?",
                "No necesariamente. Puede variar según el protocolo y el "
                "objetivo de la aplicación.",
            ),
            (
                "¿Cuánto dura la sesión?",
                "Incluye valoración, toma y procesamiento de la muestra y "
                "aplicación. El tiempo se confirma previamente.",
            ),
            (
                "¿Cuántas sesiones se necesitan?",
                "No existe una cantidad universal. Depende del área, el "
                "objetivo y la evolución.",
            ),
            (
                "¿Cuándo puedo retomar mis actividades?",
                "Depende del área tratada y de la respuesta individual. "
                "Recibirás indicaciones posteriores.",
            ),
        ],
        "image": "assets/gallery/hero-kadyfer.jpg",
        "image_alt": "Cabina principal de atención de KADYFER",
        "image_width": 1440,
        "image_height": 1080,
        "related": ["terapia-fisica"],
    },
}


def build_whatsapp_url(message):
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message, safe='')}"


def validate_services():
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
    generated_slugs = set(SERVICES)

    if len(SERVICES) != 6:
        raise ValueError("Exactly six approved services must be configured.")

    for slug, service in SERVICES.items():
        missing = required_fields.difference(service)
        extra = set(service).difference(required_fields)
        if missing or extra:
            raise ValueError(
                f"{slug} has invalid fields; missing={missing}, extra={extra}"
            )
        if any(not service[field] for field in required_fields - {"areas", "preparation", "related"}):
            raise ValueError(f"{slug} has empty required content.")
        if len(service["faq"]) < 5:
            raise ValueError(f"{slug} must include at least five FAQ entries.")
        if not set(service["related"]).issubset(generated_slugs):
            raise ValueError(f"{slug} references a service that is not generated.")


def render_service_page(slug, service):
    validate_services()

    def text(value):
        return escape(str(value), quote=True)

    whatsapp_url = build_whatsapp_url(service["whatsapp_message"])
    title = f"{service['name']} | KADYFER"
    image_url = f"../{service['image']}"
    page_path = f"servicios/{slug}.html"

    domain_metadata = ""
    breadcrumb_items = [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Inicio",
        },
        {
            "@type": "ListItem",
            "position": 2,
            "name": "Servicios",
        },
        {
            "@type": "ListItem",
            "position": 3,
            "name": service["name"],
        },
    ]

    if SITE_URL:
        site_root = SITE_URL.rstrip("/")
        page_url = f"{site_root}/{page_path}"
        domain_metadata = (
            f'    <link rel="canonical" href="{text(page_url)}">\n'
            f'    <meta property="og:url" content="{text(page_url)}">\n'
        )
        breadcrumb_items[0]["item"] = f"{site_root}/"
        breadcrumb_items[1]["item"] = f"{site_root}/#servicios"
        breadcrumb_items[2]["item"] = page_url

    breadcrumb_json = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": breadcrumb_items,
        },
        ensure_ascii=False,
        indent=2,
    )

    process_items = "\n".join(
        f"""              <li>
                <span class="process-number">{index:02d}</span>
                <p>{text(step)}</p>
              </li>"""
        for index, step in enumerate(service["process"], start=1)
    )

    areas_section = ""
    if service["areas"]:
        area_cards = "\n".join(
            f"""            <article class="application-area">
              <h3>{text(heading)}</h3>
              <p>{text(body)}</p>
            </article>"""
            for heading, body in service["areas"]
        )
        areas_section = f"""
      <section class="service-applications section-dark" aria-labelledby="applications-title">
        <div class="shell">
          <div class="service-section-heading">
            <p class="section-number" aria-hidden="true">03</p>
            <div>
              <p class="eyebrow">Áreas de aplicación</p>
              <h2 id="applications-title">Una valoración para cada objetivo</h2>
            </div>
          </div>
          <div class="application-grid">
{area_cards}
          </div>
        </div>
      </section>
"""

    preparation_section = ""
    if service["preparation"]:
        preparation_section = f"""
          <section class="consideration-block" aria-labelledby="preparation-title">
            <p class="card-label">Antes y después</p>
            <h2 id="preparation-title">Preparación y cuidados</h2>
            <p>{text(service["preparation"])}</p>
          </section>
"""

    faq_items = "\n".join(
        f"""            <details>
              <summary>
                <span>{text(question)}</span>
                <span class="faq-icon" aria-hidden="true"></span>
              </summary>
              <p>{text(answer)}</p>
            </details>"""
        for question, answer in service["faq"]
    )

    related_section = ""
    if service["related"]:
        related_cards = "\n".join(
            f"""            <a class="related-service" href="{text(related_slug)}.html">
              <span class="card-label">{text(SERVICES[related_slug]["category"])}</span>
              <strong>{text(SERVICES[related_slug]["name"])}</strong>
              <span class="related-service-action">Conocer el servicio</span>
            </a>"""
            for related_slug in service["related"]
        )
        related_section = f"""
      <section class="related-services section-warm" aria-labelledby="related-title">
        <div class="shell">
          <div class="service-section-heading">
            <p class="section-number" aria-hidden="true">07</p>
            <div>
              <p class="eyebrow eyebrow-dark">También puede interesarte</p>
              <h2 id="related-title">Servicios relacionados</h2>
            </div>
          </div>
          <div class="related-grid">
{related_cards}
          </div>
        </div>
      </section>
"""

    return f"""<!doctype html>
<html class="no-js" lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#0b0a09">
    <meta name="description" content="{text(service["meta_description"])}">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="es_EC">
    <meta property="og:site_name" content="KADYFER">
    <meta property="og:title" content="{text(title)}">
    <meta property="og:description" content="{text(service["meta_description"])}">
    <meta property="og:image" content="../assets/social/kadyfer-social-square.jpg">
{domain_metadata}    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{text(title)}">
    <meta name="twitter:description" content="{text(service["meta_description"])}">
    <meta name="twitter:image" content="../assets/social/kadyfer-social-square.jpg">
    <link rel="icon" type="image/png" href="../assets/brand/favicon.png">
    <script src="../boot.js"></script>
    <link rel="stylesheet" href="../styles.css">
    <link rel="stylesheet" href="../service-pages.css">
    <script src="../script.js" defer></script>
    <script type="application/ld+json">
{breadcrumb_json}
    </script>
    <title>{text(title)}</title>
  </head>
  <body class="service-page">
    <a class="skip-link" href="#contenido">Saltar al contenido</a>

    <header class="site-header" data-header>
      <div class="shell header-inner">
        <a class="brand" href="../index.html" aria-label="KADYFER, ir al inicio">
          <img
            class="brand-logo"
            src="../assets/brand/kadyfer-logo-header.png"
            alt="KADYFER"
            width="420"
            height="235"
          >
        </a>

        <button
          class="menu-toggle"
          type="button"
          aria-expanded="false"
          aria-controls="site-navigation"
          data-menu-toggle
        >
          <span class="menu-toggle-label">Menú</span>
          <span class="menu-toggle-icon" aria-hidden="true">
            <span></span>
            <span></span>
          </span>
        </button>

        <nav class="site-nav" id="site-navigation" aria-label="Navegación principal" data-nav>
          <a href="../index.html#servicios">Servicios</a>
          <a href="../index.html#enfoque">Enfoque</a>
          <a href="../index.html#galeria">Galería</a>
          <a href="../index.html#preguntas">Preguntas</a>
          <a
            class="nav-cta"
            href="{text(whatsapp_url)}"
            target="_blank"
            rel="noopener noreferrer"
          >
            WhatsApp
          </a>
        </nav>
      </div>
    </header>

    <main id="contenido">
      <section class="service-hero" aria-labelledby="service-title">
        <div class="shell">
          <nav class="breadcrumb" aria-label="Ruta de navegación">
            <ol>
              <li><a href="../index.html">Inicio</a></li>
              <li><a href="../index.html#servicios">Servicios</a></li>
              <li aria-current="page">{text(service["name"])}</li>
            </ol>
          </nav>

          <div class="service-hero-grid">
            <div class="service-hero-copy">
              <p class="eyebrow">{text(service["category"])}</p>
              <h1 id="service-title">{text(service["name"])}</h1>
              <p class="service-hero-summary">{text(service["summary"])}</p>
              <a
                class="button button-primary"
                href="{text(whatsapp_url)}"
                target="_blank"
                rel="noopener noreferrer"
              >
                {text(service["hero_cta"])}
                <svg aria-hidden="true" viewBox="0 0 20 20">
                  <path d="M4 10h11M11 5l5 5-5 5"></path>
                </svg>
              </a>
            </div>

            <figure class="service-hero-media">
              <img
                class="service-hero-image"
                src="{text(image_url)}"
                alt="{text(service["image_alt"])}"
                width="{service["image_width"]}"
                height="{service["image_height"]}"
                fetchpriority="high"
              >
              <figcaption>{text(service["name"])} · KADYFER</figcaption>
            </figure>
          </div>
        </div>
      </section>

      <section class="service-overview section-light" aria-labelledby="overview-title">
        <div class="shell service-overview-grid">
          <div>
            <p class="section-number" aria-hidden="true">01</p>
            <p class="eyebrow eyebrow-dark">Información general</p>
            <h2 id="overview-title">{text(service["intro_heading"])}</h2>
            <p class="lead">{text(service["intro"])}</p>
          </div>
          <article class="orientation-panel">
            <p class="card-label">Orientación</p>
            <h3>¿Para quién puede estar orientado?</h3>
            <p>{text(service["orientation"])}</p>
          </article>
        </div>
      </section>

      <section class="service-process section-warm" aria-labelledby="process-title">
        <div class="shell service-process-grid">
          <div>
            <p class="section-number" aria-hidden="true">02</p>
            <p class="eyebrow eyebrow-dark">Proceso general</p>
            <h2 id="process-title">Así se desarrolla la atención</h2>
            <p>El proceso puede ajustarse según la valoración y las necesidades de cada persona.</p>
          </div>
          <ol class="service-process-list">
{process_items}
          </ol>
        </div>
      </section>
{areas_section}
      <aside class="service-mid-cta section-gold" aria-label="Consulta por WhatsApp">
        <div class="shell service-mid-cta-inner">
          <p>{text(service["intermediate_cta"])}</p>
          <a
            class="button button-dark"
            href="{text(whatsapp_url)}"
            target="_blank"
            rel="noopener noreferrer"
          >
            Escribir por WhatsApp
            <svg aria-hidden="true" viewBox="0 0 20 20">
              <path d="M4 10h11M11 5l5 5-5 5"></path>
            </svg>
          </a>
        </div>
      </aside>

      <section class="service-considerations section-light" aria-labelledby="considerations-title">
        <div class="shell considerations-grid">
          <section class="consideration-block">
            <p class="section-number" aria-hidden="true">04</p>
            <p class="eyebrow eyebrow-dark">Antes de agendar</p>
            <h2 id="considerations-title">Consideraciones importantes</h2>
            <p>{text(service["considerations"])}</p>
          </section>
{preparation_section}        </div>
      </section>

      <section class="service-faq section-warm" aria-labelledby="faq-title">
        <div class="shell faq-grid">
          <div class="faq-intro">
            <p class="section-number" aria-hidden="true">05</p>
            <p class="eyebrow eyebrow-dark">Preguntas frecuentes</p>
            <h2 id="faq-title">Resolvemos tus primeras dudas</h2>
            <p>Para orientación sobre un caso particular, coordina una valoración profesional.</p>
          </div>
          <div class="faq-list">
{faq_items}
          </div>
        </div>
      </section>
{related_section}
      <section class="final-cta section-gold" aria-labelledby="final-cta-title">
        <div class="shell final-cta-inner">
          <p class="eyebrow eyebrow-dark">Atención personalizada</p>
          <h2 id="final-cta-title">Conversemos sobre {text(service["name"])}</h2>
          <p>Escríbenos para resolver tus dudas y coordinar el siguiente paso según tu caso.</p>
          <a
            class="button button-dark"
            href="{text(whatsapp_url)}"
            target="_blank"
            rel="noopener noreferrer"
          >
            {text(service["hero_cta"])}
            <svg aria-hidden="true" viewBox="0 0 20 20">
              <path d="M4 10h11M11 5l5 5-5 5"></path>
            </svg>
          </a>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="shell footer-grid">
        <div>
          <a class="footer-brand" href="../index.html">KADYFER</a>
          <p>Regeneración y estética biológica.</p>
        </div>
        <nav class="footer-nav" aria-label="Navegación del pie de página">
          <a href="../index.html#servicios">Servicios</a>
          <a href="../index.html#enfoque">Enfoque</a>
          <a href="../index.html#galeria">Galería</a>
          <a href="../index.html#preguntas">Preguntas</a>
        </nav>
        <div class="footer-contact">
          <p class="footer-label">Contacto</p>
          <a href="tel:+593983956295">+593 98 395 6295</a>
          <div data-optional-contact></div>
        </div>
      </div>
      <div class="shell footer-bottom">
        <p>© <span data-current-year>2026</span> KADYFER. Todos los derechos reservados.</p>
        <p>La información de este sitio no reemplaza una valoración profesional.</p>
      </div>
    </footer>
  </body>
</html>
"""


def generate_pages(check=False):
    validate_services()
    expected_pages = {
        OUTPUT_DIR / f"{slug}.html": render_service_page(slug, service)
        for slug, service in SERVICES.items()
    }

    if check:
        mismatches = []
        for path, expected in expected_pages.items():
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                mismatches.append(path.relative_to(ROOT))
        if mismatches:
            joined = ", ".join(str(path) for path in mismatches)
            raise SystemExit(f"Generated service pages are out of date: {joined}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for path, content in expected_pages.items():
        path.write_text(content, encoding="utf-8", newline="\n")
        print(f"Wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate KADYFER service pages.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail when committed pages do not match the generated output.",
    )
    arguments = parser.parse_args()
    generate_pages(check=arguments.check)
