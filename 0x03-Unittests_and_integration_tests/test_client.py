#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class in the client.py module.

These tests ensure that the org method and _public_repos_url method behave
as expected, using mocks to avoid making real HTTP requests.
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class.
    """

    @patch('client.get_json', return_value={"login": "mocked_org"})
    def test_org(self, mock_get_json: unittest.mock.Mock) -> None:
        """
        Test that GithubOrgClient.org returns the correct
        value and get_json is called.

        :param mock_get_json: The mock object for get_json.
        """
        # Create an instance of GithubOrgClient with the organization name
        client = GithubOrgClient("google")

        # Access the org property
        result = client.org

        # Assert that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google")

        # Assert that the result matches the mock return value
        self.assertEqual(result, {"login": "mocked_org"})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org: unittest.mock.Mock) -> None:
        """
        Test that _public_repos_url returns the correct
        value based on the mocked org.

        :param mock_org: The mock object for the org property.
        """
        # Set up the mock org property to return a specific payload
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the _public_repos_url method
        result = client._public_repos_url

        # Assert that the result is the expected repos_url from the mocked org property
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()
