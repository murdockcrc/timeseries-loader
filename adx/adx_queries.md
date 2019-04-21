# Kusto Queries

## Count
```
Trucks
| count 
```

```
Result: 114,048,366
Execution time: 751ms
```

## Group by DeviceId
```
Trucks
| summarize count() by deviceId 
```

```
Result: 20'000 rows (data set consists of 20'000 devices generating messages concurrently)
Execution time: 4.803s
```

## Count all messages for one deviceId
```
Trucks
| where deviceId == 'd1626544-acfc-44fd-978a-6879f345a0da.truck-01.11578'
| summarize count() 
```

```
Result: 5'698
Execution time: 412ms
```

