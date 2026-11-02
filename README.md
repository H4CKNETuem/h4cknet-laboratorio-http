# H4CKNET LAB 02 — Expediente Aurora 🦊

### Laboratorio de HTTP, Burp Suite y seguridad web

Bienvenido al laboratorio de **H4cknet**. En esta práctica trabajarás con **AuroraCorp**, un portal corporativo ficticio que hemos preparado para aprender cómo se comunican el navegador y un servidor, cómo funcionan las peticiones HTTP y cómo analizarlas con herramientas como Burp Suite.

No hace falta tener experiencia previa en pentesting: la idea es **aprender probando** y entender qué ocurre detrás de una página web.

> **Importante:** este entorno se ha creado únicamente con fines educativos. Se ejecuta en tu propio equipo y contiene comportamientos inseguros de forma intencionada. No lo publiques en Internet ni lo utilices contra sistemas ajenos.

## 📚 ¿Qué vamos a practicar?

- Entender la diferencia entre peticiones **GET** y **POST**.
- Identificar **URL, parámetros, cabeceras, cookies y cuerpos** de las peticiones HTTP.
- Interceptar y examinar tráfico web con **Burp Suite**.
- Repetir y modificar peticiones para observar cómo responde la aplicación.
- Utilizar **cURL** para realizar peticiones desde la terminal.
- Investigar el funcionamiento de un portal web mediante una metodología básica de pentesting.

**No se incluyen soluciones en este README:** parte del aprendizaje está en investigar el laboratorio por tu cuenta.

## 🧰 Requisitos

- **Docker Desktop** (Windows/macOS) o **Docker Engine con Docker Compose** (Linux).
- Un navegador web.
- **Burp Suite Community Edition** (recomendado para seguir el taller).
- Una terminal para ejecutar los comandos.

## 🚀 Instalación y puesta en marcha

### 1. Descargar el laboratorio

En este repositorio, pulsa **Code → Download ZIP** y descomprime el archivo. También puedes clonarlo si ya utilizas Git:

```bash
git clone https://github.com/TU-USUARIO/h4cknet-laboratorio-http.git
```

> Si lo descargas como ZIP, **no necesitas instalar Git**. La dirección anterior es un ejemplo: sustituye `TU-USUARIO` por la cuenta u organización donde esté publicado este repositorio.

### 2. Arrancar Docker

Abre una terminal en la carpeta del proyecto que contenga el archivo `docker-compose.yml` (o `compose.yml`) y ejecuta:

```bash
docker compose up -d --build
```

La primera ejecución puede tardar un poco porque Docker tendrá que preparar las imágenes.

### 3. Abrir el laboratorio

Con los contenedores en marcha, entra desde el navegador en:

**http://127.0.0.1:8080**

Si todo ha ido bien, aparecerá el portal de **AuroraCorp**.

### 4. Parar el laboratorio

Cuando termines, desde la misma carpeta ejecuta:

```bash
docker compose down
```

## 🔎 Primeros pasos

1. Navega por el portal e identifica qué acciones puedes realizar.
2. Abre las herramientas de desarrollador de tu navegador y observa la pestaña **Red / Network**.
3. Localiza las peticiones que se producen al cambiar de página o enviar un formulario.
4. Configura Burp Suite para interceptar el tráfico del navegador.
5. Envía alguna petición a **Repeater** y comprueba qué cambia al modificar sus parámetros.
6. Intenta repetir peticiones sencillas desde la terminal con cURL.

**Pista:** no te quedes únicamente con lo que se ve en pantalla. Fíjate también en lo que el navegador envía y en lo que devuelve el servidor.

## 💻 Un ejemplo con cURL

Para ver la respuesta HTTP de la página principal:

```bash
curl -i http://127.0.0.1:8080/
```

La opción `-i` muestra también las cabeceras de la respuesta. Puedes comparar lo que devuelve cURL con lo que ves en Burp Suite.

## 🛠️ Problemas frecuentes

**Docker no arranca:** comprueba que Docker Desktop está abierto o que el servicio Docker está en ejecución.

**No carga `127.0.0.1:8080`:** verifica que los contenedores estén iniciados con:

```bash
docker compose ps
```

**El puerto 8080 ya está ocupado:** Burp Suite suele utilizar ese puerto para su proxy. Puedes cambiar el puerto del *listener* de Burp o, si tu archivo Compose publica el puerto `8080` del contenedor, cambiar su mapeo a `127.0.0.1:8081:8080`. En ese caso, abre el laboratorio en **http://127.0.0.1:8081**.

**Quieres ver los errores de los contenedores:** ejecuta:

```bash
docker compose logs
```

## 🦊 Sobre H4cknet

**H4cknet** es una iniciativa para aprender ciberseguridad ofensiva desde cero mediante explicaciones claras, talleres y laboratorios prácticos. Aquí lo importante es comprender las herramientas y saber por qué haces cada cosa, no copiar comandos sin más.

Si has llegado desde el vídeo, ¡bienvenido al laboratorio! Ponte a probar, rompe cosas (dentro de la máquina, claro 😎) y aprende.

## 📄 Licencia

El código de este repositorio se distribuye bajo la **licencia MIT**. Consulta el archivo [`LICENSE`](LICENSE) para conocer sus condiciones.
