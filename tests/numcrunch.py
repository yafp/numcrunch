#!/usr/bin/python
"""numcrunch - a simle number cruncher"""

import unittest
import numcrunch

class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_fact(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """


if __name__ == '__main__':
    unittest.main()
