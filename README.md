# PDF Utility

A Python-based command-line application that allows users to merge multiple PDF files into a single PDF and convert multiple images into one PDF.

## Features

- **Merge PDF Files:** Combine multiple PDF documents into a single PDF.
- **Convert Images to PDF:** Convert multiple JPG, JPEG, and PNG images into one PDF.
- **File Validation:** Check whether input files exist and have supported extensions.
- **PDF Validation:** Detect invalid or corrupted PDF files using PyPDF.
- **Image Validation:** Verify image files using Pillow.
- **Input Validation:** Handle invalid menu choices and incorrect numerical inputs.
- **Exception Handling:** Handle errors during PDF merging and image conversion.

## Technologies Used

- **Python 3.13**
- **pypdf:** For reading and merging PDF documents.
- **Pillow:** For opening, processing, and converting images.
- **os:** For file and path validation.

## Project Structure

```text
pdf_merger/
│
├── main.py
├── pdf_merger.py
├── image_converter.py
├── requirements.txt
├── README.md
└── .gitignore
```

### 1. Merge PDF Files

- Select option 1.
- Enter the number of PDF files.
- Provide the file paths.
- Enter the output filename.
- The application validates and merges the selected PDFs.

### 2. Convert Images to PDF

- Select option 2.
- Enter the number of images.
- Provide the image paths.
- Supported formats: JPG, JPEG, PNG.
- Enter the output filename.
- The application converts the images into a single PDF, preserving their order.

## Future Improvements

- Develop a graphical interface using Streamlit.
- Add file upload and PDF download functionality.
