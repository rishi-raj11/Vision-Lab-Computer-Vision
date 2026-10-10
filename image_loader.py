from pathlib import Path
import cv2

def load_image(path):
    """Load a color image; raise a helpful error if it cannot be read."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Input image does not exist: {path}")
    image = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError(f"Unsupported or unreadable image file: {path}")
    return image
