"""Lightweight shim for `rtmidi` used by the nocturn project.

This provides minimal `MidiIn`/`MidiOut` classes and the
`midiconstants` module so the code can run without native extension
dependencies. It's intended as a fallback for development and testing
on systems where RTMidi bindings fail to build.
"""
from .core import MidiIn, MidiOut
from .midiconstants import *

__all__ = ["MidiIn", "MidiOut"] + [name for name in globals() if name.isupper()]
