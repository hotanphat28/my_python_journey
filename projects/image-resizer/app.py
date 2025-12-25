# -*- coding: utf-8 -*-
"""
Image Processing Tool - Flask Web Server
This application allows users to resize images by resolution, target file size, 
or convert them to black and white via a browser interface.
"""

from flask import Flask, request, render_template_string, send_file
from PIL import Image
import io
import os

# --- INITIALIZE FLASK APP ---
app = Flask(__name__)

# --- IMAGE PROCESSING LOGIC ---

def resize_by_resolution(img, width, height):
    """Resizes the image to specific pixel dimensions."""
    return img.resize((width, height), Image.Resampling.LANCZOS)

def resize_by_filesize(img, target_kb):
    """
    Reduces file size by scaling down dimensions while keeping high JPEG quality.
    Returns a BytesIO buffer and the corresponding mime type.
    """
    target_bytes = target_kb * 1024
    quality = 90  # Maintain high visual quality
    
    # Convert transparent images to RGB for JPEG compatibility
    img_rgb = img.convert('RGB') if img.mode in ('RGBA', 'LA', 'P') else img

    # Iteratively scale down until the file size target is met
    for scale_percent in range(100, 10, -5):
        width = int(img_rgb.width * scale_percent / 100)
        height = int(img_rgb.height * scale_percent / 100)

        if width < 1 or height < 1:
            break

        resized_img = img_rgb.resize((width, height), Image.Resampling.LANCZOS)
        buffer = io.BytesIO()
        resized_img.save(buffer, format="JPEG", quality=quality)
        
        if buffer.tell() <= target_bytes:
            buffer.seek(0)
            return buffer, "image/jpeg"
    
    return None, None

def convert_to_bw(img):
    """Converts the image to grayscale (Black & White)."""
    return img.convert("L")

