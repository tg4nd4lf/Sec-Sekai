import pytest
from src.helper.logo import print_logo


class TestLogo:
    """
    Class for all tests of 'logo.py'.
    """

    @pytest.mark.parametrize("test_input,expected",
                             [("", "(empty?)\n"), ("loggo.txt", "(logo?)\n"), ("../data/logo.png", "(.txt?)\n")])
    def test_print_logo(self, test_input, expected, capsys) -> None:
        """
        Test for print logo.
        """

        # act
        print_logo(logo_path=test_input)
        captured = capsys.readouterr()  # method of the capsys fixture to capture the outputs

        # assert
        assert captured.out == expected  # check 'out'
