#!/bin/bash

docker exec -it spark-master spark-submit /data/spark/python/analyse_env.py
docker exec -it spark-master spark-submit /data/spark/python/deux_analyse_env.py

exit 0
