this library allows to interact with Novation Nocturn device  
requirements:  
usage:  
    python main.py  
customization:  
    usb_client.py  
development:  
    inherit FinalDevice class and make adjustments  

todo:  
    midi interaction advanced. 
        currently this is just a 9-knob midi cc device
    osc interaction  
    wxPython interaction  
    delayed interaction / python async

Fork of the original Novation Nocturn Python project — updated
for modern Python (3.13) and development on macOS.

Key changes in this fork
- Updated dependency pins to be compatible with Python 3.13.
- Included a lightweight pure-Python `rtmidi` shim for development
    when native RtMidi bindings fail to build on macOS.
- Fixed typing and runtime issues to run the package with a venv.

Requirements
- Python 3.13
- System: `libusb` (install via Homebrew on macOS)
- Project Python dependencies: see `requirements.txt`

Quick start (macOS)
1. Install system dependency:
```bash
brew install libusb
```
2. Create and activate a Python 3.13 venv (adjust path if needed):
```bash
python3.13 -m venv .venv
source .venv/bin/activate
```
3. Install Python deps:
```bash
pip install -r requirements.txt
```
4. Run the app (from the repository root `nocturn-python`):
```bash
python -m nocturn.main
```
Notes
- The original project instantiated the USB device on import. Running
    `python -m nocturn.main` will attempt to open the Nocturn if it's
    connected; keep the device unplugged if you only want to run unit
    tests or import modules.
- If the native `python-rtmidi` package does not build on your system,
    this fork provides a shimbed `rtmidi` package in the project root
    for development (it logs messages and exposes the minimal API used
    by the project). Replace it with a native binding for full MIDI I/O.

Development pointers
- Edit `nocturn/usb_client.py` to customize behavior and button mappings.
- To avoid hardware access during import, we can refactor `dev` so it
    is created lazily via a factory — tell me if you want that change.
