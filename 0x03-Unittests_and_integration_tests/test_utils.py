#!/usr/bin/env python3
"""
Unit tests for utility functions in the utils.py module.

This file contains tests for:
- access_nested_map: A function that retrieves a value from a nested dictionary
- get_json: A function that retrieves a JSON response from a URL.
- memoize: A decorator that caches the result of a method call.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map function.

    The access_nested_map function retrieves values from a nested dictionary
    based on a sequence of keys.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple, expected: any) -> None:
        """
        Test that access_nested_map returns the correct value for a given path

        :param nested_map: Dictionary containing nested elements.
        :param path: Tuple of keys representing the path to the nested value.
        :param expected: The expected value to be returned by access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple, exception: type) -> None:
        """
        Test that access_nested_map raises KeyError for invalid paths.

        :param nested_map: Dictionary containing nested elements.
        :param path: Tuple of keys representing the path to the nested value.
        :param exception: Expected exception to be raised by access_nested_map
        """
        with self.assertRaises(exception) as context:
            access_nested_map(nested_map, path)

        # Assert the exception message contains the key inside quotes
        expected_message = repr(path[-1])
        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the get_json function in the utils.py module.

    The get_json function retrieves JSON data from a given URL.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: dict, mock_get: Mock) -> None:
        """
        Test that get_json returns the correct payload from mocked GET request

        :param test_url: The URL to fetch the JSON from.
        :param test_payload: The expected payload to be returned by get_json.
        :param mock_get: The mock object for requests.get.
        """
        # Configure the mock to return the test_payload
        mock_get.return_value.json.return_value = test_payload

        # Call the function being tested
        result = get_json(test_url)

        # Ensure the get request was called once with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Ensure the returned result is the expected payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the memoize decorator in the utils.py module.

    The memoize decorator caches the result of a method call so that
    subsequent calls return the cached result.
    """

    class TestClass:
        """Class for testing memoize decorator."""

        def a_method(self) -> int:
            """Return a constant value."""
            return 42

        @memoize
        def a_property(self) -> int:
            """Memoized property that calls a_method."""
            return self.a_method()

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_method: Mock) -> None:
        """
        Test that a_method is called only once when accessing
        the memoized property twice.

        :param mock_method: The mock object for TestClass.a_method.
        """
        test_instance = self.TestClass()

        # Call the memoized property twice
        first_call = test_instance.a_property
        second_call = test_instance.a_property

        # Assert that the memoized property returns the correct value
        self.assertEqual(first_call, 42)
        self.assertEqual(second_call, 42)

        # Assert that a_method was only called once
        mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
