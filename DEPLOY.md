# Guía de Despliegue a Producción

Esta guía explica todo lo necesario para subir la aplicación a un servidor de hosting.

## 📋 Requisitos del Servidor

### Software Necesario:
- **Python 3.8+** (recomendado 3.10 o superior)
- **poppler-utils** (para conversión de PDF)
- **Servidor WSGI** (Gunicorn recomendado)
- **Servidor web** (Nginx o Apache como reverse proxy)

### Recursos Recomendados:
- **RAM:** Mínimo 512 MB (1 GB recomendado)
- **CPU:** 1 core mínimo
- **Almacenamiento:** 5-10 GB (para archivos temporales)
- **Ancho de banda:** Según tráfico esperado

## 🔧 Preparación del Código

### 1. Actualizar requirements.txt para Producción

Agrega Gunicorn y otras dependencias de producción:

```txt
Flask>=3.0.0
pdf2image>=1.16.3
Pillow>=10.2.0
Werkzeug>=3.0.1
gunicorn>=21.2.0
```

### 2. Variables de Entorno

Crea un archivo `.env` (NO subirlo a Git) con:

```bash
SECRET_KEY=tu-clave-secreta-super-segura-aqui-cambiar-en-produccion
FLASK_ENV=production
FLASK_DEBUG=False
PORT=5000
```

**⚠️ IMPORTANTE:** Genera una SECRET_KEY segura:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 3. Configuración de Seguridad

Asegúrate de que `app/__init__.py` use variables de entorno:

```python
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
```

## 🚀 Opciones de Hosting

### Opción 1: VPS (DigitalOcean, Linode, AWS EC2, etc.)

#### Pasos:

1. **Conectar al servidor:**
```bash
ssh usuario@tu-servidor.com
```

2. **Instalar dependencias del sistema:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv nginx poppler-utils

# CentOS/RHEL
sudo yum install python3 python3-pip nginx poppler-utils
```

3. **Clonar/Subir el proyecto:**
```bash
# Opción A: Git
git clone tu-repositorio.git
cd tu-proyecto

# Opción B: SCP/SFTP
# Subir archivos manualmente
```

4. **Crear entorno virtual:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

5. **Configurar variables de entorno:**
```bash
nano .env
# Agregar las variables mencionadas arriba
```

6. **Crear archivo de servicio systemd:**
```bash
sudo nano /etc/systemd/system/pdf-converter.service
```

Contenido del servicio:
```ini
[Unit]
Description=PDF to JPG Converter Gunicorn Service
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/ruta/a/tu/proyecto
Environment="PATH=/ruta/a/tu/proyecto/venv/bin"
EnvironmentFile=/ruta/a/tu/proyecto/.env
ExecStart=/ruta/a/tu/proyecto/venv/bin/gunicorn \
    --workers 4 \
    --bind 127.0.0.1:5000 \
    --timeout 120 \
    app:app

