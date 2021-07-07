import os
import sys

import fpdf     # for txt to pdf
from win32com import client     # for excel to pdf
from docx2pdf import convert

def Text2Pdf(filename):
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=10)
    
    f=open(filename,'r')
    # writing content to pdf
    for x in f:
        pdf.cell(200,10,txt=x,ln=1,align='c')
    # pdf file saved
    pdf.output(filename.replace(".txt",".pdf"))


def Ppt2Pdf(filename):
    # executing the command, conversion done !!
    os.system("ppt2pdf file "+filename)

def Excel2Pdf(filename):
    #open microsoft excel (using it's built-in functionality)
    excel = client.Dispatch("Excel.Application")
    
    # reading excel file
    sheets=excel.Workbooks.open(os.path.abspath(filename))
    work_sheets=sheets.Worksheets[0]

    # creating new filename with .pdf extension to save resulting file in current dir
    new_file_name = filename.replace(".xlsx",".pdf")
    new_file_name = os.path.join(os.getcwd(),new_file_name)
    # converting to pdf file
    work_sheets.ExportAsFixedFormat(0,os.path.abspath(new_file_name))

def Docx2Pdf(filename):
    # conversion done
    convert(filename)

def main():
    print("---->Welcome To Universal PDF Converter<----\n")
    filename = input("Enter the file name(with extension): ")
    
    if os.path.exists(filename)==False:
        print("Error! no such file present in current directory.")
        sys.exit(-1)
    if filename.endswith(".txt"):
        Text2Pdf(filename)
    elif filename.endswith(".ppt") or filename.endswith(".pptx"):
        Ppt2Pdf(filename)
    elif filename.endswith(".docx"):
        Docx2Pdf(filename)
    elif filename.endswith(".xlsx"):
        Excel2Pdf(filename)

if __name__=="__main__":
    main()