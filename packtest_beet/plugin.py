__all__ = [
    "beet_default",
]


from beet import Context

from .mecha import modify_mecha
from .test import TestFile


def beet_default(ctx: Context):
    ctx.data.extend_namespace.append(TestFile)
    modify_mecha(ctx)
