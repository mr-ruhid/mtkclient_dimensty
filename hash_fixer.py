import hashlib

def fix_da_hash_v2(file_path):
    print(f"[*] '{file_path}' üçün Genişləndirilmiş Hash Yenilənməsi başlayır...")
    
    with open(file_path, "rb") as f:
        data = bytearray(f.read())

    # BÜTÜV faylın xam baytlarının SHA-256 dəyərini hesablayırıq
    full_hash = hashlib.sha256(data).digest()
    
    # Başlıq olmadan (0x200-dən sonra) olan hissənin hashi
    code_only_hash = hashlib.sha256(data[0x200:]).digest()
    
    print(f"[+] Bütöv Fayl SHA256: {full_hash.hex()}")
    print(f"[+] Kod Hissəsi SHA256: {code_only_hash.hex()}")


    offsets_to_patch = [0x40, 0x60, 0x80]
    
    for offset in offsets_to_patch:

        data[offset:offset+32] = full_hash

        if offset + 32 < 0x200:
            data[offset+32:offset+64] = code_only_hash

    with open(file_path, "wb") as f:
        f.write(data)
        
    print("[+] Uğurlu! Bütün daxili hash xanaları offline olaraq yeniləndi.")

if __name__ == "__main__":
    fix_da_hash_v2("DA_BR_patched.bin")
