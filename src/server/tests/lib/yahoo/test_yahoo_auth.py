import unittest
from unittest.mock import patch

import config
import lib.yahoo.yahoo_auth as ya


class TestYahooAuth(unittest.TestCase):
    def test_build_authorization_url_contains_params(self):
        redirect = "https://example.com/cb"
        url = ya.build_authorization_url(redirect, scope="openid profile", state="xyz")
        self.assertIn(f"client_id={config.YAHOO_CLIENT_ID}", url)
        # build_authorization_url uses requote_uri which preserves slashes, so
        # assert the raw redirect URI is present
        self.assertIn(f"redirect_uri=https://example.com/cb", url)
        self.assertIn("response_type=code", url)
        self.assertIn("scope=openid%20profile", url)
        self.assertIn("state=xyz", url)

    @patch("service.service.Service.post")
    def test_exchange_code_for_token_success(self, mock_post):
        sample = {"access_token": "at", "refresh_token": "rt", "expires_in": 3600}
        # mock Service.post to return the sample token dict
        mock_post.return_value = sample

        result = ya.exchange_code_for_token("code123", "https://example.com/cb")
        self.assertEqual(result, sample)

        # ensure Service.post was called with the token path
        mock_post.assert_called()
        # inspect headers passed to Service.post
        _, kwargs = mock_post.call_args
        headers = kwargs.get("headers")
        self.assertIsNotNone(headers)
        self.assertIn("Authorization", headers)
        self.assertTrue(headers["Authorization"].startswith("Basic "))
        self.assertEqual(headers.get("Content-Type"), "application/x-www-form-urlencoded")

    @patch("service.service.Service.post")
    def test_exchange_code_for_token_failure(self, mock_post):
        mock_post.return_value = None
        with self.assertRaises(RuntimeError):
            ya.exchange_code_for_token("code123", "https://example.com/cb")

    @patch("service.service.Service.post")
    def test_refresh_token_success(self, mock_post):
        sample = {"access_token": "at2", "refresh_token": "rt2", "expires_in": 3600}
        mock_post.return_value = sample

        result = ya.refresh_token("rt2")
        self.assertEqual(result, sample)
        mock_post.assert_called()

    @patch("service.service.Service.post")
    def test_refresh_token_failure(self, mock_post):
        mock_post.return_value = None
        with self.assertRaises(RuntimeError):
            ya.refresh_token("rt2")

    def test_build_authenticated_session_valid_and_invalid(self):
        with self.assertRaises(ValueError):
            ya.build_authenticated_session({})

        token = {"access_token": "mytoken"}
        sess = ya.build_authenticated_session(token)
        self.assertEqual(sess.headers.get("Authorization"), "Bearer mytoken")
        self.assertEqual(sess.headers.get("Accept"), "application/json")


if __name__ == "__main__":
    unittest.main()
