# KADYFER Service Pages Design

## Estado y objetivo

La landing KADYFER es un sitio estático formado por HTML, CSS y JavaScript
nativo, sin dependencias, servidor, compilación ni dominio público. El objetivo
de esta fase es añadir por primera vez páginas individuales para los seis
servicios cuyo contenido ya fue aprobado:

1. Desintoxicación Iónica.
2. Terapia Neural.
3. Sueroterapia Ortomolecular.
4. Terapia Física.
5. Limpieza Facial Profunda.
6. Plasma Rico en Plaquetas (PRP).

No se crearán páginas, enlaces ni contenido provisional para los otros seis
servicios.

## Restricciones

- Conservar el stack existente.
- No reconstruir ni rediseñar la landing.
- Mantener HTML semántico como fuente del contenido principal.
- Permitir navegación y lectura al abrir `index.html` directamente mediante
  `file://`, sin servidor local y sin JavaScript.
- Diseñar mobile-first desde 320 px y evitar desplazamiento horizontal.
- No introducir afirmaciones médicas absolutas, diagnósticos, medicamentos,
  dosis, fórmulas ni protocolos no confirmados.
- Usar solamente imágenes existentes que representen de forma honesta el
  servicio o, cuando no exista una específica, una imagen general del espacio.

## Arquitectura

Los archivos públicos continuarán siendo HTML estático. Para evitar mantener
manualmente seis copias divergentes de la misma estructura, se añadirá un
generador de desarrollo escrito con la biblioteca estándar de Python.

El generador tendrá:

- Una plantilla común para cabecera, navegación, breadcrumb, estructura de
  contenido, CTA y pie de página.
- Una fuente de datos por servicio con sus metadatos, textos, FAQ, enlaces,
  imagen y servicios relacionados.
- Validaciones para impedir títulos, descripciones, H1, CTA o FAQ vacíos.
- Salida de seis archivos HTML completos dentro de `servicios/`.

Los archivos HTML generados quedarán versionados. Python no será necesario para
visitar o publicar el sitio.

## Estructura de archivos

- `index.html`: landing existente; recibirá enlaces solamente hacia las seis
  rutas implementadas.
- `styles.css`: sistema visual global existente, sin duplicación.
- `service-pages.css`: estilos exclusivos de la plantilla de servicios.
- `script.js`: mejora progresiva compartida; no será requisito para navegar.
- `tools/generate_service_pages.py`: datos, plantilla, escape de contenido y
  generación determinista.
- `servicios/desintoxicacion-ionica.html`
- `servicios/terapia-neural.html`
- `servicios/sueroterapia-ortomolecular.html`
- `servicios/terapia-fisica.html`
- `servicios/limpieza-facial-profunda.html`
- `servicios/plasma-rico-en-plaquetas-prp.html`

## Plantilla visual y semántica

Cada página seguirá este orden:

1. Skip link.
2. Navbar común.
3. Breadcrumb visible con enlace a `../index.html`.
4. Hero con categoría, H1, resumen, imagen y CTA de WhatsApp.
5. Explicación sencilla.
6. Orientación general.
7. Proceso.
8. CTA intermedio contextual.
9. Consideraciones y valoración previa.
10. Preparación o cuidados, únicamente cuando exista contenido aprobado.
11. FAQ con `details` y `summary`, funcional sin JavaScript.
12. Servicios relacionados, únicamente cuando la relación y la ruta existan.
13. CTA final.
14. Footer común.

Se reutilizarán las variables CSS, `.shell`, secciones de color, tipografías,
botones, foco visible, espaciado fluido, navbar y footer existentes. Los nuevos
estilos se limitarán a breadcrumb, hero de servicio, bloques informativos,
tarjetas relacionadas y adaptaciones responsive.

## Navegación sin JavaScript

Los enlaces desde páginas de servicio usarán rutas relativas compatibles con
archivos locales:

