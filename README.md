# GitCloner
A GitHub scraper and cloner implemented in scrapy 


# Usage
To crawl you need a file (CSV) where you have a column named 'Name' and optionally 'Domain'.
You also need a GitHub API token. 

### Execution
There are two equivalent ways to run the scraper:

```commandline
python main.py <PATH_TO_FILE> <GIT_API_TOKEN>
```

```commandline
crapy crawl git-clone -s FILENAME=<PATH_TO_FILE> -s GIT_TOKEN=<GIT_API_TOKEN>
```

The second method allows for more control to ScraPy in case you want to change some parameters.
