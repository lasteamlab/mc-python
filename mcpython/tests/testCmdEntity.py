#!/usr/bin/env python3

from mcpython.minecraft import Minecraft
from mcpython.minecraft import CmdEntity
from mcpython.minecraft import CmdPlayer
from mcpython import keys



def Test():
    """
    Tests for CmdEntity

    """
    mc = Minecraft.create(keys.servername, port = 4711)

    verbose = True

    type = input("Type P to test player.  Otherwise a random entity will be chosen. \n")

    if type.lower() == "p":
        player = True
    else:
        player = False


    print("NOTE: If errors are produced, run multiple times or in verbose mode to be sure.")
    print("      Sometimes minecraft spawns faster than we can check for removal.")

    if player:
        specificEntity = CmdPlayer(mc.conn, id = keys.username)
    else:
        entitylist = mc.getEntities()
        specificEntityId = entitylist[0][0]
        specificEntity = CmdEntity(mc.conn, specificEntityId)

        if verbose:
            print()
            print("FINDING AN ENTITY")
            print()
            print("found entity list")
            print("using specific entity " + str(specificEntityId) + " of type " + entitylist[0][1])


    specificEntityName = specificEntity.getName()

    if verbose:
        print("confirming entity name: " + specificEntityName)

        print()
        print("DEFAULT GET AND REMOVE ENTITIES FROM AROUND ENTITY")
        print()

    nearbyEntitiesDefault = specificEntity.getEntities()
    if verbose:
        print()
        print("nearby entities (default): ")
        for e in nearbyEntitiesDefault:
            print(e)

    entitiesRemoved = specificEntity.removeEntities()
    if verbose:
        print("nearby entities removed (default): ")
        print(entitiesRemoved)

    nearbyEntities = specificEntity.getEntities()
    if verbose:
        print("nearby entities (default) (should be empty): ")
        for e in nearbyEntities:
            print(e)

    if len(nearbyEntities) > 0:
        print("**** ERROR: not all entities removed (default) - run again to be sure")

    nearbyEntities = []
    distance = 10

    if verbose:
        print()
        print("GETTING AND REMOVING ENTITIES WITH NON_DEFAULT DISTANCE AND TYPE")
        print()

    while len(nearbyEntities) < 3:
        distance += 10
        nearbyEntities = specificEntity.getEntities(distance = distance)
        if verbose:
            print()
            print("nearby entities (distance: " + str(distance) + "): ")
            for e in nearbyEntities:
                print(e)

    specificEntityType = nearbyEntities[0][1]
    nearbyEntities = specificEntity.getEntities(distance = distance, typeId=specificEntityType)
    if len(nearbyEntities) < 1:
        print("**** ERROR: nearby entity of specific type not found - run again to be sure")

    if verbose:
        print()
        print("nearby entities (distance: " + str(distance) + ")(type: " + specificEntityType + "): ")
        for e in nearbyEntities:
            print(e)

    entitiesRemoved = specificEntity.removeEntities(distance = distance, typeId=specificEntityType)
    if verbose:
        print()
        print("remove nearby entities (distance: " + str(distance) + ")(type: " + specificEntityType + "): ")
        print(entitiesRemoved)


    nearbyEntities = specificEntity.getEntities(distance = distance)
    for e in nearbyEntities:
        if e[1].lower() == specificEntityType.lower():
            print("**** ERROR: not all nearby entity of specific type removed - run again to be sure")

    if verbose:
        print()
        print("nearby entities (distance: " + str(distance) + ")(should be no: " + specificEntityType + "): ")
        for e in nearbyEntities:
            print(e)


    entitiesRemoved = specificEntity.removeEntities(distance = distance)
    if verbose:
        print()
        print("remove all nearby entities (distance: " + str(distance) + "): ")
        print(entitiesRemoved)

    nearbyEntities = specificEntity.getEntities(distance = distance)

    if len(nearbyEntities) > 0:
        print("**** ERROR: not all entities removed (distance) - run again to be sure")

    if verbose:
        print()
        print("nearby entities (distance: " + str(distance) + ")(should be empty)")
        for e in nearbyEntities:
            print(e)


    specificEntity.clearEvents()

    if not player:
        mc.removeEntity(specificEntity.id)
        if verbose:
            print()
            print("cleaning up by removing entity")


if __name__ == "__main__":
    Test()