# KADYFER Landing Page - Especificacion de Diseno

Fecha: 2026-06-06

## 1. Objetivo

Crear una landing page estatica, profesional y responsive para KADYFER, orientada a:

- Presentar servicios medicos, regenerativos, esteticos y dermocosmiatricos.
- Generar confianza mediante contenido claro, imagenes reales y lenguaje responsable.
- Convertir visitas en conversaciones de WhatsApp.
- Lanzar rapidamente sin exponer una base de datos, un panel administrativo ni datos sensibles.

La landing publica y el futuro ERP/CRM seran proyectos separados.

## 2. Alcance del MVP

### Incluido

- Landing de una sola pagina.
- HTML semantico, CSS y JavaScript ligero.
- Diseno mobile-first y responsive.
- Logo e identidad visual KADYFER.
- Catalogo completo de servicios.
- Tres servicios prioritarios.
- Galeria con fotos reales.
- Preguntas frecuentes.
- Enlaces de WhatsApp con mensajes prellenados.
- Metadatos basicos para SEO y redes sociales.
- Campos opcionales para ubicacion, horarios y redes.

### Excluido

- Login o autenticacion.
- Base de datos publica.
- Formularios que almacenen informacion.
- Comentarios abiertos.
- Agenda automatizada.
- Pagos en linea.
- Panel administrativo.
- Integracion con IA, n8n o APIs privadas.
- ERP/CRM.

## 3. Arquitectura

### Landing publica

Sitio estatico desplegado mediante HTTPS. Sus unicos datos dinamicos seran configuraciones locales incluidas durante la compilacion o carga de la pagina.

Componentes principales:

- Navegacion.
- Hero.
- Confianza rapida.
- Servicios prioritarios.
- Catalogo completo.
- Enfoque KADYFER.
- Galeria.
- Preguntas frecuentes.
- CTA final.
- Footer.

### ERP/CRM futuro

Proyecto independiente para uso interno, con arquitectura MVC, autenticacion, roles, auditoria, base de datos y respaldos. No compartira acceso directo con la landing publica.

## 4. Identidad visual

Direccion aprobada: premium clinico.

Paleta base:

- Negro profundo para fondos principales.
- Dorado derivado del logo para acentos y CTAs.
- Blanco calido para fondos secundarios.
- Marron oscuro y dorado tenue para textos y bordes complementarios.

Principios visuales:

- Apariencia elegante, ordenada y profesional.
- Mucho espacio visual y jerarquia tipografica clara.
- Bordes discretos y radios pequenos.
- Sin decoracion excesiva ni efectos que compitan con el contenido.
- Fotos reales, luminosas y limpias.

Uso de marca:

- Logo transparente sobre fondos oscuros.
- Version cuadrada 1:1 para favicon, Open Graph, tarjetas o superficies claras.

## 5. Navegacion

Elementos principales:

- Servicios.
- Enfoque.
- Galeria.
- Preguntas.
- WhatsApp.

En escritorio, la navegacion permanecera visible y compacta. En movil, usara un menu accesible y un CTA de WhatsApp claramente identificable.

## 6. Contenido aprobado

### 6.1 Hero

Eyebrow:

> Expertos en regeneracion y estetica biologica

Titulo:

> Tratamientos esteticos y regenerativos con atencion personalizada

Descripcion:

> Sueroterapia, terapia neural y tratamientos faciales y corporales disenados segun tus necesidades, con valoracion profesional y enfoque responsable.

CTA:

> Agendar por WhatsApp

Microconfianza:

> Respuesta directa al +593 98 395 6295

Servicios destacados:

- Sueroterapia.
- Terapia neural.
- Faciales y corporales.

Imagen sugerida:

- Cabina premium.
- Atencion profesional.
- Detalle de tratamiento facial.

No se usara una imagen clinica fuerte o un antes/despues como imagen principal.

### 6.2 Confianza rapida

Titulo:

> Cuidado estetico con criterio profesional

Texto:

> Combinamos estetica, bienestar y regeneracion biologica para orientar cada tratamiento segun tus necesidades y objetivos.

Puntos:

- Valoracion personalizada antes de recomendar un protocolo.
- Atencion enfocada en bienestar, piel y recuperacion estetica.
- Comunicacion directa para resolver dudas y agendar por WhatsApp.

### 6.3 Servicios prioritarios

#### Sueroterapia Ortomolecular

Etiqueta:

> Bienestar y soporte nutricional

Descripcion:

> Protocolos intravenosos orientados a apoyar el bienestar general, segun valoracion profesional.

CTA:

> Consultar sueroterapia

#### Terapia Neural

Etiqueta:

> Enfoque regulador

Descripcion:

> Atencion personalizada para valorar tu caso y definir si este abordaje es adecuado para tus necesidades.

CTA:

> Agendar valoracion

#### Faciales y Corporales

Etiqueta:

> Piel, figura y dermocosmiatria

Descripcion:

> Limpieza profunda, dermapen, peelings, hidratacion, reduccion de medidas y cuidado post quirurgico.

CTA:

> Ver faciales y corporales

### 6.4 Catalogo completo

