# Daniel Coelho de Oliveira - 96800
# Pedro Candoso - 86140
# Miguel Matos - 89124


import asyncio
import getpass
import json
import os

import websockets

from agent import *
from mapa import Map
from pathfinding import *


class MapPosition(SearchDomain):
    def __init__(self, mapa, pos, gstate):
        super().__init__()
        self.mapa = mapa
        self.pos = pos
        self.gstate = gstate

    def actions(self, state):
        # Can stay,move,place bomb, and possibly detonate bomb
        actlist = []
        # Right,Down,Left,Up
        dirs = ["d", "s", "a", "w"]
        for d in dirs:
            newpos = self.mapa.calc_pos(state, d)
            x, y = newpos
            test = [x, y]
            if newpos != state and test not in [e['pos'] for e in self.gstate['enemies']]:
                actlist.append(d)
        return actlist

    def result(self, state, action):
        return self.mapa.calc_pos(state, action)

    def cost(self, state, action):
        return 1

    def heuristic(self, state, goal_state):
        return manhattan_distance(state, goal_state)


async def agent_loop(server_address="localhost:8000", agent_name="student"):
    async with websockets.connect(f"ws://{server_address}/player") as websocket:

        # Receive information about static game properties
        await websocket.send(json.dumps({"cmd": "join", "name": agent_name}))
        msg = await websocket.recv()
        game_properties = json.loads(msg)

        # You can create your own map representation or use the game representation:
        mapa = Map(size=game_properties["size"], mapa=game_properties["map"])
        agent = Agent(mapa)

        while True:
            try:
                state = json.loads(
                    # em cada loop websocket.messages deve ficar vazio chamando recv() quantas vezes forem necessarias
                    await websocket.recv()
                )  # receive game state, this must be called timely or your game will get out of sync with the server
                while websocket.messages:
                    print("\nSynced\n")
                    state = json.loads(await websocket.recv())
                # Update Map
                mapa.walls = state['walls']
                # Agent Logic
                agent.update_state(state)
                # Avaliar se o bomberman necessita de um novo objetivo
                goal, action = agent.get_goal()
                # Search logic
                bombpos = state.get("bomberman")
                start = MapPosition(mapa, tuple(bombpos), state)
                problem = SearchProblem(start, start.pos, goal)
                tree = SearchTree(problem, 'astar')
                path = tree.search()
                inputs = get_inputs(path)
                inputs.append(action)
                if inputs != [] and inputs != None:
                    await websocket.send(json.dumps({"cmd": "key", "key": inputs.pop(0)}))
            except websockets.exceptions.ConnectionClosedOK:
                print("Server has cleanly disconnected us")
                return


# DO NOT CHANGE THE LINES BELLOW
# You can change the default values using the command line, example:
# $ NAME='bombastico' python3 client.py
loop = asyncio.get_event_loop()
SERVER = os.environ.get("SERVER", "localhost")
PORT = os.environ.get("PORT", "8000")
NAME = os.environ.get("NAME", getpass.getuser())
loop.run_until_complete(agent_loop(f"{SERVER}:{PORT}", NAME))
