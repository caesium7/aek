import importlib
import sys
from .client import next, rank


def forza():
    if "aek.forza" in sys.modules:
        importlib.reload(sys.modules["aek.forza"])
    else:
        import aek.forza
