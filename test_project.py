import project
import pytest
import json


SCRAPE_VALIDATION_TESTS = [
    (r"C:\Users\admin\01Hobby\cs50\cs50p\final_project\tests\data\rosario\Rosario, Pasig Profile – PhilAtlas.htm", r"./tests/data/rosario/rosario.json")
]

@pytest.mark.parametrize("input, label", SCRAPE_VALIDATION_TESTS)
def test_scrape(input, label):
    urls = input
    with open(label) as json_file:
        # run the scrape on the input data
        result = project.scrape(urls)
        # load the label (expected results) data
        label_data = json.load(json_file)
        # compare
        asrt_msg = (
            f"Result did not match expected data\n"
            f"[EXPECTED]\n"
            f"{label_data}\n"
            f"[OUTPUT]\n"
            f"{result}"
            )
        if result != label_data:
            raise AssertionError(asrt_msg)

