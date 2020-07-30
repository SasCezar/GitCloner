import json

import scrapy
import pandas
from subprocess import call
from os import path
from pathlib import Path
import shutil


class GitSpider(scrapy.Spider):
    name = "git-clone"
    repo_out = "./data/repositories/"
    meta_out = "./data/metadata/"

    api_endpoint = "https://api.github.com"
    header = "application/vnd.github.v3+json,application/vnd.github.mercy-preview+json"
    token = "c2ee73cb0147e4d724598f76715f3b87f3253939"

    clean_key = ['owner', 'organization', 'temp_clone_token']

    def start_requests(self):
        df = pandas.read_csv("./GitCloner/resources/borges_et_al_2016.csv", encoding="utf8")

        names = df['Name']
        domains = df['Domain']

        urls = [self.api_endpoint + "/repos/" + name for name in names]
        for url, domain in zip(urls, domains):
            yield scrapy.Request(url=url,
                                 callback=self.parse,
                                 headers={"Accept": self.header, "Authorization": f"token {self.token}"},
                                 cb_kwargs={"domain": domain})

    def parse(self, response, **kwargs):
        obj = response.json()
        domain = kwargs['domain']
        obj['domain'] = domain
        obj = self.clean(obj)
        clone_url = obj['clone_url']
        name = obj['full_name'].replace("/", "|")

        dirpath = Path(path.join(self.repo_out, name))
        #if dirpath.exists() and dirpath.is_dir():
        #    shutil.rmtree(dirpath)

        with open(f"{path.join(self.meta_out, name)}.json", "w", encoding="utf8") as outf:
            outf.write(json.dumps(obj, ensure_ascii=False, indent=4))

        #call(["git", "clone", "--depth", "1", clone_url, path.join(self.repo_out, name)])

    def clean(self, obj):
        for key in self.clean_key:
            if key in obj:
                del obj[key]

        return obj