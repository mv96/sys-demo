from preprocessing.grobid_clean import Preprocess_using_grobid
from preprocessing.visualize_annot import annotations_page
import pandas as pd
import cv2
import math
from tqdm import tqdm


class assigning_labels:
    def __init__(self, show_images=False, grobid_xml=None):
        self.show_images = show_images
        self.path_images = grobid_xml.rsplit("/", 1)[0] + "/images"
        self.scales = None
        self.grobid_xml = grobid_xml

    def fit(self):
        # traverse through each of the annotation box
        # further traverse through each of the boxes on the given page
        # for every box in the grobid see if this box fits under the  annotation
        # if yes then merge it all together
        prep = Preprocess_using_grobid()
        images, scales, dict_coords = prep.fit(
            grobid_xml=self.grobid_xml, show_results=False
        )

        grobid_boxes = []

        for k in dict_coords.keys():
            for element in dict_coords[k]:
                grobid_boxes.append(element)

        df = pd.DataFrame(
            data=grobid_boxes,
            columns=["page_no", "top_left", "bot_right", "text"],
        )
        return df, scales, images
