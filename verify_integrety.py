# verify that the necessary dependcies of the pdf do exist in the directory

import os


class check_integrity:
    def __init__(self, pdf_file="./store_data/test.pdf"):
        self.pdf_file = pdf_file

    def check_all_files(self):
        # if pdf, it's tei.xml , its xml file is present in the directory
        pdf = self.pdf_file
        files_to_check = [
            pdf,
            pdf.replace(".pdf", ".xml"),
            pdf.replace(".pdf", ".tei.xml"),
        ]

        status = []
        for file in files_to_check:
            status.append(os.path.exists(file))

        return all(status)


# pdf_file = "./store_data/test.pdf"
# status = check_integrity(pdf_file).check_all_files()
