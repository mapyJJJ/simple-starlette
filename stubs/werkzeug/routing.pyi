import typing as t
import typing_extensions as te
import typing
import uuid
from .datastructures import ImmutableDict as ImmutableDict, MultiDict as MultiDict
from .exceptions import BadHost as BadHost, BadRequest as BadRequest, HTTPException as HTTPException, MethodNotAllowed as MethodNotAllowed, NotFound as NotFound
from .urls import url_encode as url_encode, url_join as url_join, url_quote as url_quote, url_unquote as url_unquote
from .utils import cached_property as cached_property, redirect as redirect
from .wrappers.response import Response as Response
from .wsgi import get_host as get_host
from _typeshed.wsgi import WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment
from typing import Any

def parse_converter_args(argstr: str) -> t.Tuple[t.Tuple, t.Dict[str, t.Any]]: ...
def parse_rule(rule: str) -> t.Iterator[t.Tuple[t.Optional[str], t.Optional[str], str]]: ...

class RoutingException(Exception): ...

class RequestRedirect(HTTPException, RoutingException):
    code: int = ...
    new_url: Any = ...
    def __init__(self, new_url: str) -> None: ...
    def get_response(self, environ: t.Optional[WSGIEnvironment]=..., scope: t.Optional[dict]=...) -> Response: ...

class RequestPath(RoutingException):
    path_info: Any = ...
    def __init__(self, path_info: str) -> None: ...

class RequestAliasRedirect(RoutingException):
    matched_values: Any = ...
    def __init__(self, matched_values: t.Mapping[str, t.Any]) -> None: ...

class BuildError(RoutingException, LookupError):
    endpoint: Any = ...
    values: Any = ...
    method: Any = ...
    adapter: Any = ...
    def __init__(self, endpoint: str, values: t.Mapping[str, t.Any], method: t.Optional[str], adapter: t.Optional[MapAdapter]=...) -> None: ...
    def suggested(self) -> t.Optional[Rule]: ...
    def closest_rule(self, adapter: t.Optional[MapAdapter]) -> t.Optional[Rule]: ...

class WebsocketMismatch(BadRequest): ...
class ValidationError(ValueError): ...

class RuleFactory:
    def get_rules(self, map: Map) -> t.Iterable[Rule]: ...

class Subdomain(RuleFactory):
    subdomain: Any = ...
    rules: Any = ...
    def __init__(self, subdomain: str, rules: t.Iterable[RuleFactory]) -> None: ...
    def get_rules(self, map: Map) -> t.Iterator[Rule]: ...

class Submount(RuleFactory):
    path: Any = ...
    rules: Any = ...
    def __init__(self, path: str, rules: t.Iterable[RuleFactory]) -> None: ...
    def get_rules(self, map: Map) -> t.Iterator[Rule]: ...

class EndpointPrefix(RuleFactory):
    prefix: Any = ...
    rules: Any = ...
    def __init__(self, prefix: str, rules: t.Iterable[RuleFactory]) -> None: ...
    def get_rules(self, map: Map) -> t.Iterator[Rule]: ...

class RuleTemplate:
    rules: Any = ...
    def __init__(self, rules: t.Iterable[Rule]) -> None: ...
    def __call__(self, *args: t.Any, **kwargs: t.Any) -> RuleTemplateFactory: ...

class RuleTemplateFactory(RuleFactory):
    rules: Any = ...
    context: Any = ...
    def __init__(self, rules: t.Iterable[RuleFactory], context: t.Dict[str, t.Any]) -> None: ...
    def get_rules(self, map: Map) -> t.Iterator[Rule]: ...

