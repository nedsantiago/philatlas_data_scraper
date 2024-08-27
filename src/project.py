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


if __name__ == "__main__":
    main()