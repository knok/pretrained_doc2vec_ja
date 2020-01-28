import bz2
import gzip
import json
import pickle

from sudachipy import tokenizer
from sudachipy import dictionary
from tqdm import tqdm


wakati = dictionary.Dictionary().create()
def wakati_parse(text):
    tokens = [m.surface() for m in wakati.tokenize(text)]
    return " ".join(tokens)

cirrus_all = {}
with gzip.open("data/jawiki-20200106-cirrussearch-content.json.gz") as fin:
    with bz2.open("data/20200106cirrus_all.tsv.bz2", 'wt') as fout:
        for line in tqdm(fin, total=2271620):
            json_line = json.loads(line)
            if "index" not in json_line:
                title = json_line["title"]
                text = json_line["text"]

                if title and text:
                    print("\t".join([title, wakati_parse(text).strip()]), file=fout)
