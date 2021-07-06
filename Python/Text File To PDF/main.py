
#required module-pip install fpdf
from fpdf import FPDF

#intializing fpdf
mypdf = FPDF()

#adding a page
mypdf.add_page()

#setting a font
mypdf.set_font('times', size=16)

#opening a file
f = open('myfile.txt', 'r')


#reading a file line by line and adding to pdf
for i in f:

    mypdf.cell(200, 12, txt=i, ln=1, align='C')


#creating a pdf
mypdf.output('mypdf.pdf')

