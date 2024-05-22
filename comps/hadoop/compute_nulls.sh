#!/bin/bash

docker exec -it spark-master spark-submit /data/spark/python/troi_analyse_env.py
python3 ../python/create_merged_file.py

exit 0
