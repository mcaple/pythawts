# For a good explanation of packages see
# https://py-pkgs.org/
# https://py-pkgs.org/04-package-structure.html

# Raise an error elegantly if the module fails to import:
try:
    import pythawts
except ImportError as err:
    raise ImportError(err)

from pythawts.forthawts.core import *
