from pathlib import Path
import cv2

def ensure_dir(path):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path

def save_image(path, image):
    path = Path(path)
    if image is None or image.size == 0:
        raise ValueError(f"Cannot save an empty image to {path}")
    if not cv2.imwrite(str(path), image):
        raise OSError(f"Failed to save image to {path}")
