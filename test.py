from mcpi.minecraft import Minecraft
import os
import time

mc = Minecraft.create()

time.sleep(3)
mc.setBlock(6, 0, 0, 10)

time.sleep(3)
mc.setBlock(6, 0, 0, 128)

time.sleep(3)
mc.setBlock(6, 0, 0, 12)
