import pytest
from unittest.mock import patch
from src.utils.airmon import Airmon


class TestAirmon:
    """
    Class for all tests of 'airmon.py'.
    """

    @pytest.mark.parametrize("test_input, expected", [
        (["", "ERROR", -1], None),
        (["wlan0  IEEE 802.11  Mode:Managed", "", 0], None),
        (["wlan0  IEEE 802.11  Mode:Monitor", "", 0], "wlan0"),
        (["wlan0mon  IEEE 802.11  Mode:Monitor", "", 0], "wlan0mon")
    ])
    def test_get_monitor_interface_name(self, test_input, expected) -> None:
        """
        Test the function while mocking the real subprocess_call().
        """

        # arrange
        with patch('src.utils.airmon.subprocess_call') as mock_subprocess_call:
            # arrange
            mock_subprocess_call.return_value = (test_input[0], test_input[1], test_input[2])
            # act
            result = Airmon.get_monitor_interface_name()
            # assert
            mock_subprocess_call.assert_called_once_with(command="iwconfig")
            assert result == expected
