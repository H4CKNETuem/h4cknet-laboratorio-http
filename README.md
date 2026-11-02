# AuroraCorp · Portal de empleados — H4CKNET LAB 02

**Laboratorio local, con vulnerabilidades intencionadas y datos 100 % ficticios.**

## Arrancar

```bash
sudo docker compose up --build -d
sudo docker compose ps
```

Abre http://127.0.0.1:8080 desde el mismo Kali. Para detenerlo: `sudo docker compose down`.

Si ya tienes otra versión de AuroraCorp en el puerto 8080, detenla antes.

## Escenario

Participas en una revisión autorizada del portal interno de AuroraCorp. Se ha facilitado
una copia externa de una **nota de migración**, `credenciales_migracion.txt`,
para proporcionar el acceso inicial. El objetivo es analizar el portal y verificar
si las cuentas y recursos de otros departamentos están correctamente protegidos.

**Objetivo final:** encontrar el identificador del documento reservado de Dirección.

Puedes usar navegador, Burp Suite, curl, Bash y John/Hashcat. Documenta tus hallazgos.

## Archivos

- `credenciales_migracion.txt` — indicio externo para iniciar sesión; no está en el servidor.
- `wordlist-practica.txt` — diccionario educativo para la fase de comprobación de contraseñas.
- `app/` — código de la aplicación y plantilla del portal (no inspeccionarlo si quieres resolver el reto sin spoilers).

## Importante

- Portal disponible únicamente en `127.0.0.1:8080`; no se debe publicar en Internet.
- Las 200 cuentas son totalmente inventadas. No usar contraseñas reales.
- El código de la aplicación contiene el recorrido y el objetivo, porque el ZIP construye una imagen desde fuente. Si quieres conservar el misterio, evita leer `app/main.py` hasta terminar.
- La aplicación es deliberadamente insegura; no apta para producción.
- Diagnóstico: `sudo docker compose logs --tail=80`.
