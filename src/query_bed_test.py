"""Tests for query_bed module"""

from query import QueryLine, is_overlapping, parse_query


def test_it_works_with_general_query_line():
    """Given a query line as a string, `parse_query` works correctly."""
    line = "chr7    127471196    127472363"
    expected_result = QueryLine(
        chrom="chr7", chrom_start=127471196, chrom_end=127472363
    )
    assert parse_query(line) == expected_result


def test_is_overlapping_inside():
    """
    Given an interval B which is inside interval A, `is_overlapping` returns True.
    """
    interval_a = (0, 10)
    interval_b = (5, 6)
    assert is_overlapping(interval_a, interval_b)


def test_is_overlapping_upper():
    """
    Given an interval B which overlaps with the bottom
    part of interval A, `is_overlapping` returns True.
    """
    interval_a = (4, 10)
    interval_b = (1, 5)
    assert is_overlapping(interval_a, interval_b)


def test_is_overlapping_bottom():
    """
    Given an interval B which overlaps with the upper part of
    interval A, `is_overlapping` returns True.
    """
    interval_a = (4, 10)
    interval_b = (9, 15)
    assert is_overlapping(interval_a, interval_b)


def test_is_not_overlapping():
    """
    Given two intervals, A and B, which don't overlap,
    `is_overlapping` returns False.
    """
    interval_a = (389, 390)
    interval_b = (409, 850)
    assert not is_overlapping(interval_a, interval_b)


def test_is_not_overlapping_when_upper_bound():
    """
    Given two non-overlapping intervals, A and B, for which the lower bound
    of A is equal to the upper bound of B, `is_overlapping` returns False.
    """
    interval_a = (520, 521)
    interval_b = (418, 520)
    assert not is_overlapping(interval_a, interval_b)


def test_is_overlapping_when_lower_bound():
    """
    Given two intervals, A and B, for which the lower bound of A is equal to
    the lower bound of B, `is_overlapping` returns True.
    """
    interval_a = (520, 521)
    interval_b = (520, 525)
    assert is_overlapping(interval_a, interval_b)


def test_is_overlapping_when_coincidence():
    """Given two equal intervals, A and B, `is_overlapping` returns True."""
    interval_a = (520, 521)
    interval_b = (520, 521)
    assert is_overlapping(interval_a, interval_b)
