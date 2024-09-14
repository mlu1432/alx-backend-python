#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class in the client.py module.

These tests ensure that the org method correctly calls get_json and returns
the expected value without making actual HTTP requests.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"login": "mocked_org"})
    def test_org(self, org_name: str, mock_get_json: unittest.mock.Mock) -> None:
        """
        Test that GithubOrgClient.org returns the correct value and
        get_json is called.

        :param org_name: The name of the organization to test.
        :param mock_get_json: The mock object for get_json.
        """
        # Create an instance of GithubOrgClient with the organization name
        client = GithubOrgClient(org_name)

        # Access the org property (assuming org is a property)
        result = client.org

        # Assert that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Assert that the result matches the mock return value
        self.assertEqual(result, {"login": "mocked_org"})


if __name__ == "__main__":
    unittest.main()
