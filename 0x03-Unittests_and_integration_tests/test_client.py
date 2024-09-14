#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class in the client.py module.

These tests ensure that the org, _public_repos_url,
and public_repos methods behave as expected
using mocks to avoid making real HTTP requests.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class.

    This class contains tests for:
    - org: Test that the org method calls get_json correctly.
    - _public_repos_url: Test that the _public_repos_url method
    returns the correct URL.
    - public_repos: Test that the public_repos method returns
    the correct repository names.
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: unittest.mock.Mock) -> None:
        """
        Test that GithubOrgClient.public_repos returns the
        expected list of repositories and that the
        _public_repos_url and get_json methods are called correctly.

        :param mock_get_json: The mock object for get_json.
        """
        # Define a fake list of repos to be returned by get_json
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        # Mock _public_repos_url to return a custom URL
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value="https://api.github.com/orgs/google/repos") as mock_repos_url:

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")

            # Call the public_repos method
            repos = client.public_repos()

            # Assert the list of repos returned by public_repos matches the mock data
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            # Assert that _public_repos_url was called once
            mock_repos_url.assert_called_once()

            # Assert that get_json was called once with the correct URL
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),  # Case where license key is missing in the repo
    ])
    def test_has_license(self, repo: dict, license_key: str, expected: bool) -> None:
        """
        Test that GithubOrgClient.has_license returns the correct boolean value
        depending on the repository's license.

        :param repo: A dictionary representing the repository data.
        :param license_key: The license key to check in the repository.
        :param expected: The expected boolean result.
        """
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the has_license method and assert the result
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
