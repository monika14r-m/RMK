import cv2
import numpy as np


def remove_watermark(image):
    """
    Basic watermark removal using threshold + inpainting.
    Works only for simple/light watermarks.
    """

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect bright areas (common for watermarks)
    _, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Clean mask (remove noise)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)

    # Inpaint (fill removed region)
    result = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

    return result
