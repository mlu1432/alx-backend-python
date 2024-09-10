#!/usr/bin/env python3
"""
Integration tests for the GithubOrgClient class in the client.py module.
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for the GithubOrgClient class.

    These tests ensure the interaction between multiple methods in the class
    works as expected, including calls to
    external services like the GitHub API
    """

    @patch('client.get_json', side_effect=[
        {"repos_url": "https://api.github.com/orgs/google/repos"},
        TEST_PAYLOAD[0][1],  # Second API response (list of repos)
    ])
    def test_public_repos_integration(self, mock_get_json):
        """
        Test the public_repos method in an integration test scenario.

        Verifies that the public_repos method correctly retrieves and
        returns the list of repositories for the organization using
        mocked API responses.

        :param mock_get_json: The mock object that simulates API responses.
        :return: None
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
    def test_public_repos_with_license_integration(self, mock_get_json):
        """
        Test public_repos method with license
        filtering in an integration scenario

        This test checks whether the public_repos method returns repositories
        that match a given license using mocked API responses.

        :param mock_get_json: The mock object that simulates API responses.
        :return: None
        """
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        expected_repos = ['dagger', 'kratu', 'traceur-compiler', 'firmata.py']
        self.assertEqual(repos, expected_repos)
        self.assertEqual(mock_get_json.call_count, 2)


if __name__ == '__main__':
    unittest.main()
