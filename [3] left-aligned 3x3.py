import math
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import registerFontFamily
import textwrap
import io
import os
import datetime
import sys

# Avoid warning
if not sys.warnoptions:
    import warnings

    warnings.simplefilter("ignore")


# PDF Layout stuff
def get_pdf_width_and_height():
    return A4


def get_pdf_width():
    return get_pdf_width_and_height()[0]


def get_pdf_height():
    return get_pdf_width_and_height()[1]


num_rows = 3  # Rows of cards inside the pdf
num_columns = 3  # Number of cards per row inside the pdf
cards_per_page = num_columns * num_rows

width_margin = get_pdf_width() / 17  # Empty space on the left
height_margin = get_pdf_height() * (3 / 110)  # Empty space above
block_width = (get_pdf_width() - 2 * width_margin) / \
    num_columns + get_pdf_width() / 142
block_height = block_width * 1.38  # Aspect ratio for card size
space_between_lines = block_width / 9

font_size = 12
font_type = "Helvetica-Bold"

registerFontFamily('Helvetica', normal='Helvetica-Bold', bold='Helvetica-Bold',
                   italic='Helvetica-BoldOblique', boldItalic='Helvetica-BoldOblique')


def text_centered_position(index):
    # Return text position inside a one page pdf
    index = (cards_per_page - index - 1)

    if 0 <= index < cards_per_page:
        index_pos = (int(index / num_columns), index % num_columns)
        width = width_margin + block_width * index_pos[1]
        height = height_margin + block_height * \
            index_pos[0] + block_height / 2 + block_height / 23

        return width, height
    else:
        return None


def split_text(text):
    # Split text in several lines
    # TODO: Be careful if just one word is split
    return textwrap.wrap(text, width=25)


def write_text_to_pdf(text, index, canvas):
    # Draw text inside a pdf using canvas

    parag = Paragraph(text, stylo)
    parag.wrapOn(can, block_width - 23, block_height)
    parag.drawOn(can, text_centered_position(index)[0] + 13,
                 text_centered_position(index)[1] - len(parag.blPara.lines) * space_between_lines + 106)


black_cards_dir = "./Input/BlackCards/"
white_cards_dir = "./Input/WhiteCards/"

packet = io.BytesIO()

# Create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=A4)
can.setFont(font_type, font_size)

pdf_page_index = 0
card_index = 0  # Index inside one pdf page

black_pages = 0
white_pages = 0

black_cards = 0
white_cards = 0

# Black cards
stylo = ParagraphStyle("estilo", fontName="Helvetica", fontSize=12, textColor=colors.white,
                       leading=space_between_lines, borderWidth=0, borderColor=colors.white)

for filename in os.listdir(black_cards_dir):
    path = black_cards_dir + filename
    file_reader = open(path, "r", encoding="utf-8")

    for line in file_reader:
        write_text_to_pdf(line, card_index, can)
        card_index += 1
        black_cards += 1

        if card_index == cards_per_page:
            card_index = 0
            can.showPage()
            can.setFont(font_type, font_size)

if card_index > 0:
    can.showPage()
    can.setFont(font_type, font_size)
    card_index = 0

black_pages = math.ceil(black_cards/cards_per_page)

# White cards
stylo = ParagraphStyle("estilo", fontName="Helvetica", fontSize=12, textColor=colors.black,
                       leading=space_between_lines, borderWidth=0, borderColor=colors.black)

for filename in os.listdir(white_cards_dir):
    path = white_cards_dir + filename
    file_reader = open(path, "r", encoding="utf-8")

    for line in file_reader:
        write_text_to_pdf(line, card_index, can)
        card_index += 1
        white_cards += 1

        if card_index == cards_per_page:
            card_index = 0
            can.showPage()
            can.setFont(font_type, font_size)

white_pages = math.ceil(white_cards/cards_per_page)
pdf_page_index = black_pages + white_pages

can.showPage()
can.save()

print("All files have been read.")


# Add the watermarks and create final pdf
new_pdf = PdfReader(packet)
output = PdfWriter()

print("PDF pages generated (out of " + str(pdf_page_index) + "):", end='', flush=True)
for i in range(pdf_page_index):
    existing_pdf = None
    if i < black_pages:
        existing_pdf = PdfReader(open("./Input/cah-blanks-inverted.pdf", "rb"))
    else:
        existing_pdf = PdfReader(open("./Input/cah-blanks.pdf", "rb"))

    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[i])
    output.add_page(page)
    print(" " + str(i + 1), end='', flush=True)

print(".")

# Finally, write "output" to a real file
output_file_name = "./Output/Cards-" + str(datetime.date.today()) + ".pdf"
outputStream = open(output_file_name, "wb")
output.write(outputStream)
outputStream.close()
print("Done.")
