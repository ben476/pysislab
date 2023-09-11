"""
This type stub file was generated by pyright.
"""

from typing import Optional

__all__ = ["parse_url", "get_proxy_info"]
def parse_url(url: str) -> tuple:
    """
    parse url and the result is tuple of
    (hostname, port, resource path and the flag of secure mode)

    Parameters
    ----------
    url: str
        url string.
    """
    ...

DEFAULT_NO_PROXY_HOST = ...
def get_proxy_info(hostname: str, is_secure: bool, proxy_host: Optional[str] = ..., proxy_port: int = ..., proxy_auth: Optional[tuple] = ..., no_proxy: Optional[list] = ..., proxy_type: str = ...) -> tuple:
    """
    Try to retrieve proxy host and port from environment
    if not provided in options.
    Result is (proxy_host, proxy_port, proxy_auth).
    proxy_auth is tuple of username and password
    of proxy authentication information.

    Parameters
    ----------
    hostname: str
        Websocket server name.
    is_secure: bool
        Is the connection secure? (wss) looks for "https_proxy" in env
        instead of "http_proxy"
    proxy_host: str
        http proxy host name.
    proxy_port: str or int
        http proxy port.
    no_proxy: list
        Whitelisted host names that don't use the proxy.
    proxy_auth: tuple
        HTTP proxy auth information. Tuple of username and password. Default is None.
    proxy_type: str
        Specify the proxy protocol (http, socks4, socks4a, socks5, socks5h). Default is "http".
        Use socks4a or socks5h if you want to send DNS requests through the proxy.
    """
    ...