class Rule(RuleFactory):
    rule: Any = ...
    is_leaf: Any = ...
    map: Any = ...
    strict_slashes: Any = ...
    merge_slashes: Any = ...
    subdomain: Any = ...
    host: Any = ...
    defaults: Any = ...
    build_only: Any = ...
    alias: Any = ...
    websocket: Any = ...
    methods: Any = ...
    endpoint: Any = ...
    redirect_to: Any = ...
    arguments: Any = ...
    def __init__(self, string: str, defaults: t.Optional[t.Mapping[str, t.Any]]=..., subdomain: t.Optional[str]=..., methods: t.Optional[t.Iterable[str]]=..., build_only: bool=..., endpoint: t.Optional[str]=..., strict_slashes: t.Optional[bool]=..., merge_slashes: t.Optional[bool]=..., redirect_to: t.Optional[t.Union[str, t.Callable[..., str]]]=..., alias: bool=..., host: t.Optional[str]=..., websocket: bool=...) -> None: ...
    def empty(self) -> Rule: ...
    def get_empty_kwargs(self) -> t.Mapping[str, t.Any]: ...
    def get_rules(self, map: Map) -> t.Iterator[Rule]: ...
    def refresh(self) -> None: ...
    def bind(self, map: Map, rebind: bool=...) -> None: ...
    def get_converter(self, variable_name: str, converter_name: str, args: t.Tuple, kwargs: t.Mapping[str, t.Any]) -> BaseConverter: ...
    def compile(self) -> None: ...
    def match(self, path: str, method: t.Optional[str]=...) -> t.Optional[t.MutableMapping[str, t.Any]]: ...
    def build(self, values: t.Mapping[str, t.Any], append_unknown: bool=...) -> t.Optional[t.Tuple[str, str]]: ...
    def provides_defaults_for(self, rule: Rule) -> bool: ...
    def suitable_for(self, values: t.Mapping[str, t.Any], method: t.Optional[str]=...) -> bool: ...
    def match_compare_key(self) -> t.Tuple[bool, int, t.Iterable[t.Tuple[int, int]], int, t.Iterable[int]]: ...
    def build_compare_key(self) -> t.Tuple[int, int, int]: ...
    def __eq__(self, other: object) -> bool: ...
    __hash__: Any = ...

class BaseConverter:
    regex: str = ...
    weight: int = ...
    map: Any = ...
    def __init__(self, map: Map, *args: t.Any, **kwargs: t.Any) -> None: ...
    def to_python(self, value: str) -> t.Any: ...
    def to_url(self, value: t.Any) -> str: ...

class UnicodeConverter(BaseConverter):
    regex: Any = ...
    def __init__(self, map: Map, minlength: int=..., maxlength: t.Optional[int]=..., length: t.Optional[int]=...) -> None: ...

class AnyConverter(BaseConverter):
    regex: Any = ...
    def __init__(self, map: Map, *items: str) -> None: ...

class PathConverter(BaseConverter):
    regex: str = ...
    weight: int = ...

class NumberConverter(BaseConverter):
    weight: int = ...
    num_convert: t.Callable = ...
    regex: Any = ...
    fixed_digits: Any = ...
    min: Any = ...
    max: Any = ...
    signed: Any = ...
    def __init__(self, map: Map, fixed_digits: int=..., min: t.Optional[int]=..., max: t.Optional[int]=..., signed: bool=...) -> None: ...
    def to_python(self, value: str) -> t.Any: ...
    def to_url(self, value: t.Any) -> str: ...
    @property
    def signed_regex(self) -> str: ...

class IntegerConverter(NumberConverter):
    regex: str = ...

class FloatConverter(NumberConverter):
    regex: str = ...
    num_convert: Any = ...
    def __init__(self, map: Map, min: t.Optional[float]=..., max: t.Optional[float]=..., signed: bool=...) -> None: ...

class UUIDConverter(BaseConverter):
    regex: str = ...
    def to_python(self, value: str) -> uuid.UUID: ...
    def to_url(self, value: uuid.UUID) -> str: ...

DEFAULT_CONVERTERS: t.Mapping[str, t.Type[BaseConverter]]