[Install]
WantedBy=multi-user.target
```

7. **Iniciar el servicio:**
```bash
sudo systemctl daemon-reload
sudo systemctl enable pdf-converter
sudo systemctl start pdf-converter
sudo systemctl status pdf-converter
```

8. **Configurar Nginx como reverse proxy:**
```bash
sudo nano /etc/nginx/sites-available/pdf-converter
```

Contenido de Nginx:
```nginx
server {
    listen 80;
    server_name tu-dominio.com www.tu-dominio.com;

    client_max_body_size 20M;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 120s;
    }

    location /static {
        alias /ruta/a/tu/proyecto/static;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

9. **Habilitar sitio y reiniciar Nginx:**
```bash
sudo ln -s /etc/nginx/sites-available/pdf-converter /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

10. **Configurar SSL con Let's Encrypt (HTTPS):**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d tu-dominio.com -d www.tu-dominio.com
```

### Opción 2: Plataformas como Servicio (PaaS)

#### Heroku

1. **Instalar Heroku CLI:**
```bash
# macOS
brew tap heroku/brew && brew install heroku

# O descargar desde: https://devcenter.heroku.com/articles/heroku-cli
```

2. **Crear Procfile:**
```
web: gunicorn app:app
```

3. **Crear runtime.txt:**
```
python-3.11.0
```

4. **Actualizar requirements.txt** (agregar gunicorn)

5. **Desplegar:**
```bash
heroku login
heroku create tu-app-nombre
heroku config:set SECRET_KEY=tu-clave-secreta
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-apt
heroku buildpacks:add heroku/python

# Crear Aptfile para poppler
echo "poppler-utils" > Aptfile

git push heroku main
```

**Nota:** Heroku requiere configuración adicional para poppler.

#### Railway

1. Conectar repositorio Git
2. Configurar variables de entorno en el dashboard
3. Railway detecta automáticamente Python y ejecuta la app

#### Render

1. Conectar repositorio Git
2. Seleccionar "Web Service"
3. Comando de inicio: `gunicorn app:app`
4. Configurar variables de entorno

#### PythonAnywhere

1. Subir archivos vía web o Git
2. Configurar web app en el dashboard
3. Usar archivo WSGI: `/home/tu-usuario/mi-proyecto/app.py`
4. Instalar dependencias en la consola Bash

### Opción 3: Docker (Recomendado para escalabilidad)

#### Crear Dockerfile:

```dockerfile
FROM python:3.11-slim

# Instalar poppler
RUN apt-get update && apt-get install -y \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación
COPY . .

# Crear carpetas necesarias
RUN mkdir -p app/uploads app/outputs

# Variables de entorno
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Exponer puerto
EXPOSE 5000

# Comando de inicio
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "app:app"]
```

#### Crear docker-compose.yml:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - FLASK_ENV=production
    volumes:
      - ./app/uploads:/app/app/uploads
      - ./app/outputs:/app/app/outputs
    restart: unless-stopped
```

#### Desplegar con Docker:

```bash
docker build -t pdf-converter .
docker run -d -p 5000:5000 --env-file .env pdf-converter
```

## 🔒 Checklist de Seguridad

Antes de poner en producción:

- [ ] Cambiar `SECRET_KEY` a un valor seguro y aleatorio
- [ ] Configurar `FLASK_DEBUG=False`
- [ ] Habilitar HTTPS (SSL/TLS)
- [ ] Configurar firewall (solo puertos 80, 443)
- [ ] Configurar límites de rate limiting
- [ ] Revisar permisos de archivos (uploads/outputs)
- [ ] Configurar backups automáticos
- [ ] Monitoreo de logs
- [ ] Configurar límites de memoria/CPU

## 📊 Monitoreo y Mantenimiento

### Ver logs:
```bash
# Systemd
sudo journalctl -u pdf-converter -f

# Docker
docker logs -f nombre-contenedor

# Gunicorn directamente
tail -f /var/log/gunicorn/error.log
```

### Reiniciar servicio:
```bash
sudo systemctl restart pdf-converter
```

### Actualizar aplicación:
```bash
git pull
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart pdf-converter
```

## 🌐 Configuración de Dominio

1. **Configurar DNS:**
   - A record apuntando a la IP del servidor
   - CNAME para www (opcional)

2. **Verificar en Nginx:**
   - Actualizar `server_name` con tu dominio

3. **Renovar SSL:**
   - Let's Encrypt se renueva automáticamente
   - Verificar: `sudo certbot renew --dry-run`

## 💰 Consideraciones de Costo

- **VPS:** $5-20/mes (DigitalOcean, Linode)
- **Heroku:** $7-25/mes (dyno básico)
- **Railway/Render:** $5-20/mes (según uso)
- **Dominio:** $10-15/año
- **SSL:** Gratis (Let's Encrypt)

## 🐛 Troubleshooting

### Error: "poppler not found"
```bash
# Verificar instalación
which pdftoppm

# Instalar si falta
sudo apt install poppler-utils
```

### Error: "Permission denied"
```bash
# Ajustar permisos
sudo chown -R www-data:www-data /ruta/a/proyecto
sudo chmod -R 755 /ruta/a/proyecto
```

### Error: "Port already in use"
```bash
# Ver qué usa el puerto
sudo lsof -i :5000

# Cambiar puerto en configuración
```

### Aplicación lenta
- Aumentar workers de Gunicorn
- Optimizar imágenes (reducir DPI si es necesario)
- Implementar CDN para archivos estáticos

## 📝 Archivos Necesarios para Producción

Asegúrate de tener estos archivos listos:

1. ✅ `requirements.txt` (con gunicorn)
2. ✅ `.env` (con SECRET_KEY)
3. ✅ `Procfile` (para Heroku)
4. ✅ `Dockerfile` (si usas Docker)
5. ✅ Configuración de Nginx
6. ✅ Archivo de servicio systemd

## 🚀 Comando Rápido de Despliegue (VPS)

```bash
# En el servidor
git clone tu-repo.git
cd tu-proyecto
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn

# Configurar .env
nano .env

# Probar localmente
gunicorn app:app

# Si funciona, configurar systemd y nginx (ver arriba)
```

---

**¿Necesitas ayuda con algún paso específico?** Cada hosting tiene sus particularidades, pero estos son los pasos generales que funcionan en la mayoría de casos.
