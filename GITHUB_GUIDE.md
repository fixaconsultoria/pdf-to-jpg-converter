# 📦 Guía: Subir Proyecto a GitHub

## ¿Es necesario subir a GitHub?

### ✅ SÍ es necesario si usas:
- **Railway** - Requiere repositorio Git
- **Render** - Requiere repositorio Git
- **Heroku** - Requiere repositorio Git
- **Fly.io** - Puede usar Git o Docker

### ❌ NO es necesario si usas:
- **VPS tradicional** - Puedes subir archivos por SFTP/SCP
- **Docker en servidor propio** - Puedes subir archivos directamente
- **Algunos servicios** - Permiten subir ZIP

## 🚀 Pasos para Subir a GitHub

### Opción 1: Desde Terminal (Recomendado)

```bash
# 1. Inicializar Git (si no está inicializado)
git init

# 2. Agregar todos los archivos
git add .

# 3. Hacer commit inicial
git commit -m "Initial commit: PDF to JPG converter"

# 4. Crear repositorio en GitHub (desde la web)
#    - Ir a github.com
#    - Click en "New repository"
#    - Nombre: pdf-to-jpg-converter (o el que prefieras)
#    - NO marcar "Initialize with README"
#    - Click "Create repository"

# 5. Conectar con GitHub (reemplaza TU-USUARIO y TU-REPO)
git remote add origin https://github.com/TU-USUARIO/TU-REPO.git

# 6. Subir código
git branch -M main
git push -u origin main
```

### Opción 2: Desde GitHub Desktop (Más Fácil)

1. Descargar GitHub Desktop: https://desktop.github.com
2. Instalar y abrir
3. File → Add Local Repository
4. Seleccionar la carpeta del proyecto
5. Hacer commit inicial
6. Publish repository

### Opción 3: Desde VS Code

1. Abrir proyecto en VS Code
2. Click en el icono de Git (barra lateral)
3. Click en "Initialize Repository"
4. Agregar mensaje de commit
5. Click en "Publish to GitHub"
6. Seguir instrucciones

## ⚠️ Archivos que NO se suben (ya configurado en .gitignore):

- ✅ `.env` - Variables de entorno (seguridad)
- ✅ `venv/` - Entorno virtual
- ✅ `__pycache__/` - Archivos Python compilados
- ✅ `app/uploads/` - Archivos temporales
- ✅ `app/outputs/` - Archivos de salida
- ✅ `*.pdf`, `*.jpg`, `*.zip` - Archivos de prueba

## 🔒 Seguridad: Variables de Entorno

**IMPORTANTE:** El archivo `.env` NO se sube a GitHub (está en .gitignore).

**En el hosting, configura estas variables manualmente:**
- `SECRET_KEY` - Usar la del archivo `.env.generated.txt`
- `FLASK_ENV=production`
- `FLASK_DEBUG=False`

## 📝 Comandos Rápidos (Copia y Pega)

```bash
# Inicializar y subir
git init
git add .
git commit -m "Initial commit: PDF to JPG converter"

# Crear repo en GitHub primero, luego:
git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
git branch -M main
git push -u origin main
```

## 🎯 Después de Subir a GitHub

### Para Railway:
1. Ir a railway.app
2. "New Project" → "Deploy from GitHub repo"
3. Autorizar GitHub
4. Seleccionar tu repositorio
5. Deploy automático

### Para Render:
1. Ir a render.com
2. "New" → "Web Service"
3. Conectar GitHub
4. Seleccionar repositorio
5. Configurar y deploy

## ❓ ¿No quieres usar GitHub?

### Alternativa 1: Subir archivos directamente (VPS)
```bash
# Usando SCP
scp -r proyecto/ usuario@servidor:/ruta/destino/

# O usar SFTP (FileZilla, Cyberduck, etc.)
```

### Alternativa 2: Usar GitLab o Bitbucket
- Mismo proceso que GitHub
- Railway y Render también soportan GitLab/Bitbucket

### Alternativa 3: Docker sin Git
- Construir imagen localmente
- Subir a Docker Hub
- Usar desde cualquier hosting con Docker

---

**¿Necesitas ayuda con algún paso específico?** Puedo guiarte paso a paso.
