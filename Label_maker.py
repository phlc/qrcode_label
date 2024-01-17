
# imports
import sys
import csv
import qrcode
from reportlab.pdfgen import canvas
from PIL import Image

# constants
CSV_PATH = "ignore_info.csv"
PDF_FILE_NAME = "ignore_labels.pdf"
MEASURE = 72.0 # inches
PDF_PAGE_WIDTH = 4.8 * MEASURE
PDF_PAGE_HEIGHT = 2.4 * MEASURE
FONTSIZE = 8

# auxiliary functions
def generate_qrcode_image(data):
  qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=2,
  )
  qr.add_data(data)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  return img


### main ###

# extract info from csv
try:
  csvfile = open(CSV_PATH, newline='', encoding='utf-8-sig')

except FileNotFoundError:
  print(f'File "{CSV_PATH}" not found.')

else:
  data = []

  with csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      data.append(row[0].split(";"))

  header = data.pop(0)
  
  # create pdf file
  
  pdf_file = canvas.Canvas(PDF_FILE_NAME, pagesize = (PDF_PAGE_WIDTH, PDF_PAGE_HEIGHT) )
  pdf_file.setFont("Helvetica", FONTSIZE)

  for info in data:
    pdf_file.setFont("Helvetica", 8)
    pdf_file.drawString(PDF_PAGE_WIDTH * 0.01, PDF_PAGE_HEIGHT * 0.85, f'{header[0]}:')
    pdf_file.drawString(PDF_PAGE_WIDTH * 0.01, PDF_PAGE_HEIGHT * 0.80, info[0])

    pdf_file.drawString(PDF_PAGE_WIDTH * 0.01, PDF_PAGE_HEIGHT * 0.65, f'{header[1]}:')
    pdf_file.drawString(PDF_PAGE_WIDTH * 0.01, PDF_PAGE_HEIGHT * 0.60, info[1])

    pdf_file.drawString(PDF_PAGE_WIDTH * 0.01, PDF_PAGE_HEIGHT * 0.45, f'{header[2]}:')
    pdf_file.drawString(PDF_PAGE_WIDTH * 0.01, PDF_PAGE_HEIGHT * 0.40, info[2])

    pdf_file.drawString(PDF_PAGE_WIDTH * 0.01, PDF_PAGE_HEIGHT * 0.25, f'{header[3]}:')
    pdf_file.drawString(PDF_PAGE_WIDTH * 0.01, PDF_PAGE_HEIGHT * 0.20, info[3])   

    pdf_file.drawInlineImage(generate_qrcode_image(info[4]), PDF_PAGE_WIDTH * 0.5, PDF_PAGE_HEIGHT * 0.05, PDF_PAGE_HEIGHT *0.9, PDF_PAGE_HEIGHT *0.9)
    pdf_file.showPage()

  # save pdf file
  pdf_file.save()


  

