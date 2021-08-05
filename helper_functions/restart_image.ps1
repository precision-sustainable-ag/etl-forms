Set-Location C:\Users\mikah\Documents\crowndb-testbed
docker stop crown_testbed
docker rm crown_testbed
docker stop shadow_testbed
docker rm shadow_testbed
# docker system prune
# docker build -t psadbimgs.azurecr.us/crowndb-snapshot:2021.08.05 .
docker run --name crown_testbed -d -p 1111:5432  psadbimgs.azurecr.us/crowndb-snapshot:2021.08.05
# docker build -t psadbimgs.azurecr.us/crowndb-snapshot:2021.08.05 .
docker run --name shadow_testbed -d -p 2222:5432  psadbimgs.azurecr.us/shadowdb-snapshot:2021.08.05