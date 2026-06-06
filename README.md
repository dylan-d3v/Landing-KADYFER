# Landing KADYFER

Landing estática mobile-first construida con HTML, CSS y JavaScript sin dependencias.

## Vista local

Desde PowerShell:

```powershell
python -m http.server 4173
```

Luego abrir `http://127.0.0.1:4173`.

## Configuración

Editar `siteConfig` al inicio de `script.js` para agregar dirección, mapa, horarios o redes. Los
campos vacíos no se renderizan.

Los recursos gráficos requeridos están documentados en `ASSETS.md`.

## Producción

- Publicar como contenido estático mediante HTTPS.
- Aplicar las cabeceras documentadas en `SECURITY-HEADERS.md`.
- Reemplazar o completar metadatos de dominio cuando exista la URL definitiva.
- Crear `sitemap.xml` únicamente cuando el dominio definitivo esté confirmado.
