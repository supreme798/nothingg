from multiprocessing import process
from pymem import *
from pymem.memory import read_bytes, write_bytes
from pymem.pattern import pattern_scan_all
import os
def mkp(aob: str):
    if '??' in aob:
        if aob.startswith("??"):
            aob = f" {aob}"
            n = aob.replace(" ??", ".").replace(" ", "\\x")
            b = bytes(n.encode())
        else:
            n = aob.replace(" ??", ".").replace(" ", "\\x")
            b = bytes(f"\\x{n}".encode())
        del n
        return b
    else:
        m = aob.replace(" ", "\\x")
        c = bytes(f"\\x{m}".encode())
        del m
        return c
    




def HEADLOAD():
    try:
        # Open the process
        proc = Pymem("HD-Player")
    except pymem.exception.ProcessNotFound:
        return

    try:
        if proc:
            print("\033[31m[>]\033[0m Searching Entity...")
            # Scan for entities
            global aimbot_addresses
            entity_pattern = mkp("FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 A5 43 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 00 00 00 00 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 00 00 00 00 ?? ?? ?? ?? 00 00 00 00 ?? ?? ?? ?? ?? ?? ?? ?? 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 80 BF")
            aimbot_addresses = pattern_scan_all(proc.process_handle, entity_pattern, return_multiple=True)

            if aimbot_addresses:
                print("")
                
            else:
                print("")
    
    except:
        print("")
    finally:
        if proc:
            proc.close_process()
    return "Fitur Berhasil Di Load"
    


def HEADON():
    try:
        # Open the process
        proc = Pymem("HD-Player")
    
        if proc:
            global original_value
            # Save the original value to variable, btw all the orginal values are same so we just save one
            original_value = []
            for current_entity in aimbot_addresses:
                original_value.append((current_entity, read_bytes(proc.process_handle, current_entity + 0x6C, 4)))
                # Read the value at current_entity + 0x60
                # Read the value at current_entity + 0x2C
                value_bytes = read_bytes(proc.process_handle, current_entity + 0x70, 4)
                
                # Write the value to current_entity + 0x5C
                # Write the value to current_entity + 0x28
                write_bytes(proc.process_handle, current_entity + 0x6C, value_bytes, len(value_bytes))    
    except pymem.exception.ProcessNotFound:
        print("")
        return
    finally:
        if proc:
            proc.close_process()
           
    return "AIMBOT HEAD ON"

def HEADOFF():
        try:
            # Open the process
            proc = Pymem("HD-Player")
            
            if original_value: # check the original value is present or not
            
                for i in original_value:
                    # Write the value to current_entity + 0x5C
                    # Write the value to current_entity + 0x28
                    write_bytes(proc.process_handle, i[0] + 0x6C, i[1], len(i[1]))
        except pymem.exception.ProcessNotFound:
            print("")
            return
        finally:
            if proc:
                proc.close_process()
        return "AIMBOT HEAD OFF"



def SniperScopeon():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
       if proc:
        print("Activating Sniper Scope", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp("1A 88 03 00 09 8A 03 00 FF FF FF FF 08 00 00 00 00 00 60 40 CD CC 8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 00 00 00 00 00 00 00 00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 B0 3F 00 00 80 3F 01"), return_multiple=True)
    except:
        print("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex("1A 88 03 00 09 8A 03 00 FF FF FF FF 08 00 00 00 00 00 60 40 CD CC 8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 FF FF 00 00 00 00 00 00 F0 41 00 00 48 42 00 00 00 3F 33 33 13 40 00 00 B0 3F 00 00 80 3F 01"),99)
    print("Sniper Scope Successfully!")


def SniperScopeoff():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
       if proc:
        print("Activating Sniper Scope", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp("60 40 CD CC 8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 FF FF 00 00 00 00 00 00 F0 41 00 00 48 42"), return_multiple=True)
    except:
        print("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex("60 40 CD CC 8C 3F 8F C2 F5 3C CD CC CC 3D 06 00 00 00 00 00 00 00 00 00 00 00 00 00 F0 41 00 00 48 42"),34)
    print("Sniper Scope Successfully!")


def SniperSwitchon():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
       if proc:
        print("Activating Sniper Switch", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp("B4 42 96 00 00 00 00 00 00 00 00 00 00 3F 00 00 80 3E 00 00 00 00 04 00 00 00 00 00 80 3F 00 00 20 41 00 00 34 42 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 3D 0A 57 3F 9A 99"), return_multiple=True)
    except:
        print("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex("b4 42 96 00 00 00 00 00 00 00 ec 51 b8 3d 8f c2 f5 3c"),18)
    print("Sniper Switch Successfully!")



def SniperSwitchoff():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
       if proc:
        print("Activating Sniper Switch", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp("b4 42 96 00 00 00 00 00 00 00 ec 51 b8 3d 8f c2 f5 3c"), return_multiple=True)
    except:
        print("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex("B4 42 96 00 00 00 00 00 00 00 00 00 00 3F 00 00 80 3E 00 00 00 00 04 00 00 00 00 00 80 3F 00 00 20 41 00 00 34 42 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 80 3F 3D 0A 57 3F 9A 99"),64)
    print("Sniper Switch Successfully!")


def SniperSwitchfixOn():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
       if proc:
        print("Activating Sniper Switch", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp("06 00 a0 e1 18 d0 4b e2 02 8b bd ec 70 8c bd e8"), return_multiple=True)
    except:
        print("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex("01 00 a0 e3 18 d0 4b e2 02 8b bd ec 70 8c bd e8"),16)
    print("Sniper Switch Successfully!")

def SniperSwitchfixOff():
    try:
       proc = Pymem("HD-Player")
    except:
       print("Bluestacks is not running.\nFirst start BlueStacks then Activate Bypass")

    try:
       if proc:
        print("Activating Sniper Switch", '\n'"Scanning...")
        value = pattern_scan_all(proc.process_handle, mkp("01 00 a0 e3 18 d0 4b e2 02 8b bd ec 70 8c bd e8"), return_multiple=True)
    except:
        print("aob not found")
  
    

    if value :
      for addr in value :
        write_bytes(proc.process_handle, addr, bytes.fromhex("06 00 a0 e3 18 d0 4b e2 02 8b bd ec 70 8c bd e8"),16)
    print("Sniper Switch Successfully!")


def taskmanager():
    process_name = "Taskmgr.exe"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'task.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        process.inject_dll(open_process.process_handle, dll_path_bytes)
        print("Task Manager Injected DLL Successfully!") 

    except pymem.exception.ProcessNotFound:
        print("Task Manager not found!")
    except Exception as e:
        print(f"Error: {e}")


def CharmsRgb():
    process_name = "HD-Player"

    try:
        # Open the process
        temp_dll_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Blue.dll')

        dll_path_bytes = bytes(temp_dll_path.encode('UTF-8'))

        open_process = Pymem(process_name)

        process.inject_dll(open_process.process_handle, dll_path_bytes)
        print("Charms RGB Injected Successfully!") 

    except pymem.exception.ProcessNotFound:
        print("Bluestacks Not Found!")
    except Exception as e:
        print(f"Error: {e}")


