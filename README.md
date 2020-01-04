## Red Eclipse Server Monitor

Configuration:
	Copy `Config.py.example` to `Config.py` and edit it to match your setup.

Usage:
	`./remonitor`  
This will print a bit of info about the server. Edit `Config.py` to set up the
server address and port.  

This daemon can also push data to an InfluxDB server.

Currently this project only supports protocol version 245, which corresponds to
Red Eclipse 2.0.

Example output from my own server:
```
./remonitor.py
{'host': '10.0.1.7', 'port': 28802, 'clients': 1, 'gameVersion': 245, 'gameMode': 'deathmatch', 'mutatorFlags': 0, 'mutators': [], 'timeLeft': 454, 'maxClients': 256, 'masterMode': 'open', 'varCount': 7535, 'modCount': 0, 'mapName': 'auster', 'serverName': "enp2s0's Deathmatch Server", 'versionName': '2.0.0', 'description': "enp2s0's Deathmatch Server", 'versionBranch': 'master', 'players': [{'name': 'enp2s0', 'privilege': 'localadministrator'}]}
```
