
#Install wkhtmltopdf from the link https://wkhtmltopdf.org/downloads.html

#Also pip install pdfkit

import pdfkit
path_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_url("https://www.bing.com/", "bing.pdf", configuration=config)
#Enter any url and filename you wants