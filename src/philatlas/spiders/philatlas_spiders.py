import scrapy
from time import sleep
from .readers.factories import TableReaderFactory


class PhilAtlasSpider(scrapy.Spider):
    """
    This class is a collection of functionality for reading the
    PhilAtlas website. PhilAtlas is a website with useful demographic
    data, and is much more readable and parsable than PSA-provided data.
    """

    name = "philatlas"
    start_urls = list()

    def parse(self, response):
        # delay the parsing to reduce burden at PhilAtlas server
        sleep(5)
        # initalize dictionary
        result_data = dict()
        # get summary data
        SUMMARY_TABLE_ID = "table.iBox"
        table_reader = TableReaderFactory.get_for(SUMMARY_TABLE_ID)
        summary = table_reader(response.css(SUMMARY_TABLE_ID))

        result_data["name"] = response.css("h1::text").get()
        result_data["summary"] = summary

        # list of id's to find
        READ_TABLES = [
            "households-table",
            "popByAgeGrpTable",
            "histPop"
            ]
        # result data
        for table_id in READ_TABLES:
            # get table data
            raw_table = response.css(f"[id='{table_id}']")
            table_reader = TableReaderFactory.get_for(table_id)
            try:
                # add to dictionary
                result_data[table_id] = table_reader(raw_table)
            except ValueError as e:
                result_data[table_id] = []

        yield result_data

        # find what to add to list
        self.start_urls = self.start_urls + list(response.css("th").css("a::attr(href)").getall())

        print(f"Remaining urls to go through:\n[START LIST]\n{self.start_urls}\n[END LIST]")
        # if at start again
        if not len(self.start_urls) > 1:
            # begin condition for end sequence
            next_page = None
        else:
            # continue
            next_page = self.start_urls.pop()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)