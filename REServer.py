import sys
import socket
import bitstring

import Protocol

lastChecked = None
lastIDCounter = 0

# TODO: parse player names.
def processServerReply(host, port, reply):
	report = {}

	stream = Protocol.Stream(reply, 5)

	report["host"] = host
	report["port"] = port

	report["clients"] = stream.readNextInt()
	count = stream.readNextInt() - 1
	report["gameVersion"] = stream.readNextInt()

	serverVersion = report["gameVersion"]
	versionName = f"unknown version ({serverVersion})"
	if report["gameVersion"] == 245:
		versionName = "2.0"
		proto = Protocol.Protocol245()
	else:
		print(f"Unsupported server protocol {serverVersion}")
		return None

	gameMode = stream.readNextInt()
	report["gameMode"] = proto.gameModeFromCode(gameMode)
	count -= 1

	mutators = stream.readNextInt()
	count -= 1
	report["mutatorFlags"] = mutators
	report["mutators"] = proto.mutatorsFromFlags(mutators, gameMode)
	report["timeLeft"] = stream. readNextInt()
	count -= 1

	report["maxClients"] = stream.readNextInt()
	count -= 1

	report["masterMode"] = proto.masterModeFromCode(stream.readNextInt())
	count -= 1

	report["varCount"] = stream.readNextInt()
	count -= 1

	report["modCount"] = stream.readNextInt()
	count -= 1

	majorVersion = stream.readNextInt()
	minorVersion = stream.readNextInt()
	patchVersion = stream.readNextInt()
	count -= 3
	versionName = f"{majorVersion}.{minorVersion}.{patchVersion}"

	while count > 0:
		stream.readNextInt()
		count -= 1

	report["mapName"] = stream.readNextString()

	serverName = stream.readNextString()
	if serverName:
		report["serverName"] = serverName
	else:
		report["serverName"] = f"{host}:{port}"

	report["versionName"] = versionName
	report["description"] = serverName

	return report

def doServerQuery(host, port):
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	query = bitstring.BitArray("0x81EC040100")

	client.sendto(query.bytes, (host, port))
	reply, server = client.recvfrom(8192)
	client.close()

	report = processServerReply(host, port, bitstring.BitStream(reply))

	return report
