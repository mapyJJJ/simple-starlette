from . import exceptions as exceptions, http as http
from .filesystem import get_filesystem_encoding as get_filesystem_encoding
from collections.abc import Collection, MutableSet
from typing import Any, Optional

def is_immutable(self) -> None: ...
def iter_multi_items(mapping: Any) -> None: ...

class ImmutableListMixin:
    def __hash__(self) -> Any: ...
    def __reduce_ex__(self, protocol: Any): ...
    def __delitem__(self, key: Any) -> None: ...
    def __iadd__(self, other: Any) -> None: ...
    def __imul__(self, other: Any) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def append(self, item: Any) -> None: ...
    def remove(self, item: Any) -> None: ...
    def extend(self, iterable: Any) -> None: ...
    def insert(self, pos: Any, value: Any) -> None: ...
    def pop(self, index: int = ...) -> None: ...
    def reverse(self) -> None: ...
    def sort(self, key: Optional[Any] = ..., reverse: bool = ...) -> None: ...

class ImmutableList(ImmutableListMixin, list): ...

class ImmutableDictMixin:
    @classmethod
    def fromkeys(cls, keys: Any, value: Optional[Any] = ...): ...
    def __reduce_ex__(self, protocol: Any): ...
    def __hash__(self) -> Any: ...
    def setdefault(self, key: Any, default: Optional[Any] = ...) -> None: ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...
    def pop(self, key: Any, default: Optional[Any] = ...) -> None: ...
    def popitem(self) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def clear(self) -> None: ...

class ImmutableMultiDictMixin(ImmutableDictMixin):
    def __reduce_ex__(self, protocol: Any): ...
    def add(self, key: Any, value: Any) -> None: ...
    def popitemlist(self) -> None: ...
    def poplist(self, key: Any) -> None: ...
    def setlist(self, key: Any, new_list: Any) -> None: ...
    def setlistdefault(self, key: Any, default_list: Optional[Any] = ...) -> None: ...

class UpdateDictMixin(dict):
    on_update: Any = ...
    def setdefault(self, key: Any, default: Optional[Any] = ...): ...
    def pop(self, key: Any, default: Any = ...): ...
    __setitem__: Any = ...
    __delitem__: Any = ...
    clear: Any = ...
    popitem: Any = ...
    update: Any = ...

class TypeConversionDict(dict):
    def get(self, key: Any, default: Optional[Any] = ..., type: Optional[Any] = ...): ...

class ImmutableTypeConversionDict(ImmutableDictMixin, TypeConversionDict):
    def copy(self): ...
    def __copy__(self): ...

class MultiDict(TypeConversionDict):
    def __init__(self, mapping: Optional[Any] = ...) -> None: ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def add(self, key: Any, value: Any) -> None: ...
    def getlist(self, key: Any, type: Optional[Any] = ...): ...
    def setlist(self, key: Any, new_list: Any) -> None: ...
    def setdefault(self, key: Any, default: Optional[Any] = ...): ...
    def setlistdefault(self, key: Any, default_list: Optional[Any] = ...): ...
    def items(self, multi: bool = ...) -> None: ...
    def lists(self) -> None: ...
    def values(self) -> None: ...
    def listvalues(self): ...
    def copy(self): ...
    def deepcopy(self, memo: Optional[Any] = ...): ...
    def to_dict(self, flat: bool = ...): ...
    def update(self, mapping: Any) -> None: ...
    def pop(self, key: Any, default: Any = ...): ...
    def popitem(self): ...
    def poplist(self, key: Any): ...
    def popitemlist(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo: Any): ...

class _omd_bucket:
    prev: Any = ...
    key: Any = ...
    value: Any = ...
    next: Any = ...
    def __init__(self, omd: Any, key: Any, value: Any) -> None: ...
    def unlink(self, omd: Any) -> None: ...

