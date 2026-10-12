#!/usr/bin/env python3
"""Invoke Apple clang++ with PyTensor's obsolete Darwin library flag removed.

PyTensor 2.38.2 passes ``-ld64`` on macOS >=15, which requests a nonexistent
library rather than selecting a linker. All compilation, optimization, and
other linkage arguments pass unchanged to the installed Apple compiler.
"""
import os
import sys

args = sys.argv[1:]
if sys.platform == "darwin":
    args = [arg for arg in args if arg != "-ld64"]
os.execv("/usr/bin/clang++", ["/usr/bin/clang++", *args])
