## Red Eclipse Server Monitor

Usage:
	`./remonitor <server> <port>`  
This will print a bit of info about the server.

Currently this project only supports protocol version 245, which corresponds to
Red Eclipse 2.0.

Example output from my own server:
```
./remonitor.py 10.0.1.7 28802
{'host': '10.0.1.7', 'port': 28802, 'clients': 1, 'gameVersion': 245, 'gameMode': 'deathmatch', 'mutatorFlags': 0, 'mutators': [], 'timeLeft': 454, 'maxClients': 256, 'masterMode': 'open', 'varCount': 7535, 'modCount': 0, 'mapName': 'auster', 'serverName': "enp2s0's Deathmatch Server", 'versionName': '2.0.0', 'description': "enp2s0's Deathmatch Server", 'versionBranch': 'master', 'players': [{'name': 'enp2s0', 'privilege': 'localadministrator'}]}
```
