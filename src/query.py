"""Module for querying a genome.

The code in this module is, again, something we haven't seen yet, but you don't
need to understand it to use it. It gives you a table where you can insert
BedLine objects and then access them per chromosome. Create a table and insert
BED lines it like below, and when you later want to get only the lines relevant
for a given chromosome, you can use the get_chrom() method:

>>> from bed import BedLine
>>> table = Table()
>>> table.add_line(BedLine('chr1', 0, 1, 'foo'))
>>> table.add_line(BedLine('chr2', 0, 1, 'bar'))
>>> table.add_line(BedLine('chr1', 10, 11, 'baz'))
>>> table.get_chrom('chr1')
[BedLine(chrom='chr1', chrom_start=0, chrom_end=1, name='foo'), BedLine(chrom='chr1', chrom_start=10, chrom_end=11, name='baz')]
"""

from typing import NamedTuple
from xmlrpc.client import Boolean
from bed import BedLine
from collections import defaultdict

QueryLine = NamedTuple("QueryLine", [
    ('chrom', str),
    ('chrom_start', int),
    ('chrom_end', int)
])


def parse_query(line: str) -> QueryLine:
    """Parse a single line query (with three columns).

    >>> parse_query('chr1   1  10')
    QueryLine(chrom='chr1', chrom_start=1, chrom_end=10)

    """
    chrom, start, end = line.split()  # split on any white-space
    query_line = QueryLine(chrom, int(start), int(end))
    return query_line


def is_overlapping(x: tuple[int, int], y: tuple[int, int]) -> Boolean:
    return x[0] <= y[0] or x[1] >= y[1]


def is_query_overlapping_with_bed(query: QueryLine, bed: BedLine) -> Boolean:
    return is_overlapping(
        (query.chrom_start, query.chrom_end), (bed.chrom_start, bed.chrom_end)
    )

class Table:
    """Table containing bed-lines."""

    tbl: dict[str, list[BedLine]]

    def __init__(self) -> None:
        """Create a new table."""
        self.tbl = defaultdict(lambda: [])

    def add_line(self, line: BedLine) -> None:
        """Add line to the table."""
        self.tbl[line.chrom].append(line)

    def get_chrom(self, chrom: str) -> list[BedLine]:
        """Get all the lines that sits on chrom"""
        return self.tbl[chrom]
        
