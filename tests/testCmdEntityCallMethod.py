#!/usr/bin/env python3

from mcpython import vec3
from mcpython.minecraft import Minecraft
from mcpython.minecraft import CmdPlayer 
from mcpython.minecraft import CmdEvents 
from mcpython.minecraft import CmdEntity
from mcpython import block
from mcpython import keys
from mcpython.vec3 import Vec3 as vec
import time 

mc = Minecraft.create(keys.servername, port = 4711)
# mc = Minecraft.create()
me = CmdPlayer(mc.conn, id = keys.username)
position = me.getPos()

verbose = True

me.removeEntities()

position = position + vec(1, 0, 0)

# ------------------------- Cow and Pig (test ageable features)----------------------------

if verbose:
    print()
    print("Spawning wolf, setting collar color, and getting isAngry")

position = position + vec(1, 0, 0)

wolfid = mc.spawnEntity(position, 'WOLF')
wolf = CmdEntity(mc.conn, wolfid)
    
oldcolor = wolf.callMethod(method = "getCollarColor")
setcolor = "BLUE"
wolf.callMethod(method = "setCollarColor", args = setcolor)
newcolor = wolf.callMethod(method = "getCollarColor")

if newcolor.lower() != setcolor.lower():
    print("***** ERROR: Collar color not set correctly")
elif verbose:
    print("--- Original collar: " + oldcolor)
    print("--- New collar: " + newcolor)

anger = wolf.callMethod(method = "isAngry")

if verbose:
    print("--- anger: " + anger)

if verbose:
    print()
    print("Spawning axolotl, testing variant, and playing dead")

position = position + vec(1, 0, 0)

axolotlid = mc.spawnEntity(position, 'AXOLOTL')
axolotl = CmdEntity(mc.conn, axolotlid)
    
oldcolor = axolotl.callMethod(method = "getVariant")
setcolor = "LUCY"
axolotl.callMethod(method = "setVariant", args = setcolor)
newcolor = axolotl.callMethod(method = "getVariant")

if newcolor.lower() != setcolor.lower():
    print("***** ERROR: variant not set correctly")
elif verbose:
    print("--- Original variant: " + oldcolor)
    print("--- New variant: " + newcolor)


olddead = axolotl.callMethod(method = "isPlayingDead")
# axolotl.callMethod(method = "setPlayingDead", args = True)
newdead = axolotl.callMethod(method = "isPlayingDead")

# if "true" != newdead:
#     print("***** ERROR: play dead not set correctly")
# elif verbose:
print("--- Original play dead: " + olddead)
print("--- New play dead: " + newdead)


if verbose:
    print()
    print("Spawning bat, testing awake")

position = position + vec(1, 0, 0)

batid = mc.spawnEntity(position, 'BAT')
bat = CmdEntity(mc.conn, batid)

awake = bat.callMethod(method = "isAwake")
bat.callMethod(method = "setAwake", args = False)
asleep = bat.callMethod(method = "isAwake")

if asleep == "true":
  print("***** ERROR: not asleep")
if verbose:
    print("--- awake: " + awake)
    print("--- not asleep: " + asleep)

if verbose:
    print()
    print("Spawning bee, testing anger, hive, flower")

position = position + vec(1, 0, 0)

beeid = mc.spawnEntity(position, 'BEE')
bee = CmdEntity(mc.conn, beeid)

flower = bee.callMethod(method = "getFlower")
anger = bee.callMethod(method = "getAnger")
bee.callMethod(method = "setAnger", args = 3)
newanger = bee.callMethod(method = "getAnger")

if verbose:
    print("--- flower: " + flower)
    print("--- anger: " + anger)
    print("--- newanger: " + newanger)






    
