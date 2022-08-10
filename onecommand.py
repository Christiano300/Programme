import pyperclip
commands = """
say 1
say 2
say 3
""".strip().split("\n")
start = "summon falling_block ~ ~1 ~ {BlockState:{Name:activator_rail},Time:1,Passengers:["
end = ',{id:command_block_minecart,Command:"setblock ~ ~ ~1 command_block{Command:\\\"fill ~ ~-1 ~-1 ~ ~ ~ air\\\"} replace"},\
    {id:command_block_minecart,Command:"setblock ~ ~-1 ~1 redstone_block"},{id:command_block_minecart,Command:"kill @e[type=command_block_minecart,distance=0..2]"}]}'
insert = "{id:command_block_minecart,Command:\"§\"}"
commands.extend(["setblock ~ ~-1 ~2 minecraft:repeating_command_block[facing=up]{Command:\\\"execute positioned ~ ~1 ~-3 run kill @e[type=item,distance=..2,nbt={Age:1s}]\\\",auto:1b}",
                 "setblock ~ ~ ~2 minecraft:chain_command_block[conditional=true,facing=up]{Command:\\\"fill ~ ~ ~ ~ ~-1 ~ air\\\",auto:1b}"])
command = start + ",".join([insert.replace("§", i) for i in commands]) + end
print(command)
pyperclip.copy(command)