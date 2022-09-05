# Raise an error elegantly if the module fails to import:
try:
    import pythawts
except ImportError as err:
    raise ImportError(err)

from .forthawts.core import *
