
from rembg import remove
from PIL import Image
input_path = './output.png'
output_path = 'output2.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)

# image.save("output.png", "PNG")
# from PIL import Image
# image.show()