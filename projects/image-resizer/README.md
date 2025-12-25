# Simple Image Processing Tool

A simple desktop application built with Python to help you quickly perform one of three actions: resize an image by resolution, resize it by file size, or convert it to black and white.

## 🌟 Features

- **Simple UI**: Easy-to-use graphical interface.
- **Upload Images**: Supports common image formats like JPG, PNG, GIF, and BMP.
- **Image Preview**: Shows a thumbnail of your uploaded image along with its original dimensions and file size.
- **Three Distinct Actions**: Choose one of the following operations:

    1. **Resize by Resolution**: Specify the exact width and height in pixels.
    2. **Resize by File Size**: Set a target file size in kilobytes (KB).
    3. **Convert to Black & White**: Change the image to grayscale without altering its size.

## 📁 Project Structure

After following the setup instructions, your project directory will look like this:

```
image-resizer-project/
├── venv/ # Virtual environment directory
│   ├── bin/
│   ├── include/
│   └── ...
├── app.py # The main application script
└── README.md # This instruction file
```

## 🛠️ Prerequisites

Before you run the application, you need to have the following installed:

- **Python 3.x**: You can download it from [python.org](https://www.python.org/downloads/ "null").
- **pip**: Python's package installer, which usually comes with Python.

## 🚀 Installation

1. **Get the Code**: Navigate to the `projects/image-resizer` directory.
2. **Install Dependencies**: Ensure your virtual environment is active (see root README), then install the required library:
   ```bash
   pip install Pillow
   ```

## ▶️ How to Run the Application

1. **Run the App**: Run the following command:
2. **Run the App**: Once the environment is active, run the following command:

        python app.py
3. The application window should now appear on your screen.

## 📝 How Each Feature Works

### Resizing by Resolution

This method is straightforward. You provide a target width and height, and the application resizes the image to those exact dimensions. To maintain the best possible quality during downscaling, it uses the `LANCZOS` resampling filter, which is one of the highest quality filters available in the Pillow library.

### Resizing by File Size

This method is more complex and is primarily designed for JPEG images. Here’s the process:

1. You set a target file size (e.g., 200 KB).
2. The application takes the image and attempts to save it as a JPEG with a very high quality setting (95 out of 100).
3. It checks the resulting file size. If it's larger than your target, it reduces the quality setting (to 90, 85, 80, etc.) and tries again.
4. This process repeats until the file size is under your target. The first quality setting that meets the goal is used to save the final image.
5. **Note**: Because this method relies on JPEG compression, if you upload a PNG or another format, it will be converted to JPEG upon saving to achieve the size reduction.

This iterative approach ensures you get the highest possible quality for your desired file size.

### Convert to Black & White

This action is purely for color conversion. It changes the image to a grayscale color profile (`'L'` mode in Pillow) and saves it. The dimensions (width and height) of the image are not changed.
