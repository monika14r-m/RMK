import os
import cv2


def is_image_file(filename, supported_formats):
    return filename.lower().endswith(supported_formats)


def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise ValueError(f"Failed to load image: {path}")
    return image


def save_image(path, image):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    cv2.imwrite(path, image)


def list_images(folder, supported_formats):
    if not os.path.exists(folder):
        raise FileNotFoundError(f"Folder not found: {folder}")

    return [
        f for f in os.listdir(folder)
        if is_image_file(f, supported_formats)
    ]


def resize_image(image, width):
    h, w = image.shape[:2]
    ratio = width / float(w)
    new_dim = (width, int(h * ratio))
    return cv2.resize(image, new_dim)
