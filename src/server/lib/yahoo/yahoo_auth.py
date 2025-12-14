"""Yahoo Fantasy API OAuth helpers

This module provides convenience functions to construct an authorization URL,
exchange an authorization code for tokens, and refresh tokens using Yahoo's
OAuth2 endpoints.

It expects `YAHOO_CLIENT_ID` and `YAHOO_CLIENT_SECRET` to be available in
`src/server/config.py` (loaded from environment variables).
"""
from __future__ import annotations

import base64
from typing import Dict, Optional

from service.service import Service
import requests
import config

# Yahoo OAuth endpoints
YAHOO_AUTH_BASE = "https://api.login.yahoo.com/oauth2/request_auth"
YAHOO_TOKEN_PATH = "/oauth2/get_token"
YAHOO_BASE = "https://api.login.yahoo.com"


def build_authorization_url(redirect_uri: str, scope: Optional[str] = None, state: Optional[str] = None) -> str:
    """Builds an authorization URL for the Yahoo OAuth2 authorization code flow.

    Args:
        redirect_uri: The callback URL registered with the Yahoo app.
        scope: Optional space-separated scope string.
        state: Optional state string to protect against CSRF.

    Returns:
        A fully-formed URL where the user should be redirected to authorize access.
    """
    params = {
        "client_id": config.YAHOO_CLIENT_ID,
        "redirect_uri": redirect_uri,
        "response_type": "code",
    }
    if scope:
        params["scope"] = scope
    if state:
        params["state"] = state

    # Construct query string manually to avoid adding additional dependencies
    qs = "&".join(f"{k}={requests.utils.requote_uri(str(v))}" for k, v in params.items() if v is not None)
    return f"{YAHOO_AUTH_BASE}?{qs}"


def _basic_auth_header(client_id: str, client_secret: str) -> Dict[str, str]:
    key = f"{client_id}:{client_secret}".encode("utf-8")
    b64 = base64.b64encode(key).decode("utf-8")
    return {"Authorization": f"Basic {b64}", "Content-Type": "application/x-www-form-urlencoded"}


def exchange_code_for_token(code: str, redirect_uri: str) -> Dict[str, object]:
    """Exchange an authorization code for an access token + refresh token.

    Args:
        code: The authorization code returned by Yahoo after user consent.
        redirect_uri: The redirect URI used in the authorization request.

    Returns:
        A token dict as returned by Yahoo (access_token, refresh_token, expires_in, etc.).

    Raises:
        RuntimeError: when the token endpoint returns a non-200 response.
    """
    client_id = config.YAHOO_CLIENT_ID
    client_secret = config.YAHOO_CLIENT_SECRET
    headers = _basic_auth_header(client_id, client_secret)

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
    }

    svc = Service(YAHOO_BASE)
    result = svc.post(YAHOO_TOKEN_PATH, data=data, headers=headers)
    if not result:
        raise RuntimeError("Yahoo token exchange failed: no response or non-200 status")
    return result


def refresh_token(refresh_token: str) -> Dict[str, object]:
    """Refresh an access token using a refresh token.

    Args:
        refresh_token: The refresh token previously issued by Yahoo.

    Returns:
        A token dict as returned by Yahoo.

    Raises:
        RuntimeError: when the token endpoint returns a non-200 response.
    """
    client_id = config.YAHOO_CLIENT_ID
    client_secret = config.YAHOO_CLIENT_SECRET
    headers = _basic_auth_header(client_id, client_secret)

    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }

    svc = Service(YAHOO_BASE)
    result = svc.post(YAHOO_TOKEN_PATH, data=data, headers=headers)
    if not result:
        raise RuntimeError("Yahoo refresh token failed: no response or non-200 status")
    return result


def build_authenticated_session(token: Dict[str, object]) -> requests.Session:
    """Return a `requests.Session` already configured with an OAuth2 bearer token.

    Args:
        token: Token dict containing at least `access_token`.

    Returns:
        requests.Session instance with `Authorization` header set.
    """
    s = requests.Session()
    access_token = token.get("access_token")
    if not access_token:
        raise ValueError("token dict must contain access_token")
    s.headers.update({"Authorization": f"Bearer {access_token}"})
    s.headers.update({"Accept": "application/json"})
    return s