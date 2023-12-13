#!/usr/bin/env python3

# Filename: wlan_interfaces.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" Get information about the Wi-Fi/wlan interfaces. """

import os
import netifaces

from time import ctime

__version__ = "0.0.1"
__author__ = "klaus-moser"
__date__ = ctime(os.path.getmtime(__file__))


def get_wlan_interfaces() -> list:
    """
    Return a list of any wlan interfaces available.

    :return: List of strings. (e.g. [interface1, interface2, ...]).
    """

    return netifaces.interfaces()  # retrieve all available network interfaces on the system


if __name__ == "__main__":
    print(get_wlan_interfaces())
