#!/usr/bin/env python3

# Filename: airodump.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" Capture packets from a wireless network with an interface in monitor mode. """

import os
import argparse

from time import ctime
from monitor_mode import is_monitor_mode_enabled
from system_call import system_call
from wlan_interfaces import get_wlan_interfaces
from command_functions import build_airodump_command

__version__ = "0.0.1"
__author__ = "klaus-moser"
__date__ = ctime(os.path.getmtime(__file__))


def wifi_monitor(interface: str, channel: int = None, bssid: str = "", write: str = "") -> bool:

    if not interface in get_wlan_interfaces():
        return False

    if not is_monitor_mode_enabled(interface=interface):
        return False

    command = build_airodump_command(interface=interface, channel=channel, bssid=bssid, write=write)
    ret = system_call(command=command)

    if ret:
        return True
    else:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('interface', help="Interface to use.")  # positional argument
    parser.add_argument('-channel', '-c', type=int, choices=range(1 - 14), help="Channel to listen.")  # optional argument
    parser.add_argument('-bssid', '-s', type=str, help="SSID to listen.")  # optional argument
    parser.add_argument('-write', '-w', type=str, help="Path of file where to save captured packets.")  # optional argument
    args = parser.parse_args()

    # wifi_monitor(interface=args.interface, channel=args.channel, bssid=args.ssid, write=args.mode)
    wifi_monitor(interface=args.interface, channel=args.channel, bssid=args.bssid, write=args.write)
