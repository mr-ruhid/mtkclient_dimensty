DA_FILE = r"C:\Users\ruhid\Downloads\Infinix-GT-20-Pro-X6871-15\download_agent\DA_BR.bin"

with open(DA_FILE, 'rb') as f:
    data = f.read()

for keyword in [b"Transsion", b"transsion", b"TRANSSION", b"Infinix", b"infinix"]:
    idx = data.find(keyword)
    print(f"{keyword}: {'found at ' + hex(idx) if idx != -1 else 'NOT FOUND'}")
