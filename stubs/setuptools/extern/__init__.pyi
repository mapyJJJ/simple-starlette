from typing import Any, Optional

class VendorImporter:
    root_name: Any = ...
    vendored_names: Any = ...
    vendor_pkg: Any = ...
    def __init__(self, root_name: Any, vendored_names: Any = ..., vendor_pkg: Optional[Any] = ...) -> None: ...
    @property
    def search_path(self) -> None: ...
    def load_module(self, fullname: Any): ...
    def create_module(self, spec: Any): ...
    def exec_module(self, module: Any) -> None: ...
    def find_spec(self, fullname: Any, path: Optional[Any] = ..., target: Optional[Any] = ...): ...
    def install(self) -> None: ...

names: Any
