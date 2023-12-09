#!/usr/bin/env python3

# Filename: logo.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" For printing nice logos. """


import os

__version__ = "placeholder"
__author__ = "placeholder"
__date__ = "placeholder"


def print_logo(logo_path: str) -> None:
    """
    Print logo from a "logo.txt" file.

    :return:
    """

    if logo_path == "":
        print("(empty?)")

    elif not os.path.exists(logo_path):
        print("(logo?)")

    elif not logo_path.endswith("txt"):
        print("(.txt?)")

    else:
        try:
            with open(file="logo.txt") as l:
                logo = l.readlines()
            for line in logo:
                print(line, end="")
            print("\nVersion:\t" + __version__ + "\nAuthor(s):\t" + __author__ + "\nLast Mod.:\t" + __date__ + "\n")

        except Exception as e:
            print(e)
