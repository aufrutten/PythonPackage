from collections import Counter
from functools import lru_cache
import argparse
import os


def parse_file(file: str) -> str:
    """function for parse files, checks if path exists and that is file"""
    if os.path.isfile(file):
        with open(file, 'r') as file:
            return file.read()
    else:
        raise FileNotFoundError("file doesn't exist or that is folder")


def parse_cli_function() -> str:
    """
    function for parse our command line
    function have three priority of return, that is: 1) file 2) text 3) nothing
    function return text
    """
    parser_cli = argparse.ArgumentParser(description="Counter of unique characters")
    parser_cli.add_argument("--file",
                            type=str,
                            help="file for counting")  # add --file argument

    parser_cli.add_argument("--string",
                            type=str,
                            help="string for counting")  # add --sting argument

    cli_args = parser_cli.parse_args()  # getting all arguments in CLI
    if cli_args.file is not None:
        return parse_file(file=cli_args.file)

    elif cli_args.string is not None:
        return cli_args.string


@lru_cache(maxsize=None)
def counting_unique_characters(text: str) -> int:
    """function for counting unique characters"""
    if not isinstance(text, str):  # if text not str, raise exception
        raise TypeError('you wrote wrong type argument')
    counter = Counter(text)
    return len([num for num in counter.values() if num == 1])


def main():
    argument_of_cli = parse_cli_function()
    counter = counting_unique_characters(argument_of_cli)
    response = f'{argument_of_cli}: {counter}'
    print(response)


if __name__ == '__main__':
    main()  # pragma: no cover
