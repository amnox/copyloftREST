from pyPdf import PdfFileReader


class PDF:
    def __init__(self,input_file):
        self.input_file=input_file

    def get_page_count(self):
        pdf = PdfFileReader(self.input_file)
        return pdf.getNumPages()
