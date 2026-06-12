#!/bin/bash

docker network create asvsp

echo ">> Starting up HDFS"
docker compose -f ../Hadoop/docker-compose.yml up -d
sleep 5

echo ">> Starting up Apache Spark"
docker compose -f ../Apache-Spark/docker-compose.yml up -d
sleep 15

docker exec -it spark-master /spark/bin/spark-submit /home/scripts/ingest_data_to_hdfs.py
docker exec spark-master spark-submit /home/scripts/clean_up_data_save_to_transformation_zone.py
