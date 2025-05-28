# 🎬 Video and Audio Merger

**🌍 [Leer en Español](README.md)**

Python script to automatically merge video and audio files using FFmpeg. This script processes folders containing video files and their corresponding separate audio tracks, generating final videos with both elements combined.

## 📋 Prerequisites

Before using this script, make sure you have installed:

1. **Python 3.7 or higher**
2. **FFmpeg** (system-wide installation)

### FFmpeg Installation

#### On macOS (using Homebrew):
```bash
brew install ffmpeg
```

#### On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### On Windows:
1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extract the file and add the `bin` folder to the system PATH

## 🚀 Environment Setup

### 1. Create a Python virtual environment

```bash
# Navigate to the project directory
cd unir-video-audio

# Create the virtual environment
python3 -m venv video

# Activate the virtual environment
# On macOS/Linux:
source video/bin/activate

# On Windows:
video\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 📁 Folder Structure

The script expects the following directory structure:

```
unir-video-audio/
├── main.py
├── requirements.txt
├── README.md
├── README_EN.md
├── originales/           # Source files folder
│   ├── 01/
│   │   ├── video.mp4     # Main video file
│   │   └── video-audio.mp4  # Audio file (must contain "-audio" in the name)
│   ├── 02/
│   │   ├── another_video.mp4
│   │   └── another_video-audio.mp4
│   └── ...
└── output/               # Output folder (created automatically)
    ├── 01/
    │   └── video_final.mp4
    ├── 02/
    │   └── video_final.mp4
    └── ...
```

### Important:
- Audio files **must** contain `-audio` in their filename
- Video files **must not** contain `-audio` in their filename
- All files must have `.mp4` extension
- Subfolders can have any name (01, 02, episode1, etc.)

## 🎯 Script Usage

### 1. Activate the virtual environment (if not active)

```bash
source video/bin/activate
```

### 2. Run the script

```bash
python main.py
```

### Example output:

```
🎬 Uniendo: Video_1.mp4 + Video_1-audio.mp4
✅ Guardado en: output/01/video_final.mp4
🎬 Uniendo: Video_2.mp4 + Video_2-audio.mp4
✅ Guardado en: output/02/video_final.mp4
⚠️ Saltando carpeta 03, falta video o audio
```

## ⚙️ How the Script Works

The script performs the following operations:

1. **Scans** the `originales/` folder looking for subfolders
2. **Identifies** video and audio files in each subfolder:
   - Video: any `.mp4` file that does NOT contain `-audio`
   - Audio: any `.mp4` file that DOES contain `-audio`
3. **Combines** video and audio using FFmpeg with these parameters:
   - `vcodec='copy'`: Copies video without re-encoding (faster)
   - `acodec='aac'`: Converts audio to AAC format
4. **Saves** the result in `output/[folder_name]/video_final.mp4`

## 🔧 Customization

### Change folder names:

```python
# Modify these lines in main.py
input_root = Path("your_source_folder")
output_root = Path("your_destination_folder")
```

### Change final file name:

```python
# Modify this line in main.py
output_file = output_folder / "your_custom_name.mp4"
```

### Change codec formats:

```python
# Modify these parameters in main.py
.output(video_stream, audio_stream, str(output_file),
        vcodec='libx264',  # To re-encode video
        acodec='mp3')      # To use MP3 instead of AAC
```

## 🚨 Troubleshooting

### Error: "ffmpeg not found"
- Make sure FFmpeg is installed and in the system PATH
- Verify installation: `ffmpeg -version`

### Error: "No such file or directory"
- Verify that the `originales/` folder exists
- Confirm that files have `.mp4` extension

### Script skips folders
- Make sure each folder has exactly one video file and one audio file
- Verify that the audio file contains `-audio` in the filename

### Permission errors
- Make sure you have write permissions in the project folder
- On Unix systems, you can use: `chmod +x main.py`

## 📝 Technical Notes

- **Speed**: The script uses `vcodec='copy'` to avoid re-encoding video, making the process much faster
- **Quality**: No video quality loss when using copy
- **Compatibility**: Resulting files are compatible with most players
- **Memory**: The process is memory-efficient as FFmpeg works by streaming

## 🌍 Language Versions

- [Español (Spanish)](README.md) - Versión en español
- [English](README_EN.md) - English version

## 🤝 Contributions

If you find any issues or have suggestions for improvement, feel free to create an issue or pull request.

## 📄 License

This project is open source and available under the MIT License.
