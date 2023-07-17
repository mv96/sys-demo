# this is the main file that contains the calls to other functions that are used inside this one,

from grobid_client_python.grobid_client.grobid_client import GrobidClient


class grobid_client:
    def __init__(self, config_file_path="./grobid_client_python/config.json"):
        self.config_file_path = config_file_path
        self.client = GrobidClient(
            config_path=self.config_file_path
        )  # specify the config.json file

    def fit(self, pdf_file_path):
        res = self.client.process(
            "processFulltextDocument",
            pdf_file_path,
            n=20,
            generateIDs=True,
            consolidate_citations=False,  ####check with pierre
            tei_coordinates=True,
            segment_sentences=True,
            include_raw_affiliations=True,
            include_raw_citations=True,
        )


# pdf_file_path = "./store_data"  # using a temporary file path
# config_file_path = "./grobid_client_python/config.json"

# client = grobid_client(config_file_path="./grobid_client_python/config.json")
# client.fit(pdf_file_path)
