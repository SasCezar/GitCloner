import json
from collections import Counter
from os import listdir
from os.path import isfile, join
import csv

import re

file = open("/usr/share/dict/words", "r")
words = re.sub("[^\w]", " ", file.read()).split()
words.append("todo")
words.append("http")
words.append("https")
words.append("pentesting")
words = set(words)
words.remove('android')

def is_word(word):
    return word.lower() in words


def extract_domain_topics():
    meta_path = "../data/metadata/"
    with open("stoptopics.txt", "rt", encoding="utf8") as inf:
        languages = set([x.strip() for x in inf.readlines()])

    skipped = 0
    total = 0
    counter = Counter()

    with open("domain_topics_clean.csv", "wt", encoding="utf8") as outf:
        meta_files = [join(meta_path, f) for f in listdir(meta_path) if isfile(join(meta_path, f))]

        writer = csv.writer(outf)
        projects = Counter()
        for file in meta_files:
            with open(file, "rt", encoding="utf8") as inf:
                obj = json.load(inf)

                projects[obj["full_name"]] += 1
                for topic in obj["topics"]:
                    total += 1
                    words = [is_word(x) for x in topic.split("-")]
                    use = True
                    topic_og = topic
                    topic = "-".join([x for x, z in zip(topic.split("-"), words) if z])
                    if not topic or topic.lower() in languages  or any(
                            [1 if topic.lower() in x.lower() else 0 for x in languages]):
                        skipped += 1
                        use = False

                    if use:
                        projects[obj["full_name"]] += 1
                        counter[topic] += 1
                    writer.writerow([obj['full_name'], obj["domain"], topic, topic_og, use])

    print(total, skipped, f"{(skipped / total) * 100} % skipped")
    print(counter.most_common(100))
    print(projects.most_common(100))
    zero_p = sum([x[1] == 1 for x in projects.most_common(len(projects))])
    print(zero_p, len(projects), f"{(zero_p / len(projects)) * 100} % lost")


if __name__ == '__main__':
    extract_domain_topics()
