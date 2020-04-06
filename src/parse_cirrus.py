import bz2
import gzip
import json
import pickle

from tqdm import tqdm
from py4j.java_gateway import JavaGateway
gw = JavaGateway()
wakati = gw.entry_point
def tokenize(text):
    m = wakati.tokenize(text)
    tokens = []
    for i in range(len(m)):
        tokens.append(m[i].surface())
    return " ".join(tokens)

cirrus_all = {}
with gzip.open("data/jawiki-20200106-cirrussearch-content.json.gz") as fin:
    with bz2.open("data/201200106cirrus_all_sdt.tsv.bz2", 'wt') as fout:
        for line in tqdm(fin, total=2271620):
            json_line = json.loads(line)
            if "index" not in json_line:
                title = json_line["title"]
                text = json_line["text"]

                if title and text:
                    print("\t".join([title, tokenize(text).strip()]), file=fout)