#### Servicios medicos y regenerativos

Titulo de grupo:

> Bienestar y regeneracion

Introduccion:

> Opciones orientadas a acompanar el bienestar general y la recuperacion, siempre con valoracion profesional.

Servicios:

- Desintoxicacion Ionica.
- Terapia Neural.
- Sueroterapia Ortomolecular.
- Terapia Fisica.
- PRP.

#### Servicios esteticos y dermocosmiatricos

Titulo de grupo:

> Piel, figura y cuidado estetico

Introduccion:

> Tratamientos para el cuidado facial y corporal con enfoque personalizado y acompanamiento responsable.

Servicios:

- Limpieza Facial Profunda.
- Dermapen y Fototerapia.
- Peelings, Hidratacion y Melasma.
- Eliminacion de Lunares y Verrugas.
- Tratamientos Corporales.
- Reduccion de Medidas.
- Masajes Reductores y Post Quirurgico.

### 6.5 Enfoque KADYFER

Titulo:

> Un proceso pensado para tus necesidades

Texto:

> Antes de recomendar un tratamiento, escuchamos tus objetivos, valoramos tu caso y orientamos un protocolo adecuado para ti.

Pasos:

1. Conversamos: conocemos tus necesidades y resolvemos tus primeras dudas.
2. Valoramos: revisamos tu caso antes de recomendar un servicio o protocolo.
3. Acompanamos: brindamos indicaciones y seguimiento segun el tratamiento realizado.

### 6.6 Galeria

Titulo:

> Un espacio preparado para tu cuidado

Texto:

> Conoce nuestros espacios, parte del proceso de atencion y resultados compartidos con autorizacion.

Contenido:

- Una foto principal del local o cabina.
- Fotos del equipo o de la atencion.
- Tratamiento facial.
- Sueroterapia.
- Uno o dos resultados autorizados.
- Entre seis y nueve fotos en el MVP.

### 6.7 Preguntas frecuentes

#### Necesito una valoracion antes de agendar?

Algunos tratamientos requieren una valoracion previa para conocer tus necesidades y orientarte adecuadamente.

#### Como se cual tratamiento es adecuado para mi?

Puedes escribirnos por WhatsApp. Revisaremos tus objetivos y te indicaremos el siguiente paso.

#### Cuanto dura una sesion?

La duracion depende del servicio y del protocolo recomendado. Te informaremos antes de confirmar la cita.

#### Los resultados son iguales para todas las personas?

No. Cada persona responde de forma distinta y los resultados dependen del caso, el tratamiento y los cuidados indicados.

#### Como puedo agendar?

Pulsa cualquiera de los botones de WhatsApp y cuentanos que servicio te interesa.

### 6.8 CTA final

Eyebrow:

> Da el primer paso

Titulo:

> Agenda tu valoracion en KADYFER

Texto:

> Cuentanos que servicio te interesa y te orientaremos para coordinar tu atencion.

CTA:

> Escribir por WhatsApp

### 6.9 Footer

Contenido inicial:

- KADYFER.
- Regeneracion y estetica biologica.
- Telefono: +593 98 395 6295.
- Navegacion interna.

Campos opcionales:

- Direccion.
- Enlace de Google Maps.
- Horarios.
- Instagram.
- Facebook.
- Otras redes.

Los campos opcionales no se renderizaran mientras esten vacios.

## 7. WhatsApp

Numero:

`593983956295`

Enlace general:

`https://wa.me/593983956295?text=Hola%2C%20quiero%20agendar%20una%20valoracion%20en%20KADYFER.`

Sueroterapia:

`https://wa.me/593983956295?text=Hola%2C%20quiero%20informacion%20sobre%20Sueroterapia%20Ortomolecular%20en%20KADYFER.`

Terapia Neural:

`https://wa.me/593983956295?text=Hola%2C%20quiero%20agendar%20una%20valoracion%20para%20Terapia%20Neural%20en%20KADYFER.`

Faciales y Corporales:

`https://wa.me/593983956295?text=Hola%2C%20quiero%20informacion%20sobre%20tratamientos%20faciales%20y%20corporales%20en%20KADYFER.`

Todos los enlaces abriran en una nueva pestaña e incluiran atributos seguros para enlaces externos.

## 8. Configuracion editable

La informacion variable se centralizara en un unico archivo u objeto de configuracion.

Ejemplo conceptual:

```js
const siteConfig = {
  whatsappNumber: "593983956295",
  address: "",
  mapsUrl: "",
  schedule: "",
  instagramUrl: "",
  facebookUrl: ""
};
```

Los componentes opcionales comprobaran si existe un valor antes de mostrarse.

## 9. Seguridad y privacidad

- No almacenar datos personales en la landing.
- No solicitar cedula, diagnosticos, historias clinicas ni fotografias mediante formularios web.
- No incluir credenciales, tokens o claves de API en JavaScript.
- Usar HTTPS en produccion.
- Mantener el ERP/CRM separado de la web publica.
- Evitar dependencias innecesarias y scripts de terceros no esenciales.
- Aplicar una politica de seguridad de contenido compatible con los recursos utilizados.
- Configurar cabeceras como `X-Content-Type-Options`, `Referrer-Policy` y proteccion contra framing desde el hosting.
- Mantener los enlaces externos con `rel="noopener noreferrer"` cuando corresponda.

