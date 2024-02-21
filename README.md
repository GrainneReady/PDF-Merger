# PDF Merger
This repository contains a Python script for merging multiple PDF files into a single document using the PyPDF4 library.

## Required Libraries:
- os (Python Standard Library)
- PyPDF4

## How to Use:
- **Place all the PDF files you want to merge into the _same directory_ as `mergepdfs.py`**
- Run the Python file or execute the command `python mergepdfs.py`
- Upon successful usage, a new file called `Merged.pdf` will be created which merges all the PDFs


## (Optional) Delete Original PDF Files after Merge:
By default, the script is set to keep the original PDF files after merging. If you want to delete them, uncomment the relevant code block in the script
