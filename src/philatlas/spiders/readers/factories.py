from . import tables, ibox


class TableReaderFactory(object):
    """
    This class is a Factory that provides reader functions based on the string
    provided.
    """

    @classmethod
    def get_for(self, table_id: str) -> callable:
        """
        This method produces a reader function based on the provided string.

        Arguments:
            table_id: the HTML id of the table as seen when inspecting.
        
        Returns:
            A callable function that can read the declared table.

        Example:
            >>> histpop_reader = ReaderFactory().get("histPop")
            >>> histpop_reader(html_table)
        """

        # table id indicates what reader to use
        match table_id:
            case "histPop":
                # initialize the reader
                return tables.DateTableReader.read_raw_table
            case "popByAgeGrpTable":
                return tables.RawTableReader.read_raw_table
            case "households-table":
                # initialize the reader
                return tables.DateTableReader.read_raw_table
            case "table.iBox":
                # initialize the reader
                return ibox.read_ibox
            
            # if no cases, raise an error
            case _:
                err_msg = f"No reader for table with id={table_id}"
                raise ValueError(err_msg)
            