import sys
import time
from influxdb import InfluxDBClient
import pprint

from REServerInterface import REServerQuery
import Config

def pushReport(result):
	client = InfluxDBClient(Config.INFLUX_HOST, Config.INFLUX_PORT, Config.INFLUX_USER, Config.INFLUX_PASS, Config.INFLUX_DB)

	del result["players"]
	del result["mutators"]

	client.create_database(Config.INFLUX_DB)
	influx_data = {}

	influx_data["measurement"] = f"{Config.SERVER_HOST}:{Config.SERVER_PORT}"
	influx_data["fields"] = result
	influx_data["tags"] = {
		"server": f"{Config.SERVER_HOST}:{Config.SERVER_PORT}",
		"map": result["mapName"],
		"gameMode": result["gameMode"]
	}
	influx_data["time"] = time.strftime(f'%Y-%m-%dT%H:%M:%SZ+{Config.TIMEZONE}')

	if Config.DEBUG:
		pprint.pprint(influx_data)
	client.write_points([influx_data])
