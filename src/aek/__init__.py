import importlib
from .client import next, rank


def forza():
    import aek.forza
    importlib.reload(aek.forza)
