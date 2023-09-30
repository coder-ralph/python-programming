<<<<<<< HEAD
from rembg import remove
from PIL import Image
input_path = 'test.jpg' # input image path
output_path = 'test.png' # output image path
inp = Image.open(input_path) # load image
output = remove(inp) # remove background
=======
from rembg import remove
from PIL import Image
input_path = 'test.jpg' # input image path
output_path = 'test.png' # output image path
inp = Image.open(input_path) # load image
output = remove(inp) # remove background
>>>>>>> 74154de6fbbfa8071f20826e1b1ee9c263558d3f
output.save(output_path) # save image