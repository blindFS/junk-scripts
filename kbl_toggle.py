#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import sys
from AlienFX.AlienFXEngine import *
from pyAlienFX import Daemon_Controller, pyAlienFX_GUI

driver = AlienFX_Driver()
computer = driver.computer
controller = Daemon_Controller()
conn = controller.makeConnection()
gui = pyAlienFX_GUI()
if not conn:
    controller = AlienFX_Controller(driver)
if len(sys.argv) != 2:
    print("USAGE:kbtoggle on/off")
    sys.exit()
if sys.argv[1] == "off":
    controller.Reset(computer.RESET_ALL_LIGHTS_OFF)
elif sys.argv[1] == "on":
    gui.Set_Conf()
else:
    print("USAGE:kbtoggle on/off")
