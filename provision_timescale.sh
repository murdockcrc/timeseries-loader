az postgres up --server-name luisdel --resource-group device-simulation --location westeurope --admin-user operator --admin-password NDIANUARYSID
az postgres server configuration set -g device-simulation -s luisdel --name shared_preload_libraries --value timescaledb
az postgres server configuration set -g device-simulation -s luisdel --name pg_qs.query_capture_mode --value top
az postgres server restart -g device-simulation -n luisdel