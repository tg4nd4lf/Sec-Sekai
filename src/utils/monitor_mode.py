#!/usr/bin/env python3

# Filename: monitor-mode.py

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

from time import ctime
from re import findall
from src.utils.system_call import system_call

__version__ = "0.0.1"
__author__ = "klaus-moser"
__date__ = ctime(os.path.getmtime(__file__))


def wlan_interfaces_available() -> list:
    """
    Return a list of any wlan interfaces available.

    :return: List of strings. (e.g. [interface1, interface2, ...]).
    """

    iwconfig = system_call("iwconfig")

    if iwconfig != "":
        interfaces = findall("wlan[0-9]", iwconfig)
    else:
        interfaces = list()

    return interfaces


def monitor_mode(interface: str) -> bool:
    """
    Activate monitor for the selected interface, if a wlan interface is available.

    :param interface: Interface to use the monitor mode.
    :return: True: Activated. False: Error.
    """

    interfaces = wlan_interfaces_available()

    if not interfaces:
        return False

    if interface not in interfaces:
        return False

    ret = system_call("sudo airmon-ng start {}".format(interface))
    ret = system_call("sudo airmon-ng stop {}".format(interface))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('interface', help="Interface to use.")  # positional argument
    args = parser.parse_args()

    monitor_mode(interface=args.interface)
