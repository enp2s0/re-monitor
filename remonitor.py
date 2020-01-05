#! /usr/bin/env python3
# Red Eclipse 2.0 Server Protocol Implementation
#
# Largely based on the redflare source code, which is under the AGPLv3.
# https://github.com/stainsby/redflare/
#
# This program requires python3 and depends on bitstring and InfluxDB-python.

import sys
import time

from REServerInterface import REServerQuery
import InfluxOutput
import Config

while True:
	data = REServerQuery.doServerQuery(Config.SERVER_HOST, Config.SERVER_PORT)
	if data == None:
		continue

	if Config.DUMP_DATA:
		print(data)

	if Config.INFLUX_ENABLE:
		InfluxOutput.pushReport(data)

	if Config.ONESHOT:
		break

	time.sleep(Config.INTERVAL)
