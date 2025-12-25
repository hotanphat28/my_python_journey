# Background Remover App

A simple Python script to remove the background from images using `rembg` and `Pillow`.

## Prerequisites

- Python 3.x
- [rembg](https://github.com/danielgatis/rembg)
- [Pillow](https://python-pillow.org/)

## Installation

1. Navigate to the project directory:
   ```bash
   cd projects/remove_bg_app
   ```

2. Install the required libraries:
   ```bash
   pip install rembg Pillow
   ```

## Usage

1. Place your image (e.g., `leopard.png`) in the project directory.
2. Update the `input_path` and `output_path` variables in `app.py` if necessary:
   ```python
   input_path = "your_image.png"
   output_path = "output_image.png"
   ```
3. Run the script:
   ```bash
   python app.py
   ```
4. The image with the background removed will be saved as specified in `output_path`.
