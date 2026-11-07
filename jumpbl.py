import sys
import logging
from mtkclient.Library.mtk_class import Mtk
from mtkclient.config.mtk_config import MtkConfig

serialport = "COM6"

config = MtkConfig(loglevel=logging.INFO)
mtk = Mtk(config=config, loglevel=logging.INFO, serialportname=serialport)

print("Waiting for device (preloader mode, don't press any button)...")
if mtk.preloader.init(display=True):
    print("Connected. Trying jump_bl() ...")
    try:
        result = mtk.preloader.jump_bl()
        if result:
            print("jump_bl() REALLY succeeded — device should now continue to bootloader/fastboot.")
        else:
            print("jump_bl() returned False — command not accepted.")
    except Exception as e:
        print(f"jump_bl() raised exception: {e}")
else:
    print("Could not connect to preloader.")
