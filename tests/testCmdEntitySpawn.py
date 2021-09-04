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
    print("Spawning adult cow and setting it to baby, locking age")

cowid = mc.spawnEntity(position, 'COW')
cow = CmdEntity(mc.conn, cowid)
if not cow.isAdult():
    print("***** ERROR: spawned baby cow")
elif verbose:
    print("--- spawned adult")

cow.setBaby()

if cow.isAdult():
    print("***** ERROR: adult cow not converted to baby")
elif verbose:
    print("--- set baby")

age = -24000
cow.setAgeLock(True)
cow.setAge(age)

print("--- sleeping 5 seconds")
time.sleep(5)

if int(cow.getAge()) > -23990:
    print("***** ERROR: Cow age or agelock set incorrectly.")
elif verbose:
    print("--- age lock successful")

position = position + vec(1, 0, 0)

if verbose:
    print()
    print("Spawning baby pig and setting it to adult")

pigid = mc.spawnEntity(position, 'PIG', True)
pig = CmdEntity(mc.conn, pigid)
if pig.isAdult():
    print("***** ERROR: spawned adult pig")
elif verbose:
    print("--- spawned baby")

pig.setAdult()
time.sleep(1)
if not pig.isAdult():
    print("***** ERROR: adult pig not converted to baby")
elif verbose:
    print("--- set adult")


# ------------------------- Wolf (test tameable features)----------------------------


position = position + vec(1, 0, 0)

if verbose:
    print()
    print("Spawning wolf, setting tamed and setting owner")

wolfid = mc.spawnEntity(position, 'WOLF')
wolf = CmdEntity(mc.conn, wolfid)
    
wolf.setTamed(True)

if not wolf.isTamed():
    print("***** ERROR: Wolf not tamed.")
elif verbose:
    print("--- set tamed successful")

wolf.setTamed(False)

if wolf.isTamed():
    print("***** ERROR: Wolf still tamed.")
elif verbose:
    print("--- set not tamed successful")


wolf.setOwner(me)

if wolf.getOwner() != str(me.id):
    print("***** ERROR: Wolf owner set incorrectly.")
elif verbose:
    print("--- set owner successful")



