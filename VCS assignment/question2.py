noFoPlayers = 4
dungeon = ["SHRINE"]
dongenLength = max(14, noFoPlayers * 4)
noOfArena = max(1, noFoPlayers // 2)
noOfCorridor = (dongenLength - 3) - (noOfArena * 4)

for i in range(noOfArena):
    dungeon.append("CROSSROADS")
    dungeon.append("SHRINE")
    dungeon.append("ARENA")
    dungeon.append("TREASURE")
    for i in range(noOfCorridor // 2):
        dungeon.append("CORRIDOR")

if len(dungeon) < dongenLength-2:
    dungeon.append("CORRIDOR")

# This was giving corret output but all the corridors were at the end of the dungeon
# remainingLength = (dongenLength-2) - len(dungeon)
# for i in range(remainingLength):
#     dungeon.append("CORRIDOR")

dungeon.append("BOSS")
dungeon.append("TREASURE")
print(dungeon)