from typing import List
import logging
import os
import pytest
from dep_graph.dep_graph import DependencyHandler


@pytest.fixture(scope="module")
def expected_outputs() -> List[str]:
    case_filenames = ["case1_out.txt", "case2_out.txt", "case3_out.txt"]
    test_dir = os.path.dirname(__file__)

    all_case_outputs = []
    for case_filename in case_filenames:
        with open(os.path.join(test_dir, case_filename)) as out_file:
            case_output = out_file.read()
            all_case_outputs.append(case_output)
    return all_case_outputs


def test_print_dependencies(capfd, expected_outputs: List[str]):
    input_filenames = ["deps1.json", "deps2.json", "deps3.json"]
    test_dir = os.path.dirname(__file__)

    for input_filename, expected in zip(input_filenames, expected_outputs):
        logging.info(f"Testing input: {input_filename}")
        handler = DependencyHandler(os.path.join(test_dir, input_filename))
        handler.load_dependencies()
        handler.print_dependencies()
        out, err = capfd.readouterr()
        # assert not err, "An error is raised during the execution."
        assert (
            out == expected
        ), "Function output does not match with the expected output."
