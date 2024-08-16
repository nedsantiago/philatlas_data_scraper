import scrapy
from scrapy.crawler import CrawlerProcess
from philatlas.spiders import philatlas_spiders



def scrape(urls: list):
    """
    This runs the philatlas spider
    """
    
    if not isinstance(urls, list):
        asrt_msg = f"URL's need to be in a list object. Given {urls}"
        raise TypeError(asrt_msg)

    # replace start urls with urls
    class ASpider(philatlas_spiders.PhilAtlasSpider):
        """
        This replaces the start urls
        """

        start_urls = urls

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