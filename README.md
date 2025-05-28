# 🎬 Unir Video y Audio

**🌍 [Read this in English](README_EN.md)**

Script de Python para unir automáticamente archivos de video y audio utilizando FFmpeg. Este script procesa carpetas con archivos de video y sus correspondientes pistas de audio por separado, generando videos finales con ambos elementos combinados.

## 📋 Requisitos Previos

Antes de usar este script, asegúrate de tener instalado:

1. **Python 3.7 o superior**
2. **FFmpeg** (instalado en el sistema)

### Instalación de FFmpeg

#### En macOS (usando Homebrew):
```bash
brew install ffmpeg
```

#### En Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### En Windows:
1. Descarga FFmpeg desde [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extrae el archivo y añade la carpeta `bin` al PATH del sistema

## 🚀 Configuración del Entorno

### 1. Crear un entorno virtual de Python

```bash
# Navegar al directorio del proyecto
cd unir-video-audio

# Crear el entorno virtual
python3 -m venv video

# Activar el entorno virtual
# En macOS/Linux:
source video/bin/activate

# En Windows:
video\Scripts\activate
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## 📁 Estructura de Carpetas

El script espera la siguiente estructura de directorios:

```
unir-video-audio/
├── main.py
├── requirements.txt
├── README.md
├── originales/           # Carpeta con archivos fuente
│   ├── 01/
│   │   ├── video.mp4     # Archivo de video principal
│   │   └── video-audio.mp4  # Archivo de audio (debe contener "-audio" en el nombre)
│   ├── 02/
│   │   ├── otro_video.mp4
│   │   └── otro_video-audio.mp4
│   └── ...
└── output/               # Carpeta de salida (se crea automáticamente)
    ├── 01/
    │   └── video_final.mp4
    ├── 02/
    │   └── video_final.mp4
    └── ...
```

### Importante:
- Los archivos de audio **deben** contener `-audio` en su nombre
- Los archivos de video **no deben** contener `-audio` en su nombre
- Todos los archivos deben tener extensión `.mp4`
- Las subcarpetas pueden tener cualquier nombre (01, 02, episodio1, etc.)

## 🎯 Uso del Script

### 1. Activar el entorno virtual (si no está activo)

```bash
source video/bin/activate
```

### 2. Ejecutar el script

```bash
python main.py
```

### Ejemplo de salida:

```
🎬 Uniendo: Video_1.mp4 + Video_1-audio.mp4
✅ Guardado en: output/01/video_final.mp4
🎬 Uniendo: Video_2.mp4 + Video_2-audio.mp4
✅ Guardado en: output/02/video_final.mp4
⚠️ Saltando carpeta 03, falta video o audio
```

## ⚙️ Funcionamiento del Script

El script realiza las siguientes operaciones:

1. **Escanea** la carpeta `originales/` buscando subcarpetas
2. **Identifica** archivos de video y audio en cada subcarpeta:
   - Video: cualquier archivo `.mp4` que NO contenga `-audio`
   - Audio: cualquier archivo `.mp4` que SÍ contenga `-audio`
3. **Combina** video y audio usando FFmpeg con estos parámetros:
   - `vcodec='copy'`: Copia el video sin recodificar (más rápido)
   - `acodec='aac'`: Convierte el audio a formato AAC
4. **Guarda** el resultado en `output/[nombre_carpeta]/video_final.mp4`

## 🔧 Personalización

### Cambiar nombres de carpetas:

```python
# Modificar estas líneas en main.py
input_root = Path("tu_carpeta_origen")
output_root = Path("tu_carpeta_destino")
```

### Cambiar nombre del archivo final:

```python
# Modificar esta línea en main.py
output_file = output_folder / "tu_nombre_personalizado.mp4"
```

### Cambiar formatos de códec:

```python
# Modificar estos parámetros en main.py
.output(video_stream, audio_stream, str(output_file),
        vcodec='libx264',  # Para recodificar video
        acodec='mp3')      # Para usar MP3 en lugar de AAC
```

## 🚨 Solución de Problemas

### Error: "ffmpeg not found"
- Asegúrate de que FFmpeg esté instalado y en el PATH del sistema
- Verifica la instalación: `ffmpeg -version`

### Error: "No such file or directory"
- Verifica que la carpeta `originales/` exista
- Confirma que los archivos tengan extensión `.mp4`

### El script salta carpetas
- Asegúrate de que cada carpeta tenga exactamente un archivo de video y uno de audio
- Verifica que el archivo de audio contenga `-audio` en el nombre

### Error de permisos
- Asegúrate de tener permisos de escritura en la carpeta del proyecto
- En sistemas Unix, puedes usar: `chmod +x main.py`

## 📝 Notas Técnicas

- **Velocidad**: El script usa `vcodec='copy'` para evitar recodificar el video, lo que hace el proceso mucho más rápido
- **Calidad**: No hay pérdida de calidad en el video al usar copy
- **Compatibilidad**: Los archivos resultantes son compatibles con la mayoría de reproductores
- **Memoria**: El proceso es eficiente en memoria ya que FFmpeg trabaja por streaming

## 🌍 Versiones de Idioma

- [Español (Spanish)](README.md) - Versión en español
- [English](README_EN.md) - English version

## 🤝 Contribuciones

Si encuentras algún problema o tienes sugerencias de mejora, no dudes en crear un issue o pull request.

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
