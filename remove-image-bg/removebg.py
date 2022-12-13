from rembg import remove
from PIL import Image
input_path = 'test.jpg' # input image path
output_path = 'test.png' # output image path
inp = Image.open(input_path) # load image
output = remove(inp) # remove background
output.save(output_path) # save image