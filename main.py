import ffmpeg
import os
from pathlib import Path

# Ruta raíz de los archivos
input_root = Path("originales")
output_root = Path("output")

# Crear carpeta de salida si no existe
output_root.mkdir(exist_ok=True)

# Recorrer subcarpetas (01, 02, etc.)
for folder in sorted(input_root.iterdir()):
    if folder.is_dir():
        video = None
        audio = None

        # Buscar archivos de video y audio dentro de cada carpeta
        for file in folder.glob("*.mp4"):
            if "-audio" in file.name:
                audio = file
            else:
                video = file

        if video and audio:
            output_folder = output_root / folder.name
            output_folder.mkdir(exist_ok=True)

            output_file = output_folder / "video_final.mp4"
            print(f"🎬 Uniendo: {video.name} + {audio.name}")

            # Crear streams de entrada para video y audio
            video_stream = ffmpeg.input(str(video))
            audio_stream = ffmpeg.input(str(audio))
            
            # Unir video y audio
            (
                ffmpeg
                .output(video_stream, audio_stream, str(output_file),
                        vcodec='copy', acodec='aac')
                .run(overwrite_output=True)
            )
            print(f"✅ Guardado en: {output_file}")
        else:
            print(f"⚠️ Saltando carpeta {folder.name}, falta video o audio")
