docker stop crown_testbed
docker rm crown_testbed
docker run --name crown_testbed -d -p 2345:5432  psadbimgs.azurecr.us/crowndb-snapshot:2021.07.22