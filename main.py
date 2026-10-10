import argparse
from pathlib import Path
from image_loader import load_image
from preprocessing import grayscale, resize_image
from edge_detection import detect_edges
from image_analysis import image_statistics, save_histogram
from report_generator import save_report
from utils import ensure_dir, save_image

def main():
    parser = argparse.ArgumentParser(description="VisionLab: command-line image processing toolkit")
    parser.add_argument("image", help="Path to an input image")
    parser.add_argument("--output", default="output", help="Output directory (default: output)")
    parser.add_argument("--width", type=int, default=640, help="Maximum output width (default: 640)")
    parser.add_argument("--height", type=int, default=480, help="Maximum output height (default: 480)")
    parser.add_argument("--edge", choices=["canny", "sobel", "laplacian", "all"], default="all",
                        help="Edge detection method (default: all)")
    args = parser.parse_args()

    out = ensure_dir(args.output)
    image = load_image(args.image)
    gray = grayscale(image)
    resized = resize_image(image, args.width, args.height)
    save_image(out / "grayscale.png", gray)
    save_image(out / "resized.png", resized)

    methods = ["canny", "sobel", "laplacian"] if args.edge == "all" else [args.edge]
    for method in methods:
        save_image(out / f"{method}_edges.png", detect_edges(gray, method))

    stats = image_statistics(image)
    save_histogram(gray, out / "grayscale_histogram.png")
    save_report(stats, methods, out / "analysis_report.txt")
    print(f"Success. Results saved in: {out.resolve()}")
    print("Generated: grayscale.png, resized.png, edge map(s), grayscale_histogram.png, analysis_report.txt")

if __name__ == "__main__":
    main()
