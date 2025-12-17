"""Minimal pure-Python MidiIn/MidiOut shim.

This tries to be compatible with the small surface the project uses:
- `MidiIn()` and `MidiOut()` constructors
- `open_virtual_port(name)` and `open_port(idx)` (no-op)
- `set_callback(callable)` for `MidiIn`
- `send_message([status, data1, data2])` for `MidiOut`
- Context manager support for `MidiIn`/`MidiOut`

This shim does not provide real MIDI I/O; instead it logs messages
and stores a callback for manual invocation. Use this for development
when native RTMidi bindings are not available.
"""
import threading
import time
import sys
from collections.abc import Callable


class MidiIn:
    def __init__(self):
        self._callback = None
        self._running = False

    def open_virtual_port(self, name: str = "From-nocturn"):
        print(f"[rtmidi-shim] opened virtual input port: {name}")

    def open_port(self, idx: int = 0):
        print(f"[rtmidi-shim] opened input port index: {idx}")

    def set_callback(self, callback: Callable):
        self._callback = callback

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self._callback = None


class MidiOut:
    def __init__(self):
        self._port = None

    def open_virtual_port(self, name: str = "To-nocturn"):
        print(f"[rtmidi-shim] opened virtual output port: {name}")

    def open_port(self, idx: int = 0):
        print(f"[rtmidi-shim] opened output port index: {idx}")

    def send_message(self, msg):
        try:
            print(f"[rtmidi-shim] send_message: {msg}")
        except Exception:
            print("[rtmidi-shim] send_message failed to print msg", file=sys.stderr)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        pass
