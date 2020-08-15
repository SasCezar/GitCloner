import sys

from scrapy import cmdline
cmdline.execute(f"scrapy crawl git-clone -s FILENAME={sys.argv[1]} -s GIT_TOKEN={sys.argv[2]}".split())