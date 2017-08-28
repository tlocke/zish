from zish.core import (
    loads, load, dump, dumps, ZishException, ZishLocationException)
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__all__ = [load, loads, dump, dumps, ZishException, ZishLocationException]
