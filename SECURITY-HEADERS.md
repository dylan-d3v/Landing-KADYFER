# Cabeceras recomendadas para producción

Configurar estas cabeceras en el proveedor de hosting estático:

```text
Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; base-uri 'self'; form-action 'none'; frame-ancestors 'none'; upgrade-insecure-requests
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
Cross-Origin-Opener-Policy: same-origin
```

Servir todo el sitio mediante HTTPS y habilitar HSTS solamente cuando el dominio y todos sus
subdominios estén preparados para funcionar exclusivamente por HTTPS.
