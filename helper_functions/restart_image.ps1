Set-Location C:\Users\mikah\Documents\crowndb-testbed
docker stop crown_testbed
docker rm crown_testbed
docker system prune
docker build -t psadbimgs.azurecr.us/crowndb-snapshot:2021.07.28 .
docker run --name crown_testbed -d -p 2345:5432  psadbimgs.azurecr.us/crowndb-snapshot:2021.07.28