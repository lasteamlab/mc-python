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

me.removeEntities(distance = 30)

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
axolotl.callMethod(method = "setPlayingDead", args = True)
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
notasleep = bat.callMethod(method = "isAwake")

if notasleep == "true":
  print("***** ERROR: not asleep")
if verbose:
    print("--- awake: " + awake)
    print("--- not asleep: " + notasleep)

if verbose:
    print()
    print("Spawning bee, testing anger, hive, flower")

position = position + vec(1, 0, 0)

beeid = mc.spawnEntity(position, 'BEE')
bee = CmdEntity(mc.conn, beeid)

flower = bee.callMethod(method = "getFlower")
anger = bee.callMethod(method = "getAnger")
hive = bee.callMethod(method = "getHive")

if verbose:
    print("--- flower: " + flower)
    print("--- anger: " + anger)
    print("--- hive: " + hive)


if verbose:
    print()
    print("Spawning cat, testing collar and type")

catid = mc.spawnEntity(position, 'CAT')
cat = CmdEntity(mc.conn, catid)

oldcolor = cat.callMethod(method = "getCollarColor")
setcolor = "BLUE"
cat.callMethod(method = "setCollarColor", args = setcolor)
newcolor = cat.callMethod(method = "getCollarColor")

if newcolor.lower() != setcolor.lower():
    print("***** ERROR: Collar color not set correctly")
elif verbose:
    print("--- Original collar: " + oldcolor)
    print("--- New collar: " + newcolor)

oldcolor = cat.callMethod(method = "getCatType")
setcolor = "SIAMESE"
cat.callMethod(method = "setCatType", args = setcolor)
newcolor = cat.callMethod(method = "getCatType")

if newcolor.lower() != setcolor.lower():
    print("***** ERROR: type not set correctly")
if verbose:
    print("--- Original type: " + oldcolor)
    print("--- New type: " + newcolor)


if verbose:
    print()
    print("Spawning Horse, testing color, inventory, and style")

horseid = mc.spawnEntity(position, 'HORSE')
horse = CmdEntity(mc.conn, horseid)

oldcolor = horse.callMethod(method = "getColor")
setcolor = "GRAY"
horse.callMethod(method = "setColor", args = setcolor)
newcolor = horse.callMethod(method = "getColor")

if newcolor.lower() != setcolor.lower():
    print("***** ERROR: color not set correctly")
if verbose:
    print("--- Original color: " + oldcolor)
    print("--- New color: " + newcolor)


oldcolor = horse.callMethod(method = "getStyle")
setcolor = "WHITE_DOTS"
horse.callMethod(method = "setStyle", args = setcolor)
newcolor = horse.callMethod(method = "getStyle")

if newcolor.lower() != setcolor.lower():
    print("***** ERROR: style not set correctly")
if verbose:
    print("--- Original style: " + oldcolor)
    print("--- New style: " + newcolor)

if verbose:
    print()
    print("Spawning Goat, testing screaming")

goatid = mc.spawnEntity(position, 'GOAT')
goat = CmdEntity(mc.conn, goatid)
    
screaming = goat.callMethod(method = "isScreaming")
goat.callMethod(method = "setScreaming", args = True)
newscreaming = goat.callMethod(method = "isScreaming")

if verbose:
    print("--- screaming: " + screaming)
    print("--- new screaming: " + newscreaming)
    

if verbose:
    print()
    print("Spawning Llama, testing color, strength")

llamaid = mc.spawnEntity(position, 'LLAMA')
llama = CmdEntity(mc.conn, llamaid)

oldcolor = llama.callMethod(method = "getColor")
setcolor = "BROWN"
llama.callMethod(method = "setColor", args = setcolor)
newcolor = llama.callMethod(method = "getColor")

if newcolor.lower() != setcolor.lower():
    print("***** ERROR: color not set correctly")
if verbose:
    print("--- Original color: " + oldcolor)
    print("--- New color: " + newcolor)


oldstrength = llama.callMethod(method = "getStrength")
setstrength = "3"
llama.callMethod(method = "setColor", args = setstrength)
newstrength = llama.callMethod(method = "getStrength")

if setstrength != newstrength:
    print("***** ERROR: strength not set correctly")
if verbose:
    print("--- Original strength: " + oldstrength)
    print("--- New strength: " + newstrength)

if verbose:
    print()
    print("Spawning Parrot, testing variant")

parrotid = mc.spawnEntity(position, 'PARROT')
parrot = CmdEntity(mc.conn, parrotid)
    
oldcolor = parrot.callMethod(method = "getVariant")
setcolor = "CYAN"
parrot.callMethod(method = "setVariant", args = setcolor)
newcolor = parrot.callMethod(method = "getVariant")

if newcolor.lower() != setcolor.lower():
    print("***** ERROR: variant not set correctly")
elif verbose:
    print("--- Original variant: " + oldcolor)
    print("--- New variant: " + newcolor)

if verbose:
    print()
    print("Spawning Rabbit, testing type")

rabbitid = mc.spawnEntity(position, 'RABBIT')
rabbit = CmdEntity(mc.conn, rabbitid)

oldcolor = rabbit.callMethod(method = "getRabbitType")
setcolor = "BLACK_AND_WHITE"
rabbit.callMethod(method = "setRabbitType", args = setcolor)
newcolor = rabbit.callMethod(method = "getRabbitType")

if newcolor.lower() != setcolor.lower():
    print("***** ERROR: type not set correctly")
if verbose:
    print("--- Original type: " + oldcolor)
    print("--- New type: " + newcolor)


if verbose:
    print()
    print("Spawning Fox, testing type, trusted player, crouching")

foxid = mc.spawnEntity(position, 'FOX')
fox = CmdEntity(mc.conn, foxid)

oldcolor = fox.callMethod(method = "getFoxType")
setcolor = "SNOW"
fox.callMethod(method = "setFoxType", args = setcolor)
newcolor = fox.callMethod(method = "getFoxType")

if newcolor.lower() != setcolor.lower():
    print("***** ERROR: type not set correctly")
if verbose:
    print("--- Original type: " + oldcolor)
    print("--- New type: " + newcolor)

trusted = fox.callMethod(method = "getFirstTrustedPlayer")
fox.callMethod(method = "setFirstTrustedPlayer", args = me.id)
newtrusted = fox.callMethod(method = "getFirstTrustedPlayer")

if newtrusted != str(me.id):
    print("***** ERROR: trusted not set correctly")
if verbose:
    print("--- Original trusted: " + trusted)
    print("--- New trusted: " + newtrusted)
