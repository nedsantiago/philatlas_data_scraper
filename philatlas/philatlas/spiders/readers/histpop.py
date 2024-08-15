import datetime
from scrapy.selector.unified import SelectorList


def histpop_reader(table_data: SelectorList) -> list:
    """
    This function reads the PhilAtlas Historical Population Table and
    returns a list of dictionaries

    Arguments:
        table_data: HTML table as a result of the response.css method

    Returns:
        A list of dictionaries that can be fed into a pandas dataframe

    Example:
        >>> histpop_table = response.css("[id='histPop']")
        >>> histpop_reader(histpop_table)
    """

    # parse for header
    historical_population_headers = table_data.css("thead").css("th::text").getall()
    # parse for body
    historical_population_body = table_data.css("tbody").css("tr")

    # initialize the table output as list of dictionaries
    data = list()
    # get values in body
    for table_row in historical_population_body:
        str_date = table_row.css("th").xpath("//time/@datetime").extract_first()
        # convert date to date object
        date = datetime.date.fromisoformat(str_date)
        population = table_row.css("td::text")[0].get()
        population_increase = table_row.css("td::text")[1].get()

        # append the row header then all row data
        data.append({
            historical_population_headers[0] : date,
            historical_population_headers[1] : population,
            historical_population_headers[2] : population_increase
            })
    
    return data