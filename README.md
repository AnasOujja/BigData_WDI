# ENSIIE 2024 / Big Data - The World Bank WDI Data

This project, completed at l'ENSIIE in 2024, focuses on leveraging Big Data tools to process and visualize World Bank World Development Indicators (WDI) data. By employing technologies like Hadoop, Spark, and OpenSearch, we demonstrate Big Data methodologies for transforming, processing, and visualizing large datasets to derive meaningful insights.

## Introduction

The original dataset was collected from the [World Bank Data Catalog](https://datacatalog.worldbank.org/search/dataset/0037712/World-Development-Indicators), and the list of indicators used to create the transformed datasets are stored in the `comps/files/` directory.

## Python Codes

In the `comps/python/` directory, you'll find Python scripts responsible for transforming the original dataset to a format suitable for loading into the OpenSearch cluster and subsequent visualization. These scripts also generate configuration and template files for OpenSearch.

## Setting up the Environment

To set up the project on a different machine with RedHat/CentOS-like OS, follow these steps:

1. **Install Dependencies**: Execute the `set_my_env.sh` script. This script installs Python 3 and pandas, which are required to run the Python codes located in the `comps/python/` directory.

2. **Data Transformation**: After installing Python 3 and pandas, run the `transform.sh` shell script in the `comps/opensearch/` directory. This script creates two new datasets for environment and economy indicators from the original dataset (`comps/files/WDICSV.csv`). This transformation is necessary to properly load and visualize the data in OpenSearch.

3. **Configuration Files**: Execute the `create_confs_templates.sh` shell script to generate configuration and template files required for loading the data into the OpenSearch cluster from the Logstash component.

4. **Docker Compose Setup**: The project includes a `docker-compose.yml` file for launching the OpenSearch cluster. This file specifies the components' linking, the volumes to be mounted to the containers, and other configurations necessary for a proper launch of the OpenSearch cluster.

5. **Hadoop Cluster Setup**: The project includes a YAML file for setting up the Hadoop cluster, which will be utilized to run Spark jobs for distributed analysis. The cluster comprises 1 Spark master and 2 Spark workers, along with other components necessary for the default functioning of a Hadoop cluster.

