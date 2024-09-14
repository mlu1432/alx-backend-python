#!/usr/bin/env python3
"""
Integration tests for the GithubOrgClient class in the client.py module.

These tests ensure that the org, _public_repos_url,
and public_repos methods behave as expected
using mocks to avoid making real HTTP requests.
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient class.

    Tests interaction between multiple methods in the class, ensuring
    proper behavior with external services like the GitHub API.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """Set up the patcher for requests.get."""
        cls.get_patcher = patch('requests.get', side_effect=cls.get_json_mock)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop the patcher for requests.get after tests complete."""
        cls.get_patcher.stop()

    @staticmethod
    def get_json_mock(url):
        """
        Mock for requests.get().json() to return different fixtures based on URL.
        """
        mock_response = Mock()
        if url == "https://api.github.com/orgs/google":
            mock_response.json.return_value = TEST_PAYLOAD[0][0]
        elif url == "https://api.github.com/orgs/google/repos":
            mock_response.json.return_value = TEST_PAYLOAD[0][1]
        return mock_response

    def test_public_repos(self):
        """
        Test public_repos method.

        Ensures that public_repos method returns the correct list
        of repositories using mocked API responses.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method with license filtering.

        Ensures that repositories with a specific license are returned correctly
        using mocked API responses.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
