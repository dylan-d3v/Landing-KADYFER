# KADYFER - Contexto para Paginas Individuales de Servicios

Fecha: 2026-06-09

## 1. Proposito

Este documento transfiere a la sesion del proyecto `Landing-KADYFER` todas las decisiones aprobadas para crear paginas estaticas individuales de servicios.

La landing principal ya esta implementada.

Las paginas individuales de servicios **todavia no han sido implementadas**. En la sesion de ideacion solo se aprobaron la plantilla, las reglas generales y el contenido de seis servicios.

La nueva sesion debe inspeccionar el repositorio real unicamente para adaptar la nueva plantilla a la estructura, estilos y componentes existentes de la landing. No debe buscar paginas de servicios ya implementadas, reconstruir la landing ni cambiar el stack sin necesidad.

No existe un archivo `AGENTS.md` conocido para este proyecto. Si la nueva sesion encuentra uno en el repositorio real, debera respetarlo; si no existe, debe continuar normalmente.

## 2. Objetivo

Convertir cada nombre del catalogo de la landing en un enlace hacia una pagina estatica propia.

Beneficios buscados:

- URL compartible por servicio.
- Mejor posicionamiento SEO.
- Funcionamiento sin JavaScript.
- Informacion mas clara para el cliente.
- CTA de WhatsApp especifico.
- Preguntas frecuentes y consideraciones propias.
- Landing principal ligera y sin modales extensos.

El enfoque aprobado es equilibrado:

- Contenido suficiente para educar y posicionar.
- Lenguaje sencillo para clientes.
- Conversion constante hacia WhatsApp.
- Sin diagnosticos ni promesas de resultados.

## 3. Stack y restricciones

Se debe conservar el stack existente de la landing.

Base esperada:

- HTML.
- CSS.
- JavaScript ligero.
- Sitio estatico.
- Sin backend.
- Sin base de datos.
- Sin login.
- Sin formularios que almacenen datos.

Antes de implementar:

1. Inspeccionar la estructura real del proyecto.
2. Identificar navbar, footer, variables CSS, tipografias y componentes existentes.
3. Reutilizar los patrones actuales.
4. Evitar duplicar CSS completo en cada pagina.
5. Proponer el plan de implementacion antes de modificar archivos.

## 4. Direccion visual

Las paginas deben conservar la identidad aprobada de la landing:

- Estilo premium clinico.
- Negro profundo.
- Dorado derivado del logo.
- Blanco calido.
- Tipografia y espaciado existentes.
- Fotografias reales y autorizadas.
- Apariencia profesional, ordenada y sobria.

No deben sentirse como un micrositio separado.

## 5. Plantilla comun aprobada

Se aprobo una estructura hibrida equilibrada.

Orden:

1. Navbar comun.
2. Breadcrumb.
3. Hero con categoria, H1, resumen, imagen y CTA de WhatsApp.
4. Explicacion sencilla: que es o en que consiste.
5. Para quien puede estar orientado.
6. Proceso general.
7. CTA intermedio contextual.
8. Consideraciones y valoracion previa.
9. Preparacion o cuidados, solo cuando aplique.
10. FAQ especifico.
11. Servicios relacionados selectivos.
12. CTA final.
13. Footer comun.

### Bloques obligatorios

- Breadcrumb con retorno.
- Hero.
- Informacion general.
- Orientacion.
- Proceso.
- Al menos dos CTAs.
- Consideraciones responsables.
- FAQ.
- Footer.

### Bloques condicionales

- Preparacion o cuidados.
- Imagenes secundarias.
- Servicios relacionados.

Los bloques condicionales se ocultan completamente cuando no existe contenido.

## 6. Servicios relacionados

Regla aprobada:

- Mostrar entre uno y tres servicios.
- Mostrar solamente relaciones claras.
- No rellenar tarjetas por simetría.
- Si no existe una relacion util, ocultar el bloque.
- No presentar servicios relacionados como equivalentes, obligatorios o secuenciales.

Relaciones aprobadas:

### Terapia Neural

- Terapia Fisica.
- Plasma Rico en Plaquetas (PRP).

### Sueroterapia Ortomolecular

