"""
Tests for format_bed module.
"""

import sys

import pytest

from bed import BedLine, parse_bed, print_line


def test_it_works_with_general_bed_line():
    """
    Given a bed line with different whitespaces, `parse_bed` works correctly.
    """
    line = "chr7    127471196    127472363              foo"
    expected_result = BedLine(
        chrom="chr7", chrom_start=127471196, chrom_end=127472363, name="foo"
    )
    assert parse_bed(line) == expected_result


def test_it_raises_exception_when_more_columns():
    """
    Given a bed line with more than 4 columns, `parse_bed` raises ValueError.
    """
    line_with_more_columns = "chr7    127471196    127472363         foo bar"
    with pytest.raises(ValueError):
        parse_bed(line_with_more_columns)


def test_it_raises_exception_when_less_columns():
    """
    Given a bed line with less than 4 columns, `parse_bed` raises ValueError.
    """
    line_with_less_columns = "chr7    127471196                  foo"
    with pytest.raises(ValueError):
        parse_bed(line_with_less_columns)


def test_it_prints_strict_bed_line(capsys):
    """
    Given a BedLine tuple, `print_line` uses \t.
    """
    bed = BedLine(chrom="chr1", chrom_start=20100, chrom_end=20101, name="foo")
    print_line(bed, sys.stdout)
    captured = capsys.readouterr()
    assert captured.out == "chr1\t20100\t20101\tfoo\n"