- Inicio: `../index.html`
- Servicios: `../index.html#servicios`
- Enfoque: `../index.html#enfoque`
- Galería: `../index.html#galeria`
- Preguntas: `../index.html#preguntas`

En móvil, la navegación será visible y utilizable por defecto. `boot.js`
marcará la disponibilidad de JavaScript antes de pintar la página; solo en ese
caso se activará el botón desplegable existente. Los CTA incluirán siempre un
`href` completo de WhatsApp, aunque el JavaScript no se ejecute.

## SEO sin dominio público

Cada página tendrá desde esta fase:

- `<title>` único.
- Meta descripción propia.
- Un solo H1.
- `lang="es"`.
- Open Graph y Twitter Card con contenido propio.
- Breadcrumb visible.
- JSON-LD `BreadcrumbList`.
- Imagen social.

Un canonical correcto debe ser una URL absoluta y no existe todavía una URL
pública definitiva. No se inventará un dominio ni se publicarán canonical
`file://`. El generador conservará `site_url` como configuración vacía:

- Mientras esté vacío, omitirá `canonical`, `og:url` y URLs absolutas del
  JSON-LD.
- Cuando el sitio sea publicado, bastará configurar el origen HTTPS y regenerar
  las páginas.
- Las etiquetas que no dependen del dominio se incluirán desde ahora.

## Imágenes

Las páginas utilizarán una imagen principal con dimensiones explícitas,
`object-fit`, texto alternativo útil y `fetchpriority="high"` cuando esté en el
primer viewport. No se añadirán imágenes secundarias si no aportan información.

Asignación inicial:

- Sueroterapia: imagen existente de sueroterapia.
- Terapia Neural: imagen existente de terapia neural.
- Limpieza Facial: imagen existente de limpieza o fototerapia.
- Desintoxicación Iónica: imagen general del espacio, salvo que se identifique
  una fotografía autorizada más específica.
- Terapia Física: imagen general del espacio.
- PRP: imagen general del espacio.

Las imágenes generales no se describirán como si mostraran el procedimiento.

## Servicios relacionados

- Terapia Neural: Terapia Física y PRP.
- Sueroterapia Ortomolecular: Terapia Neural.
- Limpieza Facial Profunda: bloque oculto en esta fase porque sus relaciones
  aprobadas todavía no tienen página.
- PRP: Terapia Física.
- Desintoxicación Iónica: bloque oculto.
- Terapia Física: bloque oculto hasta aprobar una relación en ese sentido.

Un enlace relacionado solo se renderizará si su archivo pertenece al conjunto
de páginas generadas.

## FAQ aprobadas

### Terapia Neural

- **¿Requiere valoración previa?** Sí. La valoración permite revisar
  antecedentes y determinar si este procedimiento puede ser pertinente.
- **¿Qué debo informar antes de la cita?** Alergias, medicamentos, embarazo o
  lactancia, enfermedades actuales y procedimientos recientes.
- **¿Cuánto dura la sesión?** Depende de la valoración y del procedimiento
  indicado. Se informará antes de realizarlo.
- **¿Puedo retomar mis actividades?** Depende de la zona tratada y de la
  respuesta individual. Recibirás indicaciones al finalizar.
- **¿Cuántas sesiones necesito?** No existe un número igual para todas las
  personas. Se determina según valoración y evolución.

### Sueroterapia Ortomolecular

- **¿Requiere valoración previa?** Sí. La formulación y pertinencia deben
  definirse de manera individual.
- **¿La fórmula es igual para todos?** No. Los componentes se seleccionan según
  la valoración profesional.
- **¿Qué información debo comunicar?** Alergias, medicamentos, antecedentes
  renales o cardiacos, embarazo o lactancia y condiciones relevantes.
- **¿Cuánto dura la sesión?** Depende del protocolo indicado. El tiempo se
  confirmará antes de la cita.
- **¿Qué cuidados debo seguir después?** El profesional proporcionará
  indicaciones según el protocolo y tu respuesta durante la sesión.

### Limpieza Facial Profunda