- Terapia Neural.

### Limpieza Facial Profunda

- Dermapen y Fototerapia.
- Peelings, Hidratacion y Melasma.

### PRP

- Aplicacion facial: Dermapen y Fototerapia.
- Aplicacion capilar: sin relacionado obligatorio en el catalogo actual.
- Aplicacion musculoesqueletica: Terapia Fisica.

Las relaciones restantes deben definirse al redactar cada servicio pendiente.

## 7. Estrategia de expansion

Se aprobo expansion progresiva:

- Primera version: una pagina por cada item actual del catalogo.
- Mantener inicialmente los servicios agrupados.
- Separarlos en paginas individuales solo si existen demanda, contenido suficiente y validacion profesional.
- Si una URL se divide posteriormente, conservar SEO mediante redirecciones.

Ejemplos que permanecen agrupados inicialmente:

- Dermapen y Fototerapia.
- Peelings, Hidratacion y Melasma.
- Masajes Reductores y Post Quirurgico.

## 8. Mapa de URLs aprobado

### Medicos y regenerativos

- `/servicios/desintoxicacion-ionica.html`
- `/servicios/terapia-neural.html`
- `/servicios/sueroterapia-ortomolecular.html`
- `/servicios/terapia-fisica.html`
- `/servicios/plasma-rico-en-plaquetas-prp.html`

### Esteticos y dermocosmiatricos

- `/servicios/limpieza-facial-profunda.html`
- `/servicios/dermapen-y-fototerapia.html`
- `/servicios/peelings-hidratacion-y-melasma.html`
- `/servicios/eliminacion-de-lunares-y-verrugas.html`
- `/servicios/tratamientos-corporales.html`
- `/servicios/reduccion-de-medidas.html`
- `/servicios/masajes-reductores-y-post-quirurgico.html`

Reglas:

- Minusculas.
- Sin tildes.
- Palabras separadas por guiones.
- Sin IDs ni parametros.
- Una URL canonica por pagina.
- No cambiar una URL publicada sin redireccion.

## 9. Imagenes

Regla aprobada por pagina:

- Una imagen principal obligatoria.
- Maximo dos imagenes secundarias opcionales.
- Sin carrusel propio en la primera version.
- Fotos reales y autorizadas.
- Formatos optimizados para web.
- `srcset` cuando existan variantes.
- `loading="lazy"` fuera del primer viewport.
- Dimensiones explicitas.
- Texto alternativo util.

Si no existen imagenes secundarias, el diseño no debe dejar huecos.

## 10. WhatsApp

Numero:

`593983956295`

Cada pagina debe tener un mensaje propio, codificado correctamente en la URL.

Formato:

`https://wa.me/593983956295?text=MENSAJE_CODIFICADO`

Los CTAs deben usar el lenguaje aprobado para cada servicio.

Los enlaces externos deben abrirse de forma segura:

- `target="_blank"`
- `rel="noopener noreferrer"`

## 11. SEO tecnico

Cada pagina debe incluir:

- `<title>` unico: `Nombre del servicio | KADYFER`.
- Meta descripcion propia.
- Un solo `<h1>`.
- URL canonica.
- Open Graph.
- Imagen principal para compartir.
- Breadcrumb visible.
- Datos estructurados `BreadcrumbList`.
- Enlaces internos desde la landing.
- Enlaces a servicios relacionados.
- HTML semantico.
- `lang="es"`.

Evitar:

- Textos duplicados.
- Palabras clave forzadas.
- Datos estructurados medicos que impliquen certificaciones o hechos no verificados.
- Contenido oculto exclusivamente para buscadores.

## 12. Lenguaje responsable

Principios:

- Explicar, no diagnosticar.
- Usar “puede”, “puede estar orientado”, “segun valoracion” y “depende del caso”.
- No fijar resultados ni numero de sesiones sin evaluacion.
- No indicar que un servicio es apto para todas las personas.
- No sustituir valoracion medica o dermatologica.
- No publicar medicamentos, dosis, formulas o protocolos no confirmados.

Todo contenido medico debe validarse por el profesional responsable antes de publicarse.

## 13. Contenido aprobado: Terapia Neural

URL:

