"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from typing import TextIO
from bed import (
    parse_bed, print_line
)
from query import QueryLine, Table, is_overlapping, is_query_overlapping_with_bed, parse_query


def print_query_overlap(table:Table, output_file: TextIO, query:QueryLine):
    for bed in table.get_chrom(query.chrom):
        if is_query_overlapping_with_bed(query, bed):
            print_line(bed, output_file)


def read_bed_file_into_table(bed_file):
    table = Table()
    for bed_line in bed_file:
        table.add_line(
            parse_bed(bed_line)
        )
    return table

def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',  # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()
    # Record lines into table
    table = read_bed_file_into_table(args.bed)
    # Find overlaps
    for query_line in args.query:
        query = parse_query(query_line)
        print_query_overlap(table, args.outfile, query)

if __name__ == '__main__':
    main()
