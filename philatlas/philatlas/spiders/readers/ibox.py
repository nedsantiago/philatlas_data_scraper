from abc import ABC, abstractclassmethod
from scrapy.selector.unified import SelectorList


def read_ibox(table_data: SelectorList) -> dict:
    """
    This method/function reads the PhilAtlas iBox Table and
    returns a dictionary

    Arguments:
        table_data: HTML table as a result of the response.css method

    Returns:
        A list of dictionaries that can be fed into a pandas dataframe

    Example:
        >>> ibox_table = response.css("table.iBox").css("tbody").css("tr")
        >>> read_ibox(ibox_table)
    """

    asrt_msg = f"Expected: {SelectorList}, Given: {type(table_data)}"
    assert type(table_data) is SelectorList, asrt_msg

    # get body and divide into table rows
    body = table_data.css("tr")

    return_dict = dict()
    # get data for each row
    for row in body:
        # get row header
        row_header = row.css("th::text").get()
        # get data or anchor
        # try as td
        row_data = row.css("td::text").get()
        # try anchor if no data
        if not row_data:
            row_data = row.css("a::text").get()
        
        try:
            return_dict[row_header] = row_data

        except KeyError as e:
            raise e
    
    return return_dict