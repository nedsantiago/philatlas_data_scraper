import scrapy
import datetime
from time import sleep


class PhilAtlasSpider(scrapy.Spider):
    """
    This class is a collection of functionality for reading the
    PhilAtlas website. PhilAtlas is a website with useful demographic
    data, and is much more readable and parsable than PSA-provided data.
    """

    name = "philatlas"
    start_urls = [
        "https://www.philatlas.com/luzon/ncr/pasig/rosario.html",
        "https://www.philatlas.com/mindanao/r11/davao-del-sur/hagonoy/leling.html"
    ]

    def parse(self, response):
        # delay the parsing to reduce burden at PhilAtlas server
        sleep(2)
        # find historical population table
        historical_population_table = response.css("[id='histPop']")
        # parse for header
        historical_population_headers = historical_population_table.css("thead").css("th::text").getall()
        # parse for body
        historical_population_body = historical_population_table.css("tbody").css("tr")
        # get values in body
        for table_row in historical_population_body:
            str_date = table_row.css("th").xpath("//time/@datetime").extract_first()
            date = datetime.date.fromisoformat(str_date)
            population = table_row.css("td::text")[0].get()
            population_increase = table_row.css("td::text")[1].get()
            yield {
                "island_group" : "luzon",
                "region" : "ncr",
                "province" : "",
                "muni_city" : "pasig",
                "barangay" : "rosario",
                historical_population_headers[0] : date,
                historical_population_headers[1] : population,
                historical_population_headers[2] : population_increase
            }
