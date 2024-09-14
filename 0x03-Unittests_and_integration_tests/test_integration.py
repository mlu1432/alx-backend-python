#!/usr/bin/env python3
"""
Integration tests for the GithubOrgClient class in the client.py module.

These tests ensure that the methods in GithubOrgClient interact correctly
with external services (mocked for testing).
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for the GithubOrgClient class.
    """

    @patch('client.get_json', side_effect=[
        {"repos_url": "https://api.github.com/orgs/google/repos"},
        TEST_PAYLOAD[0][1],  # Second API response (list of repos)
    ])
    def test_public_repos_integration(self, mock_get_json) -> None:
        """
        Test the public_repos method in an integration test scenario.

        Verifies that the public_repos method correctly retrieves and returns
        the list of repositories for the organization
        using mocked API responses.

        :param mock_get_json: The mock object that simulates API responses.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos()
        expected_repos = [
            'episodes.dart', 'cpp-netlib', 'dagger', 'ios-webkit-debug-proxy',
            'google.github.io', 'kratu', 'build-debian-cloud',
            'traceur-compiler', 'firmata.py'
        ]
        self.assertEqual(repos, expected_repos)
        self.assertEqual(mock_get_json.call_count, 2)

    @patch('client.get_json', side_effect=[
        {"repos_url": "https://api.github.com/orgs/google/repos"},
        TEST_PAYLOAD[0][1]
    ])
    def test_public_repos_with_license_integration(self, mock_get_json) -> None:
        """
        Test public_repos method with license filtering
        in an integration scenario.

        This test checks whether the public_repos method returns repositories
        that match a given license using mocked API responses.

        :param mock_get_json: The mock object that simulates API responses.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        expected_repos = ['dagger', 'kratu', 'traceur-compiler', 'firmata.py']
        self.assertEqual(repos, expected_repos)
        self.assertEqual(mock_get_json.call_count, 2)


if __name__ == "__main__":
    unittest.main()
