from scipy.fft import fftshift
import numpy as np
from fft import FoureirTransform

from utilsio import ImageIO
from visulization import Visualizer

io = ImageIO()
vis = Visualizer()
fafat = FoureirTransform()

image = np.array(io.load_image("./images/grass.png", format="Grayscale"))

filter = np.ones_like(image)
new_image = fafat.process_image(image, filter)

vis.compare_images([image, new_image], ["Original", "Processed"])
