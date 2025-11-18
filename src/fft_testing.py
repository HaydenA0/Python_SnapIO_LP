from scipy.fft import fft2, fftshift
from scipy.fft._pocketfft.helper import np

import numpy as np

# from fft import FoureirTransform

#
from utilsio import ImageIO
from visulization import Visualizer

#
io = ImageIO()
vis = Visualizer()
# fafat = FoureirTransform()
#
# image = np.array(io.load_image("./images/grass.png", format="Grayscale"))
#
# filter = np.ones_like(image)
# new_image = fafat.process_image(image, filter)
#
# vis.compare_images([image, new_image], ["Original", "Processed"])


image = np.array([[0, 0, 1], [0, 0, 0.8], [0, 0, 0.8]])
image_fft = np.array(fft2(image))
vis.compare_images(
    [image, np.abs(fftshift(image_fft) + 1)], ["Image", "Fourer Transform"]
)

print(f"Image = {image}")
print(f"Image_FFT = {image_fft}")
