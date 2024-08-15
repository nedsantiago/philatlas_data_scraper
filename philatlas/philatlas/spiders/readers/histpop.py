import datetime
from scrapy.selector.unified import SelectorList


def read_history_population(table_data: SelectorList) -> list:
    """
    This function reads the PhilAtlas Historical Population Table and
    returns a list of dictionaries

    Arguments:
        table_data: HTML table as a result of the response.css method

    Returns:
        A list of dictionaries that can be fed into a pandas dataframe

    Example:
        >>> histpop_table = response.css("[id='histPop']")
        >>> read_history_population(histpop_table)
    """

    asrt_msg = f"Expected: {SelectorList}, Given: {type(table_data)}"
    assert type(table_data) is SelectorList, asrt_msg

    # parse for header
    historical_population_headers = table_data.css("thead").css("th::text").getall()
    # parse for body
    historical_population_body = table_data.css("tbody").css("tr")

    # initialize the table output as list of dictionaries
    data = list()
    # get values in body
    for table_row in historical_population_body:
        str_date = table_row.css("time::attr(datetime)").get()
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


def read_age_group_population(table_data: SelectorList) -> list:
    """
    This function reads the PhilAtlas Population Age Group Table and
    returns a list of dictionaries

    Arguments:
        table_data: HTML table as a result of the response.css method

    Returns:
        A list of dictionaries that can be fed into a pandas dataframe

    Example:
        >>> histpop_table = response.css("[id='histPop']")
        >>> read_age_group_population(histpop_table)
    """

    asrt_msg = f"Expected: {SelectorList}, Given: {type(table_data)}"
    assert type(table_data) is SelectorList, asrt_msg

    # parse for header
    headers = table_data.css("thead").css("th::text").getall()
    # parse for body
    body = table_data.css("tbody").css("tr")

    # initialize the table output as list of dictionaries
    data = list()
    # get values in body
    for table_row in body:
        row_dictionary = dict()
        # append the header in row
        row_header = table_row.css("th::text").get()
        # append the data in row
        row_data = table_row.css("td::text").getall()

        # recreate row as a dictionary 
        # first column
        row_dictionary[headers[0]] = row_header
        # other columns
        for i in range(1, len(headers)):
            row_dictionary[headers[i]] = row_data[i - 1]
        # append the dictionary to data
        data.append(row_dictionary)

    return data