#! /usr/bin/env python3
# Red Eclipse 2.0 Server Protocol Implementation
#
# Largely based on the redflare source code, which is under the AGPLv3.
# https://github.com/stainsby/redflare/
#
# This program requires python3 and depends on bitstring.

import sys
import REServer

if len(sys.argv) != 3:
	print("Usage: remonitor.py <server> <port>")
	exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

data = REServer.doServerQuery(host, port)
print(data)
