import datetime
from abc import ABC, abstractclassmethod
from scrapy.selector.unified import SelectorList


class TableReader(ABC):
    """
    This class collects all functions/methods realted to reading tables
    from the PhilAtlas website.
    """

    @classmethod
    def read_raw_table(self, table_data: SelectorList) -> list:
        """
        This method reads the PhilAtlas Population Age Group Table and
        returns a list of dictionaries

        Arguments:
            table_data: HTML table as a result of the response.css method

        Returns:
            A list of dictionaries that can be fed into a pandas dataframe

        Example:
            >>> histpop_table = response.css("[id='histPop']")
            >>> TableReader.read_raw_table(histpop_table)
        """

        asrt_msg = f"Expected: {SelectorList}, Given: {type(table_data)}"
        assert type(table_data) is SelectorList, asrt_msg

        # parse for header
        headers = self.get_table_headers(table_data)
        # parse for body
        body = self.get_table_body(table_data)

        # initialize the table output as list of dictionaries
        data = list()
        # get values in body
        for table_row in body:
            row_dictionary = dict()
            # append the header in row
            row_header = self.get_body_row_header(table_row)
            # append the data in row
            row_data = self.get_body_row_data(table_row)

            # recreate row as a dictionary 
            # first column
            row_dictionary[headers[0]] = row_header
            # other columns
            for i in range(1, len(headers)):
                row_dictionary[headers[i]] = row_data[i - 1]
            # append the dictionary to data
            data.append(row_dictionary)

        return data
    
    @abstractclassmethod
    def get_table_headers(cls, table_data):
        raise NotImplementedError

    @abstractclassmethod
    def get_table_body(cls, table_data):
        raise NotImplementedError

    @abstractclassmethod
    def get_body_row_header(cls, table_row):
        raise NotImplementedError

    @abstractclassmethod
    def get_body_row_data(cls, table_row):
        raise NotImplementedError
    

class RawTableReader(TableReader):
    @classmethod
    def get_table_headers(cls, table_data):
        return table_data.css("thead").css("th::text").getall()

    @classmethod
    def get_table_body(cls, table_data):
        return table_data.css("tbody").css("tr")

    @classmethod
    def get_body_row_header(cls, table_row):
        return table_row.css("th::text").get()

    @classmethod
    def get_body_row_data(cls, table_row):
        return table_row.css("td::text").getall()
    

class DateTableReader(TableReader):
    @classmethod
    def get_table_headers(cls, table_data):
        return table_data.css("thead").css("th::text").getall()

    @classmethod
    def get_table_body(cls, table_data):
        return table_data.css("tbody").css("tr")

    @classmethod
    def get_body_row_header(cls, table_row):
        # convert row header into a date object
        str_date = table_row.css("time::attr(datetime)").get()
        # convert date to date object
        date = datetime.date.fromisoformat(str_date)
        return date

    @classmethod
    def get_body_row_data(cls, table_row):
        return table_row.css("td::text").getall()
