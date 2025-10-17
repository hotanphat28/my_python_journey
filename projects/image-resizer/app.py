# -*- coding: utf-8 -*-
# Dòng trên đảm bảo mã nguồn có thể sử dụng các ký tự tiếng Việt.

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import io


# --- LỚP ỨNG DỤNG CHÍNH ---
class ImageResizerApp:
    def __init__(self, root):
        """
        Hàm khởi tạo (constructor) của lớp.
        Đây là nơi chúng ta thiết lập toàn bộ giao diện người dùng (UI) và các biến ban đầu.
        'root' là cửa sổ chính của ứng dụng.
        """
        self.root = root
        self.root.title("Simple Image Tool")  # Đặt tiêu đề cho cửa sổ
        self.root.geometry("600x500")  # Đặt kích thước ban đầu của cửa sổ
        self.root.minsize(550, 450)  # Đặt kích thước tối thiểu
        self.root.configure(bg="#f4f4f4")  # Đặt màu nền cho cửa sổ

        # --- Cấu hình giao diện (Style) ---
        # Sử dụng ttk để có các widget hiện đại hơn và tùy chỉnh giao diện của chúng.
        style = ttk.Style()
        style.configure("TFrame", background="#f4f4f4")
        style.configure("TLabel", background="#f4f4f4", font=("Inter", 10))
        style.configure("Header.TLabel", font=("Inter", 14, "bold"))
        style.configure("TButton", font=("Inter", 10, "bold"), padding=6)
        style.configure("TRadiobutton", background="#f4f4f4", font=("Inter", 10))
        style.configure("TEntry", font=("Inter", 10), padding=5)
        style.configure("TLabelframe", background="#f4f4f4")
        style.configure(
            "TLabelframe.Label", background="#f4f4f4", font=("Inter", 10, "bold")
        )

        # --- Khởi tạo các biến ---
        self.image = None  # Biến để lưu đối tượng hình ảnh đã mở (Pillow object)
        self.image_path = None  # Biến để lưu đường dẫn của tệp ảnh

        # --- Khung chính (Main Frame) ---
        # Khung này chứa tất cả các thành phần khác của giao diện.
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill="both", expand=True)
        # Cấu hình grid để các cột và hàng có thể co giãn.
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # --- Tiêu đề ---
        header_label = ttk.Label(
            main_frame, text="Image Processing Tool", style="Header.TLabel"
        )
        header_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # --- Khung xem trước ảnh (Image Preview) ---
        preview_frame = ttk.Frame(main_frame, relief="sunken", width=300, height=300)
        preview_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 10))
        preview_frame.pack_propagate(False)  # Ngăn khung tự co lại theo nội dung

        self.image_label = ttk.Label(
            preview_frame,
            text="Upload an image to see a preview",
            anchor="center",
            wraplength=280,
        )
        self.image_label.pack(fill="both", expand=True)

        # --- Khung điều khiển (Controls Frame) ---
        self.controls_frame = ttk.Frame(main_frame)
        self.controls_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

        # Nút Tải ảnh lên
        self.upload_button = ttk.Button(
            self.controls_frame, text="Upload Image", command=self.upload_image
        )
        self.upload_button.grid(
            row=0, column=0, columnspan=2, pady=(0, 10), sticky="ew"
        )

        # Nhãn hiển thị thông tin ảnh
        self.info_label = ttk.Label(
            self.controls_frame, text="Original size: N/A", justify="left"
        )
        self.info_label.grid(row=1, column=0, columnspan=2, pady=(0, 15), sticky="w")

        # --- Khung chọn hành động ---
        self.mode_var = tk.StringVar(
            value="resolution"
        )  # Biến lưu trữ lựa chọn của người dùng
        action_frame = ttk.LabelFrame(self.controls_frame, text="Select Action")
        action_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        # Các nút radio để chọn hành động
        ttk.Radiobutton(
            action_frame,
            text="Resize by Resolution (px)",
            variable=self.mode_var,
            value="resolution",
            command=self.toggle_mode,
        ).pack(anchor="w", padx=5, pady=2)
        ttk.Radiobutton(
            action_frame,
            text="Resize by File Size (KB)",
            variable=self.mode_var,
            value="filesize",
            command=self.toggle_mode,
        ).pack(anchor="w", padx=5, pady=2)
        ttk.Radiobutton(
            action_frame,
            text="Convert to Black & White",
            variable=self.mode_var,
            value="bw_only",
            command=self.toggle_mode,
        ).pack(anchor="w", padx=5, pady=2)

        # --- Khung nhập liệu (Inputs Frame) ---
        # Khung này sẽ hiển thị các ô nhập liệu tùy theo hành động được chọn.
        self.inputs_frame = ttk.Frame(self.controls_frame)
        self.inputs_frame.grid(row=3, column=0, columnspan=2, sticky="ew")

        # Các ô nhập liệu cho việc thay đổi kích thước theo độ phân giải
        self.width_label = ttk.Label(self.inputs_frame, text="Width:")
        self.width_entry = ttk.Entry(self.inputs_frame, width=8)
        self.height_label = ttk.Label(self.inputs_frame, text="Height:")
        self.height_entry = ttk.Entry(self.inputs_frame, width=8)

        # Các ô nhập liệu cho việc thay đổi kích thước theo dung lượng tệp
        self.size_label = ttk.Label(self.inputs_frame, text="Target Size:")
        self.size_entry = ttk.Entry(self.inputs_frame, width=8)
        self.kb_label = ttk.Label(self.inputs_frame, text="KB")

        self.toggle_mode()  # Gọi hàm này để thiết lập trạng thái ban đầu cho các ô nhập liệu

        # --- Nút Áp dụng (Apply Button) ---
        self.apply_button = ttk.Button(
            self.controls_frame,
            text="Apply and Save",
            command=self.apply_and_save_image,
            state="disabled",
        )
        self.apply_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    def toggle_mode(self):
        """
        Hàm này dùng để ẩn/hiện các ô nhập liệu tương ứng với hành động được chọn.
        """
        # Xóa tất cả các widget hiện có trong khung nhập liệu
        for widget in self.inputs_frame.winfo_children():
            widget.grid_forget()

        mode = self.mode_var.get()  # Lấy giá trị của radio button đang được chọn
        if mode == "resolution":
            # Hiển thị các ô nhập chiều rộng và chiều cao
            self.width_label.grid(row=0, column=0, sticky="w")
            self.width_entry.grid(row=0, column=1, sticky="e", padx=(5, 0))
            self.height_label.grid(row=0, column=2, sticky="w", padx=(10, 0))
            self.height_entry.grid(row=0, column=3, sticky="e", padx=(5, 0))
        elif mode == "filesize":
            # Hiển thị ô nhập dung lượng mục tiêu
            self.size_label.grid(row=0, column=0, sticky="w")
            self.size_entry.grid(row=0, column=1, sticky="e", padx=(5, 0))
            self.kb_label.grid(row=0, column=2, sticky="w", padx=(5, 0))
        # Không cần ô nhập liệu nào cho chế độ "bw_only" (chuyển sang trắng đen)

    def upload_image(self):
        """
        Mở hộp thoại để người dùng chọn một tệp ảnh.
        """
        path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")]
        )
        if not path:  # Nếu người dùng không chọn tệp nào
            return

        self.image_path = path  # Lưu đường dẫn
        try:
            self.image = Image.open(self.image_path)  # Mở ảnh bằng thư viện Pillow
            self.display_image_preview()  # Hiển thị ảnh xem trước

            # Lấy thông tin kích thước và dung lượng của ảnh
            file_size_kb = os.path.getsize(self.image_path) / 1024
            self.info_label.config(
                text=f"Original: {self.image.width}x{self.image.height}px, {file_size_kb:.2f} KB"
            )

            self.apply_button.config(state="normal")  # Kích hoạt nút "Apply and Save"
        except Exception as e:
            messagebox.showerror(
                "Error", f"Failed to open image: {e}"
            )  # Hiển thị lỗi nếu không mở được ảnh
            self.image = None
            self.image_path = None
            self.apply_button.config(state="disabled")  # Vô hiệu hóa nút

    def display_image_preview(self):
        """
        Hiển thị một phiên bản thu nhỏ của ảnh đã tải lên trên giao diện.
        """
        if not self.image:
            return
        preview_img = self.image.copy()  # Tạo bản sao để không ảnh hưởng đến ảnh gốc
        preview_img.thumbnail((300, 300), Image.Resampling.LANCZOS)  # Thu nhỏ ảnh

        # Chuyển đổi ảnh Pillow sang định dạng mà Tkinter có thể hiển thị
        self.photo_image = ImageTk.PhotoImage(preview_img)
        self.image_label.config(
            image=self.photo_image, text=""
        )  # Cập nhật nhãn để hiển thị ảnh

    def apply_and_save_image(self):
        """
        Thực hiện hành động đã chọn và mở hộp thoại để lưu tệp.
        """
        if not self.image:
            messagebox.showerror("Error", "No image uploaded.")
            return

        filetypes = [
            ("JPEG", "*.jpg"),
            ("PNG", "*.png"),
            ("BMP", "*.bmp"),
            ("GIF", "*.gif"),
            ("All files", "*.*"),
        ]
        original_dir, original_filename = os.path.split(self.image_path)
        filename, ext = os.path.splitext(original_filename)

        # Tạo tên tệp gợi ý dựa trên hành động
        mode = self.mode_var.get()
        suffix = "_resized"
        if mode == "bw_only":
            suffix = "_bw"

        suggested_filename = f"{filename}{suffix}{ext}"

        # Mở hộp thoại "Lưu tệp"
        output_path = filedialog.asksaveasfilename(
            initialdir=original_dir,
            initialfile=suggested_filename,
            defaultextension=".jpg",
            filetypes=filetypes,
        )

        if not output_path:
            return  # Nếu người dùng không chọn vị trí lưu

        try:
            img = self.image.copy()
            # Gọi hàm xử lý tương ứng với chế độ đã chọn
            if mode == "resolution":
                width = int(self.width_entry.get())
                height = int(self.height_entry.get())
                self.resize_by_resolution(img, width, height, output_path)
            elif mode == "filesize":
                target_kb = int(self.size_entry.get())
                self.resize_by_filesize(img, target_kb, output_path)
            elif mode == "bw_only":
                self.convert_to_bw_and_save(img, output_path)

            messagebox.showinfo(
                "Success", f"Image successfully saved to:\n{output_path}"
            )

        except ValueError:
            messagebox.showerror(
                "Error", "Invalid input. Please enter numbers for dimensions or size."
            )
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def resize_by_resolution(self, img, width, height, output_path):
        """Thay đổi kích thước ảnh theo chiều rộng và chiều cao cụ thể."""
        resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
        resized_img.save(output_path)

    def resize_by_filesize(self, img, target_kb, output_path):
        """
        Giảm dung lượng tệp bằng cách giảm kích thước (chiều rộng/cao) của ảnh,
        trong khi vẫn giữ chất lượng nén JPEG ở mức cao để bảo toàn chi tiết.
        Hàm này sẽ lặp lại việc thu nhỏ ảnh cho đến khi đạt được dung lượng mong muốn.
        """
        target_bytes = target_kb * 1024

        # Chất lượng nén JPEG được giữ không đổi ở mức cao.
        # Chúng ta sẽ thay đổi kích thước ảnh thay vì chất lượng.
        quality = 90

        # Nếu ảnh có kênh trong suốt (PNG), chuyển sang RGB vì JPEG không hỗ trợ
        if img.mode in ("RGBA", "LA", "P"):
            img_rgb = img.convert("RGB")
        else:
            img_rgb = img

        # Bắt đầu với 100% kích thước gốc và giảm dần
        for scale_percent in range(100, 10, -5):
            width = int(img_rgb.width * scale_percent / 100)
            height = int(img_rgb.height * scale_percent / 100)

            # Nếu kích thước quá nhỏ, dừng lại
            if width < 1 or height < 1:
                break

            resized_img = img_rgb.resize((width, height), Image.Resampling.LANCZOS)

            buffer = io.BytesIO()  # Tạo một buffer trong bộ nhớ
            resized_img.save(buffer, format="JPEG", quality=quality)

            # Kiểm tra kích thước của buffer
            if buffer.tell() <= target_bytes:
                # Nếu kích thước đạt yêu cầu, ghi buffer ra tệp
                with open(output_path, "wb") as f:
                    f.write(buffer.getvalue())
                return  # Hoàn thành

        raise Exception("Could not reduce file size enough. Try a larger target size.")

    def convert_to_bw_and_save(self, img, output_path):
        """Chuyển ảnh sang thang độ xám (trắng đen)."""
        bw_img = img.convert("L")  # 'L' là chế độ Grayscale trong Pillow
        bw_img.save(output_path)


# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    root = tk.Tk()  # Tạo cửa sổ chính
    app = ImageResizerApp(root)  # Tạo một instance của lớp ứng dụng
    root.mainloop()  # Bắt đầu vòng lặp sự kiện của Tkinter (để hiển thị cửa sổ và chờ tương tác)
