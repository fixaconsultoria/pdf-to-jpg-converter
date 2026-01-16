# 🔐 Autenticación en GitHub

El push falló porque necesitas autenticarte. Aquí tienes 3 opciones:

## Opción 1: GitHub CLI (Más Fácil) ⭐

```bash
# Instalar GitHub CLI (si no lo tienes)
brew install gh

# Autenticarse
gh auth login

# Seguir las instrucciones en pantalla
# Luego hacer push:
git push -u origin main
```

## Opción 2: Token de Acceso Personal

1. **Crear token en GitHub:**
   - Ir a: https://github.com/settings/tokens
   - Click "Generate new token" → "Generate new token (classic)"
   - Nombre: "PDF Converter"
   - Seleccionar scope: `repo` (marcar todo)
   - Click "Generate token"
   - **COPIAR EL TOKEN** (solo se muestra una vez)

2. **Usar el token al hacer push:**
   ```bash
   git push -u origin main
   # Username: tu-usuario-github
   # Password: PEGA-EL-TOKEN-AQUI
   ```

## Opción 3: Cambiar a SSH (Más Seguro)

1. **Generar clave SSH (si no tienes):**
   ```bash
   ssh-keygen -t ed25519 -C "tu-email@example.com"
   ```

2. **Agregar clave a GitHub:**
   ```bash
   # Copiar clave pública
   cat ~/.ssh/id_ed25519.pub
   # Copiar el output y agregarlo en:
   # https://github.com/settings/keys
   ```

3. **Cambiar remote a SSH:**
   ```bash
   git remote set-url origin git@github.com:fixaconsultoria/pdf-to-jpg-converter.git
   git push -u origin main
   ```

## Opción 4: GitHub Desktop (Más Visual)

1. Descargar: https://desktop.github.com
2. Abrir GitHub Desktop
3. File → Add Local Repository
4. Seleccionar la carpeta del proyecto
5. Click "Publish repository"
6. Seleccionar "fixaconsultoria/pdf-to-jpg-converter"
7. Click "Publish repository"

---

**Recomendación:** Opción 1 (GitHub CLI) es la más fácil y rápida.
