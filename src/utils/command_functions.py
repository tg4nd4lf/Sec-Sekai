#!/usr/bin/env python3

# Filename: command_functions.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" Holds all functions for building commands. """


import os

from time import ctime
from re import search

__version__ = "0.0.1"
__author__ = "klaus-moser"
__date__ = ctime(os.path.getmtime(__file__))


def regex_for_bssid(bssid: str) -> str:
    """
    Search the first match of a bssid in a string.

    :param bssid: String that could hold a bssid.
    :return: Match: (True, bssid); No match (False, None)
    """

    bssid_pattern = "(([0-9]){2}:){5}([0-9]){2}"

    if bssid:
        ret = search(pattern=bssid_pattern, string=bssid)
        if ret:
            return ret.group()
    else:
        return None


def build_airodump_command(interface: str, channel: int = None, bssid: str = "", write: str = "") -> str:
    """
    Build the desired airodump command.

    :param interface: Interface to use.
    :param channel: Channel to use.
    :param bssid: BSSID to use.
    :param write: Defines the path where to save the captured packets.
    :return: Command (e.g. airodump-ng wlan0mon -c 1 -bssid 42:42:42:42:42:42 -w file).
    """

    command = "airodump-ng {}".format(interface)
    path = write

    if channel and (0 < channel <= 14):
        command += " -c {}".format(channel)

    bssid = regex_for_bssid(bssid=bssid)

    if bssid:
        command += " -bssid {}".format(bssid)

    if path:
        if os.path.isdir(path):
            folder = os.path.basename(path)
            if os.path.exists(folder):
                command += " -w {}.".format(path)
        elif os.path.isfile(path):
            command += " -w {}.".format(path)

    return command


if __name__ == "__main__":
    print(__file__)
