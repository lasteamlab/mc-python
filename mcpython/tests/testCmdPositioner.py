#!/usr/bin/env python3

from mcpython.minecraft import Minecraft
from mcpython.minecraft import CmdEntity
from mcpython.minecraft import CmdPlayer
from mcpython.vec3 import Vec3
from mcpython import keys
from mcpython.minecraft import Dir

mc = Minecraft.create(keys.servername, port = 4711)

verbose = True
type = input("Type P to test player.  Otherwise a random entity will be chosen. \n")

if type.lower() == "p":
    player = True
else:
    player = False


if player:
    entity = CmdPlayer(mc.conn, id = keys.username)
    entityType = "PLAYER"
else:
    entitylist = mc.getEntities()
    entityId = entitylist[0][0]
    entity = CmdEntity(mc.conn, entityId)
    entityType = entitylist[0][1]

    if verbose:
        print()
        print("FINDING AN ENTITY")
        print()
        print("found entity list")
        print("using specific entity " + str(entityId) + " of type " + entityType)

returnedType = entity.getType()
if returnedType.lower() == entityType.lower():
    if verbose:
        print("Server returned entity type of " + returnedType + " which matches declared type of " + entityType + ".")
else:
    print("***** ERROR: Server returned entity type of " + returnedType + " does not match declared type of " + entityType + ".")


if verbose:
    print()
    print("GETTING AND SETTING POS and TILE POS")
    print()

oldpos = entity.getPos()
setpos = Vec3(oldpos.x, oldpos.y + 5, oldpos.z)
entity.setPos(setpos)
newpos = entity.getPos()


if newpos == setpos:
    if verbose:
        print("Entity position is : " + str(oldpos.x) + ", " + str(oldpos.y) + ", " + str(oldpos.z))
        print("Setting new position to: " + str(setpos.x) + ", " + str(setpos.y) + ", " + str(setpos.z))
        print("New position is: " + str(newpos.x) + ", " + str(newpos.y) + ", " + str(newpos.z))
        print()
else:
    print("***** ERROR: entity pos was set to " + str(setpos.x) + ", " + str(setpos.y) + ", " + str(setpos.z) + " but is actually: "  + str(newpos.x) + ", " + str(newpos.y) + ", " + str(newpos.z))


oldpos = entity.getTilePos()
setpos = Vec3(oldpos.x, oldpos.y + 5, oldpos.z)
entity.setTilePos(setpos)
newpos = entity.getTilePos()


if newpos == setpos:
    if verbose:
        print("Entity position is : " + str(oldpos.x) + ", " + str(oldpos.y) + ", " + str(oldpos.z))
        print("Setting new position to: " + str(setpos.x) + ", " + str(setpos.y) + ", " + str(setpos.z))
        print("New position is: " + str(newpos.x) + ", " + str(newpos.y) + ", " + str(newpos.z))
        print()
else:
    print("***** ERROR: entity tile pos was set to " + str(setpos.x) + ", " + str(setpos.y) + ", " + str(setpos.z) + " but is actually: "  + str(newpos.x) + ", " + str(newpos.y) + ", " + str(newpos.z))

if verbose:
    print()
    print("GETTING AND SETTING DIRECTION, ROTATION, and PITCH")
    print()


olddir = entity.getDirection()
setdir = Vec3(olddir.x + 1, olddir.y, olddir.z).unit()
entity.setDirection(setdir)
newdir = entity.getDirection()


if newdir.isclose(setdir, 1e-3, 1e-3):
    if verbose:
        print("Entity direction is : " + str(olddir.x) + ", " + str(olddir.y) + ", " + str(olddir.z))
        print("Setting new direction to: " + str(setdir.x) + ", " + str(setdir.y) + ", " + str(setdir.z))
        print("New direction is: " + str(newdir.x) + ", " + str(newdir.y) + ", " + str(newdir.z))
        print()
else:
    print("***** ERROR: entity direction was set to " + str(setdir.x) + ", " + str(setdir.y) + ", " + str(setdir.z) + "but is actually: "  + str(newdir.x) + ", " + str(newdir.y) + ", " + str(newdir.z))


oldrot = entity.getRotation()
setrot = Dir.SOUTH
entity.setRotation(setrot)
newrot = entity.getRotation()


if setrot == newrot:
    if verbose:
        print("Entity rotation is : " + str(oldrot))
        print("Setting new rotation to: " + str(setrot))
        print("New rotation is: " + str(newrot))
        print()
else:
    print("***** ERROR: entity rotation was set to " + str(setrot) + " but is actually: "  + str(newrot))


oldpitch = entity.getPitch()
setpitch = Dir.FORWARD
print(setpitch)
entity.setPitch(setpitch)
newpitch = entity.getPitch()


if setpitch == newpitch:
    if verbose:
        print("Entity pitch is : " + str(oldpitch))
        print("Setting new pitch to: " + str(setpitch))
        print("New pitch is: " + str(newpitch))
        print()
else:
    print("***** ERROR: entity pitch was set to " + str(setpitch) + " but is actually: "  + str(newpitch))


