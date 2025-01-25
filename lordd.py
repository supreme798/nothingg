from multiprocessing import process
from pymem import *
from pymem.memory import read_bytes, write_bytes
from pymem.pattern import pattern_scan_all
import os

def SniperScopeon():
    try:
       proc = Pymem("HD-Player")
    except:
    try:
       if proc:
        print("Activating Sniper Scope", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, bytes.fromhex("1A 88 03 00 09 8A 03 00 FF FF FF FF 08 00 00 00 00 00 60 40 CD CC 8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 00 00 00 00 00 00 00 00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 B0 3F 00 00 80 3F 01"), return_multiple=True)
    except:
        print("aob not found")
  
    if value:
      for addr in value:
        write_bytes(proc.process_handle, addr, bytes.fromhex("1A 88 03 00 09 8A 03 00 FF FF FF FF 08 00 00 00 00 00 60 40 CD CC 8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 FF FF 00 00 00 00 00 00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 B0 3F 00 00 80 3F 01"), 99)
    print("Sniper Scope Successfully!")

def SniperScopeoff():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
       if proc:
        print("Activating Sniper Scope", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, bytes.fromhex("60 40 CD CC 8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 FF FF 00 00 00 00 00 00 F0 41 00 00 48 42"), return_multiple=True)
    except:
        print("aob not found")
  
    if value:
      for addr in value:
        write_bytes(proc.process_handle, addr, bytes.fromhex("60 40 CD CC 8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 00 00 00 00 00 00 00 00 F0 41 00 00 48 42"), 34)
    print("Sniper Scope Successfully!")

def SniperSwitchon():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
       if proc:
        print("Activating Sniper Switch", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, bytes.fromhex("B4 42 96 00 00 00 00 00 00 00 00 00 00 3F 00 00 80 3E 00 00 00 00 04 00 00 00 00 00 80 3F 00 00 20 41 00 00 34 42 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 3D 0A 57 3F 9A 99"), return_multiple=True)
    except:
        print("aob not found")
  
    if value:
      for addr in value:
        write_bytes(proc.process_handle, addr, bytes.fromhex("b4 42 96 00 00 00 00 00 00 00 ec 51 b8 3d 8f c2 f5 3c"), 18)
    print("Sniper Switch Successfully!")

def SniperSwitchoff():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
       if proc:
        print("Activating Sniper Switch", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, bytes.fromhex("b4 42 96 00 00 00 00 00 00 00 ec 51 b8 3d 8f c2 f5 3c"), return_multiple=True)
    except:
        print("aob not found")
  
    if value:
      for addr in value:
        write_bytes(proc.process_handle, addr, bytes.fromhex("B4 42 96 00 00 00 00 00 00 00 00 00 00 3F 00 00 80 3E 00 00 00 00 04 00 00 00 00 00 80 3F 00 00 20 41 00 00 34 42 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 3D 0A 57 3F 9A 99"), 64)
    print("Sniper Switch Successfully!")

def SniperSwitchfixOn():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
       if proc:
        print("Activating Sniper Switch", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, bytes.fromhex("06 00 a0 e1 18 d0 4b e2 02 8b bd ec 70 8c bd e8"), return_multiple=True)
    except:
        print("aob not found")
  
    if value:
      for addr in value:
        write_bytes(proc.process_handle, addr, bytes.fromhex("01 00 a0 e3 18 d0 4b e2 02 8b bd ec 70 8c bd e8"), 16)
    print("Sniper Switch Successfully!")

def SniperSwitchfixOff():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
       if proc:
        print("Activating Sniper Switch", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, bytes.fromhex("01 00 a0 e3 18 d0 4b e2 02 8b bd ec 70 8c bd e8"), return_multiple=True)
    except:
        print("aob not found")
  
    if value:
      for addr in value:
        write_bytes(proc.process_handle, addr, bytes.fromhex("06 00 a0 e3 18 d0 4b e2 02 8b bd ec 70 8c bd e8"), 16)
    print("Sniper Switch Successfully!")
