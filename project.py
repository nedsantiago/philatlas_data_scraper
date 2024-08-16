# The majority of the work making this python program was
# for making the following:
# philatlas/spiders/philatlas_spider.py - a web scraper
# philatlas/spiders/readers/factories.py - an OOP implementation using Factory
#   and abstract factory
# test_project.py - a module for testing the code
# philatlas/spiders/readers/ibox.py - a module for interpreting html summaries
# philatlas/spiders/readers/tables/py  - a module for interpreting html tables
# 
# Due to the nature of the Scrapy module, implementing pytests was limited
# since restarting the scrapy is not allowed by the module itself.

from scrapy.crawler import CrawlerProcess
from philatlas.spiders import philatlas_spiders
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python -m scrapy philatlas [PhilAtlas]")
    else:
        url = sys.argv[1]
    # scrape for aguho
    scrape(url)


def scrape(urls: str):
    """
    This runs the philatlas spider
    """

    asrt_msg = "Scrape function only supports one url at a time"
    assert isinstance(urls, str), asrt_msg
    
    class ASpider(philatlas_spiders.PhilAtlasSpider):
        """
        This replaces the start urls
        """

        start_urls = [urls]

    # initialize a processing object
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "output.jsonl": {"format": "json"},
            },
        }
    )
    process.crawl(ASpider)
    process.start()


def scrape_aguho():
    # declare file location
    WEBSITE = "https://www.philatlas.com/visayas/r07/cebu/daanbantayan/aguho.html"
    # begin scrape
    scrape(WEBSITE)


def scrape_leling():
    # declare file location
    WEBSITE = "https://www.philatlas.com/mindanao/r11/davao-del-sur/hagonoy/leling.html"
    # begin scrape
    scrape(WEBSITE)

def scrape_rosario():
    # declare file location
    WEBSITE = "https://www.philatlas.com/luzon/ncr/pasig/rosario.html"
    # begin scrape
    scrape(WEBSITE)


if __name__ == "__main__":
    main()