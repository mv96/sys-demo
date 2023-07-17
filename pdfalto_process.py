# this code file applies pdfalto on pdfs
import os
import subprocess


class pdfalto_on_pdfs:
    def __init__(self, pdfalto_path="./pdfalto/pdfalto"):
        self.pdfalto_path = pdfalto_path

    def fit(self, pdf):
        subprocess.run(
            [
                "{}".format(self.pdfalto_path),
                "-annotation",
                "-readingOrder",
                "{}".format(pdf),
            ]
        )


# file_path = "./store_data/test.pdf"
# pdfalto = "./pdfalto/pdfalto"

# client = pdfalto_on_pdfs(pdfalto_path=pdfalto)
# client.fit(file_path)
