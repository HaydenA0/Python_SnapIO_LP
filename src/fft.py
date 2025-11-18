from scipy.fft import fft2, ifft2
import numpy as np


class FoureirTransform:
    def __init__(self) -> None:
        pass

    def process_image(self, image, filter_defined):
        image_fft = fft2(image)
        image_fft_filterd = image_fft * filter_defined
        reverse_image = np.array(ifft2(image_fft_filterd))
        return np.real(reverse_image)
