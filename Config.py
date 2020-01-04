# re-monitor Configuration File

# Enables debug mode.
DEBUG = True

# RE2 Server Settings
SERVER_HOST = "10.0.1.7"
SERVER_PORT = 28802

# InfluxDB Settings
INFLUX_ENABLE = True
INFLUX_HOST = "status.net.lan"
INFLUX_PORT = 8086
INFLUX_USER = ""
INFLUX_PASS = ""
INFLUX_DB = "redeclipse"

# Reporting Settings
# Run once and exit.
ONESHOT = False
# Report rate in seconds.
INTERVAL = 3
# Print the raw server JSON.
DUMP_DATA = False
# Hours behind UTC
TIMEZONE = 5
