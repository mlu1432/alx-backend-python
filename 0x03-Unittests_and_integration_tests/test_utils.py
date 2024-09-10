#!/usr/bin/env python3
"""
Unit tests for utility functions in the utils.py module.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map function.

    The access_nested_map function retrieves values from a nested dictionary
    based on a sequence of keys.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: dict, path: tuple, expected: any
    ) -> None:
        """
        Test that access_nested_map returns the correct value for a given path

        :param nested_map: Dictionary containing nested elements.
        :param path: Tuple of keys representing the path to the nested value.
        :param expected: The expected value to be returned by access_nested_map
        :return: None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map: dict, path: tuple, exception: type
    ) -> None:
        """
        Test that access_nested_map raises KeyError for invalid paths.

        :param nested_map: Dictionary containing nested elements.
        :param path: Tuple of keys representing the path to the nested value.
        :param exception: expected exception to be raised by access_nested_map
        :return: None
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
