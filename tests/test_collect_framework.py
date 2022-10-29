import os
import sys
from unittest.mock import patch, MagicMock
import pytest
import collect_framework


class TestCountingUniqueCharacters:
    """test class for testing func: 'counting_unique_characters' """

    def test_counting_unique_characters(self):
        assert collect_framework.counting_unique_characters('abbbccdf') == 3
        assert collect_framework.counting_unique_characters('aabcdfee') == 4

    def test_counting_unique_characters_assertion(self):
        with pytest.raises(TypeError):
            collect_framework.counting_unique_characters(123)


def create_template_file(func):
    def inner(self):
        path_to_temp_file = 'tempText.txt'
        text_of_file_to_write = 'Hello, my name is Test'
        with open(path_to_temp_file, 'w') as file:
            file.write(text_of_file_to_write)
        func(self, file=path_to_temp_file, text=text_of_file_to_write)
        os.remove(path_to_temp_file)
    return inner


class TestParseCLI:
    """test class  for testing func: 'parse_file' """

    @create_template_file
    def test_function_for_parse_file(self, file, text):
        """function tests 'parse_file', any case which have"""
        assert collect_framework.parse_file(file) == text
        with pytest.raises(FileNotFoundError):
            collect_framework.parse_file('non_existentText.txt')

    @create_template_file
    @patch('collect_framework.argparse.ArgumentParser.parse_args')
    def test_parse_cli_function(self, mock_parse_args, file, text):
        """test function of 'parse_cli_function' """

        # first case
        mock_return_value = MagicMock(file=None, string=text)
        mock_parse_args.return_value = mock_return_value
        assert collect_framework.parse_cli_function() == text

        # second case
        mock_return_value = MagicMock(file=file, string=None)
        mock_parse_args.return_value = mock_return_value
        assert collect_framework.parse_cli_function() == text


class TestMain:

    @create_template_file
    @patch('collect_framework.parse_cli_function')
    def test_main_from_collect_framework(self, mock_parse_cli_function, file, text):
        mock_parse_cli_function.return_value = text  # text = 'Hello, my name is Test'
        original_stdout = sys.stdout  # saving original sys.stdout
        with open(file, 'w') as temp_file:
            sys.stdout = temp_file
            collect_framework.main()
            sys.stdout = original_stdout
        with open(file, 'r') as temp_file:
            assert temp_file.read() == 'Hello, my name is Test: 9\n'


