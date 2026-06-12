#!/bin/bash

echo "> Bringing down cluster services"
docker compose -f ../Apache-Spark/docker-compose.yml down -v

docker compose -f ../Hadoop/docker-compose.yml down -v

   
echo "> Deleting 'asvsp' network"
docker network rm asvsp
