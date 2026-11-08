#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Self-contained unit tests uploaded for this test repository.

The file has no third-party dependencies and is compatible with
Python 2.7 and Python 3.x. Run it directly:

    python test_demo.py -v
"""

import unittest


def add(left, right):
    """Return the sum of two numbers."""
    return left + right


def normalize_name(name):
    """Trim surrounding whitespace and fall back to ``anonymous``."""
    if not isinstance(name, str):
        return "anonymous"
    return name.strip() or "anonymous"


class DemoTest(unittest.TestCase):
    """Basic checks that exercise the helpers above."""

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_normalize_name_trims_whitespace(self):
        self.assertEqual(normalize_name("  Ada  "), "Ada")

    def test_normalize_name_blank_falls_back(self):
        self.assertEqual(normalize_name("   "), "anonymous")

    def test_normalize_name_non_string_falls_back(self):
        self.assertEqual(normalize_name(None), "anonymous")


if __name__ == "__main__":
    unittest.main()
