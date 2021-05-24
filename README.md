# GitCloner
A GitHub scraper and cloner implemented in scrapy 


# Usage
To crawl you need a file (CSV) where you have a column named 'Name' and optionally 'Domain' which indicates the label of the
project.  The 'Name' is formatted as `<user>/<repo>` (e.g. `SasCezar/GitCloner`). 
You also need your GitHub username and a [GitHub API token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token),
this is optional, but it will drastically increase the limit of the APIs. 

### Execution
There are two equivalent ways to run the scraper:

```commandline
python main.py <PATH_TO_FILE> <GIT_USERNAME> <GIT_API_TOKEN>
```

```commandline
scrapy crawl git-clone -s FILENAME=<PATH_TO_FILE> -s USER_AGENT=<USERNAME> -s GIT_TOKEN=<GIT_API_TOKEN>
```

The second method allows for more control to scrapy in case you want to change other parameters.
