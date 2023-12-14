#!/usr/bin/env python3

# Filename: system-call.py

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""" Make system calls """

import os
import subprocess

from time import ctime


__version__ = "0.0.1"
__author__ = "klaus-moser"
__date__ = ctime(os.path.getmtime(__file__))


def system_call(command: str) -> bool:
    """
    Use this function for primary for 'sudo' commands.

    :param command: Command to execute.
    :return: 0: Success; -1: No success.
    """

    try:
        ret = os.system(command=command)
        if ret == -1:
            return False
        return True

    # TODO: finer exception
    except Exception as e:
        # TODO: log error + return code
        return False


def subprocess_call(command: str) -> tuple:
    """
    Make system calls and return the stdout.

    :param command: Command to execute.
    :return: Tuple: stdout, stderr, return code.
    """

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Retrieving output and error messages, if any
        stdout = result.stdout.decode('utf-8')  # Decode bytes to string
        stderr = result.stderr.decode('utf-8')  # Decode bytes to string
        return_code = result.returncode

        return stdout, stderr, return_code

    except subprocess.SubprocessError as e:  # Handle subprocess-related errors
        print(f"Subprocess error occurred: {e}")
        return None, None, -1  # Return an error indicator or handle as needed

    except FileNotFoundError as e:  # Handle file not found error (command not available on the system)
        print(f"Command not found: {e}")
        return None, None, -1  # Return an error indicator or handle as needed


if __name__ == "__main__":
    print(__file__)
