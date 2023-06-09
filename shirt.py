
from fpdf import FPDF, Align
import sys

def get_text():
    text = input("Text: ").strip()
    if not text:
        sys.exit("empty text")
    else:
        return text    

def get_path():
    path = input("output name: ").strip()
    if not path:
            sys.exit("empty path")
    if len(text) > 20:
            sys.exit("text is too long (max 20 characters)")
    else:
        return path
    
def get_font_size():
    range_ = [x+5 for x in range(36)]
    while True:
        try:
            font_size = int(input("font size(5-40): ").strip())
            if font_size not in range_:
                raise ValueError
            return font_size
        except ValueError:
            pass

text = get_text()
path = get_path()
if path.endswith('.pdf'):
    path = path.replace('.pdf','')
path = path + '.pdf'
size = get_font_size()


class PDF(FPDF):
    def header(self):
        pdf.image("assets/T-shirt.png",w = 190, x = Align.C)
        pdf.set_font("helvetica",style='',size= size)
        pdf.set_text_color(255,255,255)
        pdf.cell(txt= text,h= -270, w = 0, align= 'C')
            
pdf = PDF(orientation='portrait', unit='mm' ,format='A4')    
pdf.output(path)

