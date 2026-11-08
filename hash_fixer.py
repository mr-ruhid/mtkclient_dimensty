import hashlib
import struct

def fix_da_hash(file_path):
    print(f"[*] '{file_path}' üçün daxili Hash yenilənməsi başlayır...")
    
    with open(file_path, "rb") as f:
        data = bytearray(f.read())


    header_size = 0x200
    actual_code = data[header_size:]


    new_hash = hashlib.sha256(actual_code).digest()
    print(f"[+] Yeni hesablanan SHA256: {new_hash.hex()}")


    hash_offset = 0x40 
    

    data[hash_offset:hash_offset+32] = new_hash

    with open(file_path, "wb") as f:
        f.write(data)
        
    print("[+] Uğurlu! DA_BR.bin faylının daxili imza (hash) xətası offline olaraq düzəldildi.")

if __name__ == "__main__":
    fix_da_hash("DA_BR_patched.bin")
