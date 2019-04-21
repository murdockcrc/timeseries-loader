CREATE TABLE Trucks
(
    latitude numeric(9,6) NOT NULL,
    longitude numeric(9,6) NOT NULL,
    speed integer NOT NULL,
    speed_unit varchar(5) NOT NULL,
    temperature numeric(6,3) NOT NULL,
    temperature_unit varchar(2) NOT NULL,
    EventProcessedUtcTime TIMESTAMPTZ NOT NULL,
    ConnectionDeviceId varchar(200) NOT NULL
);

SELECT create_hypertable('trucks', 'eventprocessedutctime');
