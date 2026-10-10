import cv2
import numpy as np

def detect_edges(gray_image, method="canny"):
    """Return an edge map using Canny, Sobel magnitude, or Laplacian."""
    if gray_image is None or gray_image.ndim != 2:
        raise ValueError("Expected a valid grayscale image.")
    method = method.lower()
    if method == "canny":
        return cv2.Canny(gray_image, 100, 200)
    if method == "sobel":
        sx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sy = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        magnitude = cv2.magnitude(sx, sy)
        return cv2.convertScaleAbs(magnitude)
    if method == "laplacian":
        lap = cv2.Laplacian(gray_image, cv2.CV_64F)
        return cv2.convertScaleAbs(lap)
    raise ValueError("Unknown method. Choose canny, sobel, or laplacian.")
