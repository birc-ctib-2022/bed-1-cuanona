# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from query import QueryLine, is_overlapping, parse_query


def test_it_works_with_general_query_line():
    line = "chr7    127471196    127472363"
    expected_result = QueryLine(
        chrom='chr7', chrom_start=127471196, chrom_end=127472363)
    assert parse_query(line) == expected_result


def test_is_overlapping():
    segment1 = (0, 10)
    segment2 = (5, 6)
    assert is_overlapping(segment1, segment2) == True

    segment1 = (4, 10)
    segment2 = (1, 5)
    assert is_overlapping(segment1, segment2) == True

    segment1 = (4, 10)
    segment2 = (9, 15)
    assert is_overlapping(segment1, segment2) == True