`/servicios/terapia-neural.html`

### Hero

Titulo:

> Terapia Neural

Resumen:

> Un abordaje medico personalizado que requiere valoracion previa para determinar si puede ser adecuado para tu caso.

CTA:

> Agendar valoracion por WhatsApp

### Que es

> Es un procedimiento medico en el que se realizan aplicaciones cuidadosamente seleccionadas de un anestesico local en puntos definidos durante la valoracion. La tecnica y los puntos de aplicacion dependen de los antecedentes y necesidades de cada persona.

El medicamento debe permanecer sin especificar.

No publicar:

- Nombre del anestesico.
- Dosis.
- Puntos de aplicacion.
- Numero recomendado de sesiones.
- Lista de enfermedades tratadas.

### Para quien

> Para personas que buscan una valoracion profesional de molestias persistentes o situaciones en las que el profesional considere pertinente este tipo de abordaje complementario.

### Proceso

> Conversacion clinica, revision de antecedentes, valoracion, explicacion del procedimiento y aplicacion solo si el profesional determina que corresponde.

### CTA intermedio

> No sabes si este servicio es para ti? Escribenos para coordinar una valoracion.

### Consideraciones

> No todas las personas son candidatas. Antes del procedimiento deben revisarse antecedentes, alergias, medicamentos, embarazo o lactancia y otras condiciones relevantes. Los resultados varian y no pueden garantizarse.

### FAQ

- Requiere valoracion previa?
- Que debo informar antes de la cita?
- Cuanto dura la sesion?
- Puedo retomar mis actividades?
- Cuantas sesiones necesito?

### CTA final

> Hola, quiero agendar una valoracion para Terapia Neural en KADYFER.

## 14. Contenido aprobado: Sueroterapia Ortomolecular

URL:

`/servicios/sueroterapia-ortomolecular.html`

La composicion debe permanecer general.

No enumerar:

- Vitaminas.
- Minerales.
- Medicamentos.
- Dosis.
- Formulas.
- Beneficios universales.

### Hero

Titulo:

> Sueroterapia Ortomolecular

Resumen:

> Administracion intravenosa de una formulacion seleccionada de manera individual, sujeta a valoracion profesional previa.

CTA:

> Consultar sueroterapia por WhatsApp

### Que es

> Es un procedimiento intravenoso mediante el cual se administran liquidos y componentes seleccionados por el profesional responsable. La formulacion no es igual para todas las personas y debe responder a la valoracion realizada.

### Para quien

> Para personas cuya valoracion profesional determine que una administracion intravenosa puede ser pertinente. La pagina no permite saber por si sola si el procedimiento es adecuado para un caso concreto.

### Proceso

> Revision de antecedentes y medicamentos, valoracion, seleccion del protocolo cuando corresponda, explicacion del procedimiento y administracion con seguimiento durante la sesion.

### CTA intermedio

> Quieres saber si este servicio puede ser adecuado para ti? Escribenos para coordinar una valoracion.

### Consideraciones

> No todas las personas son candidatas. Antes de la sesion deben revisarse alergias, medicamentos, antecedentes renales o cardiacos, embarazo o lactancia y otras condiciones relevantes. La composicion y duracion dependen del protocolo indicado.

### FAQ

- Requiere valoracion previa?
- La formula es igual para todos?
- Que informacion debo comunicar?
- Cuanto dura la sesion?
- Que cuidados debo seguir despues?

### CTA final

> Hola, quiero informacion sobre Sueroterapia Ortomolecular en KADYFER.

## 15. Contenido aprobado: Limpieza Facial Profunda

URL:

`/servicios/limpieza-facial-profunda.html`

### Hero

Titulo:

> Limpieza Facial Profunda

Resumen:

> Un protocolo de cuidado facial orientado a retirar impurezas, trabajar la congestion visible y complementar la rutina de la piel.

CTA:

> Consultar limpieza facial por WhatsApp

### En que consiste

> Es un procedimiento estetico que combina limpieza, preparacion de la piel y pasos seleccionados segun sus caracteristicas. Puede incluir extraccion controlada cuando corresponde, ademas de hidratacion y cuidado final.

### Para quien

