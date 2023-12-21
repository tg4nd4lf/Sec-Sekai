import pytest
from src.helper.logo import print_logo


class TestLogo:
    """
    Class for all tests of 'logo.py'.
    """

    @pytest.mark.parametrize("test_input,expected",
                             [("", "(empty?)\n"), ("loggo.txt", "(logo?)\n"), ("../test_files/logo.png", "(.txt?)\n")])
    def test_print_logo(self, test_input, expected, capsys) -> None:
        """
        Method: def print_logo(logo_path: str) -> None

        :param test_input: Input.
        :param expected: Expected result.
        :param capsys: Built-in pytest fixture that captures the output to stdout and stderr.
        :return:
        """

        # act
        print_logo(logo_path=test_input)
        captured = capsys.readouterr()  # method of the capsys fixture to capture the outputs

        # assert
        assert captured.out == expected  # check 'out'
