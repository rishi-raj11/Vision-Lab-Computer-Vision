from pathlib import Path
import cv2
import numpy as np

def image_statistics(image):
    """Calculate basic image dimensions and channel intensity statistics."""
    if image is None or image.size == 0:
        raise ValueError("Image is empty.")
    return {
        "width": int(image.shape[1]),
        "height": int(image.shape[0]),
        "channels": int(1 if image.ndim == 2 else image.shape[2]),
        "mean_intensity": round(float(np.mean(image)), 3),
        "standard_deviation": round(float(np.std(image)), 3),
        "minimum_intensity": int(np.min(image)),
        "maximum_intensity": int(np.max(image)),
    }

def save_histogram(gray_image, output_path):
    """Save a grayscale intensity histogram."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 4))
    plt.hist(gray_image.ravel(), bins=256, range=(0, 256))
    plt.title("Grayscale Intensity Histogram")
    plt.xlabel("Pixel intensity")
    plt.ylabel("Pixel count")
    plt.tight_layout()
    plt.savefig(output_path, dpi=140)
    plt.close()