> Para personas que desean complementar su cuidado facial o presentan acumulacion de impurezas y congestion visible. Si existe acne inflamatorio, irritacion intensa o una condicion dermatologica, puede requerirse otra valoracion.

### Proceso

> Observacion inicial de la piel, higiene, preparacion, extraccion solo cuando es adecuada, aplicacion de productos seleccionados, hidratacion y recomendaciones posteriores.

### CTA intermedio

> Quieres conocer el protocolo adecuado para tu piel? Escribenos y cuentanos que deseas mejorar.

### Consideraciones

> El protocolo puede cambiar segun sensibilidad, tratamientos recientes y estado de la piel. Puede presentarse enrojecimiento temporal. La limpieza facial no sustituye el tratamiento medico de acne, rosacea, dermatitis u otras enfermedades de la piel.

### FAQ

- La extraccion se realiza siempre?
- Es adecuada para piel sensible?
- Puedo maquillarme despues?
- Cada cuanto puede realizarse?
- Que debo informar antes de la cita?

### CTA final

> Hola, quiero informacion sobre Limpieza Facial Profunda en KADYFER.

## 16. Contenido aprobado: Desintoxicacion Ionica

URL:

`/servicios/desintoxicacion-ionica.html`

Decision:

- Conservar el nombre comercial “Desintoxicacion Ionica”.
- Mantener una descripcion neutral.
- No publicar una lista de beneficios clinicos no verificados.
- No entrar en debates sobre el color del agua.

### Hero

Titulo:

> Desintoxicacion Ionica

Resumen:

> Una sesion de bienestar y descanso realizada mediante un bano ionico de pies, en un entorno comodo y supervisado.

CTA:

> Consultar este servicio por WhatsApp

### En que consiste

> Los pies se colocan en un recipiente con agua mientras funciona un dispositivo ionico. La sesion se desarrolla en un ambiente preparado para brindar comodidad y relajacion.

### Para quien

> Para personas que desean incorporar una experiencia complementaria de bienestar y cuidado de los pies, siempre que no existan condiciones que requieran posponerla.

### Proceso

> Revision breve de consideraciones relevantes, preparacion del recipiente, inmersion de los pies durante el tiempo definido y recomendaciones basicas al finalizar.

### CTA intermedio

> Tienes dudas sobre si puedes realizar la sesion? Escribenos antes de agendar.

### Consideraciones

> Antes de la sesion deben informarse heridas, infecciones, irritacion, sensibilidad reducida u otras condiciones relevantes en los pies. El servicio puede posponerse si la piel requiere otro tipo de atencion.

### FAQ

- Cuanto dura la sesion?
- Que debo informar antes?
- Puedo realizarla si tengo una herida?
- Que debo llevar?
- Que cuidados siguen despues?

### CTA final

> Hola, quiero informacion sobre Desintoxicacion Ionica en KADYFER.

## 17. Contenido aprobado: Terapia Fisica

URL:

`/servicios/terapia-fisica.html`

Decision:

- No publicar credenciales del profesional.
- No atribuir una especialidad concreta.
- No listar tecnicas o equipos no confirmados.

### Hero

Titulo:

> Terapia Fisica

Resumen:

> Atencion personalizada orientada a acompanar el movimiento, la movilidad y el bienestar fisico segun las necesidades de cada persona.

CTA:

> Consultar Terapia Fisica por WhatsApp

### En que consiste

> Es una atencion basada en la valoracion del estado fisico y en la seleccion de actividades o recursos adecuados para acompanar objetivos de movilidad, recuperacion funcional y bienestar.

### Para quien

> Para personas que desean recibir orientacion sobre movilidad, rigidez, recuperacion fisica o retorno progresivo a sus actividades. La pertinencia del servicio depende de la valoracion inicial.

### Proceso

> Conversacion inicial, revision de antecedentes relevantes, observacion del movimiento, definicion de objetivos y aplicacion de un plan ajustado a la respuesta de la persona.

### CTA intermedio

> Cuentanos que deseas mejorar y te orientaremos sobre el siguiente paso.

### Consideraciones

