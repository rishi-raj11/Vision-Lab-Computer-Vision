# VisionLab: Image Processing and Edge Detection Toolkit

VisionLab is a command-line Computer Vision project that preprocesses an image, detects edges with three classic methods, calculates basic statistics, and saves a histogram and text report.

## Features
- Load and validate an image.
- Convert it to grayscale and resize it within chosen dimensions.
- Detect edges using Canny, Sobel, and Laplacian.
- Calculate image dimensions and intensity statistics.
- Save generated images and a text report to an output folder.
- Run basic automated tests.

## Requirements
Python 3.9 or newer and pip.

## Setup
1. Clone/download this repository and open a terminal in its root directory.
2. Create a virtual environment:
   - Windows: `py -m venv .venv`
   - macOS/Linux: `python3 -m venv .venv`
3. Activate it:
   - Windows PowerShell: `.venv\Scripts\Activate.ps1`
   - Windows Command Prompt: `.venv\Scripts\activate.bat`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies: `python -m pip install -r requirements.txt`

## Run
Use any local image file, for example `sample.jpg`:
```bash
python main.py sample.jpg
```
Choose output folder, dimensions, and one edge method:
```bash
python main.py sample.jpg --output results --width 800 --height 600 --edge canny
```
Supported edge choices: `canny`, `sobel`, `laplacian`, `all`. If no edge option is given, all three methods run.

Output files include `grayscale.png`, `resized.png`, edge-map PNG files, `grayscale_histogram.png`, and `analysis_report.txt`.

## Tests
```bash
python -m pytest -q
```

## Workflow
Input image → validation/loading → grayscale and resize → edge detection → statistics/histogram → saved outputs and report.

## Limitations
Edge quality depends on image contrast and the fixed Canny thresholds. This project is a classical image-processing toolkit, not an object-recognition model. Use images you have permission to process.

## Project documentation
See `statement.md` for the problem statement, scope, target users, and high-level features.
