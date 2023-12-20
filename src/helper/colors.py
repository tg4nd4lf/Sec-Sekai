#!/usr/bin/env python3

# Filename: colors.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" Class for printing colors. """

import os

from time import ctime

__version__ = "1.0"
__author__ = "klaus-moser"
__date__ = ctime(os.path.getmtime(__file__))


#  os.system('color')  # that ANSI escape sequence start working


class Colors:
    """
    Class to define colors.
    """

    COLORS_DICT = {
        # basics
        'BLACK': '\033[30m',        # Black
        'GREY': '\033[37m',         # Grey
        'WHITE': '\033[97m',        # White
        'NORMAL': '\033[0m',        # White (normal)
        # light colors
        'LRED': '\033[91m',         # Light Red
        'LGREEN': '\033[92m',       # Light Green
        'LYELLOW': '\033[93m',      # Light Yellow
        'LBLUE': '\033[94m',        # Light Blue
        'LMAGENTA': '\033[95m',     # Light Magenta
        'LCYAN': '\033[96m',        # Light Cyan
        # normal colors
        'RED': '\033[31m',          # Red
        'GREEN': '\033[32m',        # Green
        'YELLOW': '\033[33m',       # Yellow
        'BLUE': '\033[34m',         # Blue
        'MAGENTA': '\033[35m',      # Magenta
        'CYAN': '\033[36m',         # Cyan
        # background
        'BG_RED': '\033[41m',       # Background Red
        'BG_GREEN': '\033[42m',     # Background Green
        'BG_RESET': '\033[49m',     # Background Reset
        # formatting
        'BOLD': '\033[1m',          # Bold
        'UNDERLINE': '\033[4m',     # Underline
        # end
        'ENDC': '\033[0m',          # Ends color or formatting options
        'RESET': '\033[39m'         # Set text color back to default
    }


if __name__ == "__main__":
    print("*** Color ANSI Codes Table ***")
    print(30 * "=")

    for name, code in Colors.COLORS_DICT.items():  # Print the table
        print(f"{code}{name.ljust(10)}: This is {name} {Colors.COLORS_DICT.get('ENDC')}")

    print(30 * "=")
