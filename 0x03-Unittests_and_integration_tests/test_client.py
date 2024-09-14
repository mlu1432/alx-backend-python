#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class in the client.py module.

These tests ensure that the org, _public_repos_url,
and public_repos methods behave as expected
using mocks to avoid making real HTTP requests.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class([
    {"org_payload": TEST_PAYLOAD[0][0], "repos_payload": TEST_PAYLOAD[0][1],
     "expected_repos": TEST_PAYLOAD[0][2], "apache2_repos": TEST_PAYLOAD[0][3]},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for the GithubOrgClient class.
    These tests ensure the public_repos method works with fixtures.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the mock for requests.get to return the appropriate fixture data
        """
        cls.get_patcher = patch('requests.get', side_effect=cls.mocked_requests_get)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Stop the patcher for requests.get.
        """
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """
        A static method to mock requests.get() behavior based on the URL.
        It will return mock response objects with JSON data.
        """
        class MockResponse:
            def __init__(self, json_data):
                self._json_data = json_data

            def json(self):
                return self._json_data

        if url == "https://api.github.com/orgs/google":
            return MockResponse(TEST_PAYLOAD[0][0])
        elif url == "https://api.github.com/orgs/google/repos":
            return MockResponse(TEST_PAYLOAD[0][1])
        return MockResponse(None)

    def test_public_repos(self):
        """
        Test GithubOrgClient.public_repos to ensure it returns
        the expected repository names.
        """
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test the public_repos method when filtering by
        license (e.g., "apache-2.0").
        """
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
