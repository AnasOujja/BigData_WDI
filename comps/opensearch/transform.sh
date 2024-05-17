#!/bin/bash

echo "Transforming WDICSV.."
python3 ../python/transform.py

echo "Constructing CSV files based on selected indicators.."
python3 ../python/create_csvs_from_indicators.py
echo "CSV files constructed for environment and economy categories"

exit 0
