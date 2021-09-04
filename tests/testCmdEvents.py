#!/usr/bin/env python3

from mcpython.minecraft import Minecraft
from mcpython.minecraft import CmdEvents
from mcpython.minecraft import CmdPlayer
from mcpython import keys

mc = Minecraft.create(keys.servername, port = 4711)
player = CmdPlayer(mc.conn, id = keys.username)
print(player.getName())

# BLOCK HITS
input("Testing static CmdEvents methods")
input("Hit block with sword and hit ENTER to continue.")

blockhits = CmdEvents.pollBlockHits(mc.conn)
print("all blockhits: " + str(blockhits))

#  CHAT POSTS
input("Post to chat and hit ENTER to continue.")

chatposts = CmdEvents.pollChatPosts(mc.conn)
print("all chatposts: " + str(chatposts))

#  PROJECTILE HITS
input("Hit block with projectile and hit ENTER to continue.")

projectilehits = CmdEvents.pollProjectileHits(mc.conn)
print("all projectilehits: " + str(projectilehits))


# BLOCK HITS
input("Testing CmdPlayer events methods (through CmdEntity)")
input("Hit block with sword and hit ENTER to continue.")

blockhits = player.pollBlockHits()
print("all blockhits: " + str(blockhits))

#  CHAT POSTS
input("Post to chat and hit ENTER to continue.")

chatposts = player.pollChatPosts()
print("all chatposts: " + str(chatposts))

#  PROJECTILE HITS
input("Hit block with projectile and hit ENTER to continue.")

projectilehits = player.pollProjectileHits()
print("all projectilehits: " + str(projectilehits))

