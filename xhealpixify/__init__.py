from importlib.metadata import version

from xhealpixify.grid import HealpyGridInfo  # noqa: F401
from xhealpixify.regridder import HealpyRegridder  # noqa: F401

try:
    __version__ = version("xhealpixify")
except Exception:
    __version__ = "999"