Las fotos de pacientes, rostros o resultados solo se publicaran con autorizacion. No contendran nombres, fichas, mensajes, documentos ni otros datos identificables.

## 10. Contenido responsable

El sitio usara expresiones como:

- Valoracion personalizada.
- Segun cada caso.
- Protocolos profesionales.
- Acompanamiento.
- Orientado a apoyar.
- Puede ayudar.

Se evitaran afirmaciones como:

- Cura.
- Garantizado.
- Sin riesgos.
- Resultados permanentes.
- Elimina definitivamente.

La informacion del sitio sera promocional e informativa y no reemplazara una valoracion profesional.

## 11. Accesibilidad

- Contraste suficiente entre texto y fondo.
- Navegacion operable con teclado.
- Indicadores de foco visibles.
- Textos alternativos utiles en imagenes informativas.
- Imagenes decorativas con texto alternativo vacio.
- Botones y enlaces con nombres claros.
- FAQ implementado con controles accesibles.
- Soporte para `prefers-reduced-motion`.
- Tamano tactil adecuado en botones de movil.
- Estructura correcta de encabezados.

## 12. Responsive

La pagina debe funcionar como minimo en:

- Moviles desde 320 px.
- Tablets.
- Escritorio.
- Pantallas anchas.

El hero mostrara parte de la siguiente seccion en los viewports principales. Las tarjetas se apilaran en movil y no habra texto recortado ni elementos superpuestos.

## 13. Rendimiento

- Imagenes convertidas a formatos modernos cuando sea posible.
- Variantes responsive mediante `srcset`.
- Carga diferida fuera del primer viewport.
- Dimensiones explicitas para evitar saltos de layout.
- CSS y JavaScript minimos.
- Sin frameworks pesados para el MVP.
- Fuentes limitadas y optimizadas.

Objetivos:

- Lighthouse Performance de 90 o superior en condiciones razonables.
- Sin errores de consola.
- Sin enlaces rotos.
- Carga visual rapida en movil.

## 14. SEO y metadatos

- Titulo descriptivo de pagina.
- Meta descripcion.
- Etiquetas Open Graph.
- Imagen cuadrada KADYFER para compartir.
- Favicon.
- HTML semantico.
- `lang="es"`.
- Datos estructurados de negocio local cuando existan direccion y horarios verificados.
- Sitemap y robots.txt si el hosting y dominio lo requieren.

No se publicaran datos estructurados incompletos o inventados.

## 15. Comportamiento y errores

Al ser un sitio estatico:

- Si JavaScript falla, el contenido principal continuara visible.
- Los links de WhatsApp se generaran con valores conocidos y codificados.
- Los campos opcionales vacios no generaran bloques ni enlaces.
- Las imagenes tendran dimensiones y textos alternativos.
- Los errores 404 dependeran de la configuracion del hosting.

## 16. Pruebas

### Funcionales

- Cada CTA abre el mensaje correcto en WhatsApp.
- La navegacion interna lleva a la seccion correspondiente.
- Los campos opcionales aparecen solo cuando contienen valores.
- La FAQ abre y cierra correctamente.
- No existen enlaces vacios.

### Visuales

- Verificacion en movil, tablet y escritorio.
- Sin desbordamientos horizontales.
- Sin superposicion de elementos.
- Logo legible sobre fondos oscuros y claros.
- Galeria proporcionada y sin deformaciones.

### Accesibilidad

- Recorrido completo con teclado.
- Foco visible.
- Contraste.
- Etiquetas y nombres accesibles.
- Prueba con movimiento reducido.

### Seguridad

- Sin secretos en el codigo fuente.
- Sin formularios de datos personales.
- Cabeceras del hosting verificadas.
- Dependencias revisadas si se incorpora alguna.

## 17. Criterios de aceptacion

El MVP estara listo cuando:

1. Todas las secciones aprobadas esten implementadas.
2. La pagina sea responsive desde 320 px.
3. Los cuatro flujos de WhatsApp funcionen.
4. El logo y las imagenes reales carguen correctamente.
5. La galeria use unicamente material autorizado.
6. Los campos opcionales vacios permanezcan ocultos.
7. No existan errores de consola ni enlaces rotos.
8. Se cumplan los controles basicos de accesibilidad.
9. El sitio pueda desplegarse por HTTPS como contenido estatico.
10. El ERP/CRM y cualquier dato sensible queden fuera del proyecto.

## 18. Evolucion posterior

Orden recomendado:

1. Lanzar la landing estatica.
2. Agregar direccion, horarios y redes cuando esten disponibles.
3. Medir clics a WhatsApp con una solucion respetuosa de privacidad.
4. Crear el ERP/CRM como proyecto privado e independiente.
5. Evaluar automatizaciones con n8n y WhatsApp.
6. Evaluar IA o RAG solo cuando exista una necesidad concreta y contenido validado.
