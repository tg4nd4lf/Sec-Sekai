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

from re import search
from time import ctime
from system_call import system_call, subprocess_call


__version__ = "0.0.1"
__author__ = "klaus-moser"
__date__ = ctime(os.path.getmtime(__file__))


def get_wlan_interfaces() -> list:
    """
    Return a list of any wlan interfaces available.

    :return: List of strings. (e.g. [interface1, interface2, ...]).
    """

    return netifaces.interfaces()  # retrieve all available network interfaces on the system


def is_monitor_mode_enabled(interface: str) -> bool:
    """
    Check if monitor mode for given interface is already enabled.

    interface: Interface to check monitor mode.
    :return:
    """

    stdout, stderr, code = subprocess_call(command="iwconfig")

    ret = False
    if stdout and not code == -1:
        if "{}mon".format(interface) in stdout:
            interface = interface + "mon"
        regex = "({})(.)+(Mode:Monitor)".format(interface)
        match = search(regex, stdout)

        if match:
            return True
    return ret


def switch_monitor_mode(interface: str, mode: str = None) -> bool:
    """
    Activate monitor for the selected interface, if a wlan interface is available.

    :param interface: Interface to use the monitor mode.
    :param mode: Mode: start or stop the monitor mode.
    :return: True: Activated. False: Error.
    """

    interfaces = get_wlan_interfaces()

    if not interfaces or interface not in interfaces:
        return False

    # TODO: airmon kill etc.
    if not mode:
        if is_monitor_mode_enabled(interface=interface):
            mode = "stop"
        else:
            mode = "start"

    ret = system_call("airmon-ng {} {}".format(mode, interface))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('interface', help="Interface to use.")  # positional argument
    parser.add_argument('mode', choices=['start', 'stop'], help="Mode to use.")  # positional argument
    args = parser.parse_args()

    switch_monitor_mode(interface=args.interface, mode=args.mode)
