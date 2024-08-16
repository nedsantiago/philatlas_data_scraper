import scrapy
from scrapy.crawler import CrawlerProcess
from philatlas.spiders import philatlas_spiders



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


scrape("https://www.philatlas.com/mindanao/r11/davao-del-sur/hagonoy/leling.html")