# --- FRONT-END UI (HTML/CSS/JS) ---

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Tool - Web</title>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Space Grotesk', sans-serif;
            background-color: #101010; /* black */
            color: #F4F4F4; /* light */
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 1rem;
            box-sizing: border-box;
        }
        .container {
            background-color: #282828; /* dark */
            padding: 2rem 2.5rem;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            width: 100%;
            max-width: 550px;
        }
        h1 {
            color: #FFC90E; /* golden */
            font-weight: 700;
            text-align: center;
            margin-top: 0;
            margin-bottom: 2rem;
        }
        form > div {
            margin-bottom: 1.5rem;
        }
        label, .label-header {
            display: block;
            font-family: 'Space Mono', monospace;
            font-weight: 700;
            font-size: 0.9rem;
            margin-bottom: 0.75rem;
            color: #D6D6D6; /* light-gray */
        }
        input[type="file"] {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1rem;
            width: 100%;
        }
        input[type="file"]::file-selector-button {
            font-family: 'Space Mono', monospace;
            font-weight: 700;
            background-color: #646464; /* dark-gray */
            color: #F4F4F4;
            border: none;
            padding: 10px 15px;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        input[type="file"]::file-selector-button:hover {
            background-color: #FFC90E;
            color: #101010;
        }
        .radio-group {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .radio-group input[type="radio"] {
            opacity: 0;
            position: fixed;
            width: 0;
        }
        .radio-group label {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 400;
            font-size: 1rem;
            display: inline-block;
            background-color: #101010;
            padding: 10px 15px;
            border: 2px solid #646464;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-bottom: 0;
        }
        .radio-group input[type="radio"]:checked + label {
            border-color: #FFC90E;
            background-color: #282828;
            color: #FFC90E;
            font-weight: 700;
        }
        .input-row {
            display: flex;
            gap: 10px;
        }
        .input-row input[type="number"] {
            font-family: 'Space Mono', monospace;
            font-size: 1rem;
            width: 80px;
            padding: 10px;
            background: #101010;
            border: 2px solid #646464;
            color: #F4F4F4;
            border-radius: 8px;
        }
        .input-row span {
            align-self: center;
            color: #D6D6D6;
            font-family: 'Space Mono', monospace;
        }
        button[type="submit"] {
            background-color: #FFC90E;
            color: #101010;
            border: none;
            padding: 14px 20px;
            font-family: 'Space Mono', monospace;
            font-weight: 700;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1.1rem;
            width: 100%;
            transition: background-color 0.3s ease;
            margin-top: 1rem;
        }
        button[type="submit"]:hover {
            background-color: #FFFFFF;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Image Processor 🚀</h1>
        <form action="/upload" method="POST" enctype="multipart/form-data">
            <div>
                <label for="image">1. Upload Image:</label>
                <input type="file" name="image" id="image" accept="image/*" required>
            </div>
            
            <div>
                <span class="label-header">2. Select Action:</span>
                <div class="radio-group">
                    <input type="radio" id="res" name="mode" value="resolution" checked onchange="toggleInputs()">
                    <label for="res">By Resolution</label>
                    
                    <input type="radio" id="size" name="mode" value="filesize" onchange="toggleInputs()">
                    <label for="size">By File Size</label>
                    
                    <input type="radio" id="bw" name="mode" value="bw_only" onchange="toggleInputs()">
                    <label for="bw">Black & White</label>
                </div>
            </div>

            <div id="inputs-frame">
                <div id="resolution-inputs">
                    <span class="label-header">3. Enter Dimensions (px):</span>
                    <div class="input-row">
                        <input type="number" name="width" placeholder="W" min="1">
                        <span>x</span>
                        <input type="number" name="height" placeholder="H" min="1">
                    </div>
                </div>
                <div id="filesize-inputs" style="display:none;">
                    <span class="label-header">3. Enter Target Size (KB):</span>
                    <div class="input-row">
                        <input type="number" name="size" placeholder="KB" min="1">
                        <span>KB</span>
                    </div>
                </div>
            </div>
            
            <button type="submit">Process & Download</button>
        </form>
    </div>
    
    <script>
        function toggleInputs() {
            const mode = document.querySelector('input[name="mode"]:checked').value;
            document.getElementById('resolution-inputs').style.display = (mode === 'resolution') ? 'block' : 'none';
            document.getElementById('filesize-inputs').style.display = (mode === 'filesize') ? 'block' : 'none';
        }
    </script>
</body>
</html>
"""

# --- SERVER ROUTES ---

@app.route('/')
def index():
    """Serves the main tool page."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handles image uploads, processing, and delivery."""
    if 'image' not in request.files:
        return "Error: No file uploaded.", 400
    
    file = request.files['image']
    if not file or file.filename == '':
        return "Error: Empty file provided.", 400

    mode = request.form['mode']
    
    try:
        img = Image.open(file.stream)
        filename, ext = os.path.splitext(file.filename)
        processed_img = None
        save_format = "JPEG"
        suffix = "_processed"

        # INVERSION OVER NESTING: Handle filesize first as it returns a unique buffer
        if mode == 'filesize':
            target_kb = int(request.form['size'])
            buffer, mime = resize_by_filesize(img, target_kb)
            if not buffer:
                return "Error: Could not meet target size. Try a larger value.", 400
            
            return send_file(buffer, mimetype=mime, as_attachment=True, download_name=f"{filename}_scaled.jpg")

        # Handle other modes
        if mode == 'resolution':
            width, height = int(request.form['width']), int(request.form['height'])
            processed_img = resize_by_resolution(img, width, height)
            suffix = "_resized"
            save_format = "PNG" if img.mode == 'RGBA' else "JPEG"
        
        elif mode == 'bw_only':
            processed_img = convert_to_bw(img)
            suffix = "_bw"
            save_format = "PNG" if img.mode == 'RGBA' else "JPEG"

        if not processed_img:
            return "Error: Invalid mode.", 400

        # Save processed image to buffer
        buffer = io.BytesIO()
        if save_format == 'JPEG' and processed_img.mode in ('RGBA', 'LA', 'P'):
            processed_img = processed_img.convert('RGB')
        
        processed_img.save(buffer, format=save_format)
        buffer.seek(0)
        
        return send_file(buffer, mimetype=f"image/{save_format.lower()}", as_attachment=True, download_name=f"{filename}{suffix}.{save_format.lower()}")

    except ValueError:
        return "Error: Invalid input numbers.", 400
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
