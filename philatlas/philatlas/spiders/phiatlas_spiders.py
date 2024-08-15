import scrapy
from time import sleep
from .readers import factories


class PhilAtlasSpider(scrapy.Spider):
    """
    This class is a collection of functionality for reading the
    PhilAtlas website. PhilAtlas is a website with useful demographic
    data, and is much more readable and parsable than PSA-provided data.
    """

    name = "philatlas"
    start_urls = [
       "https://www.philatlas.com/luzon/ncr/pasig/rosario.html"
    ]

    def parse(self, response):
        # delay the parsing to reduce burden at PhilAtlas server
        sleep(2)
        table_id = "histPop"
        # find historical population table
        historical_population_table = response.css(f"[id='{table_id}']")
        table_reader = factories.TableReaderFactory.get_for(table_id)
        yield {
            table_id : table_reader(historical_population_table)
            }