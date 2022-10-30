from unittest.mock import patch, MagicMock
import pytest
import collect_framework


class TestCountingUniqueCharacters:
    """test class for testing func: 'counting_unique_characters' """

    def test_counting_unique_characters(self):
        assert collect_framework.counting_unique_characters('abbbccdf') == 3
        assert collect_framework.counting_unique_characters('aabcdfee') == 4
        assert collect_framework.counting_unique_characters('Hello That file test') == 8

    def test_counting_unique_characters_assertion(self):
        with pytest.raises(TypeError):
            collect_framework.counting_unique_characters(123)


class TestParseCLI:
    """test class  for testing func: 'parse_file' """

    def test_function_for_parse_file(self, tmp_file):
        """function tests 'parse_file', any case which have"""
        file, text = tmp_file
        assert collect_framework.parse_file(file) == text
        with pytest.raises(FileNotFoundError):
            collect_framework.parse_file('non_existentText.txt')

    @patch('collect_framework.argparse.ArgumentParser.parse_args')
    def test_parse_cli_function(self, mock_parse_args, tmp_file):
        """test function of 'parse_cli_function' """
        file, text = tmp_file

        # first case
        mock_return_value = MagicMock(file=None, string='another string')
        mock_parse_args.return_value = mock_return_value
        assert collect_framework.parse_cli_function() == 'another string'

        # second case
        mock_return_value = MagicMock(file=file, string=None)
        mock_parse_args.return_value = mock_return_value
        assert collect_framework.parse_cli_function() == text

        # third case
        mock_return_value = MagicMock(file=file, string='another string')
        mock_parse_args.return_value = mock_return_value
        assert collect_framework.parse_cli_function() == text


class TestMain:

    @patch('collect_framework.parse_cli_function')
    def test_main_from_collect_framework(self, mock_parse_cli_function, capsys):
        mock_parse_cli_function.return_value = 'Hello, my name in Test'
        collect_framework.main()
        out, err = capsys.readouterr()
        assert out == 'Hello, my name in Test: 9\n'
