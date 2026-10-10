import cv2

def grayscale(image):
    """Convert a BGR image to a single-channel grayscale image."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def resize_image(image, width=640, height=480):
    """Resize while preserving aspect ratio inside the requested bounds."""
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    h, w = image.shape[:2]
    scale = min(width / w, height / h)
    new_size = (max(1, round(w * scale)), max(1, round(h * scale)))
    return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA if scale < 1 else cv2.INTER_LINEAR)
