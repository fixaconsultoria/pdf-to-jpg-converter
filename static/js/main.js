/**
 * Script principal para la herramienta PDF a JPG.
 * Código reutilizable que puede adaptarse para futuras herramientas.
 */

// Configuración de la API
const API_ENDPOINT = '/api/pdf-to-jpg/convert';
const MAX_FILE_SIZE = 20 * 1024 * 1024; // 20 MB

// Elementos del DOM
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const progressContainer = document.getElementById('progressContainer');
const progressFill = document.getElementById('progressFill');
const progressText = document.getElementById('progressText');
const resultContainer = document.getElementById('resultContainer');
const errorContainer = document.getElementById('errorContainer');
const downloadBtn = document.getElementById('downloadBtn');
const retryBtn = document.getElementById('retryBtn');
const errorMessage = document.getElementById('errorMessage');

// Variable para almacenar el blob de descarga
let downloadBlob = null;

/**
 * Inicialización de eventos
 */
function init() {
    // Click en el área de subida
    uploadArea.addEventListener('click', () => fileInput.click());
    
    // Drag and drop
    uploadArea.addEventListener('dragover', handleDragOver);
    uploadArea.addEventListener('dragleave', handleDragLeave);
    uploadArea.addEventListener('drop', handleDrop);
    
    // Cambio de archivo en el input
    fileInput.addEventListener('change', handleFileSelect);
    
    // Botones
    downloadBtn.addEventListener('click', handleDownload);
    retryBtn.addEventListener('click', resetForm);
    
    // Prevenir comportamiento por defecto del navegador en drag and drop
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false);
    });
}

/**
 * Prevenir comportamiento por defecto
 */
function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

/**
 * Manejar drag over
 */
function handleDragOver(e) {
    uploadArea.classList.add('dragover');
}

/**
 * Manejar drag leave
 */
function handleDragLeave(e) {
    uploadArea.classList.remove('dragover');
}

/**
 * Manejar drop de archivo
 */
function handleDrop(e) {
    uploadArea.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        processFile(files[0]);
    }
}

/**
 * Manejar selección de archivo
 */
function handleFileSelect(e) {
    const file = e.target.files[0];
    if (file) {
        processFile(file);
    }
}

/**
 * Validar y procesar archivo
 */
function processFile(file) {
    // Validar tipo
    if (!file.type.includes('pdf') && !file.name.toLowerCase().endsWith('.pdf')) {
        showError('Por favor, selecciona un archivo PDF válido.');
        return;
    }
    
    // Validar tamaño
    if (file.size > MAX_FILE_SIZE) {
        showError(`El archivo es demasiado grande. Tamaño máximo: ${(MAX_FILE_SIZE / 1024 / 1024).toFixed(0)} MB`);
        return;
    }
    
    // Ocultar otros contenedores
    hideAllContainers();
    
    // Mostrar progreso
    showProgress();
    
    // Subir y convertir
    uploadAndConvert(file);
}

/**
 * Subir archivo y convertir
 */
async function uploadAndConvert(file) {
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        // Simular progreso (ya que no tenemos eventos de progreso reales del servidor)
        simulateProgress();
        
        const response = await fetch(API_ENDPOINT, {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({ error: 'Error desconocido' }));
            throw new Error(errorData.error || `Error ${response.status}`);
        }
        
        // Obtener el blob del ZIP
        const blob = await response.blob();
        downloadBlob = blob;
        
        // Mostrar resultado
        showResult();
        
    } catch (error) {
        console.error('Error:', error);
        showError(error.message || 'Error al procesar el archivo. Por favor, intenta de nuevo.');
    }
}

/**
 * Simular progreso (puede mejorarse con eventos reales del servidor)
 */
function simulateProgress() {
    let progress = 0;
    const interval = setInterval(() => {
        progress += Math.random() * 15;
        if (progress >= 90) {
            progress = 90; // Mantener en 90% hasta que termine
            clearInterval(interval);
        }
        updateProgress(progress);
    }, 200);
}

/**
 * Actualizar barra de progreso
 */
function updateProgress(percent) {
    progressFill.style.width = `${percent}%`;
}

/**
 * Mostrar progreso
 */
function showProgress() {
    progressContainer.style.display = 'block';
    progressFill.style.width = '0%';
    progressText.textContent = 'Procesando tu PDF...';
}

/**
 * Mostrar resultado
 */
function showResult() {
    hideAllContainers();
    resultContainer.style.display = 'block';
    progressFill.style.width = '100%';
}

/**
 * Mostrar error
 */
function showError(message) {
    hideAllContainers();
    errorContainer.style.display = 'block';
    errorMessage.textContent = message;
}

/**
 * Ocultar todos los contenedores
 */
function hideAllContainers() {
    progressContainer.style.display = 'none';
    resultContainer.style.display = 'none';
    errorContainer.style.display = 'none';
}

/**
 * Manejar descarga
 */
function handleDownload() {
    if (downloadBlob) {
        const url = window.URL.createObjectURL(downloadBlob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `pdf_images_${Date.now()}.zip`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
        
        // Resetear después de descargar
        setTimeout(() => {
            resetForm();
        }, 1000);
    }
}

/**
 * Resetear formulario
 */
function resetForm() {
    hideAllContainers();
    fileInput.value = '';
    downloadBlob = null;
    uploadArea.classList.remove('dragover');
}

// Inicializar cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

/**
 * NOTA PARA FUTURAS HERRAMIENTAS:
 * 
 * Para crear una nueva herramienta, puedes:
 * 1. Copiar este archivo y adaptarlo
 * 2. Cambiar API_ENDPOINT al nuevo endpoint
 * 3. Ajustar validaciones según el tipo de archivo
 * 4. Modificar el flujo de conversión si es necesario
 * 
 * Ejemplo para PDF a PNG:
 * - Cambiar API_ENDPOINT a '/api/pdf-to-png/convert'
 * - Ajustar mensajes y textos
 */
