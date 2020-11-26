import sys

from scrapy import cmdline
cmdline.execute(f"scrapy crawl git-clone "
                f"-s FILENAME={sys.argv[1]} "
                f"-s USER_AGENT={sys.argv[2]} "
                f"-s GIT_TOKEN={sys.argv[3]}".split())