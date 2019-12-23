import platform
import subprocess

from typing import List
from ping import Ping
from latency_table import LatencyTable

WORLD_MIN = 1
WORLD_MAX = 25
GAME = 'oldschool'

def ping_rs(world: str, game: str):
    """
    Pings a list of runescape worlds

    Args:
        worlds: list of world numbers, i.e. [1, 2, 3]
        game: prefix for osrs/rs3: 'oldschool' or 'world' 
    """
    uri = "{}{}.runescape.com".format(game, world)
    cmd = Ping(platform.system(), uri, count='1')
    return (uri, cmd.average(cmd.send()))

def prompt():
    worlds = range(WORLD_MIN, WORLD_MAX + 1)
    game = 'oldschool'
    table = LatencyTable()
    for world in worlds:
        world, latency = ping_rs(world, game)
        table.worlds[world] = latency
    lowest = table.sort_lowest()
    for line in lowest:
        print(line)


if __name__ == '__main__':
    prompt()