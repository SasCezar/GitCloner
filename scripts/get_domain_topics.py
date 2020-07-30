import json
from os import listdir
from os.path import isfile, join
import csv


def extract_domain_topics():
    meta_path = "../data/metadata/"
    with open("domain_topics.csv", "wt", encoding="utf8") as outf:
        meta_files = [join(meta_path, f) for f in listdir(meta_path) if isfile(join(meta_path, f))]

        writer = csv.writer(outf)

        for file in meta_files:
            with open(file, "rt", encoding="utf8") as inf:
                obj = json.load(inf)

                for topic in obj["topics"]:
                    writer.writerow([obj['full_name'], obj["domain"], topic])


if __name__ == '__main__':
    extract_domain_topics()
