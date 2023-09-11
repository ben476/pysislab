"""
This type stub file was generated by pyright.
"""

from ._exceptions import *
from ._http import *
from ._logging import *
from ._socket import *

"""
_handshake.py
websocket - WebSocket client library for Python

Copyright 2023 engn33r

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
__all__ = ["handshake_response", "handshake", "SUPPORTED_REDIRECT_STATUSES"]
VERSION = ...
SUPPORTED_REDIRECT_STATUSES = ...
SUCCESS_STATUSES = ...
CookieJar = ...
class handshake_response:
    def __init__(self, status: int, headers: dict, subprotocol) -> None:
        ...
    


def handshake(sock, url: str, hostname: str, port: int, resource: str, **options): # -> handshake_response:
    ...

_HEADERS_TO_CHECK = ...
