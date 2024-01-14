# IOT-Internet-Speed-Monitor
Setup project for IOT discipline. The main goal is to get familiar with linux using a Raspberry Pi.

## Speedtest CLI
- Speedtest CLI is a command-line interface for testing internet bandwidth using speedtest.net
- A python script is used to run the **speedtest-cli** and regex is used to extract the necessary data from the output of the speedtest.

### Database setup
- We use **InfluxDB** as the database for storing the data. It is an open-source time series database.
- We install the InfluxDB client as well as the library for python.
- Use **systemctl** to start the influxdb service and enable it to start at boot time.
- We format the data into a JSON like format and use the **influxdb** library to write the data to the database.
- A write operation is performed with the following fields:
    - Download speed
    - Upload speed
    - Ping
    - Jitter



## Grafana
- Grafana is an open-source analytics and monitoring solution. We use it to visualize the data stored in the database.
- We install Grafana and start the service using **systemctl**.
- Through SQL queries, we can visualize the data in the form of graphs and charts.
- Basic data processing such as calculating the average, minimum, maximum are done for an enhanced visualization experience.
- Graphana is accessible through the **browser at port 3000.**


## Crontab jobs

- A cron job is a time-based task scheduler in Unix-like operating systems. Users can schedule jobs (commands or scripts) to run periodically at fixed times, dates, or intervals
- In this project, we use **crontab** to schedule the execution of a python script that will update the database with data that monitors the status of the network.
- The script is executed once every minute.
- Use the following command to edit the crontab file:
```
crontab -e
```
- Verify that the crontab file has been edited with the following command:
```
crontab -l
```

## Systemctl services
- Check that **user defined services** are enabled running using the following command:
```
systemctl list-unit-files --type=service --state=enabled
```
