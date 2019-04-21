# Timescale queries

## Count

```
select count(*) from trucks;
```

```
Result: 113737258
Execution time: 5mins 22secs
```

Second execution (I suppose indexes are still being built after ingesting over 100 million rows of data)
```
Result: 113737258
Execution time: 1min 10secs
```

## Group by deviceId
```
select connectiondeviceid, count(*) from trucks                                                              group by connectiondeviceid;
```

```
Result: 20'000 rows
Execution time: 1min 30secs
```

## Count all messages for one deviceId
```
select count(*) from trucks                                                                                  where connectiondeviceid = 'd1626544-acfc-44fd-978a-6879f345a0da.truck-01.11578';
```

```
Result: 5'682
Execution time: 1min 12secs
```