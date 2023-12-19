#!/usr/bin/env python3

# Filename: airmon.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" Activate the monitor mode. """

import os
import argparse

from re import search
from time import ctime
from system_call_functions import system_call, subprocess_call
from netifaces import interfaces

__version__ = "0.0.1"
__author__ = "klaus-moser"
__date__ = ctime(os.path.getmtime(__file__))


class Airmon:
    """
    Wrapper for the 'airmon-ng' program.
    """

    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def get_interfaces() -> list:
        """
        Return a list of any available network interfaces on the system.

        :return: List of strings. (e.g. [interface1, interface2, ...]).
        """

        return interfaces()

    @staticmethod
    def is_monitor_mode_enabled(interface: str) -> bool:
        """
        Check if monitor mode for given interface is already enabled.

        interface: Interface to check monitor mode.
        :return: True: Enabled; False: Disabled.
        """

        stdout, stderr, code = subprocess_call(command="iwconfig")

        ret = False
        if stdout and not code == -1:
            if "{}mon".format(interface) in stdout:  # TODO: interface + mon
                interface = interface + "mon"

            regex = "({})(.)+(Mode:Monitor)".format(interface)
            match = search(regex, stdout.replace("\n", ""))

            if match:
                return True
        return ret

    @classmethod
    def switch_monitor_mode(cls, interface: str) -> bool:
        """
        Activate monitor for the selected interface, if a wlan interface is available.

        :param interface: Interface to use the monitor mode.
        :return: True: Activated. False: Error.
        """

        interfaces = cls.get_interfaces()

        if not interfaces:  # empty list
            return False
        # TODO: interface + mon
        elif interface not in interfaces:  # interface not in list
            if interface + 'mon' in interfaces:  # interface + mon in list
                interface += 'mon'
            else:  # interface + mon not in list
                return False

        if cls.is_monitor_mode_enabled(interface=interface):
            command = "airmon-ng stop {} && service network-manager restart".format(interface)
        else:
            command = "airmon-ng start {} && airmon-ng check kill".format(interface)

        ret = system_call(command=command)

        if ret:
            return True
        else:
            return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('interface', help="Interface to use.")  # positional argument
    args = parser.parse_args()

    c = Airmon()
    c.switch_monitor_mode(args.interface)
