

Code : Human made
README : Ai generated under my guidance

---


# WIP : Simple Image Processing Toolkit

### 0. Demonstration

![Some image at last](./bigging.png)

### 1. General information

-   **Name of the project**: Cython-Accelerated Image Processing Toolkit
-   **Type of the project**: Learning 
-   **Main Language(s) of the project**: Python, Cython
-   **Goal of this project**: My goal for this project is to build a small, modular library for basic image processing tasks. A key objective is to learn about performance optimization in Python by rewriting a computationally intensive function—2D convolution—in Cython to make it run faster.
-   **Scope of this project**: This project currently includes utilities for image input/output, inspection, visualization, and processing. The core feature is the implementation of two versions of a 2D convolution function: one in pure Python for baseline comparison, and a second, much faster version accelerated with Cython and parallelized with OpenMP. The project is still in development, with plans to add more features and unit tests.
-   **Why**: College Image Processing course was interesting, so I made this small simple wrapper of a libray
-   **Compatibility**: The project is developed in Python. To run it, you will need a C compiler (like GCC on Linux or Clang on macOS) installed on your system to compile the Cython code. The necessary Python packages are `numpy`, `scipy`, `opencv-python`, `matplotlib`, and `cython`.

### 2. Project

For this project, I have structured the code into several distinct classes to handle different responsibilities.

-   **I/O and Visualization**: I created an `ImageIO` class using OpenCV (`cv2`) to handle loading and saving images in various formats. A separate `Visualizer` class uses Matplotlib to display images, show side-by-side comparisons, and plot histograms.

-   **Image Analysis**: The `ImageInspector` class is a utility I wrote to extract useful metadata and statistics from an image. It can report basic properties like dimensions and file size, as well as calculate content-based metrics like Shannon entropy (for complexity) and Laplacian variance (for blur detection).

-   **Core Processing and Optimization**: The main focus of the project is in the `processing.py` and `convolution.pyx` files. I implemented a 2D convolution operation, which is fundamental to many image filtering effects like blurring and edge detection.
    -   First, I wrote `apply_kernel_old`, a straightforward implementation in pure Python using nested `for` loops. This version is easy to understand but is quite slow for large images.
    -   To address the performance bottleneck, I rewrote the convolution logic in Cython (`apply_kernel_cython`). In this version, I used static C-type declarations, NumPy memory views for efficient data access, and released Python's Global Interpreter Lock (`nogil`). This allowed me to parallelize the loops using OpenMP's `prange`, which significantly speeds up the computation on multi-core processors. The `playground.py` script is set up to directly compare the outputs of these two methods.

-   **Fourier Transform**: I also began experimenting with Fast Fourier Transform (FFT) using `scipy.fft` to explore image processing in the frequency domain.

### 3. How to run the project :

You will need Python, pip, and a C compiler (like GCC or Clang) installed.

1.  **Install Dependencies**
    First, install the required Python packages. You can install them using pip:
    ```sh
    pip install numpy scipy opencv-python matplotlib cython
    ```

2.  **Compile the Cython Module**
    The high-performance convolution function is in a `.pyx` file and needs to be compiled into a C extension. Navigate to the `src` directory and run the setup script:
    ```sh
    cd src
    python convolution-setup.py build_ext --inplace
    ```
    This command will create a file named `convolution.cpython-....so` (on Linux/macOS) or `convolution.pyd` (on Windows) in the same directory. The `--inplace` flag is important.

3.  **Run the Demonstration Script**
    The `playgroud.py` script is the main entry point to see the project in action. It loads an image and applies a blur filter using both the slow Python function and the fast Cython function.
    To run it, execute the following command from the `src` directory:
    ```sh
    python playgroud.py
    ```
    This will display a comparison of the original and the blurred image. You can also run `fft_testing.py` to see the Fourier Transform experiments.

