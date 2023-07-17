# this python file will run the entire preprocessing step just before running the models
from grobid_client_process import grobid_client
from pdfalto_process import pdfalto_on_pdfs
from verify_integrety import check_integrity
from merge import preprocessed_dataframe
import time

start = time.time()
# initialize the grobid server do with cmd line before
pdf_path = "./store_data/test.pdf"
pdf_folder = pdf_path.rsplit("/", 1)[0]  # this is the pdf we want to convert

# running the grobid client
Grobidclient = grobid_client()
tick = time.time()
Grobidclient.fit(pdf_file_path=pdf_folder)
print("the time to run the grobid client is", time.time() - tick)

# running pdf alto
client = pdfalto_on_pdfs()
tick = time.time()
client.fit(pdf_path)
print("the time to run the pdfalto client is", time.time() - tick)

# verify integrety
status = check_integrity(pdf_path).check_all_files()
if status:  # if everything is okay then run merge
    # build the dependency path from the pdf_file
    grobid_xml = pdf_path.replace(".pdf", ".tei.xml")
    pdf_alto_xml_main = pdf_path.replace(".pdf", ".xml")
    set = [grobid_xml, pdf_alto_xml_main, pdf_path]
    excel_file = "./preprocessing/output.xlsx"

    prep = preprocessed_dataframe(set=set, excel_file=excel_file)
    tick = time.time()
    res = prep.fit()
    res.to_csv("data.csv")
    print("the time to run the merge client is", time.time() - tick)
end = time.time()
print("total code time is ", end - start)
