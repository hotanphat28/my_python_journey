# Image Processing Web Tool

A browser-based image processing tool created with Flask. It allows you to:
- Resize images by resolution (Height x Width).
- Resize images by checking the target file size (KB).
- Convert images to Black & White (Grayscale).

## 🌟 Features

- **Web Interface**: Simple and responsive UI using HTML5 & CSS.
- **Image Upload**: Supports common formats (JPG, PNG, WebP, etc.).
- **Live Preview**: No live preview in this version (process & download workflow).
- **Processing Modes**:
    1. **By Resolution**: Resize using Lanczos resampling.
    2. **By File Size**: Compress JPEG images to meet a target size in KB.
    3. **Black & White**: Convert images to grayscale.

## ️ Prerequisites

- **Python 3.x**
- **Flask**
- **Pillow** (PIL Fork)

## 🚀 Installation

1. Navigate to the project directory:
   ```bash
   cd projects/image-resizer
   ```

2. Install dependencies (ensure `venv` is active - see root README):
   ```bash
   pip install Flask Pillow
   ```

## ▶️ Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000`.
3. Upload an image, select a mode, enter required parameters, and click **Process & Download**.