- **¿La extracción se realiza siempre?** No. Solo se realiza cuando el estado
  de la piel permite hacerlo de forma adecuada.
- **¿Es adecuada para piel sensible?** Puede adaptarse, pero primero debe
  observarse la sensibilidad y el estado actual de la piel.
- **¿Puedo maquillarme después?** Generalmente se recomienda esperar y seguir
  las indicaciones recibidas para evitar irritación.
- **¿Cada cuánto puede realizarse?** La frecuencia depende del tipo de piel, su
  estado y la rutina de cuidado.
- **¿Qué debo informar antes de la cita?** Sensibilidad, alergias, tratamientos
  dermatológicos, productos activos y procedimientos recientes.

### Desintoxicación Iónica

- **¿Cuánto dura la sesión?** El tiempo se define según el protocolo del
  establecimiento y se confirma antes de comenzar.
- **¿Qué debo informar antes?** Heridas, infecciones, irritación, sensibilidad
  reducida y otras condiciones relevantes de los pies.
- **¿Puedo realizarla si tengo una herida?** Puede ser necesario posponerla
  hasta que la piel se encuentre en condiciones adecuadas.
- **¿Qué debo llevar?** No necesitas elementos especiales; se recomienda
  asistir con ropa cómoda.
- **¿Qué cuidados siguen después?** Mantener los pies limpios y secos y seguir
  cualquier indicación proporcionada al finalizar.

### Terapia Física

- **¿Requiere valoración previa?** Sí. La valoración permite conocer tus
  necesidades, limitaciones y objetivos.
- **¿Qué ropa debo usar?** Ropa cómoda que permita observar y movilizar la zona
  que será valorada.
- **¿Qué antecedentes debo informar?** Lesiones, cirugías, dolor intenso,
  inflamación, diagnósticos y recomendaciones médicas previas.
- **¿Cuánto dura una sesión?** Depende de la valoración y del plan seleccionado.
  Se informará al coordinar la atención.
- **¿Cuántas sesiones pueden necesitarse?** Depende del objetivo, la evolución
  y la respuesta individual.

### Plasma Rico en Plaquetas

- **¿El PRP proviene de mi propia sangre?** Sí. Se obtiene de una muestra de
  sangre de la propia persona.
- **¿Requiere valoración previa?** Sí. Debe definirse el objetivo, la zona y si
  el procedimiento es pertinente.
- **¿La preparación es igual para todos?** No necesariamente. Puede variar
  según el protocolo y el objetivo de la aplicación.
- **¿Cuánto dura la sesión?** Incluye valoración, toma y procesamiento de la
  muestra y aplicación. El tiempo se confirma previamente.
- **¿Cuántas sesiones se necesitan?** No existe una cantidad universal. Depende
  del área, el objetivo y la evolución.
- **¿Cuándo puedo retomar mis actividades?** Depende del área tratada y de la
  respuesta individual. Recibirás indicaciones posteriores.

## Validación

La implementación deberá comprobar:

- Generación determinista de exactamente seis páginas.
- Ausencia de enlaces hacia páginas pendientes.
- Un H1, title y descripción no vacíos por página.
- Dos o más CTA de WhatsApp con el mensaje específico correcto.
- `target="_blank"` y `rel="noopener noreferrer"` en enlaces externos.
- Breadcrumb y navegación funcionales mediante `file://`.
- Contenido principal y FAQ disponibles sin JavaScript.
- Sin overflow horizontal a 320, 375, 768 y escritorio.
- Navegación por teclado, skip link y foco visible.
- Dimensiones y alt text de imágenes.
- HTML válido, JSON-LD válido cuando corresponda y ausencia de enlaces rotos.
- Ausencia de errores de consola con JavaScript habilitado.

## Fuera de alcance

- Publicación, hosting, dominio, sitemap y canonical absolutos.
- Nuevas imágenes o edición de fotografías.
- Contenido para los seis servicios pendientes.
- Formularios, backend, base de datos, login o almacenamiento.
- Rediseño general de la landing.
