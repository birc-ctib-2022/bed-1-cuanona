# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from bed import parse_bed
from query import QueryLine, is_overlapping, parse_query


def test_it_works_with_general_query_line():
    line = "chr7    127471196    127472363"
    expected_result = QueryLine(
        chrom='chr7', chrom_start=127471196, chrom_end=127472363)
    assert parse_query(line) == expected_result

def test_is_overlapping_inside():
    segment1 = (0, 10)
    segment2 = (5, 6)
    assert is_overlapping(segment1, segment2) == True


def test_is_overlapping_upper():
    segment1 = (4, 10)
    segment2 = (1, 5)
    assert is_overlapping(segment1, segment2) == True


def test_is_overlapping_bottom():
    segment1 = (4, 10)
    segment2 = (9, 15)
    assert is_overlapping(segment1, segment2) == True


def test_is_not_overlapping():
    segment1 = (389, 390)
    segment2 = (409, 850)
    assert is_overlapping(segment1, segment2) == False


def test_is_not_overlapping_when_upper_bound():
    segment1 = (520, 521)
    segment2 = (418,520)
    assert is_overlapping(segment1, segment2) == False


def test_is_overlapping_when_lower_bound():
    segment1 = (520, 521)
    segment2 = (520, 525)
    assert is_overlapping(segment1, segment2) == True


def test_is_overlapping_when_coincidence():
    segment1 = (520, 521)
    segment2 = (520, 521)
    assert is_overlapping(segment1, segment2) == True
