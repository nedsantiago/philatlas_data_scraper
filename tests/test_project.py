import project
import pytest
import json
import logging
from pathlib import Path
from philatlas.spiders.readers.tables import DateTableReader
from scrapy.selector.unified import SelectorList
from twisted.internet.error import ReactorNotRestartable

relpath = Path(r"./tests/data/rosario/Rosario, Pasig Profile – PhilAtlas.htm")
abspath = relpath.resolve()
rosario_path = f"file://{abspath.as_posix()}"

SCRAPE_VALIDATION_TESTS = [
    (f"file://{abspath.as_posix()}", r"./tests/data/rosario/rosario.json")
]

@pytest.mark.parametrize("input, label", SCRAPE_VALIDATION_TESTS)
def test_scrape(input, label):
    # erase data from output file
    open('output.jsonl', 'w').close()
    logger = logging.getLogger(__name__)
    url = input

    with open(label, "r", encoding="utf-8") as json_file:
        # run the scrape on the input data
        project.scrape(url)
        # load the label (expected results) data
        label_data = json.load(json_file)
    with open("output.jsonl", "r", encoding="utf-8") as output_file:
        result = json.load(output_file)
        # compare
        asrt_msg = (
            f"Result did not match expected data\n"
            f"[EXPECTED]\n"
            f"{label_data}\n"
            f"[OUTPUT]\n"
            f"{result}"
            )
        if result != label_data:
            logger.critical(asrt_msg)
            raise AssertionError(asrt_msg)


def test_scrape_aguho():
    with pytest.raises(ReactorNotRestartable):
        project.scrape_aguho()
        


def test_scrape_leling():
    with pytest.raises(ReactorNotRestartable):
        project.scrape_leling()