> Deben informarse lesiones recientes, cirugias, dolor intenso, inflamacion, limitaciones importantes y recomendaciones medicas previas. Algunas situaciones requieren evaluacion o autorizacion medica antes de iniciar.

### FAQ

- Requiere valoracion previa?
- Que ropa debo usar?
- Que antecedentes debo informar?
- Cuanto dura una sesion?
- Cuantas sesiones pueden necesitarse?

### CTA final

> Hola, quiero informacion sobre Terapia Fisica en KADYFER.

## 18. Contenido aprobado: Plasma Rico en Plaquetas (PRP)

URL:

`/servicios/plasma-rico-en-plaquetas-prp.html`

La pagina debe separar claramente tres areas:

- Facial.
- Capilar.
- Musculoesqueletica.

### Hero

Titulo:

> Plasma Rico en Plaquetas (PRP)

Resumen:

> Procedimiento autologo que utiliza una preparacion obtenida de la propia sangre de la persona, segun el objetivo definido durante la valoracion.

CTA:

> Agendar valoracion para PRP

### Que es

> Se obtiene una muestra de sangre, se procesa para separar una fraccion con mayor concentracion de plaquetas y se aplica mediante el protocolo seleccionado. La preparacion, la zona y la tecnica dependen del objetivo y de la valoracion profesional.

### PRP facial

> Puede considerarse dentro de protocolos orientados al aspecto y la calidad de la piel. Los resultados y el nivel de evidencia varian segun la tecnica y el caso.

### PRP capilar

> Puede valorarse como parte de un abordaje para ciertas formas de perdida de cabello. Antes debe identificarse la causa y determinar si el procedimiento es pertinente.

### PRP musculoesqueletico

> Puede evaluarse en determinados problemas de tendones, articulaciones o tejidos blandos. La indicacion depende de la lesion, el diagnostico y otras opciones de tratamiento.

### CTA intermedio

> Selecciona el area que deseas consultar y coordinaremos una valoracion antes del procedimiento.

### Proceso

> Valoracion, revision de antecedentes, toma de una muestra de sangre, preparacion del PRP, aplicacion segun el protocolo y recomendaciones posteriores.

### Consideraciones

> Deben informarse medicamentos, alteraciones de coagulacion, infecciones, enfermedades activas, embarazo o lactancia y procedimientos recientes. Puede existir dolor, inflamacion, hematomas u otras reacciones locales.

### FAQ

- El PRP proviene de mi propia sangre?
- Requiere valoracion previa?
- La preparacion es igual para todos?
- Cuanto dura la sesion?
- Cuantas sesiones se necesitan?
- Cuando puedo retomar mis actividades?

### CTA final

> Hola, quiero agendar una valoracion para PRP en KADYFER.

## 19. Paginas pendientes de contenido

La siguiente sesion debe continuar el proceso de ideacion y aprobacion, una pagina a la vez o en grupos pequenos:

1. Dermapen y Fototerapia.
2. Peelings, Hidratacion y Melasma.
3. Eliminacion de Lunares y Verrugas.
4. Tratamientos Corporales.
5. Reduccion de Medidas.
6. Masajes Reductores y Post Quirurgico.

No implementar textos medicos inventados. Investigar con fuentes primarias u oficiales cuando sea necesario y solicitar detalles reales del servicio si cambian el contenido.

## 20. Estado de implementacion

Las decisiones de este documento fueron ideadas fuera del repositorio real de la landing.

Estado confirmado al crear este documento:

- Landing principal: implementada en otro proyecto/sesion.
- Plantilla de paginas de servicios: aprobada conceptualmente, no implementada.
- Paginas individuales de servicios: ninguna implementada.
- Enlaces del catalogo hacia paginas individuales: no implementados.
- Contenido aprobado: seis servicios.
- Contenido pendiente: seis servicios.

### Seis propuestas aprobadas

1. Terapia Neural.
2. Sueroterapia Ortomolecular.
3. Limpieza Facial Profunda.
4. Desintoxicacion Ionica.
5. Terapia Fisica.
6. Plasma Rico en Plaquetas (PRP).

El ultimo servicio aprobado en la sesion de ideacion fue **Plasma Rico en Plaquetas (PRP)**.

