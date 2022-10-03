"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    parse_bed_line, print_line
)
from query import Table, is_overlapping, is_query_overlapping_with_bed, parse_query


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

    for query_line in args.query:
        query = parse_query(query_line)
        for bed_line in args.bed:
            if query.chrom != bed.chrom:
                pass
            else:
                bed = parse_bed_line(bed_line)
                if is_query_overlapping_with_bed(query, bed):
                    print_line(bed, args.outfile)
    

if __name__ == '__main__':
    main()
