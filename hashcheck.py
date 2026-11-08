import logging
import sys
from mtkclient.Library.mtk_class import Mtk
from mtkclient.config.mtk_config import MtkConfig
from mtkclient.Library.DA.daconfig import DAconfig
from mtkclient.Library.DA.mtk_daloader import DaLoader

DA_FILE = r"C:\Users\ruhid\Downloads\Infinix-GT-20-Pro-X6871-15\download_agent\DA_BR.bin"  # ORIJINAL fayl, patched YOX

config = MtkConfig(loglevel=logging.INFO)
config.init_hwcode(0x1172)   # sizin HW code
config.hwver = 0xca00
config.swver = 0
config.loader = DA_FILE

mtk = Mtk(config=config, loglevel=logging.INFO, serialportname=None)
daloader = DaLoader(mtk, loglevel=logging.INFO)
mtk.daloader = daloader

daconfig = DAconfig(mtk=mtk, loader=DA_FILE, preloader=None, loglevel=logging.INFO)
daconfig.setup()

with open(DA_FILE, 'rb') as f:
    da1offset = daconfig.da_loader.region[1].m_buf
    da1size = daconfig.da_loader.region[1].m_len
    da1sig_len = daconfig.da_loader.region[1].m_sig_len
    f.seek(da1offset)
    da1 = f.read(da1size)

    da2offset = daconfig.da_loader.region[2].m_buf
    da2size = daconfig.da_loader.region[2].m_len
    da2sig_len = daconfig.da_loader.region[2].m_sig_len
    f.seek(da2offset)
    da2 = f.read(da2size)

print(f"DA1: offset={hex(da1offset)}, size={hex(da1size)}, sig_len={hex(da1sig_len)}")
print(f"DA2: offset={hex(da2offset)}, size={hex(da2size)}, sig_len={hex(da2sig_len)}")

hashaddr, hashmode, hashlen = daloader.compute_hash_pos(
    da1, da2, da1sig_len, da2sig_len, daconfig.da_loader.v6
)
print(f"hashaddr={hex(hashaddr) if hashaddr else None}")
print(f"hashmode={hashmode}")
print(f"hashlen={hashlen}")
