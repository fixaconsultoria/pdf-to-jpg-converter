# 🚀 Guía Rápida de Despliegue

## ✅ Lo que YA tienes listo:

- ✅ Código de la aplicación
- ✅ `requirements.txt` (con gunicorn)
- ✅ `Procfile` (para Heroku/Railway)
- ✅ `Dockerfile` (para Docker)
- ✅ `docker-compose.yml` (para desarrollo/producción)
- ✅ `.gitignore` (configurado)

## 📦 Lo que NECESITAS hacer:

### 1. Variables de Entorno

Crea un archivo `.env` (NO subirlo a Git):

```bash
SECRET_KEY=tu-clave-super-segura-aqui
FLASK_ENV=production
FLASK_DEBUG=False
PORT=5000
```

**Generar SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 2. Requisitos del Servidor

**Software necesario:**
- Python 3.8+
- poppler-utils (para convertir PDFs)
- Gunicorn (ya está en requirements.txt)

**Instalar poppler:**
```bash
# Ubuntu/Debian
sudo apt install poppler-utils

# macOS (local)
brew install poppler

# CentOS/RHEL
sudo yum install poppler-utils
```

## 🌐 Opciones de Hosting (Elige una):

### Opción A: Heroku (Más fácil)

1. Instalar Heroku CLI
2. `heroku login`
3. `heroku create tu-app`
4. `heroku config:set SECRET_KEY=tu-clave`
5. `git push heroku main`

**Ventajas:** Muy fácil, maneja todo automáticamente
**Desventajas:** Puede ser costoso, necesita Aptfile para poppler

### Opción B: Railway / Render (Recomendado)

1. Conectar repositorio Git
2. Configurar variables de entorno en el dashboard
3. Deploy automático

**Ventajas:** Gratis para empezar, fácil de usar
**Desventajas:** Límites en plan gratuito

### Opción C: VPS (DigitalOcean, Linode, etc.)

**Pasos:**
1. Crear servidor Ubuntu
2. SSH al servidor
3. Instalar: `sudo apt install python3 python3-pip python3-venv nginx poppler-utils`
4. Clonar proyecto
5. Crear venv e instalar dependencias
6. Configurar Gunicorn + Nginx
7. Configurar SSL con Let's Encrypt

**Ventajas:** Control total, más barato a largo plazo
**Desventajas:** Requiere más configuración

### Opción D: Docker (Cualquier hosting con Docker)

1. `docker build -t pdf-converter .`
2. `docker run -d -p 5000:5000 --env-file .env pdf-converter`

**Ventajas:** Funciona en cualquier lado, fácil de escalar
**Desventajas:** Requiere conocimiento de Docker

## ⚡ Comandos Rápidos por Hosting:

### Heroku:
```bash
heroku create
heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
git push heroku main
```

### Railway/Render:
- Conectar Git → Configurar variables → Deploy automático

### VPS (Ubuntu):
```bash
# En el servidor
git clone tu-repo.git
cd proyecto
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn app:app
```

### Docker:
```bash
docker-compose up -d
```

## 🔒 Checklist ANTES de subir:

- [ ] Cambiar SECRET_KEY a valor seguro
- [ ] FLASK_DEBUG=False
- [ ] Probar localmente con `gunicorn app:app`
- [ ] Verificar que poppler funciona
- [ ] Configurar HTTPS (SSL)
- [ ] Revisar .gitignore (no subir .env)

## 📝 Archivos Importantes:

- `requirements.txt` - Dependencias Python
- `Procfile` - Para Heroku/Railway
- `Dockerfile` - Para Docker
- `.env` - Variables (NO subir a Git)
- `DEPLOY.md` - Guía completa detallada

## 🆘 Problemas Comunes:

**"poppler not found"**
→ Instalar: `sudo apt install poppler-utils`

**"Port already in use"**
→ Cambiar puerto en .env o configuración

**"Module not found"**
→ `pip install -r requirements.txt`

**"Permission denied"**
→ Verificar permisos de carpetas uploads/outputs

---

**¿Necesitas más detalles?** Revisa `DEPLOY.md` para guías completas de cada opción.
