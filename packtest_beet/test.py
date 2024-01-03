
from typing import ClassVar, Tuple

from beet import TextFile


class TestFile(TextFile):
    """Class representing an test function."""

    scope: ClassVar[Tuple[str, ...]] = ("tests",)
    extension: ClassVar[str] = ".mcfunction"