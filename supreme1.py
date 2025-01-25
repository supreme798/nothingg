from pymem import *
from pymem.memory import read_bytes, write_bytes
from pymem.pattern import pattern_scan_all
import os

def mkp(aob: str):
    # This function converts the AOB string into bytes
    m = aob.replace(" ", "\\x")  # Replacing spaces with \x
    c = bytes(f"\\x{m}".encode())  # Convert AOB string to bytes format
    del m
    return c

def SniperScopeon():
    try:
        proc = Pymem("HD-Player")
    except:
        print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
        if proc:
            print("Activating Sniper Scope", '\n' "Scanning...")
            value = pattern_scan_all(proc.process_handle, mkp("1A 88 03 00 09 8A 03 00 FF FF FF FF 08 00 00 00 00 00 60 40 CD CC 8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 00 00 00 00 00 00 00 00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 B0 3F 00 00 80 3F 01"), return_multiple=True)
    except:
        print("AOB not found")

    if value:
        for addr in value:
            write_bytes(proc.process_handle, addr, bytes.fromhex("1A 88 03 00 09 8A 03 00 FF FF FF FF 08 00 00 00 00 00 60 40 CD CC 8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 FF FF 00 00 00 00 00 00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 B0 3F 00 00 80 3F 01"), 99)
        print("Sniper Scope Successfully Activated!")
