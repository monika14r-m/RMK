from PIL import Image
import numpy as np

def load_image(path):
    """Load an image from file into a NumPy array."""
    return np.array(Image.open(path))

def save_image(img, path):
    """Save a NumPy array as an image file."""
    Image.fromarray(img).save(path)
