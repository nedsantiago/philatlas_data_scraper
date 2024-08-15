import scrapy
from time import sleep
from . import readers


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
        # list of id's to find
        READ_TABLES = [
            "households-table",
            "popByAgeGrpTable",
            "histPop"
            ]
        # result data
        result_data = dict()
        for table_id in READ_TABLES:
            # get table data
            raw_table = response.css(f"[id='{table_id}']")
            table_reader = readers.factories.TableReaderFactory.get_for(table_id)
            try:
                # add to dictionary
                result_data[table_id] = table_reader(raw_table)
            except ValueError as e:
                result_data[table_id] = []

        yield result_data
