# PDF Text Extractor

This repository contains a Python script that extracts text from PDF image files by converting each page to an image and then using OCR (Optical Character Recognition) to extract the text from those images. The extracted text is then checked against a list of parameters, and the results are saved into a CSV file.

## Requirements

- Python 3.x
- `tqdm`: Library for displaying progress bars
- `Pillow (PIL)`: Python Imaging Library for image processing
- `pytesseract`: Tesseract-OCR Engine for extracting text from images
- `csv`: Built-in Python library for handling CSV files
- `pypdfium2`: Library for handling PDF files

## Installation

Make sure you have all required libraries installed. You can install them using pip:

```bash
pip install tqdm pillow pytesseract pypdfium2
```

Additionally, you need to have Tesseract-OCR installed on your system. You can download it from [here](https://github.com/tesseract-ocr/tesseract).

## How It Works

1. **Traverse Directories**: The script walks through the current working directory and its subdirectories to find PDF files.
2. **Convert PDF Pages to Images**: For each found PDF file, it converts every page into an image.
3. **Extract Text**: Uses Tesseract-OCR to extract text from each image.
4. **Search Parameters**: Checks if any of the specified parameters are present in the extracted text.
5. **Save Results**: If any parameter is found, it saves the detailed result into a CSV file named `result.csv`.
6. **Clean Up**: Deletes all the generated images after processing.

## Usage

To run the script:

1. Place your PDF files in or below your current working directory.
2. Adjust the `paramsList` variable with the parameters you want to search for in the extracted text.
3. Execute the script:

```bash
python pdf_text_extractor.py
```

The results will be appended to a file named `result.csv`.

### Parameters List

The variable `paramsList` contains strings that will be searched within each page's extracted text.

Example:
```python
paramsList = ["param1", "param2", "param3", "param4"]
```

### Results Format

The results will be saved in a CSV file (`result.csv`) with columns indicating whether each parameter was found, along with details such as filename and page number.

## Functions Overview

1. **extract_text_from_image(image_path)**: Extracts text from an image using Tesseract-OCR.
2. **addContentToFile(content, fileName)**: Appends content (dictionary) into a CSV file.
3. **importPdfFile(path)**: Imports a PDF file and returns its object and number of pages.
4. **makeNewFileName(path, file)**: Generates new filenames for images converted from PDFs.
5. **convertPdfToImg(pdfFile, pageNumber, rootName)**: Converts a specific page of a PDF into an image and saves it.
6. **findTextInImgFile(imgPath, paramsList)**: Searches for predefined parameters in extracted text from an image.

## Acknowledgments

Special thanks to:
- [TQDM](https://github.com/tqdm/tqdm) for providing progress bar functionality.
- [Pillow](https://python-pillow.org/) for image processing capabilities.
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) for OCR functionalities.
- [PyPDFium2](https://github.com/pymupdf/pymupdf) for handling PDFs efficiently.

Feel free to contribute or report issues!

---

Happy coding!