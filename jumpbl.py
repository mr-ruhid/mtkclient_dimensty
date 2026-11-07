import sys
import logging
from mtkclient.Library.mtk_class import Mtk
from mtkclient.config.mtk_config import MtkConfig

serialport = "COM6"  # öz COM portunuzu yazın

config = MtkConfig(loglevel=logging.INFO)
mtk = Mtk(config=config, loglevel=logging.INFO, serialportname=serialport)

print("Waiting for device (preloader mode, don't press any button)...")
if mtk.preloader.init(display=True):
    print("Connected. Trying jump_bl() ...")
    if mtk.preloader.jump_bl():
        print("jump_bl() succeeded — device should now continue to bootloader/fastboot.")
    else:
        print("jump_bl() failed or not supported.")
else:
    print("Could not connect to preloader.")
