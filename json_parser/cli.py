"""
The command-line interface for the parser
"""

import argparse
from pprint import pprint
from .commodity_json_parser import json_parser


def main():
    parser = argparse.ArgumentParser(
        description="A json file parser to demonstrate python packaging."
    )
    parser.add_argument(
        "filepath", type=str,
        help="The PATH of the json file to be parsed."
    )
    parser.add_argument(
        "--output", "-o",
        help=("Destination of the result file path. If not set, the result "
                "will be exported to the current working directory, with filename "
                "'result.json'.")
    )
    args = parser.parse_args()
    results = json_parser(args.filepath, dest_path=args.output)
    print(f"Parsed successful! \nThe Results: ")
    pprint(results, sort_dicts=False)

if __name__ == "__main__":
    main()