#!/bin/bash

python3 ../python/create_template_environment.py
python3 ../python/create_template_economy.py

python3 ../python/create_conf_environment.py
python3 ../python/create_conf_economy.py

exit 0

