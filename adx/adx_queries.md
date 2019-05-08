Trucks
| count 

Trucks
| summarize count() by deviceId 

Trucks
| where deviceId == 'd1626544-acfc-44fd-978a-6879f345a0da.truck-01.11578'
| summarize count() 

Trucks
| summarize max(timestamp), min(timestamp)

let endtime = todatetime('2019-04-14T22:29:56.28Z');
let starttime = datetime_add('hour', -4, endtime);
Trucks
| where deviceId == 'd1626544-acfc-44fd-978a-6879f345a0da.truck-01.11578'
| where timestamp between (starttime .. endtime)

let endtime = todatetime('2019-04-14T22:29:56.28Z');
let starttime = endtime - time(4h);
let interval = 30min;
Trucks
| where deviceId == 'd1626544-acfc-44fd-978a-6879f345a0da.truck-01.11578'
| where timestamp between (starttime .. endtime)
| summarize count() 

let endtime = todatetime('2019-04-14T22:29:56.28Z');
let starttime = endtime - time(4h);
let interval = 30min;
Trucks
| where deviceId == 'd1626544-acfc-44fd-978a-6879f345a0da.truck-01.11578'
| make-series avg(temperature), min(temperature), max(temperature) on timestamp from starttime to endtime step interval
| render linechart with (xcolumn = timestamp, ycolumns = avg_temperature, min_temperature, max_temperature)

let endtime = todatetime('2019-04-14T22:29:56.28Z');
let starttime = endtime - time(5h);
let interval = 30min;
Trucks
| make-series avg(temperature), min(temperature), max(temperature) on timestamp from starttime to endtime step interval
| render linechart with (xcolumn = timestamp, ycolumns = avg_temperature, min_temperature, max_temperature)

let endtime = todatetime('2019-04-14T22:29:56.28Z');
let starttime = endtime - time(4h);
let interval = 30min;
Trucks
//| where deviceId == 'd1626544-acfc-44fd-978a-6879f345a0da.truck-01.11578'
| where timestamp between ( starttime .. endtime )
| summarize avg(temperature), min(temperature), max(temperature) by bin(timestamp, interval)
| render linechart with (xcolumn = timestamp, ycolumns = avg_temperature, min_temperature, max_temperature)

let endtime = todatetime('2019-04-14T22:29:56.28Z');
let starttime = endtime - time(4h);
let interval = 30min;
Trucks
| project temperature, timestamp  
| render linechart with (xcolumn = timestamp, ycolumns = temperature)

let endtime = todatetime('2019-04-14T22:29:56.28Z');
let starttime = endtime - time(4h);
let interval = 30min;
Trucks
| where deviceId == 'd1626544-acfc-44fd-978a-6879f345a0da.truck-01.11578'
| summarize avg(temperature) by bin(timestamp, 1h)
| render timechart