import typing as t
from ..datastructures import Accept as Accept, Authorization as Authorization, CharsetAccept as CharsetAccept, ETags as ETags, HeaderSet as HeaderSet, Headers as Headers, IfRange as IfRange, ImmutableList as ImmutableList, ImmutableMultiDict as ImmutableMultiDict, LanguageAccept as LanguageAccept, MIMEAccept as MIMEAccept, MultiDict as MultiDict, Range as Range, RequestCacheControl as RequestCacheControl
from ..http import parse_accept_header as parse_accept_header, parse_authorization_header as parse_authorization_header, parse_cache_control_header as parse_cache_control_header, parse_cookie as parse_cookie, parse_date as parse_date, parse_etags as parse_etags, parse_if_range_header as parse_if_range_header, parse_list_header as parse_list_header, parse_options_header as parse_options_header, parse_range_header as parse_range_header, parse_set_header as parse_set_header
from ..urls import url_decode as url_decode
from ..user_agent import UserAgent as UserAgent
from ..utils import cached_property as cached_property, header_property as header_property
from .utils import get_current_url as get_current_url, get_host as get_host
from datetime import datetime
from typing import Any

class Request:
    charset: str = ...
    encoding_errors: str = ...
    parameter_storage_class: t.Type[MultiDict] = ...
    dict_storage_class: t.Type[MultiDict] = ...
    list_storage_class: t.Type[t.List] = ...
    user_agent_class: Any = ...
    trusted_hosts: t.Optional[t.List[str]] = ...
    method: Any = ...
    scheme: Any = ...
    server: Any = ...
    root_path: Any = ...
    path: Any = ...
    query_string: Any = ...
    headers: Any = ...
    remote_addr: Any = ...
    def __init__(self, method: str, scheme: str, server: t.Optional[t.Tuple[str, t.Optional[int]]], root_path: str, path: str, query_string: bytes, headers: Headers, remote_addr: t.Optional[str]) -> None: ...
    @property
    def url_charset(self) -> str: ...
    def args(self) -> MultiDict[str, str]: ...
    def access_route(self) -> t.List[str]: ...
    def full_path(self) -> str: ...
    @property
    def is_secure(self) -> bool: ...
    def url(self) -> str: ...
    def base_url(self) -> str: ...
    def root_url(self) -> str: ...
    def host_url(self) -> str: ...
    def host(self) -> str: ...
    def cookies(self) -> ImmutableMultiDict[str, str]: ...
    content_type: Any = ...
    def content_length(self) -> t.Optional[int]: ...
    content_encoding: Any = ...
    content_md5: Any = ...
    referrer: Any = ...
    date: Any = ...
    max_forwards: Any = ...
    @property
    def mimetype(self) -> str: ...
    @property
    def mimetype_params(self) -> t.Dict[str, str]: ...
    def pragma(self) -> HeaderSet: ...
    def accept_mimetypes(self) -> MIMEAccept: ...
    def accept_charsets(self) -> CharsetAccept: ...
    def accept_encodings(self) -> Accept: ...
    def accept_languages(self) -> LanguageAccept: ...
    def cache_control(self) -> RequestCacheControl: ...
    def if_match(self) -> ETags: ...
    def if_none_match(self) -> ETags: ...
    def if_modified_since(self) -> t.Optional[datetime]: ...
    def if_unmodified_since(self) -> t.Optional[datetime]: ...
    def if_range(self) -> IfRange: ...
    def range(self) -> t.Optional[Range]: ...
    def user_agent(self) -> UserAgent: ...
    def authorization(self) -> t.Optional[Authorization]: ...
    origin: Any = ...
    access_control_request_headers: Any = ...
    access_control_request_method: Any = ...
    @property
    def is_json(self) -> bool: ...