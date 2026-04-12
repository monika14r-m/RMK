import cv2


def inpaint_image(image, mask, method="telea", radius=3):
    """
    Applies inpainting to the masked region.

    Args:
        image: Original image (BGR)
        mask: Binary mask (white = area to remove)
        method: 'telea' or 'ns' (Navier-Stokes)
        radius: Inpainting radius

    Returns:
        Inpainted image
    """

    if method == "telea":
        flag = cv2.INPAINT_TELEA
    elif method == "ns":
        flag = cv2.INPAINT_NS
    else:
        raise ValueError(f"Invalid method: {method}")

    result = cv2.inpaint(image, mask, radius, flag)
    return result
