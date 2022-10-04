"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.
import sys
from typing import TextIO

from bed import BedLine, parse_bed, print_line
from query import QueryLine, Table, is_query_overlapping_with_bed, parse_query


def find_query_overlaps(table: Table, query: QueryLine) -> BedLine:
    """A generator that yields overlapping lines from the table with the query"""
    for bed in table.get_chrom(query.chrom):
        if is_query_overlapping_with_bed(query, bed):
            yield bed


def read_bed_file_into_table(bed_file: TextIO):
    """It reads a TextIO of bed seq"""
    table = Table()
    for bed_line in bed_file:
        table.add_line(parse_bed(bed_line))
    return table


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(description="Extract regions from a BED file")
    argparser.add_argument("bed", type=argparse.FileType("r"))
    argparser.add_argument("query", type=argparse.FileType("r"))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument(
        "-o",
        "--outfile",  # use an option to specify this
        metavar="output",  # name used in help text
        type=argparse.FileType("w"),  # file for writing
        default=sys.stdout,
    )

    # Parse options and put them in the table args
    args = argparser.parse_args()
    # Record lines into table
    table = read_bed_file_into_table(args.bed)
    # Find overlaps
    for query_line in args.query:
        query = parse_query(query_line)
        for match in find_query_overlaps(table, query):
            print_line(match, args.outfile)


if __name__ == "__main__":
    main()
