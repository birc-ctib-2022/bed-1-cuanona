# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from sys import stdout
import sys
import pytest
from bed import BedLine, parse_bed, print_line


def test_it_works_with_general_bed_line():
    line = "chr7    127471196    127472363              foo"
    expected_result = BedLine(
        chrom='chr7', chrom_start=127471196, chrom_end=127472363, name='foo')
    assert parse_bed(line) == expected_result


def test_it_raises_exception_when_more_columns():
    line_with_more_columns = "chr7    127471196    127472363         foo bar"
    with pytest.raises(ValueError):
        parse_bed(line_with_more_columns)


def test_it_raises_exception_when_less_columns():
    line_with_less_columns = "chr7    127471196                  foo"
    with pytest.raises(ValueError):
        parse_bed(line_with_less_columns)


def test_it_prints_strict_BedLine(capsys):
    bed = BedLine(chrom='chr1', chrom_start=20100, chrom_end=20101, name='foo')
    print_line(bed, sys.stdout)
    captured = capsys.readouterr()
    assert captured.out == 'chr1\t20100\t20101\tfoo\n'