En la sesion `Landing-KADYFER`:

1. Inspeccionar el codigo actual de la landing para comprender su estructura.
2. Identificar navbar, footer, variables CSS, tipografias, componentes y convenciones reutilizables.
3. Confirmar que no existen paginas individuales de servicios implementadas.
4. Proponer el mecanismo mas simple para reutilizar navbar, footer y estructura.
5. No introducir un framework nuevo sin una razon tecnica clara.
6. Implementar primero la plantilla y las seis paginas con contenido aprobado.
7. No implementar las seis paginas pendientes hasta aprobar su contenido.
8. Convertir los nombres del catalogo en enlaces solo cuando las rutas correspondientes existan, evitando enlaces rotos.

## 21. Orden recomendado para continuar

1. Leer completamente este documento.
2. Inspeccionar el codigo real de la landing.
3. Resumir la estructura encontrada y las piezas reutilizables.
4. Definir la estrategia de plantilla comun compatible con el codigo existente.
5. Crear un plan de implementacion.
6. Implementar la plantilla comun.
7. Implementar las seis paginas aprobadas.
8. Actualizar el catalogo para enlazar solamente esas seis rutas existentes.
9. Verificar movil, escritorio, SEO, accesibilidad y WhatsApp.
10. Continuar la ideacion desde Dermapen y Fototerapia.
11. Aprobar el contenido de las seis paginas restantes.
12. Implementar las seis paginas restantes.
13. Completar todos los enlaces internos y relacionados.
14. Verificar que no existan enlaces rotos ni contenido duplicado.

## 22. Criterios de aceptacion

- Todas las paginas reutilizan la identidad visual de la landing.
- Funcionan desde 320 px.
- No existe desplazamiento horizontal.
- Cada pagina tiene H1, title, description, canonical y Open Graph propios.
- Breadcrumb visible y accesible.
- WhatsApp abre el mensaje correcto.
- Servicios relacionados aparecen solo cuando corresponden.
- Imagenes optimizadas y sin deformacion.
- No existen datos sensibles ni secretos.
- No existen afirmaciones medicas absolutas.
- No existen errores de consola.
- No existen enlaces rotos.
- El sitio funciona sin JavaScript para navegacion y contenido principal.

## 23. Prompt sugerido para la nueva sesion

> Vamos a implementar por primera vez las paginas individuales de servicios de la landing KADYFER.
>
> Lee completamente el archivo adjunto `KADYFER-service-pages-context.md`. Ese documento es la fuente de verdad para las decisiones aprobadas.
>
> Contexto importante:
>
> - La landing principal ya esta implementada en este proyecto.
> - Ninguna pagina individual de servicio ha sido implementada.
> - No existe un archivo `AGENTS.md` conocido; si encuentras uno, respetalo, y si no existe continua normalmente.
> - Ya fueron aprobados la plantilla comun, las 12 URLs, SEO, imagenes, WhatsApp, responsive, accesibilidad y servicios relacionados.
> - Ya existe contenido completo aprobado para seis servicios: Terapia Neural, Sueroterapia Ortomolecular, Limpieza Facial Profunda, Desintoxicacion Ionica, Terapia Fisica y Plasma Rico en Plaquetas (PRP).
> - El ultimo servicio aprobado fue PRP.
> - Quedan seis servicios sin contenido aprobado; no los implementes todavia.
>
> Antes de modificar codigo:
>
> 1. Inspecciona el repositorio actual de `Landing-KADYFER`.
> 2. Identifica el stack, estructura, navbar, footer, variables CSS, componentes y patrones existentes.
> 3. Confirma que no existen paginas individuales de servicios.
> 4. Explica como reutilizaras la identidad visual sin duplicar innecesariamente codigo o estilos.
> 5. Presenta un plan concreto para implementar primero la plantilla comun y las seis paginas aprobadas.
>
> No cambies el stack, no reconstruyas la landing y no implementes hasta que yo apruebe el plan.
>
> La implementacion debe conservar el estilo premium clinico, ser mobile-first desde 320 px, funcionar sin JavaScript para navegacion y contenido principal, incluir SEO propio, accesibilidad y mensajes especificos de WhatsApp.
