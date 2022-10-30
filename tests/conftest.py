import pytest


@pytest.fixture
def tmp_file(tmp_path):
    text_of_test = 'Hello That file test'
    temp_directory = tmp_path / 'collect_framework'
    temp_directory.mkdir()
    temp_file = temp_directory / 'test_text.txt'
    temp_file.write_text(text_of_test)

    return temp_file, text_of_test
