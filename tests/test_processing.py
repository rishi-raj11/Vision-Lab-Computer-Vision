import numpy as np
import pytest
from preprocessing import grayscale, resize_image
from edge_detection import detect_edges
from image_analysis import image_statistics
from image_loader import load_image

def test_grayscale_shape():
    image = np.zeros((20, 30, 3), dtype=np.uint8)
    assert grayscale(image).shape == (20, 30)

def test_resize_stays_within_bounds():
    image = np.zeros((100, 200, 3), dtype=np.uint8)
    result = resize_image(image, 50, 50)
    assert result.shape[1] <= 50 and result.shape[0] <= 50

def test_resize_rejects_invalid_dimensions():
    with pytest.raises(ValueError):
        resize_image(np.zeros((10, 10, 3), dtype=np.uint8), 0, 20)

@pytest.mark.parametrize("method", ["canny", "sobel", "laplacian"])
def test_edge_methods_return_grayscale_map(method):
    gray = np.zeros((30, 30), dtype=np.uint8)
    result = detect_edges(gray, method)
    assert result.shape == gray.shape

def test_unknown_edge_method_rejected():
    with pytest.raises(ValueError):
        detect_edges(np.zeros((10, 10), dtype=np.uint8), "unknown")

def test_statistics():
    stats = image_statistics(np.zeros((12, 18, 3), dtype=np.uint8))
    assert stats["width"] == 18
    assert stats["height"] == 12
    assert stats["channels"] == 3

def test_missing_file_rejected():
    with pytest.raises(FileNotFoundError):
        load_image("this_file_should_not_exist_visionlab.png")