class OrderedMultiDict(MultiDict):
    def __init__(self, mapping: Optional[Any] = ...) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    __hash__: Any = ...
    def __reduce_ex__(self, protocol: Any): ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def keys(self): ...
    def __iter__(self) -> Any: ...
    def values(self): ...
    def items(self, multi: bool = ...) -> None: ...
    def lists(self) -> None: ...
    def listvalues(self) -> None: ...
    def add(self, key: Any, value: Any) -> None: ...
    def getlist(self, key: Any, type: Optional[Any] = ...): ...
    def setlist(self, key: Any, new_list: Any) -> None: ...
    def setlistdefault(self, key: Any, default_list: Optional[Any] = ...) -> None: ...
    def update(self, mapping: Any) -> None: ...
    def poplist(self, key: Any): ...
    def pop(self, key: Any, default: Any = ...): ...
    def popitem(self): ...
    def popitemlist(self): ...

class Headers:
    def __init__(self, defaults: Optional[Any] = ...) -> None: ...
    def __getitem__(self, key: Any, _get_mode: bool = ...): ...
    def __eq__(self, other: Any) -> Any: ...
    __hash__: Any = ...
    def get(self, key: Any, default: Optional[Any] = ..., type: Optional[Any] = ..., as_bytes: bool = ...): ...
    def getlist(self, key: Any, type: Optional[Any] = ..., as_bytes: bool = ...): ...
    def get_all(self, name: Any): ...
    def items(self, lower: bool = ...) -> None: ...
    def keys(self, lower: bool = ...) -> None: ...
    def values(self) -> None: ...
    def extend(self, *args: Any, **kwargs: Any) -> None: ...
    def __delitem__(self, key: Any, _index_operation: bool = ...) -> None: ...
    def remove(self, key: Any): ...
    def pop(self, key: Optional[Any] = ..., default: Any = ...): ...
    def popitem(self): ...
    def __contains__(self, key: Any): ...
    def has_key(self, key: Any): ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def add(self, _key: Any, _value: Any, **kw: Any) -> None: ...
    def add_header(self, _key: Any, _value: Any, **_kw: Any) -> None: ...
    def clear(self) -> None: ...
    def set(self, _key: Any, _value: Any, **kw: Any) -> None: ...
    def setlist(self, key: Any, values: Any) -> None: ...
    def setdefault(self, key: Any, default: Any): ...
    def setlistdefault(self, key: Any, default: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...
    def to_wsgi_list(self): ...
    def copy(self): ...
    def __copy__(self): ...

class ImmutableHeadersMixin:
    def __delitem__(self, key: Any, **kwargs: Any) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def set(self, _key: Any, _value: Any, **kw: Any) -> None: ...
    def setlist(self, key: Any, values: Any) -> None: ...
    def add(self, _key: Any, _value: Any, **kw: Any) -> None: ...
    def add_header(self, _key: Any, _value: Any, **_kw: Any) -> None: ...
    def remove(self, key: Any) -> None: ...
    def extend(self, *args: Any, **kwargs: Any) -> None: ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...
    def insert(self, pos: Any, value: Any) -> None: ...
    def pop(self, key: Optional[Any] = ..., default: Any = ...) -> None: ...
    def popitem(self) -> None: ...
    def setdefault(self, key: Any, default: Any) -> None: ...
    def setlistdefault(self, key: Any, default: Any) -> None: ...

class EnvironHeaders(ImmutableHeadersMixin, Headers):
    environ: Any = ...
    def __init__(self, environ: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    __hash__: Any = ...
    def __getitem__(self, key: Any, _get_mode: bool = ...): ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def copy(self) -> None: ...

class CombinedMultiDict(ImmutableMultiDictMixin, MultiDict):
    def __reduce_ex__(self, protocol: Any): ...
    dicts: Any = ...
    def __init__(self, dicts: Optional[Any] = ...) -> None: ...
    @classmethod
    def fromkeys(cls, keys: Any, value: Optional[Any] = ...) -> None: ...
    def __getitem__(self, key: Any): ...
    def get(self, key: Any, default: Optional[Any] = ..., type: Optional[Any] = ...): ...
    def getlist(self, key: Any, type: Optional[Any] = ...): ...
    def keys(self): ...
    def __iter__(self) -> Any: ...
    def items(self, multi: bool = ...) -> None: ...
    def values(self) -> None: ...
    def lists(self): ...
    def listvalues(self): ...
    def copy(self): ...
    def to_dict(self, flat: bool = ...): ...
    def __len__(self): ...
    def __contains__(self, key: Any): ...
    def has_key(self, key: Any): ...

class FileMultiDict(MultiDict):
    def add_file(self, name: Any, file: Any, filename: Optional[Any] = ..., content_type: Optional[Any] = ...) -> None: ...

class ImmutableDict(ImmutableDictMixin, dict):
    def copy(self): ...
    def __copy__(self): ...

class ImmutableMultiDict(ImmutableMultiDictMixin, MultiDict):
    def copy(self): ...
    def __copy__(self): ...

class ImmutableOrderedMultiDict(ImmutableMultiDictMixin, OrderedMultiDict):
    def copy(self): ...
    def __copy__(self): ...

class Accept(ImmutableList):
    provided: bool = ...
    def __init__(self, values: Any = ...): ...
    def __getitem__(self, key: Any): ...
    def quality(self, key: Any): ...
    def __contains__(self, value: Any): ...
    def index(self, key: Any): ...
    def find(self, key: Any): ...
    def values(self) -> None: ...
    def to_header(self): ...
    def best_match(self, matches: Any, default: Optional[Any] = ...): ...
    @property
    def best(self): ...

class MIMEAccept(Accept):
    @property
    def accept_html(self): ...
    @property
    def accept_xhtml(self): ...
    @property
    def accept_json(self): ...

class LanguageAccept(Accept):
    def best_match(self, matches: Any, default: Optional[Any] = ...): ...

class CharsetAccept(Accept): ...

def cache_control_property(key: Any, empty: Any, type: Any): ...
def cache_property(key: Any, empty: Any, type: Any): ...

class _CacheControl(UpdateDictMixin, dict):
    no_cache: Any = ...
    no_store: Any = ...
    max_age: Any = ...
    no_transform: Any = ...
    on_update: Any = ...
    provided: Any = ...
    def __init__(self, values: Any = ..., on_update: Optional[Any] = ...) -> None: ...
    def to_header(self): ...
    cache_property: Any = ...

class RequestCacheControl(ImmutableDictMixin, _CacheControl):
    max_stale: Any = ...
    min_fresh: Any = ...
    only_if_cached: Any = ...

class ResponseCacheControl(_CacheControl):
    public: Any = ...
    private: Any = ...
    must_revalidate: Any = ...
    proxy_revalidate: Any = ...
    s_maxage: Any = ...
    immutable: Any = ...

def csp_property(key: Any): ...

class ContentSecurityPolicy(UpdateDictMixin, dict):
    base_uri: Any = ...
    child_src: Any = ...
    connect_src: Any = ...
    default_src: Any = ...
    font_src: Any = ...
    form_action: Any = ...
    frame_ancestors: Any = ...
    frame_src: Any = ...
    img_src: Any = ...
    manifest_src: Any = ...
    media_src: Any = ...
    navigate_to: Any = ...
    object_src: Any = ...
    prefetch_src: Any = ...
    plugin_types: Any = ...
    report_to: Any = ...
    report_uri: Any = ...
    sandbox: Any = ...
    script_src: Any = ...
    script_src_attr: Any = ...
    script_src_elem: Any = ...
    style_src: Any = ...
    style_src_attr: Any = ...
    style_src_elem: Any = ...
    worker_src: Any = ...
    on_update: Any = ...
    provided: Any = ...
    def __init__(self, values: Any = ..., on_update: Optional[Any] = ...) -> None: ...
    def to_header(self): ...

class CallbackDict(UpdateDictMixin, dict):
    on_update: Any = ...
    def __init__(self, initial: Optional[Any] = ..., on_update: Optional[Any] = ...) -> None: ...

class HeaderSet(MutableSet):
    on_update: Any = ...
    def __init__(self, headers: Optional[Any] = ..., on_update: Optional[Any] = ...) -> None: ...
    def add(self, header: Any) -> None: ...
    def remove(self, header: Any) -> None: ...
    def update(self, iterable: Any) -> None: ...
    def discard(self, header: Any) -> None: ...
    def find(self, header: Any): ...
    def index(self, header: Any): ...
    def clear(self) -> None: ...
    def as_set(self, preserve_casing: bool = ...): ...
    def to_header(self): ...
    def __getitem__(self, idx: Any): ...
    def __delitem__(self, idx: Any) -> None: ...
    def __setitem__(self, idx: Any, value: Any) -> None: ...
    def __contains__(self, header: Any): ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def __bool__(self): ...

class ETags(Collection):
    star_tag: Any = ...
    def __init__(self, strong_etags: Optional[Any] = ..., weak_etags: Optional[Any] = ..., star_tag: bool = ...) -> None: ...
    def as_set(self, include_weak: bool = ...): ...
    def is_weak(self, etag: Any): ...
    def is_strong(self, etag: Any): ...
    def contains_weak(self, etag: Any): ...
    def contains(self, etag: Any): ...
    def contains_raw(self, etag: Any): ...
    def to_header(self): ...
    def __call__(self, etag: Optional[Any] = ..., data: Optional[Any] = ..., include_weak: bool = ...): ...
    def __bool__(self): ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def __contains__(self, etag: Any): ...

class IfRange:
    etag: Any = ...
    date: Any = ...
    def __init__(self, etag: Optional[Any] = ..., date: Optional[Any] = ...) -> None: ...
    def to_header(self): ...

class Range:
    units: Any = ...
    ranges: Any = ...
    def __init__(self, units: Any, ranges: Any) -> None: ...
    def range_for_length(self, length: Any): ...
    def make_content_range(self, length: Any): ...
    def to_header(self): ...
    def to_content_range_header(self, length: Any): ...

class ContentRange:
    on_update: Any = ...
    def __init__(self, units: Any, start: Any, stop: Any, length: Optional[Any] = ..., on_update: Optional[Any] = ...) -> None: ...
    units: Any = ...
    start: Any = ...
    stop: Any = ...
    length: Any = ...
    def set(self, start: Any, stop: Any, length: Optional[Any] = ..., units: str = ...) -> None: ...
    def unset(self) -> None: ...
    def to_header(self): ...
    def __bool__(self): ...

class Authorization(ImmutableDictMixin, dict):
    type: Any = ...
    def __init__(self, auth_type: Any, data: Optional[Any] = ...) -> None: ...
    @property
    def username(self): ...
    @property
    def password(self): ...
    @property
    def realm(self): ...
    @property
    def nonce(self): ...
    @property
    def uri(self): ...
    @property
    def nc(self): ...
    @property
    def cnonce(self): ...
    @property
    def response(self): ...
    @property
    def opaque(self): ...
    @property
    def qop(self): ...
    def to_header(self): ...

def auth_property(name: Any, doc: Optional[Any] = ...): ...

class WWWAuthenticate(UpdateDictMixin, dict):
    on_update: Any = ...
    def __init__(self, auth_type: Optional[Any] = ..., values: Optional[Any] = ..., on_update: Optional[Any] = ...) -> None: ...
    def set_basic(self, realm: str = ...) -> None: ...
    def set_digest(self, realm: Any, nonce: Any, qop: Any = ..., opaque: Optional[Any] = ..., algorithm: Optional[Any] = ..., stale: bool = ...) -> None: ...
    def to_header(self): ...
    type: Any = ...
    realm: Any = ...
    domain: Any = ...
    nonce: Any = ...
    opaque: Any = ...
    algorithm: Any = ...
    qop: Any = ...
    @property
    def stale(self): ...
    @stale.setter
    def stale(self, value: Any) -> None: ...
    auth_property: Any = ...

class FileStorage:
    name: Any = ...
    stream: Any = ...
    filename: Any = ...
    headers: Any = ...
    def __init__(self, stream: Optional[Any] = ..., filename: Optional[Any] = ..., name: Optional[Any] = ..., content_type: Optional[Any] = ..., content_length: Optional[Any] = ..., headers: Optional[Any] = ...) -> None: ...
    @property
    def content_type(self): ...
    @property
    def content_length(self): ...
    @property
    def mimetype(self): ...
    @property
    def mimetype_params(self): ...
    def save(self, dst: Any, buffer_size: int = ...) -> None: ...
    def close(self) -> None: ...
    def __bool__(self): ...
    def __getattr__(self, name: Any): ...
    def __iter__(self) -> Any: ...