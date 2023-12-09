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
import netifaces

from time import ctime
from re import findall
from src.utils.system_call import system_call

__version__ = "0.0.1"
__author__ = "klaus-moser"
__date__ = ctime(os.path.getmtime(__file__))


def get_wlan_interfaces() -> list:
    """
    Return a list of any wlan interfaces available.

    :return: List of strings. (e.g. [interface1, interface2, ...]).
    """

    wifi_interfaces = list()
    interfaces = netifaces.interfaces()  # retrieve all available network interfaces on the system

    for iface in interfaces:
        iface_details = netifaces.ifaddresses(iface)  # details (IP-Address, etc.) for interface

        if netifaces.AF_INET in iface_details and netifaces.AF_INET6 in iface_details:  # check if IPv4 and IPv6 are there
            if netifaces.AF_INET in iface_details[netifaces.AF_INET][0] and 'wireless' in iface_details[netifaces.AF_INET][0]:  # check if interface is Wi-Fi
                wifi_interfaces.append(iface)

    return wifi_interfaces


def monitor_mode(interface: str) -> bool:
    """
    Activate monitor for the selected interface, if a wlan interface is available.

    :param interface: Interface to use the monitor mode.
    :return: True: Activated. False: Error.
    """

    interfaces = get_wlan_interfaces()

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
