from PyPDF4 import PdfFileMerger
import os 

file_merger = PdfFileMerger()

# Append all pdf files in the current directory to the PdfFileMerger
for file in os.listdir():
    if file.endswith('.pdf'):
        with open(file, 'rb') as pdf_file:
            file_merger.append(pdf_file)

# Write the merged PDF file using the PdfFileMerger
with open("Merged.pdf", 'wb') as merged_file:
    file_merger.write(merged_file)

# This for loop DELETES the original PDF files after they are merged.
#for file in os.listdir():
#    if file != 'Merged.pdf' and file.endswith('.pdf'):
#        os.remove(file)