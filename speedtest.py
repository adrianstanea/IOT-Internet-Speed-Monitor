import re
import subprocess
from influxdb import InfluxDBClient

# https://pimylifeup.com/raspberry-pi-internet-speed-monitor/
response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr',
                            shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)
download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
jitter = re.search('Latency:.*?jitter:\s+(.*?)ms', response, re.MULTILINE)

ping = ping.group(1)
download = download.group(1)
upload = upload.group(1)
jitter = jitter.group(1)

speed_data = [
    {
        "measurement" : "internet_speed",
        "tags" : {
            "host": "astanea@rpi"
        },
        "fields" : {
            "download": float(download),
            "upload": float(upload),
            "ping": float(ping),
            "jitter": float(jitter)
        }
    }
]

# https://influxdb-python.readthedocs.io/en/latest/api-documentation.html
client = InfluxDBClient(host='localhost', 
                        port=8086,
                        username='astanea', 
                        password='astanea',
                        database='internet_speed')
client.write_points(speed_data)