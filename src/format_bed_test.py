# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import pytest
from bed import BedLine, parse_line


def test_it_works_with_general_bed_line():
    line = "chr7    127471196    127472363              foo"
    expected_result = BedLine(
        chrom='chr7', chrom_start=127471196, chrom_end=127472363, name='foo')
    assert parse_line(line) == expected_result


def test_it_raises_exception_when_more_columns():
    line_with_more_columns = "chr7    127471196    127472363         foo bar"
    with pytest.raises(ValueError):
        parse_line(line_with_more_columns)


def test_it_raises_exception_when_less_columns():
    line_with_less_columns = "chr7    127471196                  foo"
    with pytest.raises(ValueError):
        parse_line(line_with_less_columns)
