"""Native thread controls for Apple's thread-local BLAS implementation."""

from __future__ import annotations

import ctypes
import sys

from threadpoolctl import LibController, register


class _AccelerateController(LibController):
    """Expose Accelerate's real single-thread mode through threadpoolctl.

    Apple's macOS15 API selects automatic or single-threaded BLAS/LAPACK in
    the calling thread. Automatic mode has no queryable numeric worker cap,
    so it is reported as None. A requested positive cap selects one worker,
    the only bounded mode this API supports; restoring None selects automatic.
    """

    user_api = "blas"
    internal_api = "accelerate"
    # The full basename avoids threadpoolctl's generic non-Windows libblas guard.
    filename_prefixes = ("libblas.dylib",)
    check_symbols = ("BLASGetThreading", "BLASSetThreading")

    def get_version(self) -> None:
        return None

    def get_num_threads(self) -> int | None:
        getter = self.dynlib.BLASGetThreading
        getter.argtypes = ()
        getter.restype = ctypes.c_uint
        return 1 if getter() == 1 else None

    def set_num_threads(self, num_threads: int | None) -> None:
        if num_threads is not None and num_threads < 1:
            raise ValueError("Accelerate requires a positive thread cap or automatic mode")
        setter = self.dynlib.BLASSetThreading
        setter.argtypes = (ctypes.c_uint,)
        setter.restype = ctypes.c_int
        if setter(0 if num_threads is None else 1) != 0:
            raise RuntimeError("Accelerate rejected the BLAS threading model")


_accelerate_registered = False


def register_accelerate_controller() -> None:
    """Register the documented native controller once before parallel IPCA work."""
    global _accelerate_registered
    if sys.platform == "darwin" and not _accelerate_registered:
        register(_AccelerateController)
        _accelerate_registered = True
