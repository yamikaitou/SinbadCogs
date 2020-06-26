from os import PathLike
from typing import Any, BinaryIO, FrozenSet, Optional, Union

from typing_extensions import Final

VALID_STATIC_FORMATS: Final[FrozenSet[str]] = ...
VALID_AVATAR_FORMATS: Final[FrozenSet[str]] = ...

class Asset:
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    async def read(self) -> bytes: ...
    async def save(
        self, fp: Union[BinaryIO, PathLike[str], str], *, seek_begin: bool = ...
    ) -> int: ...