class Map:
    default_converters: Any = ...
    lock_class: Any = ...
    default_subdomain: Any = ...
    charset: Any = ...
    encoding_errors: Any = ...
    strict_slashes: Any = ...
    merge_slashes: Any = ...
    redirect_defaults: Any = ...
    host_matching: Any = ...
    converters: Any = ...
    sort_parameters: Any = ...
    sort_key: Any = ...
    def __init__(self, rules: t.Optional[t.Iterable[RuleFactory]]=..., default_subdomain: str=..., charset: str=..., strict_slashes: bool=..., merge_slashes: bool=..., redirect_defaults: bool=..., converters: t.Optional[t.Mapping[str, t.Type[BaseConverter]]]=..., sort_parameters: bool=..., sort_key: t.Optional[t.Callable[[t.Any], t.Any]]=..., encoding_errors: str=..., host_matching: bool=...) -> None: ...
    def is_endpoint_expecting(self, endpoint: str, *arguments: str) -> bool: ...
    def iter_rules(self, endpoint: t.Optional[str]=...) -> t.Iterator[Rule]: ...
    def add(self, rulefactory: RuleFactory) -> None: ...
    def bind(self, server_name: str, script_name: t.Optional[str]=..., subdomain: t.Optional[str]=..., url_scheme: str=..., default_method: str=..., path_info: t.Optional[str]=..., query_args: t.Optional[t.Union[t.Mapping[str, t.Any], str]]=...) -> MapAdapter: ...
    def bind_to_environ(self, environ: WSGIEnvironment, server_name: t.Optional[str]=..., subdomain: t.Optional[str]=...) -> MapAdapter: ...
    def update(self) -> None: ...

class MapAdapter:
    map: Any = ...
    server_name: Any = ...
    script_name: Any = ...
    subdomain: Any = ...
    url_scheme: Any = ...
    path_info: Any = ...
    default_method: Any = ...
    query_args: Any = ...
    websocket: Any = ...
    def __init__(self, map: Map, server_name: str, script_name: str, subdomain: t.Optional[str], url_scheme: str, path_info: str, default_method: str, query_args: t.Optional[t.Union[t.Mapping[str, t.Any], str]]=...) -> None: ...
    def dispatch(self, view_func: t.Callable[[str, t.Mapping[str, t.Any]], WSGIApplication], path_info: t.Optional[str]=..., method: t.Optional[str]=..., catch_http_exceptions: bool=...) -> WSGIApplication: ...
    @typing.overload
    def match(self, path_info: t.Optional[str]=..., method: t.Optional[str]=..., return_rule: te.Literal[False]=..., query_args: t.Optional[t.Union[t.Mapping[str, t.Any], str]]=..., websocket: t.Optional[bool]=...) -> t.Tuple[str, t.Mapping[str, t.Any]]: ...
    @typing.overload
    def match(self, path_info: t.Optional[str]=..., method: t.Optional[str]=..., return_rule: te.Literal[True]=..., query_args: t.Optional[t.Union[t.Mapping[str, t.Any], str]]=..., websocket: t.Optional[bool]=...) -> t.Tuple[Rule, t.Mapping[str, t.Any]]: ...
    def test(self, path_info: t.Optional[str]=..., method: t.Optional[str]=...) -> bool: ...
    def allowed_methods(self, path_info: t.Optional[str]=...) -> t.Iterable[str]: ...
    def get_host(self, domain_part: t.Optional[str]) -> str: ...
    def get_default_redirect(self, rule: Rule, method: str, values: t.MutableMapping[str, t.Any], query_args: t.Union[t.Mapping[str, t.Any], str]) -> t.Optional[str]: ...
    def encode_query_args(self, query_args: t.Union[t.Mapping[str, t.Any], str]) -> str: ...
    def make_redirect_url(self, path_info: str, query_args: t.Optional[t.Union[t.Mapping[str, t.Any], str]]=..., domain_part: t.Optional[str]=...) -> str: ...
    def make_alias_redirect_url(self, path: str, endpoint: str, values: t.Mapping[str, t.Any], method: str, query_args: t.Union[t.Mapping[str, t.Any], str]) -> str: ...
    def build(self, endpoint: str, values: t.Optional[t.Mapping[str, t.Any]]=..., method: t.Optional[str]=..., force_external: bool=..., append_unknown: bool=..., url_scheme: t.Optional[str]=...) -> str: ...
