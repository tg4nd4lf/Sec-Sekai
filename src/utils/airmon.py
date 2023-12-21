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
from src.utils.system_call_functions import system_call, subprocess_call
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
    def get_monitor_interface_name() -> str:
        """
        Check if monitor mode for given interface is already enabled.
        If no interface is given the method tries to find if any interface has
        the monitor mode enabled and returns the name.

        interface: Interface to check monitor mode. None: check if any other NIC has.
        :return: interface_name or None.
        """

        stdout, stderr, code = subprocess_call(command="iwconfig")

        if not stdout and code == -1:  # error
            return None

        regex = "(.)+(Mode:Monitor)"  # is any NIC in monitor mode
        match = search(regex, stdout.replace("\n", ""))

        if match:  # monitor mode enabled
            interface_local = match.group().split()[0]

            return interface_local

        else:  # no monitor mode found
            return None

    @staticmethod
    def is_monitor_mode_enabled(interface: str) -> bool:
        """
        Check if monitor mode for given interface is already enabled.
        ATTENTION: This function checks both possibilities:

         1. <interface-name>
         2. <interface-name>mon

        interface: Interface to check monitor mode.
        :return: True: enabled. False: disabled.
        """

        stdout, stderr, code = subprocess_call(command="iwconfig")

        if not stdout and code == -1:  # error
            return False

        regex = "(.)+(Mode:Monitor)"  # is any NIC in monitor mode
        match = search(regex, stdout.replace("\n", ""))

        if match:  # monitor mode enabled
            interface_local = match.group().split()[0]

            if interface == interface_local or interface + "mon" == interface_local:
                return True
            else:
                return False

        else:  # no monitor mode found
            return False

    @classmethod
    def switch_monitor_mode(cls, interface: str) -> bool:
        """
        Activate monitor for the selected interface, if a wlan interface is available.

        :param interface: Interface to use the monitor mode.
        :return: True: Activated. False: Error.
        """

        interfaces_local = cls.get_interfaces()

        if not interfaces_local:  # no interfaces available at all
            return False

        if cls.is_monitor_mode_enabled(interface=interface):  # monitor mode enabled
            monitor_interface_name = cls.get_monitor_interface_name()

            if interface in monitor_interface_name and not interface == monitor_interface_name:  # take the right name
                interface = monitor_interface_name  # e.g. wlan0mon instead of wlan0

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
