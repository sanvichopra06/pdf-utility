# PDF Utility

A Python-based application that allows users to merge multiple PDF files into a single document and convert multiple images into one PDF. It includes both a command-line interface (CLI) and a Streamlit-based web interface.

## Versions

- **V1.0 – CLI Application:** Command-line tool for PDF merging and image-to-PDF conversion.
- **V2.0 – Streamlit Web Interface:** Interactive web application with file uploads and downloadable PDF outputs.

## Features

### Core Functionality
- **Merge PDF Files:** Combine multiple PDF documents into a single PDF.
- **Convert Images to PDF:** Convert multiple JPG, JPEG, and PNG images into one PDF.
- **File Validation:** Check file existence and supported extensions.
- **PDF Validation:** Detect invalid or corrupted PDF files using pypdf.
- **Image Validation:** Verify image files using Pillow.
- **Input Validation:** Handle invalid menu choices and incorrect numerical inputs.
- **Exception Handling:** Handle errors during PDF merging and image conversion.

### V2.0 – Streamlit Features
- Interactive web interface.
- Upload multiple PDF files directly through the browser.
- Merge PDFs and download the resulting document.
- Upload multiple JPG, JPEG, and PNG images.
- Convert images into a single PDF.
- Download converted PDF documents.
- Custom pink-themed interface.

## Technologies Used

- **Python 3.13**
- **Streamlit:** For the web interface.
- **pypdf:** For reading and merging PDF documents.
- **Pillow:** For opening, processing, and converting images.
- **os:** For file and path handling.
- **tempfile:** For temporary file storage during web-based processing.

## Project Structure

```text
pdf_merger/
│
├── .streamlit/
│   └── config.toml
│
├── app.py
├── main.py
├── pdf_merger.py
├── image_converter.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/sanvichopra06/pdf-utility.git
cd pdf-utility
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

### V1.0 – Command-Line Interface

Run the CLI application:

```bash
python main.py
```

**Merge PDF Files**
1. Select option 1.
2. Enter the number of PDF files.
3. Provide the file paths.
4. Enter the output filename.
5. The application validates and merges the selected PDFs.

**Convert Images to PDF**
1. Select option 2.
2. Enter the number of images.
3. Provide the image paths.
4. Enter the output filename.
5. The application converts the images into one PDF while preserving their order.

### V2.0 – Streamlit Web Interface

Run the web application:

```bash
streamlit run app.py
```

1. Open the local URL displayed in the terminal.
2. Select PDF merging or image-to-PDF conversion.
3. Upload the required files.
4. Process the files.
5. Download the generated PDF.

## Screenshots

Screenshots of the Streamlit web interface will be added here.

## Future Improvements

- Add more PDF manipulation features.
- Improve file management and processing capabilities.
- Explore additional document conversion options.

## Author

**Sanvi Chopra**

[GitHub Repository](https://github.com/sanvichopra06/pdf-utility)
