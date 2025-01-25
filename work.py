import pymem
from concurrent.futures import ThreadPoolExecutor
def search_and_replace(processName, search, replace):
    try:
        pm = pymem.Pymem(processName)
        pm.open_process_from_id(pm.process_id)
        matches = pm.pattern_scan_all(search, return_multiple=True)

        if matches:
            for match in matches:
                pm.write_bytes(match, replace, len(replace))
            return True 
    except Exception as e:
        pass
    return False 
def parallel_search_and_replace(process_name, search_replace_pairs, max_workers=16):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(lambda pair: search_and_replace(process_name, pair[0], pair[1]), search_replace_pairs))
    return results
search_replace_pairs = [ (rb"\x1A\x88\x03\x00\x09\x8A\x03\x00\xFF\xFF\xFF\xFF\x08\x00\x00\x00\x00\x00\x60\x40\xCD\xCC\x8C\x3F\x8F\xC2\xF5\x3C\xCD\xCC\xCC\x3D\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xF0\x41\x00\x00\x48\x42\x00\x00\x00\x3F\x33\x33\x13\x40\x00\x00\xB0\x3F\x00\x00\x80\x3F\x01", b"\x1A\x88\x03\x00\x09\x8A\x03\x00\xFF\xFF\xFF\xFF\x08\x00\x00\x00\x00\x00\x60\x40\xCD\xCC\x8C\x3F\x8F\xC2\xF5\x3C\xCD\xCC\xCC\x3D\x06\x00\x00\x00\x00\x00\xFF\xFF\x00\x00\x00\x00\x00\x00\xF0\x41\x00\x00\x48\x42\x00\x00\x00\x3F\x33\x33\x13\x40\x00\x00\xB0\x3F\x00\x00\x80\x3F\x01"),]
results = parallel_search_and_replace('HD-Player.exe', search_replace_pairs, max_workers=16)
for idx, result in enumerate(results, start=1):
    print(f"Step {idx} {'Activated' if result else 'Failed'}")