# coding=UTF-8
# Author: Dennis Lutter <lad1337@gmail.com>
# URL: https://sickchill.github.io
#
# This file is part of SickChill.
#
# SickChill is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SickChill is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SickChill. If not, see <http://www.gnu.org/licenses/>.

"""
Test exception logging
"""

# Stdlib Imports
import os.path
import sys
import unittest


def exception_generator():
    """
    Dummy function to raise a fake exception and log it
    """
    try:
        raise Exception('FAKE EXCEPTION')
    except Exception as error:
        logger.exception("FAKE ERROR: " + str(error))
        logger.submit_errors()
        raise


class IssueSubmitterBasicTests(unittest.TestCase):
    """
    Tests logging of exceptions
    """
    def test_submitter(self):
        """
        Test that an exception is raised
        """
        self.assertRaises(Exception, exception_generator)


if __name__ == "__main__":
    print("==================")
    print("STARTING - ISSUE SUBMITTER TESTS")
    print("==================")
    print("######################################################################")

    SUITE = unittest.TestLoader().loadTestsFromTestCase(IssueSubmitterBasicTests)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
