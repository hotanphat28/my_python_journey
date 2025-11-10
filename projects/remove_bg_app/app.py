from rembg import remove
from PIL import Image

input_path = "leopard.png"
output_path = "leopard_remove_bg.png"

input_image = Image.open(input_path)

output_image = remove(input_image)

output_image.save(output_path)
